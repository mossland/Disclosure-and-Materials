## MOC Activation Season 1 — Day 60 보고

**작성일: 2026-10-07** · **지표 관측 시각: 2026-10-07 00:19 UTC**

> 발행일은 본 문서를 포함한 커밋이 이 저장소의 기본 브랜치에 병합된 시각입니다. 작성·관측 시각과 발행 시각이 다를 수 있으며, 본문은 관측 시각을 기준으로 씁니다. Day 60은 예정된 보고 회차명이고, 실제 관측은 시즌 61일차입니다.

### 핵심 요약

* 「MOC Activation Season 1 — 자가지갑 참여 전환 (90일 파일럿)」의 **Day 60 보고**입니다. 시즌 기간은 2026-08-07 ~ 2026-11-05이며, [2026-08-14 공시](./2026-08-14_moc-activation-season1-vote-results.md) 및 [Day 30 보고](./2026-09-08_moc-activation-season1-day30.md)와 같은 지표를 기록합니다.
* **예고된 기한 2026-10-06을 넘겼습니다.** 2026-10-07 관측·작성 시점까지 공시·증빙 커밋·포럼 답글의 이행 묶음이 완료되지 않았습니다. 이 보고는 10월 7일 수집값이며, 10월 6일 시점값으로 소급하지 않습니다. 발행 시점과 정확한 초과 일수는 병합 기록으로 확정됩니다(§5).
* **두 안건의 참여는 baseline과 같습니다.** Season 1과 MIP-1은 각각 **같은 2개 지갑 · 108,988.96676301 MOC**가 참여했고, Day 30 이후 새로 시작된 안건은 공개 목록 전수 조회에서 확인되지 않았습니다. 두 안건 모두 제안자 지갑의 가중치는 99,888.96676301 MOC로 합계의 **91.65%**입니다. 제안을 거듭할수록 참여가 커진다는 전제는 이번 관측까지 확인되지 않았습니다.
* Passport 인증 지갑은 **11개**, 검증 홀더 지갑은 **3개**입니다(Day 30: 11 / 3). 홀더 기준(100 MOC)에 못 미치는 인증 지갑은 8개입니다. **지갑 수는 사람 수가 아닙니다.**
* 종료된 두 안건의 투표 가중 산정 방식은 Day 30 기록과 같습니다. 4표 중 자가 위임 스냅샷 3표·잔고 스냅샷 1표이며, 제3자 위임 표는 0표입니다. 현재 Passport API의 위임 지갑 수는 2입니다.
* 지표의 원본 JSON과 SHA-256 해시는 [증빙 폴더](./2026-10-07_moc-activation-season1-day60-evidence/)에 모았습니다. 9월분 당월 카운터는 10월 관측값과 분리해 §3에 적었습니다.

### 1. 보고 기준

| 구분 | 내용 |
| --- | --- |
| 시즌 | MOC Activation Season 1 (90일 파일럿) |
| 시즌 기간 | 2026-08-07 (비준일) ~ 2026-11-05 |
| 지표 관측 시각 | 2026-10-07 00:19 UTC (시즌 61일차) |
| 예고된 기한 | 2026-10-06 — **초과** (초과 일수는 발행일 기준) |
| 안건 페이지 | <https://agora.moss.land/proposals/6a4decb73697e1a9d307e327> |
| 근거 | 2026-08-14 공시 §5 「Season 1 기간 및 보고 일정」 |

### 2. 참여 지표 (원칙 2 이행)

비준된 원칙 2에 따라, Season 1 baseline과 시즌 중 진행된 안건의 참여를 같은 형식으로 기록합니다.

| 안건 | 투표 기간 (KST) | 참여 MOC (가중) | 참여 지갑 수 | 결과 |
| --- | --- | ---: | ---: | --- |
| Season 1 (baseline) | 2026-07-08 ~ 08-07 | 108,988.96676301 | 2 | 가결 (찬성 100%) |
| MIP-1 생명주기 정책 | 2026-08-19 ~ 09-02 | 108,988.96676301 | 2 | 가결 (찬성 100%) |

Day 30 보고의 「인원」은 투표한 지갑 수입니다. 이번 보고는 이를 「참여 지갑 수」로 명시하며, 고유한 사람 수를 뜻하지 않습니다. 홀더·검증 홀더도 지갑 단위 집계입니다.

**두 안건의 참여 지갑과 가중 합계가 동일합니다.** 지갑은 Day 30 보고와 같은 축약 표기로 적습니다.

| 지갑 | Season 1 산정 방식 | MIP-1 산정 방식 | Voting Power (MOC) |
| --- | --- | --- | ---: |
| `0x1d67e226…4e59c464` (제안자 지갑) | onchain_balance_snapshot | onchain_votes_snapshot | 99,888.96676301 |
| `0xe645cd81…335c60b2` | onchain_votes_snapshot | onchain_votes_snapshot | 9,100.0 |

두 안건에서 제안자 지갑의 가중치 비중은 각각 91.65%입니다. Season 1의 제안자 지갑 1표는 위임 없는 잔고 스냅샷이고, 나머지 3표는 자가 위임 스냅샷입니다. 제3자 위임 표는 0표입니다. 이 구분은 투표 가중치 산정 방식이며, 별도 참여자 4명을 뜻하지 않습니다. 투표 export 두 파일과 MIP-1 안건 레코드는 Day 30 증빙과 바이트 단위로 같습니다.

참여율은 8-14 공시와 같은 수치 기준을 이어가되, 분모의 이름을 바로잡습니다.

| 지표 | 값 | 기준 |
| --- | ---: | --- |
| MOC 총공급 대비 참여율 | 0.0218% | 안건별 참여 MOC / 총공급 500,000,000 MOC |
| Passport 인증 지갑 잔고 합 대비 참여율 | 34.60% | 인증 지갑 잔고 합(지갑별 마지막 인증 시점) 314,988.96676301 MOC |
| 거래소 보관 MOC (운영자 추정치) | 412,218,535.29 (총공급의 82.44%) | Passport 공개 API 제공값; 원칙 3에 따라 구속 투표 밖 |

인증 지갑 잔고 합은 Day 30 보고의 「검증 홀더 잔고」와 같은 값(`behavior.holderBalanceMoc`)입니다. 인증 지갑 전체의 지갑별 마지막 인증 시점 잔고 합이며, 검증 홀더만의 합이나 관측 시각 잔고가 아닙니다. 분자인 안건별 참여 MOC는 종료된 투표의 스냅샷 값이므로 분모와 기준 시점이 다릅니다. Day 30 표기를 이번 보고에서 바로잡습니다. 이 비율을 관측 시각의 활성 이용자 참여율로 해석하지 않습니다.

거래소 보관 MOC는 공개 API의 `behavior.exchangeCustodyMoc`를 옮긴 운영자 추정치입니다. 거래소 지갑의 분류·목록을 이번 증빙에서 독립적으로 재현하지 않았으므로, 전체 거래소 보관량을 독립 검증한 값으로 제시하지 않습니다.

### 3. Passport 채택 지표 (원칙 4 이행)

비준된 원칙 4는 인증·위임·참여·보전 집계의 상시 공개와 월간 요약 공시를 정했습니다. 다섯 시점의 스냅샷을 나란히 놓습니다. 앞의 세 시점은 선행 공시의 증빙에, 9월 말과 이번 관측은 이 보고의 증빙에 있습니다. 2026-09-30 열은 **2026-09-30 23:50 UTC(10월 1일 08:50 KST)**의 관측이며, 9월(UTC) 당월 카운터의 **경계 전 마지막 관측값**입니다. 월말 경계까지 약 9분의 미관측 구간이 있어 최종 확정값으로 부르지 않습니다.

| 지표 | 2026-08-14 | 2026-09-02 | 2026-09-08 (Day 30) | 2026-09-30 | 2026-10-07 (Day 60 보고 관측) |
| --- | ---: | ---: | ---: | ---: | ---: |
| 인증 지갑 | 10 | 11 | 11 | 11 | **11** |
| 홀더 / 검증 홀더 (지갑 수) | 3 / 3 | 3 / 3 | 3 / 3 | 3 / 3 | **3 / 3** |
| 위임 지갑 | 2 | 2 | 2 | 2 | **2** |
| 당월 체크인 | 2 (8월) | 0 (9월) | 2 (9월) | 2 (9월) | **0 (10월)** |
| 당월 활성화 | 0 (8월) | 0 (9월) | 0 (9월) | 0 (9월) | **0 (10월)** |
| Exit Pass 브로드캐스트 (누적) | 1 | 1 | 1 | 1 | **1** |
| 보전 지급 (누적) | 1 | 1 | 1 | 1 | **1** |
| 인증 지갑 잔고 합 (MOC, 지갑별 마지막 인증 시점) | 314,988.96676301 | 314,988.96676301 | 314,988.96676301 | 314,988.96676301 | **314,988.96676301** |
| 누적 스탬프 | — | — | 65 | 65 | **65** |

읽는 법을 함께 적습니다.

* **당월 값은 UTC 월 경계에서 초기화됩니다.** 9월 체크인 2건·활성화 0건과 10월 체크인 0건·활성화 0건은 서로 다른 월의 진행 상태입니다. 누적 증감으로 비교하지 않습니다. 9월 원본의 `behavior.period`는 `2026-09`, 이번 원본은 `2026-10`입니다.
* 인증 지갑 11개와 검증 홀더 지갑 3개의 차이는 홀더 기준 100 MOC 미만인 지갑 8개입니다. 어느 값도 사람 수를 직접 측정하지 않습니다.
* **Exit Pass와 보전 지급은 첫 관측(2026-08-14) 이후 각 1건에서 변동이 없습니다.** 그 1건의 발생일은 이 증빙으로 확정할 수 없습니다. 가장 이른 스냅샷이 시즌 시작(2026-08-07)보다 뒤이므로, 시즌 중 집행 또는 시즌 이전 집행이라고 단정하지 않습니다.
* 공개 집계 API는 `walletsOnchainMatched: 2`와 위임 합계 **108,988.96676301 MOC**를 반환합니다. 이는 API가 보고하는 온체인 대조 결과입니다. 이번 수집은 공개 GET이므로 별도 노드 질의에 의한 독립 검증을 수행했다는 뜻은 아닙니다.

### 4. 시즌 전제에 대한 중간 판정

Season 1은 제안을 거듭하며 참여가 커지는지를 추적하는 90일 파일럿입니다. 8-14 공시가 정한 baseline은 108,988.96676301 MOC / 2개 지갑입니다.

**실제 관측일인 시즌 61일차에도 그 전제는 아직 확인되지 않았습니다.** 비교 안건은 Season 1과 MIP-1 두 건이며 참여 지갑과 가중 합계가 같습니다. Day 30과 이번 관측의 인증 지갑·검증 홀더 지갑·누적 스탬프는 각각 11·3·65로 같습니다. 이 결과로 전체 수요나 고유한 사람 수를 판정하지 않습니다.

남은 29일에 대한 판단은 시즌 종료 후 최종 보고에서 같은 형식으로 이어갑니다.

참여율 계산에 필요한 집계 API의 `proposals[].verifiedMocSum`은 두 안건 모두 **`null`**입니다. 따라서 [관리 목록](../TRACKING.md) #6의 「집계 API가 검증 MOC 합계를 반환」하는 트리거는 이번 관측에서 확인되지 않았습니다. 이 보고는 API의 데이터 상태를 기록하며, 결과 화면의 렌더 여부는 이번 수집의 별도 검증 범위에 포함하지 않았습니다.

### 5. 기한 초과에 대하여

Day 60 보고의 기한은 2026-08-14 공시 §5의 「2026-10-06 전후」, 같은 날 포럼 답글의 「Day 60 보고(2026-10-06)」, [공시 예고 관리 목록](../TRACKING.md) #1의 **2026-10-06**에 명시되어 있었습니다. 공시와 포럼 답글이 기한 안에 공개되지 않아 기한을 넘겼습니다. 이번 보고의 지표 관측은 2026-10-07이며 발행은 병합 시점입니다. 정확한 초과 일수는 병합 기록으로 확정하고, 공시·증빙 커밋·포럼 답글의 세 요소가 모두 확인되기 전에는 #1을 이행 완료로 보지 않습니다.

이 보고는 확인된 지연 사실을 기록합니다. 지연의 근본 원인이나 확인되지 않은 재발 방지 효과를 추정해 적지 않습니다.

남은 예고 항목은 다음과 같습니다.

| 예고 항목 | 트리거 사건 | 담당 | 기한 |
| --- | --- | --- | --- |
| 최종 보고 | 시즌 종료 (2026-11-05) | `MosslandOpenDevs` | 2026-11-19 (종료 +14일) |
| 월간 시즌 요약 | 매월 말일 경과 | `MosslandOpenDevs` | 익월 7일 |

이 표는 [공시 예고 관리 목록](../TRACKING.md)의 발췌입니다. 9월분 월간 요약의 기한은 2026-10-07입니다. 이 보고 §3과 동반 증빙에 그 월의 집계를 담았으며, 갈음 이행과 기한 판정은 실제 발행 시각을 기준으로 #3에 기록합니다. 10월분 기한은 2026-11-07입니다. 기존 담당·기한을 변경하거나 새 항목을 추가하지 않습니다.

### 6. 증빙 (Evidence)

[증빙 폴더](./2026-10-07_moc-activation-season1-day60-evidence/)에는 이번 관측 원본 JSON 7개, 9월 말 관측 원본 JSON 2개, `fetch-metadata.json`, `SHA256SUMS.txt`, `README.md`가 있습니다. 공시와 증빙은 같은 커밋에 포함하는 단위입니다.

수집 시각은 수집자의 기록이며, GitHub 커밋·병합 기록이 정확한 API 수집 시각 자체를 증명하는 것은 아닙니다. 병합 기록은 해당 내용이 늦어도 병합 시점까지 존재했음을 뒷받침합니다. 9월 원본 `transparency-2026-09-30.json`·`connect-stats-2026-09-30.json`의 별도 시각과 수집 시점 해시는 `septemberSnapshot`에, 이번 요청별 시각은 `currentRequests`에 적었습니다. 공개 안건 목록 전수 조회의 범위와 집계 요약은 `proposalInventoryCheck`에 있습니다.

---

## English Summary

**Day 60 report — MOC Activation Season 1 (90-day pilot)**

This report covers the ratified season (2026-08-07 to 2026-11-05), using the same metrics as the [2026-08-14 disclosure](./2026-08-14_moc-activation-season1-vote-results.md) and [Day 30 report](./2026-09-08_moc-activation-season1-day30.md). “Day 60” is the scheduled reporting milestone. The actual observation was **2026-10-07 00:19 UTC (season day 61)**; these are not backdated observations for 2026-10-06.

**The promised deadline of 2026-10-06 has passed.** At the observation and drafting time, the disclosure, evidence commit and forum reply had not been completed as a publication package. Publication is the merge time, which determines the exact disclosure overrun. Tracking item #1 can be closed only after all three elements are verified. The reason for the delay and any preventive effect are not inferred from the observed status.

**Participation matches the baseline:** Season 1 and MIP-1 each received votes from the same two wallets, weighted at 108,988.96676301 MOC. The proposer wallet accounts for 99,888.96676301 MOC, or **91.65%**, in each proposal. Three of the four votes use self-delegation snapshots; the remaining Season 1 vote uses a raw-balance snapshot. No third-party delegation vote is present. The full public proposal listing showed no proposal starting after Day 30. The season premise that participation grows as proposals accumulate is not yet confirmed at this observation (day 61). These are wallet counts, not counts of distinct people.

Passport reports **11 verified wallets, 3 verified-holder wallets and 65 cumulative stamps**, the same values as Day 30. The holder threshold is 100 MOC. Exit Pass broadcasts and reimbursement payments remain one each since the first observation on 2026-08-14. The timing of that single case cannot be determined from these snapshots; this report does not assign it to before or during the season.

The denominator previously labelled “verified holder balance” is corrected to **the sum of verified-wallet balances at each wallet’s last verification**, 314,988.96676301 MOC (`holderBalanceMoc`). It covers all verified wallets, not only holder wallets, and is not a balance snapshot at this report’s observation time. The vote-snapshot numerator and that denominator have different reference times. The resulting ratio is 34.60% and should not be read as an active-user participation rate at the observation time; the share of total token supply is 0.0218%. Exchange custody is an **operator estimate reported by the API**, 412,218,535.29 MOC (82.44% of total supply); the wallet classification and list were not independently reproduced here.

The delegation API reports 2 on-chain-matched wallets and 108,988.96676301 MOC. This reports the API’s result, not a fresh independent node verification. Both proposals’ `verifiedMocSum` values remain `null`, so the data-return trigger for tracking item #6 was not observed. The result screen’s rendering was not separately verified in this collection.

Section 3 includes September’s last observation before the UTC month boundary: **2 check-ins and 0 activations at 2026-09-30 23:50 UTC**. The final roughly nine minutes before the boundary (from 23:50:38 UTC) were not observed. October’s counters at this observation are **0 and 0**; monthly counters reset and should not be read as a cumulative decline. The September summary is due 2026-10-07, and its substitution by this report is recorded against the actual publication time in tracking item #3. The remaining 29 days are assessed in the final report, due 2026-11-19 after the season ends on 2026-11-05; the October summary is due 2026-11-07.

Raw JSON, SHA-256 hashes, request times and source URLs are in the [evidence folder](./2026-10-07_moc-activation-season1-day60-evidence/). Collection times are collector records. The eventual merge record establishes existence by that time, not independent proof of the exact collection times.

---

작성 방식: **AI 보조 · 사람 검토** · [AI 생성 콘텐츠 표시 정책 v1.0](./2026-09-16_ai-content-labelling-policy.md) / Authoring: **AI-assisted · human-reviewed** · [AI-Generated Content Labelling Policy v1.0](./2026-09-16_ai-content-labelling-policy.md)
