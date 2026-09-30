#!/usr/bin/env python3
"""관찰 가능한 에이전트 결정 사례 — 집계 재현 (정의: 공시 §2).
공개 API만 읽는다. 결과: cases.csv(심의 완결 전수, 개인 식별 문자열 없음), fetch-metadata.json, 표준 출력 요약.
사용: python3 reproduce.py [--out 폴더]   (Python 3 표준 라이브러리만)
"""
import argparse, csv, datetime as dt, hashlib, json, os, sys, urllib.request

WIN_START, WIN_END = "2026-07-01T00:00:00Z", "2026-10-01T00:00:00Z"   # 결론 시각 기준 UTC 창
DEF_DATE = "2026-09-18T00:00:00Z"                                      # 정의일 (UTC 자정)
LIMIT = 5000
URLS = {
    "algora_sessions":  "https://algora.moss.land/api/agora/sessions?status=completed",
    "algora_dp":        f"https://algora.moss.land/api/governance-os/documents?type=DP&limit={LIMIT}",
    "algora_proposals": f"https://algora.moss.land/api/proposals?limit={LIMIT}",
    "algora_outcomes":  "https://algora.moss.land/api/outcomes",
    "algora_prop_stats":"https://disclosure.moss.land/api/algora/proposals/stats",
    "bridge_proposals": "https://bridge.moss.land/api/proposals",
    "bridge_stats":     "https://bridge.moss.land/api/stats",
    "bridge_outcomes":  "https://bridge.moss.land/api/outcomes",
    "ao_pipeline":      "https://disclosure.moss.land/api/ao/pipeline",
    "ao_plans":         "https://disclosure.moss.land/api/ao/plans",
}

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "mossland-q3-reproduce/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        body = r.read()
    return body, hashlib.sha256(body).hexdigest()

def norm(ts):   # 'Z' 통일, 비교는 문자열(ISO 8601 고정폭)
    return ts.replace("+00:00", "Z") if ts else ts

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", default="."); a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    t0 = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    raw, meta = {}, {"observed_at_utc": t0, "window": [WIN_START, WIN_END], "definition_date_utc": DEF_DATE, "limit": LIMIT, "responses": {}}
    for k, u in URLS.items():
        body, h = fetch(u); raw[k] = json.loads(body)
        meta["responses"][k] = {"url": u, "sha256": h, "bytes": len(body)}

    # ---- 전수 확인 (limit 절단 방지) ----
    dp_docs = raw["algora_dp"]["documents"]; dp_total = raw["algora_dp"].get("total")
    props = raw["algora_proposals"]["proposals"] if isinstance(raw["algora_proposals"], dict) else raw["algora_proposals"]
    prop_total = raw["algora_prop_stats"]["stats"]["proposals"]["total"]
    checks = {"dp_received_vs_total": [len(dp_docs), dp_total, len(dp_docs) == dp_total],
              "algora_proposals_received_vs_stats_total": [len(props), prop_total, len(props) == prop_total]}
    meta["completeness_checks"] = checks
    if not (checks["dp_received_vs_total"][2] and checks["algora_proposals_received_vs_stats_total"][2]):
        print("!! 전수 미확보 — limit 을 올려 다시 실행", checks, file=sys.stderr)

    # ---- Algora: DP → issue_id 그룹 → 완결 세션(결론 시각) 결합 ----
    sessions = raw["algora_sessions"]["sessions"] if isinstance(raw["algora_sessions"], dict) else raw["algora_sessions"]
    sess_by_issue, sess_by_id = {}, {}
    for s in sessions:
        sess_by_id[s["id"]] = s
        if s.get("issue_id"): sess_by_issue.setdefault(s["issue_id"], []).append(s)
    groups = {}   # issue_id -> [dp ids]
    for d in dp_docs:
        try: c = json.loads(d["content"]) if isinstance(d["content"], str) else (d["content"] or {})
        except Exception: c = {}
        iid = c.get("issueId")
        if not iid:
            sid = c.get("sessionId") or c.get("sourceId")
            iid = sess_by_id.get(sid, {}).get("issue_id") if sid else None
        if iid: groups.setdefault(iid, []).append(d["id"])
    prop_by_issue = {}
    for p in props:
        if p.get("issue_id"): prop_by_issue.setdefault(p["issue_id"], p)
    rows = []
    for iid, dps in groups.items():
        concl = [norm(s["concluded_at"]) for s in sess_by_issue.get(iid, []) if s.get("status") == "completed" and s.get("concluded_at")]
        if not concl: continue                              # 완결 세션이 붙지 않은 DP 그룹 제외
        t = max(concl)
        if not (WIN_START <= t < WIN_END): continue
        human = any(s.get("human_participants") for s in sess_by_issue.get(iid, []))
        p = prop_by_issue.get(iid)
        rows.append({"system": "algora", "input_id": iid, "output_id": sorted(dps)[0], "n_outputs": len(dps),
                     "concluded_at_utc": t, "grade": "deliberation_concluded", "proposal_status": (p or {}).get("status", ""),
                     "human_participation": "yes" if human else "no", "after_definition_date": "yes" if t >= DEF_DATE else "no",
                     "path": f"algora.moss.land/api/governance-os/documents/{sorted(dps)[0]}"})

    # ---- BRIDGE: DP 있는 제안, synthetic 카테고리 분리, UTC 창 ----
    bstats = raw["bridge_stats"]
    synthetic_cats = {x["category"] for x in bstats["signals"]["synthetic"]["byCategory"]}
    bprops = raw["bridge_proposals"]["proposals"] if isinstance(raw["bridge_proposals"], dict) else raw["bridge_proposals"]
    seen = set(); n_real = n_syn = 0
    for p in bprops:
        d = p.get("decisionPacket") or {}
        if not d: continue
        cat = ((d.get("issue") or {}).get("category")) if isinstance(d.get("issue"), dict) else None
        if cat in synthetic_cats: n_syn += 1; continue
        n_real += 1
        iid = d.get("issueId") or p.get("id")
        if iid in seen: continue
        seen.add(iid)
        t = norm(d.get("createdAt") or p.get("createdAt"))
        if not (WIN_START <= t < WIN_END): continue
        tally = p.get("tally") or {}
        rows.append({"system": "bridge", "input_id": iid, "output_id": d.get("id", ""), "n_outputs": 1,
                     "concluded_at_utc": t, "grade": "deliberation_concluded", "proposal_status": p.get("status", ""),
                     "human_participation": "no" if p.get("proposer") == "auto-system" else "unknown",
                     "after_definition_date": "yes" if t >= DEF_DATE else "no", "path": f"bridge.moss.land/api/proposals/{p.get('id')}"})
    checks["bridge_real_vs_stats"] = [n_real, bstats["proposals"]["total"], n_real == bstats["proposals"]["total"]]
    checks["bridge_synthetic_vs_stats"] = [n_syn, bstats["proposals"]["synthetic"]["total"], n_syn == bstats["proposals"]["synthetic"]["total"]]

    # ---- 실행·검증 (L2) ----
    l2 = {"algora_outcomes": raw["algora_outcomes"].get("outcomes", []),
          "bridge_outcomes_count": raw["bridge_outcomes"].get("count"),
          "bridge_totalProofs": bstats["outcomes"]["totalProofs"]}
    n_l2 = len(l2["algora_outcomes"]) + (l2["bridge_outcomes_count"] or 0)

    # ---- 출력 ----
    rows.sort(key=lambda r: (r["system"], r["concluded_at_utc"]))
    cols = ["system", "input_id", "output_id", "n_outputs", "concluded_at_utc", "grade", "proposal_status", "human_participation", "after_definition_date", "path"]
    with open(os.path.join(a.out, "cases.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)
    alg = [r for r in rows if r["system"] == "algora"]; brg = [r for r in rows if r["system"] == "bridge"]
    ao_pl = raw["ao_pipeline"]
    summary = {
        "observed_at_utc": t0,
        "decision_cases_executed_verified": n_l2, "l2_sources": l2,
        "deliberation_concluded_total": len(rows), "algora": len(alg), "ao": 0, "bridge": len(brg),
        "after_definition_date": sum(1 for r in rows if r["after_definition_date"] == "yes"),
        "before_definition_date": sum(1 for r in rows if r["after_definition_date"] == "no"),
        "algora_proposal_status": {k: sum(1 for r in alg if r["proposal_status"] == k) for k in sorted({r["proposal_status"] for r in alg})},
        "bridge_status": {k: sum(1 for r in brg if r["proposal_status"] == k) for k in sorted({r["proposal_status"] for r in brg})},
        "human_participation_any": sum(1 for r in rows if r["human_participation"] == "yes"),
        "algora_votes_system_total": raw["algora_prop_stats"]["stats"]["voting"]["totalVotes"],
        "ao_pipeline_plans": ((ao_pl.get("stages") or {}).get("plans") or {}).get("count"),
        "completeness_checks": checks,
    }
    meta["summary"] = summary
    with open(os.path.join(a.out, "fetch-metadata.json"), "w", encoding="utf-8") as f: json.dump(meta, f, ensure_ascii=False, indent=1)
    print(json.dumps(summary, ensure_ascii=False, indent=1))

if __name__ == "__main__":
    main()
