# 증빙 자료 — MOC Activation Season 1 Day 30 보고 (2026-09-08 공시)

본 폴더는 [2026-09-08 MOC Activation Season 1 Day 30 보고](../2026-09-08_moc-activation-season1-day30.md)의 증빙입니다.
공시 문서와 **같은 커밋**에 포함되어, GitHub 커밋 타임스탬프가 수집 시점의 무결성을 뒷받침합니다.

| 파일 | 내용 | 출처 |
| --- | --- | --- |
| `transparency.json` | Day 30 시점 Passport Transparency 스냅샷 (인증·홀더·위임·체크인·보전 지표) | `https://passport.moss.land/api/transparency` |
| `wall.json` | 서명의 벽 공개분 — 공개에 동의한 서명 기록 | `https://passport.moss.land/api/wall` |
| `connect-stats.json` | 누적 스탬프 발급 수와 서비스별 연결 수 | `https://passport.moss.land/api/connect/stats` |
| `governance-aggregates.json` | 위임 집계와 안건별 검증 상태 (온체인 대조 결과 포함) | `https://passport.moss.land/api/governance-pack/aggregates` |
| `season1-votes.json` | Season 1 안건 투표 export — 지갑, 선택, voting power, EIP-712 서명 | `https://agora.moss.land/api/proposal-votes/6a4decb73697e1a9d307e327` |
| `mip1-votes.json` | 시즌 중 두 번째 안건(MIP-1) 투표 export — 참여 비교의 근거 | `https://agora.moss.land/api/proposal-votes/6a85129f8be190cf5d2ebcc1` |
| `mip1-proposal.json` | MIP-1 안건 공식 레코드 (snapshot block, 투표 규칙 포함) | `https://agora.moss.land/api/governance/proposals/6a85129f8be190cf5d2ebcc1` |
| `fetch-metadata.json` | 수집 시각(UTC)과 원본 URL | — |
| `SHA256SUMS.txt` | 위 파일들의 SHA-256 해시 | — |

## 재검증 방법

```bash
# 1) 해시 검증 — 이 폴더에서
shasum -a 256 -c SHA256SUMS.txt

# 2) 원본 대조 — 전부 인증 없이 조회 가능한 공개 엔드포인트다
curl -s https://passport.moss.land/api/transparency
curl -s https://passport.moss.land/api/governance-pack/aggregates
curl -s https://agora.moss.land/api/proposal-votes/6a85129f8be190cf5d2ebcc1
```

## 시계열 대조

Day 30 보고 §3의 표는 시즌 중 확보된 **세 시점**을 나란히 놓은 것입니다. 앞의 두 시점은 각각 선행 공시의 증빙 폴더에 같은 형식으로 들어 있어, 이 저장소 안에서 독립 대조가 가능합니다.

```bash
# 2026-08-14 (baseline) · 2026-09-02 · 2026-09-08 (Day 30)
jq .behavior ../2026-08-14_moc-activation-season1-vote-evidence/transparency.json
jq .behavior ../2026-09-02_mip-1-lifecycle-policy-vote-evidence/transparency.json
jq .behavior ./transparency.json
```

## 주의

- 살아 있는 API 응답에는 시간에 따라 변하는 필드(`generatedAt`, `asOf` 등)가 있어 재조회 시 바이트 단위로 같지 않습니다. 검증 대상은 **지표의 실질 값**입니다.
- `behavior.checkinsThisMonth` 는 **당월 값**이며 월 경계에서 초기화됩니다. 세 스냅샷의 이 필드는 시계열이 아니라 각 달의 진행 상태입니다 — 보고 본문 §3에 같은 주의를 적었습니다.
- `wall.json` 은 **공개에 동의한 서명만** 포함합니다. 따라서 여기서 열거되는 수는 `transparency.json` 의 전체 집계보다 작으며, 그 차이는 공개 미동의분입니다. 이 격차는 결함이 아니라 동의 기반 공개의 결과입니다.
- 각 투표의 EIP-712 서명은 서명자 지갑 주소로 온체인 데이터 없이도 독립 검증이 가능합니다.
