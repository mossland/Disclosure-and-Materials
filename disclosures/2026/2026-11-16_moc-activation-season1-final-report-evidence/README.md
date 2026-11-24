# 증빙 자료 — MOC Activation Season 1 최종 보고 (2026-11-16 작성)

본 폴더는 [Season 1 최종 보고](../2026-11-16_moc-activation-season1-final-report.md)의 증빙입니다. 보고서의 발행 시점은 이 저장소의 기본 브랜치에 병합된 시각으로 확인합니다. 시즌 종료 뒤 보고 시점에 받은 공개 GET 응답 원문 7개를 공시와 같은 커밋에 포함하는 단위로 모았습니다. 그 가운데 2026-11-15 23:57 UTC (11월 16일 08:57 KST) 보고 시점 관측의 응답은 보고 §4의 세 가지 확인(시즌 종료 전에 기록된 벽 항목의 유지, 공개 설정의 `activation`·`exitPass`, `verifiedMocSum`)에만 쓰고 시즌 표에는 넣지 않습니다. 시즌 표(보고 §3)의 8개 시점 원본은 각 공시의 증빙 폴더에 있어 다시 넣지 않았습니다. 모두 인증 없는 공개 경로의 응답이며, 내부 기록은 포함하지 않았습니다.

| 파일 | 내용 | 출처 |
| --- | --- | --- |
| `transparency.json` | 보고 시점 Passport 공개 집계와 공개 설정(`activation`·`exitPass`). 보고는 공개 설정 비교에만 인용합니다 | `https://passport.moss.land/api/transparency` |
| `wall.json` | 같은 시각 Wall 서명 기록 첫 쪽. 쪽이 가득 차 `nextCursor`가 265로 왔습니다 | `https://passport.moss.land/api/wall` |
| `wall-before-265.json` | 바로 이어서 조회한 다음 쪽. `nextCursor` null — 벽을 끝 쪽까지 받았음을 보입니다 | `https://passport.moss.land/api/wall?before=265` |
| `connect-stats.json` | 같은 시각 누적 스탬프와 서비스별 연결 집계(시즌 뒤 값이며 보고에 인용하지 않습니다) | `https://passport.moss.land/api/connect/stats` |
| `governance-aggregates.json` | 같은 시각 API 위임 대조 결과와 안건별 `verifiedMocSum` | `https://passport.moss.land/api/governance-pack/aggregates` |
| `health.json` | 같은 시각 서비스 상태 | `https://passport.moss.land/api/health` |
| `polls.json` | 2026-11-16 01:07 UTC Passport 공개 설문 목록(원칙 3의 비구속 시그널·설문 확인, 보고 §7) | `https://passport.moss.land/api/polls` |
| `fetch-metadata.json` | 관측별 시각·원본 URL·파일별 상태·크기·해시, 세 가지 확인 결과(`reportTimeChecks`), 이전 관측의 위치(`earlierObservations`), 시즌 종료 기준 시각과 지표별 처리(`seasonEnd`), 11월 당월 카운터와 12월 1일 경계 처리(`monthBoundary`), 공개 안건 목록 전수 조회 요약(`proposalInventoryCheck`), 공개 설문 목록 조회(`pollsCheck`), 이전 공시에 같은 단서로 공개한 내부 기록 값의 위치(`unpreservedChecks`) | — |
| `SHA256SUMS.txt` | 원본 7개와 `fetch-metadata.json`의 SHA-256 | — |

## 재검증 방법

```bash
# 이 폴더에서 보존된 파일 8개를 검증합니다.
shasum -a 256 -c SHA256SUMS.txt
```

`fetch-metadata.json`의 `sources`는 인증 없는 공개 GET URL입니다. 재조회 시 `generatedAt`·`asOf`와 당월 카운터·누적값은 바뀔 수 있으므로 현재 응답의 바이트 일치를 요구하지 않습니다. 보존본은 위 해시로, 현재 상태는 공개 원본의 실질 값으로 대조합니다. SHA256SUMS와 README 자신은 해시 목록에서 제외했습니다.

## 보고 시점 관측의 세 가지 확인

```bash
# (1) 안건별 verifiedMocSum — 보고 §6, 관리 목록 #6
jq '[.proposals[] | {proposalId, verifiedMocSum}]' ./governance-aggregates.json
# (2) 11월 6일 목록에서 확인한 종료 전 생성 기록 30건이 보고 시점에도 같은 id·상태로 남아 있는지 — 보고 §4
#     빈 배열([])이면 30건 모두 같은 id와 같은 status로 있습니다.
jq -n --slurpfile old ../2026-11-06_moc-activation-season1-october-summary-evidence/wall.json \
  '([inputs | .items[]] | map({key: (.id|tostring), value: .status}) | from_entries) as $now
   | [$old[0].items[] | {id, before: .status, now: $now[(.id|tostring)]} | select(.before != .now)]' \
  ./wall.json ./wall-before-*.json
# (3) 공개 설정의 activation·exitPass를 2026-08-14 관측과 비교 — 보고 §4 (출력이 없으면 같음)
diff <(jq -S '{activation, exitPass}' ../2026-08-14_moc-activation-season1-vote-evidence/transparency.json) \
     <(jq -S '{activation, exitPass}' ./transparency.json)
```

## 8개 시점 대조

보고 §3 시즌 표의 각 열은 아래 파일에 있습니다. `behavior.checkinsThisMonth`·`activationsThisMonth`는 해당 UTC 월의 진행 상태이며, 서로 다른 달을 누적 증감으로 읽지 않습니다.

```bash
jq .behavior ../2026-08-14_moc-activation-season1-vote-evidence/transparency.json
jq .behavior ../2026-09-02_mip-1-lifecycle-policy-vote-evidence/transparency.json
jq .behavior ../2026-09-08_moc-activation-season1-day30-evidence/transparency.json
jq .behavior ../2026-10-07_moc-activation-season1-day60-evidence/transparency-2026-09-30.json
jq .behavior ../2026-10-07_moc-activation-season1-day60-evidence/transparency.json
jq .behavior ../2026-11-06_moc-activation-season1-october-summary-evidence/transparency-2026-10-14.json
jq .behavior ../2026-11-06_moc-activation-season1-october-summary-evidence/transparency-2026-11-02.json
jq .behavior ../2026-11-06_moc-activation-season1-october-summary-evidence/transparency.json
jq '{stampsIssued, connectByService}' \
  ../2026-09-08_moc-activation-season1-day30-evidence/connect-stats.json \
  ../2026-10-07_moc-activation-season1-day60-evidence/connect-stats-2026-09-30.json \
  ../2026-10-07_moc-activation-season1-day60-evidence/connect-stats.json \
  ../2026-11-06_moc-activation-season1-october-summary-evidence/connect-stats-2026-11-02.json \
  ../2026-11-06_moc-activation-season1-october-summary-evidence/connect-stats.json
jq '{n: (.items | length), withheld: ([.items[] | select(.status != "public")] | length), nextCursor}' \
  ../2026-09-08_moc-activation-season1-day30-evidence/wall.json \
  ../2026-10-07_moc-activation-season1-day60-evidence/wall.json \
  ../2026-11-06_moc-activation-season1-october-summary-evidence/wall-2026-10-14.json \
  ../2026-11-06_moc-activation-season1-october-summary-evidence/wall-2026-11-02.json \
  ../2026-11-06_moc-activation-season1-october-summary-evidence/wall.json \
  ../2026-11-06_moc-activation-season1-october-summary-evidence/wall-before-1.json
# 공개 설정 activation·exitPass — 여덟 줄의 해시가 모두 같으면 8개 시점의 설정이 같습니다(보고 §4)
for f in ../2026-08-14_moc-activation-season1-vote-evidence/transparency.json ../2026-09-02_mip-1-lifecycle-policy-vote-evidence/transparency.json ../2026-09-08_moc-activation-season1-day30-evidence/transparency.json ../2026-10-07_moc-activation-season1-day60-evidence/transparency-2026-09-30.json ../2026-10-07_moc-activation-season1-day60-evidence/transparency.json ../2026-11-06_moc-activation-season1-october-summary-evidence/transparency-2026-10-14.json ../2026-11-06_moc-activation-season1-october-summary-evidence/transparency-2026-11-02.json ../2026-11-06_moc-activation-season1-october-summary-evidence/transparency.json; do jq -S -c '{activation, exitPass}' "$f" | shasum -a 256; done
# 시즌 종료 기준 시각(2026-11-05T15:00:00Z)과 벽 기록 시각 — 보고 §4
jq '[.items[].createdAt] | max' ../2026-11-06_moc-activation-season1-october-summary-evidence/wall.json
jq '[.items[] | select(.kind == "connect" and .period == "svc:wa")] | length' ../2026-11-06_moc-activation-season1-october-summary-evidence/wall.json
```

## 범위와 한계

- 보고 시점 관측은 시즌 종료(2026-11-05 24:00 KST) 뒤의 관측입니다. 원본에는 시즌 종료 뒤의 카운터·누적값·벽 항목과 거래소 보관 추정치도 들어 있으나, 보고는 세 가지 확인 밖에서 이 값들을 인용하거나 해석하지 않으며 시즌 지표로 세지 않습니다.
- 시즌 종료 직전과 당일에 보존한 관측은 없습니다. 종료 시점의 지표별 처리는 보고 §4와 `fetch-metadata.json`의 `seasonEnd`에 있습니다.
- `wall*.json`은 Wall에 게시된 서명 기록입니다. 공개 서명과 전체 인증 지갑은 집계 범위가 다르며, 서명 기록의 수를 지갑 수나 사람 수로 보지 않습니다. 주소·원문·서명은 이미 공개된 검증 자료입니다. 이번 작업에서 서명을 암호학적으로 다시 검증하거나 독립 노드를 질의했다고 주장하지 않습니다.
- 거래소 보관량은 API가 제공하는 운영자 추정치입니다. 지정 지갑 분류·목록을 이 묶음에서 독립 검증하지 않았습니다.
- 공개 안건 목록의 응답 본문은 넣지 않았습니다. 조회 범위와 요약은 `fetch-metadata.json`의 `proposalInventoryCheck`에 있습니다.
- 응답 헤더, 내부 작업 기록, 집계의 자동화 관련 분류에 쓰인 내부 기록은 이 폴더에 포함하지 않았습니다. 수집 시각은 수집자 기록입니다. 병합 기록은 그 시점까지 파일이 존재했음을 뒷받침하며 정확한 수집 시각을 독립 증명하지 않습니다. `health.json`은 조회 시각의 상태 응답일 뿐 가동률 집계가 아닙니다.

---

작성 방식: **AI 보조 · 사람 검토** · [AI 생성 콘텐츠 표시 정책 v1.0](../2026-09-16_ai-content-labelling-policy.md)
