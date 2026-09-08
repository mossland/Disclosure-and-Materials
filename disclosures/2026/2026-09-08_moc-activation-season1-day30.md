## MOC Activation Season 1 — Day 30 보고

**작성일: 2026-09-08**

### 핵심 요약

* 「MOC Activation Season 1 — 자가지갑 참여 전환 (90일 파일럿)」의 **Day 30 보고**입니다. 시즌 기간 2026-08-07 ~ 2026-11-05 중 32일차 시점의 지표를 [2026-08-14 공시](./2026-08-14_moc-activation-season1-vote-results.md)와 **같은 형식**으로 기록합니다.
* **본 보고는 예고한 기한을 넘겨 발행되었습니다.** 8-14 공시 §5와 그 포럼 답글이 Day 30 보고를 2026-09-06로 명시했으므로, 2일 지연입니다. 사유와 재발 방지는 §5에 적었습니다.
* **참여 규모는 baseline에서 변하지 않았습니다.** 시즌 중 상정된 두 번째 안건(MIP-1)의 참여는 Season 1과 **동일한 2개 지갑 · 동일한 108,988.96676301 MOC**입니다. 안건이 전제한 "제안을 거듭할수록 참여가 커진다"는 2회차까지 확인되지 않았습니다.
* Passport 인증 지갑은 10 → 11로 늘었으나, **검증 홀더 수는 3명으로 고정**입니다. 늘어난 지갑은 홀더 기준(100 MOC) 미만입니다.
* 메커니즘 측에서는 진전이 있습니다 — MIP-1에서는 두 표 **모두** 온체인 위임 스냅샷(`onchain_votes_snapshot`)으로 산정되었습니다. Season 1에서는 한 표가 잔고 폴백이었습니다.
* 본 보고의 모든 수치는 [증빙 폴더](./2026-09-08_moc-activation-season1-day30-evidence/)의 원본 JSON과 SHA-256 해시로 **같은 커밋**에 포함되어 있습니다.

### 1. 보고 기준

| 구분 | 내용 |
| --- | --- |
| 시즌 | MOC Activation Season 1 (90일 파일럿) |
| 시즌 기간 | 2026-08-07 (비준일) ~ 2026-11-05 |
| 본 보고 기준 시각 | 2026-09-08 13:23 UTC (시즌 32일차) |
| 예고된 기한 | 2026-09-06 — **2일 초과** |
| 안건 페이지 | <https://agora.moss.land/proposals/6a4decb73697e1a9d307e327> |
| 근거 | 2026-08-14 공시 §5 「Season 1 기간 및 보고 일정」 |

### 2. 참여 지표 (원칙 2 이행)

비준된 원칙 2에 따라, 시즌 중 진행된 **모든 안건**의 참여를 같은 형식으로 기록합니다.

| 안건 | 투표 기간 (KST) | 참여 MOC (가중) | 인원 | 결과 |
| --- | --- | ---: | ---: | --- |
| Season 1 (baseline) | 2026-07-08 ~ 08-07 | 108,988.96676301 | 2 | 가결 (찬성 100%) |
| MIP-1 생명주기 정책 | 2026-08-19 ~ 09-02 | 108,988.96676301 | 2 | 가결 (찬성 100%) |

**두 안건의 참여 지갑과 가중 합계가 완전히 동일합니다.**

| 지갑 | Season 1 산정 방식 | MIP-1 산정 방식 | Voting Power (MOC) |
| --- | --- | --- | ---: |
| `0x1d67e226…4e59c464` | onchain_balance_snapshot | **onchain_votes_snapshot** | 99,888.96676301 |
| `0xe645cd81…335c60b2` | onchain_votes_snapshot | onchain_votes_snapshot | 9,100.0 |

산정 방식이 잔고 폴백에서 위임 스냅샷으로 바뀐 것은 위임 경로가 실제로 동작하게 되었다는 뜻입니다. 다만 **참여의 크기는 그대로**이므로, 이는 메커니즘의 진전이지 참여의 확대가 아닙니다.

참여율은 8-14 공시와 같은 기준으로 산출합니다.

| 지표 | 값 | 기준 |
| --- | ---: | --- |
| MOC 총공급 대비 참여율 | 0.0218% | 총공급 500,000,000 MOC |
| Passport 검증 홀더 잔고 대비 참여율 | 34.60% | 검증 홀더 잔고 314,988.96676301 MOC |
| 거래소 보관 MOC | 412,654,465.41 (총공급의 82.53%) | 원칙 3에 따라 구속 투표 밖 |

### 3. Passport 채택 지표 (원칙 4 이행)

비준된 원칙 4는 인증·위임·참여·보전 집계의 상시 공개와 월간 요약 공시를 정했습니다. 시즌 중 확보된 세 시점의 스냅샷을 나란히 놓습니다. 세 값 모두 본 공시 및 선행 공시의 증빙 폴더에 원본 JSON으로 들어 있습니다.

| 지표 | 2026-08-14 | 2026-09-02 | 2026-09-08 (Day 30) |
| --- | ---: | ---: | ---: |
| 인증 지갑 | 10 | 11 | **11** |
| 홀더 / 검증 홀더 | 3 / 3 | 3 / 3 | **3 / 3** |
| 위임 지갑 | 2 | 2 | **2** |
| 당월 체크인 | 2 (8월) | 0 (9월) | **2 (9월)** |
| 당월 활성화 | 0 | 0 | **0** |
| Exit Pass 브로드캐스트 (누적) | 1 | 1 | **1** |
| 보전 지급 (누적) | 1 | 1 | **1** |
| 검증 홀더 잔고 (MOC) | 314,988.96676301 | 314,988.96676301 | **314,988.96676301** |
| 누적 스탬프 | — | — | **65** |

읽는 법을 함께 적습니다.

* **당월 체크인은 월 단위로 초기화됩니다.** 8-14의 2건은 8월분, 9-02의 0건은 9월 초 시점의 9월분입니다. 세 값은 시계열이 아니라 각 달의 진행 상태입니다.
* **인증 지갑(11)과 검증 홀더(3)의 차이는 결함이 아닙니다.** 홀더 판정 기준은 100 MOC이며, 서명으로 지갑을 인증했으나 그 기준에 못 미치는 지갑이 8개입니다.
* **Exit Pass와 보전 지급은 시즌 시작 이전부터 각 1건이며 시즌 중 늘지 않았습니다.** 원칙 1(출금 비용 보전)의 실집행은 아직 1건에 머뭅니다.
* 위임 2건은 온체인에서 독립 검증됩니다 — `walletsOnchainMatched: 2`, 합계 108,988.96676301 MOC가 API 값과 소수점까지 일치합니다.

### 4. 시즌 전제에 대한 중간 판정

안건은 "참여는 제안을 거듭할수록 커진다"를 전제로 90일 파일럿을 제안했고, 8-14 공시는 108,988.96676301 MOC / 2명을 **baseline**으로 기록하며 "시즌 동안 제안을 거듭하며 이 참여율이 어떻게 변하는지를 이후 보고에서 같은 형식으로 추적한다"고 밝혔습니다.

**32일차 기준으로 그 전제는 아직 확인되지 않았습니다.** 두 번째 안건의 참여는 첫 안건과 지갑 단위로 동일했고, 검증 홀더 수도 3명에서 움직이지 않았습니다. 늘어난 것은 인증 지갑 1개(비홀더)와 스탬프이며, 이는 참여의 폭이 아니라 등록의 폭입니다.

본 보고는 이 사실을 해석 없이 기록합니다. 남은 58일에 대한 판단은 Day 60(2026-10-06 전후) 보고와 시즌 종료 후 최종 보고에서 같은 형식으로 이어갑니다.

한편 **비준 원칙 2가 예고한 참여율(%) 화면 표시는 아직 미구현입니다.** 안건 결과 화면은 참여 MOC와 인원을 표기하지만, 총공급·Passport 활성 MOC 대비 비율은 렌더되지 않습니다 — 집계 API가 해당 값을 `null`로 반환하기 때문입니다(증빙 `governance-aggregates.json`의 `verifiedMocSum`). 8-14 공시가 "데이터 연동이 완료되는 대로 단계적으로 추가한다"고 유보한 항목이며, 현재 상태를 그대로 기재합니다.

### 5. 기한 초과에 대하여

Day 30 보고의 기한은 두 곳에 명문화되어 있었습니다 — 2026-08-14 공시 §5, 그리고 같은 날 Agora 포럼 답글("Day 30 보고(2026-09-06), Day 60 보고(2026-10-06) … 각각 공시 1건과 이 스레드 답글로 공유합니다"). 본 보고는 그보다 2일 늦은 2026-09-08에 발행되었습니다.

지연의 원인은 예고된 보고 항목을 기한과 함께 추적하는 관리 목록이 없어, 기한이 사람의 기억에만 의존했다는 점입니다. 이는 2026 Q2 분기 리포트가 상시 운영 규범으로 정한 「공시 예고 이행 절차」가 아직 절차로 구현되지 않았다는 뜻이며, 그 첫 위반 사례로 해당 분기 리포트에 기재됩니다.

재발 방지로 남은 예고 항목을 여기에 명시합니다.

| 예고 항목 | 트리거 | 기한 |
| --- | --- | --- |
| Day 60 보고 | 시즌 60일차 | 2026-10-06 전후 |
| 최종 보고 | 시즌 종료(2026-11-05) | 종료 후 |
| 월간 시즌 요약 | 매월 | 익월 초 |

### 6. 증빙 (Evidence)

본 공시와 같은 커밋에 포함된 [증빙 폴더](./2026-09-08_moc-activation-season1-day30-evidence/)의 파일과 SHA-256 해시입니다. GitHub 커밋 타임스탬프가 수집 시점을 증명합니다.

수집 시각·원본 URL·해시는 증빙 폴더의 `fetch-metadata.json`과 `SHA256SUMS.txt`에 있으며, 검증 방법은 같은 폴더의 `README.md`에 적었습니다.

---

## English Summary

**Day 30 report — MOC Activation Season 1 (90-day pilot)**

This is the Day 30 report for the ratified Season 1 pilot (2026-08-07 to 2026-11-05), recorded in the same format as the [2026-08-14 disclosure](./2026-08-14_moc-activation-season1-vote-results.md).

**It was published two days late.** The 2026-08-14 disclosure §5 and its forum reply both named 2026-09-06. The cause and the preventive measure are in §5 above.

**Participation has not moved from the baseline.** The second proposal tabled during the season (MIP-1) drew participation from **the same two wallets and the same 108,988.96676301 MOC**. The premise the proposal argued from — that participation grows as proposals accumulate — is not yet borne out at day 32.

Passport verified wallets went from 10 to 11, but **verified holders remain at 3**: the additional wallet is below the 100 MOC holder threshold. Exit Pass broadcasts and reimbursement payments both stand at 1 cumulative, unchanged since before the season began, so Principle 1 (withdrawal-cost reimbursement) still has a single executed case.

There is progress on the mechanism side. In MIP-1 **both** votes were weighted from an on-chain delegation snapshot (`onchain_votes_snapshot`), whereas Season 1 had one vote fall back to a balance snapshot. Delegation is independently verifiable on-chain: 2 wallets, 108,988.96676301 MOC, matching the API to the decimal. This is a change in how participation is measured, not an increase in it.

The percentage-of-supply display promised by ratified Principle 2 is **still not rendered** on the proposal result screen, because the aggregation API returns `null` for the verified MOC sum (see `governance-aggregates.json`). The 2026-08-14 disclosure deferred this as "to be added in stages as the data integration completes"; the current state is recorded here as it is.

Judgement on the remaining 58 days is deferred to the Day 60 report (on or around 2026-10-06) and the final report after the season closes, in this same format.

All figures are backed by raw JSON and SHA-256 hashes committed alongside this document in the [evidence folder](./2026-09-08_moc-activation-season1-day30-evidence/).
