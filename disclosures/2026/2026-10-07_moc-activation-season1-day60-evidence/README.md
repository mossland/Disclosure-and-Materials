# 증빙 자료 — MOC Activation Season 1 Day 60 보고 (2026-10-07 관측)

본 폴더는 [Day 60 보고](../2026-10-07_moc-activation-season1-day60.md)의 증빙입니다. 이번 원본 7개와 9월 원본 2개를 공시와 같은 커밋에 포함하는 단위로 모았습니다. Day 60은 보고 회차명이며, 실제 관측은 10월 7일(시즌 61일차)입니다.

| 파일 | 내용 | 출처 |
| --- | --- | --- |
| `transparency.json` | 2026-10-07 Passport 인증·홀더·위임·체크인·보전 지표 | `https://passport.moss.land/api/transparency` |
| `wall.json` | Wall 서명 기록(1쪽 19개: 공개 17 · 주소·원문·서명을 가린 `withheld` 2, nextCursor=null) | `https://passport.moss.land/api/wall` |
| `connect-stats.json` | 누적 스탬프와 서비스별 연결 집계 | `https://passport.moss.land/api/connect/stats` |
| `governance-aggregates.json` | API 위임 대조 결과와 안건별 verifiedMocSum | `https://passport.moss.land/api/governance-pack/aggregates` |
| `season1-votes.json` | Season 1 투표 export(지갑·가중치·산정 방식·EIP-712 서명) | `https://agora.moss.land/api/proposal-votes/6a4decb73697e1a9d307e327` |
| `mip1-votes.json` | MIP-1 투표 export | `https://agora.moss.land/api/proposal-votes/6a85129f8be190cf5d2ebcc1` |
| `mip1-proposal.json` | MIP-1 공식 안건 레코드와 스냅샷 규칙 | `https://agora.moss.land/api/governance/proposals/6a85129f8be190cf5d2ebcc1` |
| `transparency-2026-09-30.json` | 9월(UTC) 월 경계 전 마지막 Passport 관측 | `https://passport.moss.land/api/transparency` |
| `connect-stats-2026-09-30.json` | 같은 시점의 누적 스탬프·연결 집계 | `https://passport.moss.land/api/connect/stats` |
| `fetch-metadata.json` | 첫 조회 시각·원본 URL·요청별 시각 및 해시·9월 별도 출처·안건 목록 전수 판정 요약 | — |
| `SHA256SUMS.txt` | 원본 9개와 fetch-metadata.json의 SHA-256 | — |

## 재검증 방법

```bash
# 이 폴더에서 보존된 파일 10개를 검증합니다.
shasum -a 256 -c SHA256SUMS.txt
```

`fetch-metadata.json`의 `sources`는 인증 없는 공개 GET URL입니다. 재조회 시 `generatedAt`·`asOf`와 월별 카운터 등은 바뀔 수 있으므로 현재 응답의 바이트 일치를 요구하지 않습니다. 보존본은 위 해시로, 현재 상태는 공개 원본의 실질 값으로 대조합니다. SHA256SUMS와 README 자신은 해시 목록에서 제외했습니다.

## 다섯 시점 대조

보고 §3의 2026-08-14·09-02·09-08 값은 해당 선행 공시 증빙에 있습니다. 09-30과 10-07 값은 이 폴더에 있습니다. `behavior.checkinsThisMonth`·`activationsThisMonth`는 해당 UTC 월의 진행 상태이며, 서로 다른 달을 누적 증감으로 읽지 않습니다.

```bash
jq .behavior ../2026-08-14_moc-activation-season1-vote-evidence/transparency.json
jq .behavior ../2026-09-02_mip-1-lifecycle-policy-vote-evidence/transparency.json
jq .behavior ../2026-09-08_moc-activation-season1-day30-evidence/transparency.json
jq .behavior ./transparency-2026-09-30.json
jq .behavior ./transparency.json
```

## 범위와 한계

- `wall.json`은 Wall에 게시된 서명 기록입니다(19개 중 공개 17개, 주소·원문·서명을 가린 `withheld` 2개). 공개 서명과 전체 인증 지갑은 집계 범위가 다르며, 공개 자료만으로 차이의 원인별 규모를 확정할 수 없습니다. 서명 기록의 수를 지갑 수나 사람 수로 보지 않습니다.
- 투표 export의 지갑 주소·EIP-712 서명은 이미 공개된 검증 자료입니다. 투표 원본 두 개와 MIP-1 안건 원본은 Day 30 증빙과 바이트 단위로 같습니다. 이번 작업에서 서명을 다시 암호학적으로 검증하거나 독립 노드를 질의했다고 주장하지 않습니다.
- 9월 파일 2개는 2026-09-30T23:50:38Z 수집 기록과 당시 SHA-256에 일치합니다. 경계까지 약 9분은 관측되지 않았습니다. 9월 전체 최종값을 보증하는 캡처가 아닙니다.
- 수집 시각은 수집자 기록입니다. `septemberSnapshot`은 9월 별도 시각·원본 URL·당시 해시를, `currentRequests`는 이번 파일별 시각·응답 상태·크기·해시를 적습니다. 병합 기록은 그 시점까지 파일이 존재했음을 뒷받침하며 정확한 수집 시각을 독립 증명하지 않습니다.
- 공개 안건 목록 3쪽(42개)을 전수 확인한 요약은 `proposalInventoryCheck`에 있습니다. 이는 판정용 집계이며 원본 투표 export가 아닙니다. 작성자 정보를 포함하는 목록·포럼 응답 본문, 응답 헤더, 내부 작업 기록은 이 폴더에 포함하지 않았습니다.
- 거래소 보관량은 API가 제공하는 운영자 추정치입니다. 지정 지갑 분류·목록을 이 묶음에서 독립 검증하지 않았습니다. 인증 지갑 잔고 합은 지갑별 마지막 인증 시점의 잔고이며, 검증 홀더만의 합이나 이번 관측 시각 잔고가 아닙니다.

---

작성 방식: **AI 보조 · 사람 검토** · [AI 생성 콘텐츠 표시 정책 v1.0](../2026-09-16_ai-content-labelling-policy.md)
