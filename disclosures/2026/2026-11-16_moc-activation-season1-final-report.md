## MOC Activation Season 1 — 최종 보고

**최초 작성일: 2026-11-16** · **수정일: 2026-11-24** · **시즌 종료 기준 시각: 2026-11-05 24:00 KST (15:00 UTC)** · 종료 전 마지막 관측: 2026-11-02 02:51 UTC · 종료 뒤 관측: 2026-11-06 01:25 UTC · 보고 시점 관측: 2026-11-15 23:57 UTC (11월 16일 08:57 KST)

> 발행일은 본 문서를 포함한 커밋이 이 저장소의 기본 브랜치에 병합된 시각입니다. 작성·관측 시각과 발행 시각이 다를 수 있으며, 본문은 관측 시각을 기준으로 씁니다. 시즌 종료 기준 시각에 보존한 관측은 없으며, 종료 전후의 관측값을 그대로 종료 시점 값으로 부르지 않습니다(§4).

### 핵심 요약

* 「MOC Activation Season 1 — 자가지갑 참여 전환 (90일 파일럿)」의 **최종 보고**입니다. [2026-08-14 공시](./2026-08-14_moc-activation-season1-vote-results.md) §5가 정한 시즌 전체 지표 요약과 Season 2 여부 판단 자료를 담고, 11월분 월간 시즌 요약도 갈음합니다. 최종 보고의 기한(관리 목록 #2, 2026-11-19)은 지났습니다. 11월분 요약의 별도 기한은 2026-12-07입니다(#3). 발행일은 병합 기록으로 확정됩니다.
* **시즌 종료 기준 시각 직전과 당일에 보존한 관측은 없습니다.** 종료 약 3일 12시간 전(2026-11-02 02:51 UTC)과 약 10시간 26분 뒤(2026-11-06 01:25 UTC)의 관측에서 확인한 지표별 값을 적었습니다(§4).
* **시즌 종료(90일차)까지 시즌 전제는 확인되지 않았습니다.** 비준 뒤 시즌 종료까지 투표가 열린 안건은 MIP-1 한 건이며(11월 16일 공개 안건 목록 전수 조회 기준), 참여는 baseline과 같은 **2개 지갑 · 108,988.96676301 MOC**, 제안자 지갑 비중은 **91.65%입니다**.
* **누적 인증 지갑은 10개(8월 14일)에서 24개(11월 2일)가 되었고, 시즌 종료 다음 날(11월 6일)에는 26개였습니다.** 두 관측만으로는 종료 시점의 인증 지갑 수를 확정할 수 없습니다(§4). 11월 2일 기준 24개 중 16개는 재단의 사후 검토에서 자동화 관련으로 분류했고, 11월 2일 뒤 변동은 분류하지 않았습니다. 원집계는 유지하되 이용 증가로 해석하지 않습니다. **지갑 수는 사람 수가 아닙니다.**
* 홀더 / 검증 홀더 3 / 3, 위임 지갑 2, Exit Pass 브로드캐스트·보전 지급 누적 각 1, 인증 지갑 잔고 합 314,988.96676301 MOC는 8월 14일부터 11월 6일까지 보존한 관측마다 같았습니다. Exit Pass 브로드캐스트와 보전 지급의 각 발생일 및 두 기록이 같은 사례에 해당하는지는 이 집계로 확인할 수 없습니다.
* `verifiedMocSum`은 집계 응답이 공시 증빙에 있는 네 시점(9월 8일·10월 7일·11월 2일·11월 6일)에서 모두 `null`이었고(#6 트리거 미관측), 보고 시점 관측에서는 두 안건 모두 `null`입니다. **이 보고는 Season 2 진행 여부를 정하지 않습니다**(판단 자료는 §7).
* 보고 시점 관측의 원본과 SHA-256 해시는 [증빙 폴더](./2026-11-16_moc-activation-season1-final-report-evidence/)에, 표에 인용한 이전 공개 응답은 해당 공시의 증빙 폴더에 있습니다.

### 1. 보고 기준

| 구분 | 내용 |
| --- | --- |
| 시즌 | MOC Activation Season 1 (90일 파일럿) |
| 시즌 기간 | 2026-08-07 (비준일) ~ 2026-11-05 |
| 시즌 종료 기준 시각 | 2026-11-05 24:00 KST (15:00 UTC) — §4 |
| 대상 기간 | 시즌 전체 · 11월분(11월 1일\~시즌 종료일 11월 5일, 당월 카운터는 UTC 월 기준) |
| 종료 전후 관측 | 2026-11-02 02:51 UTC (87일차) · 2026-11-06 01:25 UTC (종료 다음 날) |
| 보고 시점 관측 | 2026-11-15 23:57 UTC (11월 16일 08:57 KST) — 시즌 종료 뒤, 세 가지 확인에만 인용(§4) |
| 기한 | 최종 보고(#2)는 2026-11-19(종료 +14일) 기한을 넘김. 11월분 요약(#3)의 기한은 2026-12-07 |
| 안건 페이지 | <https://agora.moss.land/proposals/6a4decb73697e1a9d307e327> |
| 근거 | 2026-08-14 공시 §5 「Season 1 기간 및 보고 일정」 · [공시 예고 관리 목록](../TRACKING.md) #2 · 11월분은 원칙 4와 #3 |

### 2. 참여 지표 (원칙 2 이행)

원칙 2에 따라 baseline과 시즌 중 안건의 참여를 [Day 60 보고](./2026-10-07_moc-activation-season1-day60.md)와 같은 형식으로 적습니다.

| 안건 | 투표 기간 (KST) | 참여 MOC (가중) | 참여 지갑 수 | 결과 |
| --- | --- | ---: | ---: | --- |
| Season 1 (baseline) | 2026-07-08 ~ 08-07 | 108,988.96676301 | 2 | 가결 (찬성 100%) |
| MIP-1 생명주기 정책 | 2026-08-19 ~ 09-02 | 108,988.96676301 | 2 | 가결 (찬성 100%) |

비준 뒤 시즌 종료까지 투표가 열린 안건은 MIP-1 한 건이며(11월 16일 공개 안건 목록 전수 조회 기준), Season 1 투표는 시즌을 비준한 투표로 비준일에 끝났습니다. 11월 16일 01:07 UTC에 별도로 공개 안건 목록의 마지막 페이지까지 조회한 결과 전체 42건이었고, MIP-1(2026-08-19 시작) 뒤 시즌 종료 전에 시작한 안건은 없었습니다. 9월 2일 뒤 시즌 종료까지 투표가 열린 안건은 없었습니다(요약은 증빙 `fetch-metadata.json`의 `proposalInventoryCheck`).

**두 안건의 참여 지갑과 가중 합계가 같습니다.**

| 지갑 | Season 1 산정 방식 | MIP-1 산정 방식 | Voting Power (MOC) |
| --- | --- | --- | ---: |
| 제안자 지갑 | onchain_balance_snapshot | onchain_votes_snapshot | 99,888.96676301 |
| 다른 1개 지갑 | onchain_votes_snapshot | onchain_votes_snapshot | 9,100.0 |

제안자 지갑의 가중치 비중은 두 안건 모두 91.65%입니다. 4표 중 3표는 자가 위임 스냅샷, Season 1의 제안자 지갑 1표는 위임 없는 잔고 스냅샷이고 제3자 위임 표는 0표입니다. 이 구분은 가중치 산정 방식이며 별도 참여자 4명을 뜻하지 않고, 참여 지갑 수도 고유한 사람 수가 아닙니다. 축약 주소와 투표 원본은 Day 60 보고 §2와 그 증빙에 있습니다.

| 지표 | 값 | 기준 |
| --- | ---: | --- |
| MOC 총공급 대비 참여율 | 0.0218% | 안건별 참여 MOC / 총공급 500,000,000 MOC |
| Passport 인증 지갑 잔고 합 대비 참여율 | 34.60% | 인증 지갑 잔고 합(지갑별 마지막 인증 시점) 314,988.96676301 MOC |
| 거래소 보관 MOC (운영자 추정치) | 412,416,770.50 (총공급의 82.48%) | 2026-11-06 01:25 UTC Passport 공개 API 제공값; 원칙 3에 따라 구속 투표 밖 |

분자는 종료된 투표의 스냅샷 값, 분모는 지갑별 마지막 인증 시점의 잔고 합이어서 기준 시점이 다르므로 이 비율을 관측 시각의 활성 이용자 참여율로 해석하지 않습니다. 거래소 보관 MOC는 공개 API의 `behavior.exchangeCustodyMoc`를 옮긴 운영자 추정치이며, 지갑 분류와 목록을 독립 검증하지 않았습니다.

### 3. Passport 채택 지표 (원칙 4 이행)

원칙 4에 따라 시즌 기간과 종료 직후에 공개 경로([Passport Transparency](https://passport.moss.land/transparency)와 그 API)의 응답 원본이 공시 증빙에 있는 8개 시점을 모두 싣고(원본: [8월 14일](./2026-08-14_moc-activation-season1-vote-evidence/) · [9월 2일](./2026-09-02_mip-1-lifecycle-policy-vote-evidence/) · [9월 8일](./2026-09-08_moc-activation-season1-day30-evidence/) · [9월 30일·10월 7일](./2026-10-07_moc-activation-season1-day60-evidence/) · [10월 14일·11월 2일·11월 6일](./2026-11-06_moc-activation-season1-october-summary-evidence/) 증빙 폴더), 증빙에 응답이 없는 칸은 '—'와 각주로 둡니다. 표는 이 보고가 쓰는 종료 뒤 관측인 11월 6일(01:25 UTC) 열에서 끝납니다.

| 지표 | 2026-08-14 | 2026-09-02 | 2026-09-08 (Day 30) | 2026-09-30 | 2026-10-07 (Day 60) | 2026-10-14 | 2026-11-02 | 2026-11-06 (종료 뒤) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 인증 지갑 | 10 | 11 | 11 | 11 | 11 | 24 | 24 | 26 |
| 홀더 / 검증 홀더 (지갑 수) | 3 / 3 | 3 / 3 | 3 / 3 | 3 / 3 | 3 / 3 | 3 / 3 | 3 / 3 | 3 / 3 |
| 위임 지갑 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| Exit Pass 브로드캐스트 (누적) | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 보전 지급 (누적) | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 인증 지갑 잔고 합 (MOC, 지갑별 마지막 인증 시점) | 314,988.96676301 | 314,988.96676301 | 314,988.96676301 | 314,988.96676301 | 314,988.96676301 | 314,988.96676301 | 314,988.96676301 | 314,988.96676301 |
| 누적 스탬프 | —¹ | —¹ | 65 | 65 | 65 | —² | 117 | 126 |
| 벽 등재 항목 (건, 가린 항목 2 포함) | —¹ | —¹ | 19 | —³ | 19 | 27 | 27 | 30 |
| 거래소 보관 MOC (API 운영자 추정, 지갑 9개) | 412,701,334.83 | 416,426,769.48 | 412,654,465.41 | 412,591,581.50 | 412,218,535.29 | 412,889,535.28 | 412,845,844.44 | 412,416,770.50 |

¹ 8월 14일·9월 2일 증빙의 Passport 응답은 Transparency뿐입니다.\
² 10월 14일에는 스탬프 집계 응답을 보존하지 않았습니다. 재단 내부 기록의 같은 날 값은 117입니다([10월 요약](./2026-11-06_moc-activation-season1-october-summary.md) §2 각주).\
³ 9월 30일(23:50 UTC 관측)의 벽 응답은 증빙에 없습니다. 같은 수집의 벽 원문이 Day 30 증빙 `wall.json`과 같다는 대조는 [2026 Q3 보고서](https://mossland.github.io/Disclosure-and-Materials/disclosures/2026-q3/) §7.2에 있습니다.

당월 카운터는 UTC 월 경계에서 초기화되므로(`behavior.period`는 관측 시각의 UTC 월) 월별로 따로 적고, 서로 다른 달을 누적 증감으로 비교하지 않습니다.

| 월 (UTC) | 당월 체크인 | 당월 활성화 (보전 신청) | 값의 성격 |
| --- | ---: | ---: | --- |
| 2026년 8월 | 2 | 0 | 8월 14일 06:34 UTC 진행값(8월 1일부터 세어 시즌 전 날짜 포함), 월말 관측 없음 |
| 2026년 9월 | 2 | 0 | 9월 30일 23:50 UTC, 경계 약 9분 전 마지막 관측값(최종 확정값 아님) |
| 2026년 10월 | 15 | 0 | 10월 14일 04:54 UTC 마지막 보존 관측값. 체크인은 그 뒤 늘지 않았다는 추정(내부 기록에 의존해 공개 집계만으로 재현할 수 없음, 확정값 아님), 활성화는 그 뒤 공개 집계로 확인할 수 없음(10월 요약 §3) |
| 2026년 11월 시즌분 (11-01 00:00 ~ 11-05 15:00 UTC) | 0 → 2 | 0 → 0 | 각각 11월 2일과 11월 6일 관측값. 시즌 종료 시점의 두 카운터 값은 미확정(§4) |

읽는 법을 함께 적습니다.

* 인증 지갑과 검증 홀더 지갑의 차이(8월 14일 7개, 11월 6일 23개)는 홀더 기준 100 MOC 미만인 지갑이며, 어느 값도 사람 수를 직접 측정하지 않습니다.
* **Exit Pass와 보전 지급은 2026-08-14부터 11월 6일까지 보존한 관측마다 누적 각 1건이었습니다.** 첫 관측이 시즌 시작보다 뒤여서 각 기록의 발생일과 시즌 귀속을 확정할 수 없습니다. 두 누적 집계만으로는 두 기록이 같은 사례인지도 확인할 수 없습니다.
* 공개 집계 API는 응답이 공시 증빙에 있는 네 시점(9월 8일·10월 7일·11월 2일·11월 6일)에서 `walletsOnchainMatched: 2`와 위임 합계 108,988.96676301 MOC를 반환했습니다. API가 보고하는 결과이며 별도 노드 질의에 의한 독립 검증이 아니고, 위임 지갑과 투표 지갑이 같은지는 대조하지 않았습니다.
* 벽 등재 항목은 서명 기록의 수이며 지갑 수가 아닙니다. 8개 시점 가운데 증빙에 벽 응답이 있는 다섯 시점 모두 주소·원문·서명을 가린 같은 2건을 포함하고, 19건(9월 8일·10월 7일)과 27건(10월 14일·11월 2일)은 각각 `id` 집합이 같으며, 11월 6일 조회는 다음 쪽이 빈 전체 목록입니다.
* 변화는 절대 수로만 적고, 인증 지갑·스탬프·벽 항목의 증가를 이용이나 참여의 확대로 해석하지 않습니다(§5).

### 4. 시즌 종료 기준 시각과 11월분

**기준 시각.** 시즌 기간은 비준일(투표 종료 2026-08-07 16:57 KST)부터 날짜로 정해졌고 Day 30 보고의 일차 계산(9월 8일 = 32일차)으로 11월 5일이 90일차이므로, 이 보고는 그날의 끝인 2026-11-05 24:00 KST(15:00 UTC)를 시즌 종료 기준 시각으로 씁니다.

**관측.** 시즌 종료 직전과 당일에 보존한 관측은 없습니다. 종료 전 마지막 관측(11월 2일 02:51 UTC, 87일차)은 기준 시각보다 약 3일 12시간 앞이고, 종료 뒤 보존 관측 가운데 이 보고가 시즌 표와 종료 시점 대조에 쓰는 관측(11월 6일 01:25 UTC)은 약 10시간 26분 뒤입니다. 11월 6일 01:19 UTC에 먼저 읽은 응답은 수집 도구의 벽 쪽 넘김이 불완전해(같은 쪽을 두 번 조회) 증빙에 넣지 않았고, 당월·누적값은 01:25 UTC 관측과 같습니다(10월 요약 §3). 관측 공백은 수집 측의 사정이며, 근본 원인이나 재발 방지 효과를 추정해 적지 않습니다.

**종료 시점의 지표별 처리.** 두 관측의 공개 응답을 필드별로 대조했습니다.

* **종료 전후 관측이 같은 지표:** 홀더 / 검증 홀더 3 / 3, 위임 지갑 2(API 대조 2개 지갑 · 108,988.96676301 MOC), Exit Pass·보전 지급 누적 각 1, 인증 지갑 잔고 합 314,988.96676301 MOC, 11월 활성화 0건. 두 관측의 값이 같아도 그 사이인 종료 시각의 값은 확인할 수 없습니다.
* **종료 전에 생성되어 11월 6일 벽에 남아 있던 기록:** 전체 목록 **30건**(공개 28 · 가림 2)의 `createdAt`은 모두 기준 시각 전이며, 이 가운데 **11건**이 Mossverse 연결 항목입니다. 11월 2일 목록의 27건은 모두 같은 `id`로 남아 있었고, 새 3건은 11월 5일 09:35\~09:39 UTC의 Mossverse 연결이었습니다(가장 늦은 항목은 09:39 UTC). 조회 전에 삭제된 항목 수는 알 수 없습니다. 연결 수는 벽 연결 항목의 `createdAt` 기준이며(연결이 모두 벽에 기록된다는 대응은 추론입니다), 연결 집계(`connectByService`)는 두 응답이 함께 공시 증빙에 있는 네 시점(9월 8일·10월 7일·11월 2일·11월 6일)에서 벽의 서비스별 연결 항목 수와 같았습니다.
* **두 관측의 값이 다른 지표:** 11월 2일과 11월 6일에 각각 인증 지갑은 24개와 26개, 누적 스탬프는 117개와 126개, 11월 체크인은 0건과 2건이었습니다. 공개 집계에는 변동 시각이 없어 시즌 종료 시점의 값이나 가능한 범위를 확정할 수 없습니다.
* 어느 경우든 두 관측 사이에 추가와 삭제가 상쇄됐을 가능성은 공개 집계로 배제할 수 없습니다. 거래소 보관 MOC는 계속 바뀌는 운영자 추정치여서 종료 시점 값으로 적지 않습니다.

**보고 시점 관측.** 시즌 뒤의 값이므로 시즌 표에 넣지 않고 세 가지 확인에만 씁니다(보고 시점의 공개 안건 목록·설문 목록 조회는 이와 별도이며 §2·§7에 적습니다). 11월 6일 목록에서 시즌 종료 전 생성된 것으로 확인한 벽 항목 30건이 모두 같은 `id`로 남아 있었습니다. 공개 설정 응답의 `activation`·`exitPass` 부분은 공시 증빙의 8개 시점에서 같았고, 보고 시점 관측에서는 2026-08-14 관측과 같았습니다. 이 보고는 이 기능들의 종료나 변경을 정하지 않습니다. 셋째인 `verifiedMocSum`은 §6에 적고, 시즌 종료 뒤 기록된 벽 항목과 카운터 값은 시즌 지표로 세지 않습니다.

**11월분 갈음.** 이 절과 §3의 11월 행이 11월분 월간 시즌 요약(11월 1일\~시즌 종료일 11월 5일, 기한 2026-12-07)을 갈음합니다. 11월 당월 카운터는 2026-11-01 00:00 UTC(11월 1일 09:00 KST)부터 세므로, 11월 1일 00:00 KST부터 09:00 KST 직전까지의 활동은 10월 카운터에 속하며 10월 요약 §3의 범위입니다. 보전 지급은 11월 2일과 11월 6일 01:25 UTC 관측에서 모두 누적 1건이었습니다. 갈음 이행과 기한 판정은 실제 발행 시각을 기준으로 [관리 목록](../TRACKING.md) #3에 기록합니다. 갈음은 이행이지만 기한을 지우지 않습니다.

**12월 1일 경계.** 이 보고로 11월분을 갈음하므로 시즌 1 월간 요약을 위한 12월 1일 월 경계 관측은 계획하지 않았습니다. 11월 당월 카운터 가운데 시즌 종료 뒤 부분은 시즌 지표로 보고하지 않습니다.

### 5. 자동화 관련 기록의 분류

[2026 Q3 보고서](https://mossland.github.io/Disclosure-and-Materials/disclosures/2026-q3/) §7.2와 [10월 요약](./2026-11-06_moc-activation-season1-october-summary.md) §4의 분류를 잇습니다.

* 원집계는 유지합니다. 누적으로는 11월 2일 기준 인증 지갑 24개 중 16개(7월 29일 점검분 3개와 10월의 13개)가 재단의 사후 검토에서 자동화 관련으로 분류된 기록이며, 10월 7일→14일 증가분의 지표별 분류는 10월 요약 §4의 표에 있습니다.
* 분류는 내부 기록에 의존하며 공개 집계에서 재현할 수 없습니다. 자동화의 주체·목적·사용 도구는 이 집계로 확인할 수 없습니다.
* 10월 14일 점검 기준으로 이 기록이 보전 지급·위임·안건 투표를 바꾼 흔적은 없습니다.
* 11월 2일과 11월 6일 관측 사이의 변동(인증 지갑 +2, 서비스 연결 +3, 누적 스탬프 +9, 11월 체크인 2건)은 분류하지 않았고, 이 변동을 이용 증가로 해석하지 않습니다.

### 6. 시즌 전제에 대한 최종 판정

안건은 「참여율은 작게 시작해 시즌 동안 제안을 거듭할수록 커지는 것」을 목적으로 밝히고 참여율 상승이 「제안을 거듭하며」 나타난다고 전제했으며, 8-14 공시는 108,988.96676301 MOC / 2개 지갑을 baseline으로 기록했습니다.

**시즌 종료(90일차)까지 그 전제는 확인되지 않았습니다.** 비준 뒤 시즌 종료까지 투표가 열린 안건은 MIP-1 한 건이며(11월 16일 공개 안건 목록 전수 조회 기준), 참여 지갑과 가중 합계가 baseline과 같습니다. 검증 홀더 지갑은 첫 관측부터 11월 6일까지 보존한 관측마다 3개였습니다. 10월 7일과 11월 2일 관측을 비교하면 인증 지갑·누적 스탬프·벽 등재 항목이 늘었습니다. 이 지표들은 등록 활동을 집계합니다. 10월 7일\~14일 증가분은 대부분 자동화 관련으로 분류됐고, 11월 2일과 11월 6일 관측 사이의 변동은 분류하지 않았습니다(§5).

이 결과로 전체 수요나 고유한 사람 수를 판정하지 않습니다. 시즌 전체의 사실은 §7에 모았습니다.

집계 API의 `proposals[].verifiedMocSum`은 집계 응답이 공시 증빙에 있는 네 시점(9월 8일·10월 7일·11월 2일·11월 6일)에서 두 안건 모두 **`null`이었으므로**, [관리 목록](../TRACKING.md) #6의 「집계 API가 검증 MOC 합계를 반환」하는 트리거는 이 관측들에서 확인되지 않았습니다. 보고 시점 관측에서는 두 안건 모두 `null`입니다. 이 보고는 API의 데이터 상태를 기록하며, 결과 화면의 렌더 여부는 검증 범위에 포함하지 않았습니다.

### 7. Season 2 여부 판단 자료

2026-08-14 공시 §5에 따라 비준된 원칙별로 확인한 내용을 정리합니다. 시즌 종료 뒤의 관측은 해당 관측일을 함께 적었습니다.

| 원칙 | 확인한 내용 | 근거 |
| --- | --- | --- |
| 1. 출금 비용 보전만 | 보전 지급·Exit Pass 누적 각 1건, 8월 14일\~11월 6일 각 관측에서 같은 값(발생일 미확정). 월별 당월 활성화 관측값은 모두 0건 | §3 |
| 2. 참여 지표 표시 | 결과 화면의 참여 MOC·투표 지갑 수 표기는 Day 30 보고 §4에 기록. 참여율(%) 표시에 필요한 `verifiedMocSum`은 집계 응답이 공시 증빙에 있는 네 시점(9월 8일·10월 7일·11월 2일·11월 6일)에서 모두 `null`(#6 트리거 미관측) | §6 · [Day 30 보고](./2026-09-08_moc-activation-season1-day30.md) §4 |
| 3. 구속 투표 = 자가지갑만 | 비준 뒤 시즌 종료까지 구속 투표가 열린 안건 1건(MIP-1, §2의 확인 범위), 참여 2개 지갑. 거래소 보관 MOC는 운영자 추정치로 구속 투표 밖(§2). 비구속 시그널·설문: 11월 16일 01:07 UTC에 별도로 조회한 공개 설문 목록(`/api/polls`)은 0건(원본은 증빙). 11월 6일 벽 전체 목록 30건의 항목 종류는 소유 증명·서비스 연결·재게시뿐이고 시그널 투표 기록은 없음. Passport 밖 채널은 확인하지 않음 | §2 · §3 |
| 4. 지표 공개 | §3의 8개 시점 공개 응답을 공시 증빙에 보존(가동률은 집계하지 않음). 월간 공시: 8월분 2일 초과(Day 30 보고 갈음), 9월분 당일(Day 60 보고 갈음), 10월분 당일, 11월분 이 보고 갈음(판정은 #3). Day 30 보고 3일 초과, Day 60 보고 1일 초과. 보존 관측 공백: 8월 월말 관측 없음, 9월 경계 전 약 9분, 10월 경계 전 약 17일 19시간, 시즌 종료 전후(§4) | [관리 목록](../TRACKING.md) #0 · #1 · #3 |

이 보고는 Season 2 진행 여부를 정하지 않습니다. Season 1 비준 안건은 90일 파일럿 한 시즌을 채택했고 [MIP-1](./2026-09-02_mip-1-lifecycle-policy-vote-results.md)은 승인하지 않는 것으로 Season 2를 명시했으므로, 두 안건 모두 Season 2를 승인하지 않았습니다.

### 8. 기한과 예고 항목

최종 보고의 기한은 시즌 종료 14일 후인 **2026-11-19**였으며 이미 지났습니다. [공시 예고 관리 목록](../TRACKING.md) #2는 공시 문서·증빙 커밋·Agora 포럼 답글 세 가지가 모두 확인되면 이행한 것으로 봅니다(2026-08-14 공시 §5). 공시의 발행 시각은 병합 기록으로 확정합니다. #2의 실제 이행일과 지연 일수는 공시 병합과 포럼 답글 게시 가운데 늦은 쪽의 KST 날짜로 기록합니다. 11월분 요약(#3)은 2026-12-07이 별도 기한이며, 이 보고의 실제 병합일(KST)을 기준으로 판정합니다.

| 예고 항목 | 트리거 사건 | 담당 | 기한 |
| --- | --- | --- | --- |
| 참여율(%) 화면 표시 — 데이터 연동 완료 시 공시 | 집계 API가 검증 MOC 합계를 반환 | `MosslandOpenDevs` | 트리거 +14일 |

이 표는 [공시 예고 관리 목록](../TRACKING.md)의 발췌입니다. 기존 담당·기한을 변경하거나 새 항목을 추가하지 않습니다.

### 9. 증빙 (Evidence)

[증빙 폴더](./2026-11-16_moc-activation-season1-final-report-evidence/)에는 2026-11-15 23:57 UTC (11월 16일 08:57 KST) 보고 시점 관측의 원본 JSON 6개(벽의 다음 쪽 포함)와 공개 설문 목록 원본 1개, `fetch-metadata.json`, `SHA256SUMS.txt`, `README.md`가 있습니다. 그 전 관측은 각 공시의 증빙 폴더에 있어 다시 넣지 않았습니다. 공개 안건 목록의 응답 본문은 넣지 않았고, 조회 범위와 요약은 이번 최종 보고 증빙의 `fetch-metadata.json` 중 `proposalInventoryCheck`에 있습니다. 공시와 증빙은 같은 커밋에 포함하는 단위입니다.

수집 시각은 수집자의 기록이며, GitHub 커밋·병합 기록이 정확한 API 수집 시각 자체를 증명하는 것은 아닙니다. 병합 기록은 해당 내용이 늦어도 병합 시점까지 존재했음을 뒷받침합니다. `health.json`은 조회 시각의 상태 응답일 뿐 가동률 집계가 아닙니다. 자동화 관련 분류에 쓰인 내부 기록은 증빙에 포함하지 않았습니다.

---

## English Summary

**Final report — MOC Activation Season 1 (90-day pilot)**

Season 1 ran from 2026-08-07 to 2026-11-05. As required by §5 of the [2026-08-14 disclosure](./2026-08-14_moc-activation-season1-vote-results.md), this final report summarizes the season’s metrics and provides evidence for a decision on Season 2. It also substitutes for the November monthly season summary. The final report deadline of 2026-11-19 has passed (tracking item #2). The November summary has a separate deadline of 2026-12-07 (#3). The report was first drafted on 2026-11-16 and revised on 2026-11-24. Its publication date is the date it merges into the repository’s default branch. The dates below identify when the measurements were taken.

**No observation was preserved immediately before or on the season end.** The season was set in dates from the ratification day (the vote ended 2026-08-07 16:57 KST); counting days as the Day 30 report did (8 September = day 32), 5 November is day 90, so this report uses the end of that day, 2026-11-05 24:00 KST (15:00 UTC), as the season-end reference time. The last preserved observation before it, 2026-11-02 02:51 UTC (day 87), is about 3 days and 12 hours earlier; among the preserved observations after it, the one this report uses for the season tables and the season-end comparison, 2026-11-06 01:25 UTC, is about 10 hours and 26 minutes later. An earlier read at 01:19 UTC on 2026-11-06 was not placed in the evidence because the collector's wall paging was incomplete (the same page was fetched twice); its monthly and cumulative values are the same as at 01:25 UTC (October summary §3). The gap is on the collection side; its root cause and any preventive effect are not inferred.

**The season end is handled metric by metric**, comparing the public responses of the two observations field by field. The following values were the same in both observations, with no measurement at the reference time: holder / verified-holder wallets 3 / 3, delegated wallets 2 (API match: 2 wallets, 108,988.96676301 MOC), cumulative Exit Pass broadcasts and reimbursement payments 1 each, the verified-wallet balance sum 314,988.96676301 MOC and 0 November activations. The complete 2026-11-06 wall list contained **30 records created before the cutoff** (28 public and 2 withheld), including **11 Mossverse connection records**. It still contained all 27 items from the 2026-11-02 list. The 3 additional items were Mossverse connections recorded between 09:35 and 09:39 UTC on 2026-11-05, with the latest at 09:39 UTC. These times come from each record’s `createdAt` field. The list cannot show whether other items were removed before the 6 November read. The per-service counts matched `connectByService` at all four observations with both responses (2026-09-08, 2026-10-07, 2026-11-02 and 2026-11-06). The evidence does not establish that every connection was recorded on the wall. On 2 November and 6 November, respectively, verified wallets numbered 24 and 26, cumulative stamps totalled 117 and 126, and November check-ins totalled 0 and 2. The public aggregates do not give the times of the changes, so they establish neither the season-end counts nor bounds on those counts. In every case, offsetting additions and removals between the two observations cannot be excluded from public counts. Exchange custody, a changing operator estimate, is not given as a season-end value.

**Participation in the two proposals did not move from the baseline.** The only proposal with a vote open after the ratification and before the season end is MIP-1 (per the full public proposal listing read on 2026-11-16); the Season 1 vote ratified the season and closed on the ratification day. The separate public proposal-listing check at 01:07 UTC on 16 November returned 42 proposals across all pages, none of which started after MIP-1 (started 2026-08-19) and before the season end; no proposal had a vote open after 2 September up to the season end (summary in `proposalInventoryCheck` of the evidence `fetch-metadata.json`). Season 1 and MIP-1 both drew the same two wallets and 108,988.96676301 MOC; the proposer wallet's 99,888.96676301 MOC is **91.65%** of each and the other wallet's 9,100.0 MOC the remainder. Three of the four votes use self-delegation snapshots and the proposer wallet's Season 1 vote a raw-balance snapshot without delegation; there is no third-party delegation vote. This is how weight was computed, not four separate participants, and participating-wallet counts are not counts of distinct people. Abbreviated addresses and vote exports are in the [Day 60 report](./2026-10-07_moc-activation-season1-day60.md) §2 and its evidence. Participation is 0.0218% of total supply (500,000,000 MOC) and 34.60% of the verified-wallet balance sum at each wallet's last verification (314,988.96676301 MOC); numerator and denominator have different reference times, so this is not an active-user participation rate at the observation time. Exchange custody, 412,416,770.50 MOC across 9 wallets (82.48% of total supply) at 2026-11-06 01:25 UTC, is an operator estimate reported by the API (`behavior.exchangeCustodyMoc`) and is outside binding votes under Principle 3; its wallet classification and list were not independently verified.

**The Passport table shows all 8 time points, during and just after the season, whose public responses are in the disclosure evidence**, from 2026-08-14 to 2026-11-06; raw files are in the evidence folders linked in §3, and cells with no response in the evidence are marked '—' (the only Passport response in the 2026-08-14 and 2026-09-02 evidence is Transparency; no stamp-count response was preserved on 2026-10-14, although the Foundation’s internal record shows 117, as noted in October summary §2; the 2026-09-30 23:50 UTC wall response is not in the evidence, and the [2026 Q3 report](https://mossland.github.io/Disclosure-and-Materials/disclosures/2026-q3/) §7.2 records that the wall file from the same collection is identical to the Day 30 evidence `wall.json`). The table ends at the 2026-11-06 (01:25 UTC) column, the post-season observation used here. Verified wallets rose from 10 (2026-08-14) to 24 (2026-10-14, 2026-11-02) and were 26 on 2026-11-06, the day after the season end (the season-end count is unknown, §4); the holder, delegation, Exit Pass, reimbursement and balance-sum rows showed the same values at each preserved observation. Cumulative stamps were 65 on 2026-09-08, 2026-09-30 and 2026-10-07, 117 on 2026-11-02 and 126 on 2026-11-06. The exchange-custody row (API operator estimate, 9 wallets) reads 412,701,334.83 (2026-08-14), 416,426,769.48 (2026-09-02), 412,654,465.41 (2026-09-08), 412,591,581.50 (2026-09-30), 412,218,535.29 (2026-10-07), 412,889,535.28 (2026-10-14), 412,845,844.44 (2026-11-02) and 412,416,770.50 MOC (2026-11-06). The verified/verified-holder difference (7 on 2026-08-14, 23 on 2026-11-06) is wallets below the 100 MOC holder threshold; neither value directly measures people. Every preserved observation from 2026-08-14 to 2026-11-06 recorded one cumulative Exit Pass broadcast and one cumulative reimbursement payment. The earliest observation was after the season began. These counters do not establish when either event occurred, whether it fell within the season, or whether the two records refer to the same case. The delegation API returned 2 on-chain-matched wallets and 108,988.96676301 MOC at the four points whose responses are in the disclosure evidence (2026-09-08, 2026-10-07, 2026-11-02, 2026-11-06) — the API's reported result, not an independent verification by a separate node query; whether delegated and voting wallets are the same was not checked. Wall items are signature records, not wallets: of those 8 points, all five with a wall response in the evidence include the same 2 withheld items; the 19 items (2026-09-08, 2026-10-07) and the 27 items (2026-10-14, 2026-11-02) each have identical id sets on both of their dates; and the 2026-11-06 list is complete, with an empty next page. Changes are given as absolute counts and are not read as growth in use or participation.

**Monthly counters reset at the UTC month boundary** (`behavior.period` is the observation's UTC month) and are listed by month, not compared cumulatively. August: 2 check-ins and 0 activations (reimbursement requests) at 06:34 UTC on 14 August, counted from 1 August and so including pre-season days; no month-end observation. September: 2 and 0 at 23:50 UTC on 30 September, about 9 minutes before the boundary, not a final figure. October: 15 and 0 at the last preserved observation (04:54 UTC on 14 October); check-ins are estimated not to have risen afterwards (an estimate that depends on internal records, cannot be reproduced from public counts and is not a final figure), and activations after that could not be confirmed from public counts (October summary §3). November season portion (2026-11-01 00:00 to 2026-11-05 15:00 UTC): check-ins totalled 0 on 2 November and 2 on 6 November. Activations were 0 at both observations. The values of both counters at the season end are unknown.

**The post-season observation at 2026-11-15 23:57 UTC (08:57 KST on 16 November) was used for three checks.** The season tables end with the 6 November observation. The public proposal and poll listings were read separately on 2026-11-16 at 01:07 UTC, as described in §2 and under Principle 3. The 30 wall items recorded before the season end were all still present with the same ids. The `activation` and `exitPass` parts of the public configuration were the same at all 8 points in the disclosure evidence, and at the report-time observation they were the same as on 2026-08-14. This report does not decide to end or change these features. The third check, `verifiedMocSum`, is covered below; wall items and counter values recorded after the season end are not counted as season metrics.

Under Principle 4 (tracking item #3), **this report substitutes for the November monthly summary** (1 November to the season end on 5 November; due 2026-12-07) through §4 and the November row of §3. The November counter starts at 2026-11-01 00:00 UTC, exactly 09:00 KST on 1 November. Activity from 00:00 KST up to but excluding 09:00 KST that day belongs to the October counter covered by the October summary §3. The cumulative reimbursement payment count was 1 both on 2 November and at the 2026-11-06 01:25 UTC observation. Tracking item #3 uses the KST date of this report’s actual merge to determine whether the November summary met its deadline. Because this report covers the November season summary, no 1 December month-boundary observation was planned for that purpose. November activity after the season ended is outside the season metrics.

**Automation-related records.** Following the [2026 Q3 report](https://mossland.github.io/Disclosure-and-Materials/disclosures/2026-q3/) §7.2 and the [October summary](./2026-11-06_moc-activation-season1-october-summary.md) §4, the original counts are retained. Cumulatively, 16 of the 24 verified wallets as of 2026-11-02 (3 from the 2026-07-29 check and 13 from October) are records the Foundation classified as automation-related in its subsequent reviews; the per-metric table for the 2026-10-07 to 2026-10-14 increase is in the October summary §4. The classification depends on internal records and cannot be reproduced from public counts; the actor, purpose and tools cannot be determined from these counts. The 2026-10-14 review found no evidence that the records classified as automation-related affected reimbursement payments, delegations or proposal votes. The changes between the 2026-11-02 and 2026-11-06 observations were not classified. Verified wallets rose by 2, service connections by 3 and cumulative stamps by 9, while the November check-in counter rose from 0 to 2. These changes do not establish growth in usage. **Wallet counts are not counts of people.**

**The season premise was not confirmed by the season end (day 90).** The proposal anticipated that voting participation would start small and grow as more proposals came to a vote. The 2026-08-14 disclosure recorded a baseline of 108,988.96676301 MOC from 2 wallets. The only proposal with a vote open after the ratification and before the season end, MIP-1 (per the full public proposal listing read on 2026-11-16), drew the same wallets and weight, and verified-holder wallets numbered 3 at every preserved observation through 2026-11-06. The 2 November observation showed more verified wallets, cumulative stamps and wall items than the 7 October observation. These increases concern registrations and activity recorded on Passport. Voting participation stayed at the baseline. The Foundation classified most of the 2026-10-07 to 2026-10-14 increases as automation-related. Changes between 2026-11-02 and 2026-11-06 were not classified. The aggregates do not establish the season-end counts of verified wallets, stamps or November check-ins (§4). This result does not determine overall demand or the number of distinct people. `proposals[].verifiedMocSum` was `null` for both proposals at the four points whose aggregation responses are in the disclosure evidence (2026-09-08, 2026-10-07, 2026-11-02, 2026-11-06), so the trigger for tracking item #6 (the aggregation API returns the verified MOC sum) was not observed in them; at the report-time observation both were still `null`. This records the API's data state; rendering of the result screen was not verified.

**Evidence for a Season 2 decision, by principle.** The observations below are dated individually, including those made after the season ended. Principle 1 (compensation limited to withdrawal-fee reimbursement): the counters showed 1 reimbursement payment and 1 Exit Pass broadcast at every preserved observation from 2026-08-14 to 2026-11-06. The date of each event is unknown. Every observed monthly activation counter was 0. Principle 2 (participation metrics displayed): the result screen's display of participating MOC and voting-wallet count was recorded in the [Day 30 report](./2026-09-08_moc-activation-season1-day30.md) §4; `verifiedMocSum`, needed for a percentage display, was `null` at all four points whose aggregation responses are in the disclosure evidence (2026-09-08, 2026-10-07, 2026-11-02, 2026-11-06; #6 trigger not observed). Principle 3 (binding votes from self-custody wallets only): one proposal with a binding vote open after the ratification and before the season end (MIP-1, within the §2 checking scope), from 2 wallets; exchange custody is an operator estimate outside binding votes (above); non-binding signals and surveys: the separate 16 November read of the public poll list (`/api/polls`) returned an empty list (raw response in the evidence). The complete 2026-11-06 wall list (30 items) holds only ownership-proof, service-connection and republication items, with no signal-vote records; channels outside Passport were not checked. Principle 4 (metrics published on Passport Transparency): public responses at the 8 points in §3 are preserved in the disclosure evidence (availability is not tallied); monthly summaries were 2 days late for August (Day 30 report), on the due date for September (Day 60 report) and October, and substituted by this report for November (judged in #3); the Day 30 report was 3 days late and the Day 60 report 1 day late; gaps in preserved observations are the missing August month-end observation, about 9 minutes before the September boundary, about 17 days and 19 hours before the October boundary, and around the season end (§4). **This report does not decide whether a Season 2 will run.** The Season 1 ratification adopted one 90-day pilot season and [MIP-1](./2026-09-02_mip-1-lifecycle-policy-vote-results.md) named Season 2 among what it does not approve, so neither proposal approved a Season 2.

**Deadline and tracking.** The final report deadline was **2026-11-19**, 14 days after the season end, and has passed (#2). The commitment is one package of disclosure, evidence commit and Agora forum reply (2026-08-14 disclosure §5), and #2 is not treated as fulfilled until all three are confirmed; the later of the merge and the forum reply, in KST, determines the fulfilment date and the number of days late for #2. The November summary has its own deadline of 2026-12-07 (#3), assessed against the KST date of the report’s actual merge. The excerpt of the [tracking list](../TRACKING.md) in this report is item #6 (participation-rate (%) screen display, disclosed when the data integration is complete; trigger: the aggregation API returns the verified MOC sum; `MosslandOpenDevs`; trigger + 14 days). No owner or deadline is changed and no new item is added.

The [evidence folder](./2026-11-16_moc-activation-season1-final-report-evidence/) holds 6 raw JSON files (including the wall’s next page) from the 2026-11-15 23:57 UTC observation (08:57 KST on 16 November), plus 1 raw poll-list response from the separate 01:07 UTC check on 16 November. It also contains `fetch-metadata.json`, `SHA256SUMS.txt` and `README.md`. Earlier observations remain in their original evidence folders. The `proposalInventoryCheck` field in this report’s `fetch-metadata.json` records the scope and results of the proposal-listing check. The proposal-listing response bodies are not included. The disclosure and its evidence are one unit in the same commit. Collection times are collector records; the eventual merge record establishes existence by that time, not the exact collection times. `health.json` is a status response, not an availability tally. Internal records used for the automation classification are not included.

---

작성 방식: **AI 보조 · 발행 전 사람 검토 예정** · [AI 생성 콘텐츠 표시 정책 v1.0](./2026-09-16_ai-content-labelling-policy.md) / Authoring: **AI-assisted · human review pending before publication** · [AI-Generated Content Labelling Policy v1.0](./2026-09-16_ai-content-labelling-policy.md)
