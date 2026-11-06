# 증빙 자료 — MOC Activation Season 1 10월 월간 시즌 요약 (2026-11-06 관측)

본 폴더는 [10월 월간 시즌 요약](../2026-11-06_moc-activation-season1-october-summary.md)의 증빙입니다. 세 시점의 공개 GET 응답 원문 12개를 공시와 같은 커밋에 포함하는 단위로 모았습니다. 모두 인증 없는 공개 경로의 응답이며, 내부 기록은 포함하지 않았습니다.

| 파일 | 내용 | 출처 |
| --- | --- | --- |
| `transparency.json` | 2026-11-06 01:25 UTC Passport 인증·홀더·위임·당월 카운터·보전 지표(`behavior.period` `2026-11`) | `https://passport.moss.land/api/transparency` |
| `wall.json` | 같은 시각 Wall 서명 기록 전체(30건: 공개 28 · 주소·원문·서명을 가린 `withheld` 2). 항목 수가 쪽 크기(30)와 같아 `nextCursor`가 1로 왔습니다 | `https://passport.moss.land/api/wall` |
| `wall-before-1.json` | 바로 이어서 조회한 다음 쪽. `items` 0 · `nextCursor` null — 30건이 전부임을 보입니다 | `https://passport.moss.land/api/wall?before=1` |
| `connect-stats.json` | 같은 시각 누적 스탬프와 서비스별 연결 집계 | `https://passport.moss.land/api/connect/stats` |
| `governance-aggregates.json` | 같은 시각 API 위임 대조 결과와 안건별 `verifiedMocSum` | `https://passport.moss.land/api/governance-pack/aggregates` |
| `health.json` | 같은 시각 서비스 상태 | `https://passport.moss.land/api/health` |
| `transparency-2026-11-02.json` | 2026-11-02 02:51 UTC — 10월(UTC) 월 경계 뒤 첫 관측(`behavior.period` `2026-11`) | `https://passport.moss.land/api/transparency` |
| `wall-2026-11-02.json` | 같은 시각 Wall 27건(`nextCursor` null) | `https://passport.moss.land/api/wall` |
| `connect-stats-2026-11-02.json` | 같은 시각 누적 스탬프·연결 집계 | `https://passport.moss.land/api/connect/stats` |
| `governance-aggregates-2026-11-02.json` | 같은 시각 위임 대조·안건별 `verifiedMocSum` | `https://passport.moss.land/api/governance-pack/aggregates` |
| `transparency-2026-10-14.json` | 2026-10-14 04:54 UTC — 10월 당월 카운터가 든 **경계 전 마지막 보존 관측**(`behavior.period` `2026-10`) | `https://passport.moss.land/api/transparency` |
| `wall-2026-10-14.json` | 같은 시각 Wall 27건. 2026-11-02 파일과 항목 `id` 집합이 같습니다 | `https://passport.moss.land/api/wall` |
| `fetch-metadata.json` | 관측별 시각·원본 URL·파일별 상태·크기·해시, 월 경계·시즌 종료 관련 메모, 공개 안건 목록 첫 쪽 판정 요약(`proposalInventoryCheck`), 응답을 보존하지 않은 10월 23일 확인 기록(`unpreservedChecks`) | — |
| `SHA256SUMS.txt` | 원본 12개와 `fetch-metadata.json`의 SHA-256 | — |

## 재검증 방법

```bash
# 이 폴더에서 보존된 파일 13개를 검증합니다.
shasum -a 256 -c SHA256SUMS.txt
```

`fetch-metadata.json`의 `sources`는 인증 없는 공개 GET URL입니다. 재조회 시 `generatedAt`·`asOf`와 당월 카운터·누적값은 바뀔 수 있으므로 현재 응답의 바이트 일치를 요구하지 않습니다. 보존본은 위 해시로, 현재 상태는 공개 원본의 실질 값으로 대조합니다. SHA256SUMS와 README 자신은 해시 목록에서 제외했습니다.

## 네 시점 대조

보고 §2의 2026-10-07 값은 [Day 60 증빙](../2026-10-07_moc-activation-season1-day60-evidence/)에 있습니다. 10-14·11-02·11-06 값은 이 폴더에 있습니다. `behavior.checkinsThisMonth`·`activationsThisMonth`는 해당 UTC 월의 진행 상태이며, 서로 다른 달을 누적 증감으로 읽지 않습니다.

```bash
jq .behavior ../2026-10-07_moc-activation-season1-day60-evidence/transparency.json
jq .behavior ./transparency-2026-10-14.json
jq .behavior ./transparency-2026-11-02.json
jq .behavior ./transparency.json
jq '{period, stats, n: (.items | length)}' ./wall-2026-10-14.json ./wall-2026-11-02.json ./wall.json
```

## 범위와 한계

- **10월 당월 카운터의 월 경계 직전 관측은 없습니다.** 경계 전 마지막 보존 관측은 2026-10-14 04:54 UTC이고, 그 뒤 경계(2026-11-01 00:00 UTC)까지 약 17일 19시간은 공개 응답을 보존한 관측이 없습니다(2026-10-23 15:08 UTC의 미보존 확인은 `fetch-metadata.json`의 `unpreservedChecks`). 10월 최종값을 보증하는 캡처가 아닙니다. 2026-10-14 파일의 수집 시각은 transparency 응답의 `generatedAt`이며(벽 응답은 같은 점검에서 받았고 자체 시각 필드가 없습니다), 수집자의 별도 요청 시각 기록은 없습니다.
- `wall*.json`은 Wall에 게시된 서명 기록입니다. 공개 서명과 전체 인증 지갑은 집계 범위가 다르며, 서명 기록의 수를 지갑 수나 사람 수로 보지 않습니다. 주소·원문·서명은 이미 공개된 검증 자료입니다. 이번 작업에서 서명을 암호학적으로 다시 검증하거나 독립 노드를 질의했다고 주장하지 않습니다.
- 거래소 보관량은 API가 제공하는 운영자 추정치입니다. 지정 지갑 분류·목록을 이 묶음에서 독립 검증하지 않았습니다. 인증 지갑 잔고 합은 지갑별 마지막 인증 시점의 잔고이며, 이번 관측 시각의 잔고가 아닙니다.
- 응답 헤더, 내부 작업 기록, 집계의 자동화 관련 분류에 쓰인 내부 기록은 이 폴더에 포함하지 않았습니다. 수집 시각은 수집자 기록입니다. 병합 기록은 그 시점까지 파일이 존재했음을 뒷받침하며 정확한 수집 시각을 독립 증명하지 않습니다.

---

작성 방식: **AI 보조 · 사람 검토** · [AI 생성 콘텐츠 표시 정책 v1.0](../2026-09-16_ai-content-labelling-policy.md)
