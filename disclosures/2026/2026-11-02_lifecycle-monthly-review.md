## MIP-1 생명주기 월 1회 검토 결과 — 2026년 10월

**작성일: 2026-11-02** · **관측 시각: 2026-11-02 15:41~16:41 KST**

> 발행일은 본 문서를 포함한 커밋이 이 저장소의 기본 브랜치에 병합된 시각입니다. 작성·관측 시각과 발행 시각이 다를 수 있으며, 본문은 관측 시각을 기준으로 씁니다.

**관측 기준:** registry와 서비스 상태는 2026-11-02 15:57 KST, Q3 공개 파일·대시보드 배포 파일·Algora 보존 정리 기록은 같은 날 15:47 KST이고, 그 밖의 공개 페이지·RSS는 같은 날 15:41~16:41 KST에 확인했습니다. 완료일은 실제 공개 반영일입니다. §6의 links 반영 기록과 §4의 MOSS.AO 소개글 정정 안내만 이 관측 뒤, 병합 전의 값입니다.

**근거:** [MIP-1 결과 공시](https://github.com/mossland/Disclosure-and-Materials/blob/main/disclosures/2026/2026-09-02_mip-1-lifecycle-policy-vote-results.md) 제4조의 월 1회 검토와 [공시 예고 관리 목록](https://github.com/mossland/Disclosure-and-Materials/blob/main/disclosures/TRACKING.md) #5입니다.

**용어:** registry = links.moss.land가 공개하는 공식 서비스 목록 파일 · lifecycle = MIP-1이 정한 등급(Core 상시 운영 / Beta 운영 중·변동 가능 / Lab 실험 / Archive 종료·보존) · 부담당자 = 담당자와 함께 배포·복구 권한을 갖는 두 번째 담당자(MIP-1 제2조) · statusUrl = 서비스별 상태 확인 주소 · note = registry에 적는 서비스별 메모 · health = statusUrl이 돌려주는 상태 응답 · 칩 = links 목록 카드의 표시 · ④-N = Q3 §1.2의 ‘④ 공시·집계 체계 정비’ 산출물 번호. 끝에 Z가 붙은 시각은 UTC이며, 한국 시각은 9시간을 더합니다.

### 핵심 요약

- **공개 기한 2026-10-31을 넘겨 발행했습니다.** 사유는 §7에 적었습니다. 이 문서의 값은 11월 2일 관측값이며, 10월 31일 시점값으로 소급하지 않습니다. 정확한 초과 일수는 병합일 기준으로 확정합니다.
- 검토 대상은 공식 registry에서 생명주기 등급이 있는 **17개 서비스**입니다. 9월과 같이 Beta 8 · Lab 7 · Archive 2 · Core 0이며, 등급 변경은 없습니다. Algora의 운영 상태 표기는 10월 12일 `operational`에서 `deprecated`로 바뀌었습니다([links PR #37](https://github.com/MosslandOpenDevs/links/pull/37)). 기존 Archive 등급을 새로 부여한 것은 아닙니다.
- **Algora(AI 에이전트 실험 서비스로, MOC 보유자가 투표하는 Mossland Agora와 별개입니다)는 10월 12일 읽기 전용 아카이브로 전환했습니다.** City의 일일 기록 안내 정정은 10월 9일, City의 Algora 대응은 10월 12일 반영했습니다. Signal의 설명 정정은 10월 12일, 기본 AI 안내는 10월 15일 반영했습니다.
- **Alpha의 AI 답글·질문 화면(Ask) 표시와 MOSS.AO의 기본 AI 안내는 10월 21일 배포했습니다.** Alpha의 두 표시 오류는 정책 §7의 7일을 넘겨 인지 후 25일 만에 정정했고, 8월 28일 MOSS.AO 소개글에는 7일을 넘겨 11월 6일 정정 안내를 붙였습니다(§4). Medium 글 4건의 작성 방식 표시 누락은 11월 2일 정정했습니다(§4). 공시 대시보드의 9월 지적 표기 5곳과 Q3 분기 데이터 연동은 10월 23일 반영했습니다. 재단 지갑 밖 수량의 온체인 산출 근거는 10월 19일 Q3 보고서와 함께 공개했습니다. 이 날짜들로 Q3 말 판정을 바꾸지 않습니다.
- 부담당자 미지정, Alpha의 호스트 밖 백업·일부 설명·사이트 전역 표준 AI 안내, MOSS.AO의 `approved` 표현, 대시보드 시장 영역 표기, Media의 표현 차이, AO의 상태 확인 범위 등은 남아 있습니다. registry 검토 시각은 이 문서 병합 전에 11월 2일 관측 시각 `2026-11-02T06:57:06Z`로 갱신했습니다. 이전 값에서 33일 뒤이며 10월 안의 시각은 아닙니다(§6).
- 이번 회차에는 **Beta 8개의 제3조 예외와 Signal의 실험 칩을 유지**합니다. 9월에서 넘어온 Algora의 과거 삭제·내용 가림에 대한 정책 적용 판단은 이번에도 결론 내지 못해 미결로 남기고, registry 밖 추가 검토 대상은 이름 공개를 보류하고 내부 목록으로 관리하며, 이번 회차에 처리 결과를 확정한 대상은 없습니다(§5).

### 1. 검토 대상과 상태 응답

[공식 registry](https://links.moss.land/ecosystem-registry.json)는 30개 항목 중 17개에 `lifecycle`을 부여합니다. 나머지 13개는 외부 링크·자료 항목입니다. 17개 중 `statusUrl`이 있는 서비스는 16개이며, Media에는 없습니다. 공개 화면에서 숨겨진 registry 행도 검토 대상에 포함했습니다.

| 서비스 | lifecycle | registry 운영 상태 | 11/2 15:57 KST 상태 응답 및 이번 회차 확인점 |
|---|---|---|---|
| Mossland | Beta | operational | HTTP 200 · `ok` |
| Disclosure | Beta | operational | HTTP 200 · `ok` · 표기 정정과 Q3 분기 카드 반영 |
| Passport | Beta | beta | HTTP 200 · `ok` |
| Agora | Beta | operational | HTTP 200 · `ok` |
| links | Beta | operational | HTTP 200 · `ok` · 응답 시각은 빌드 시각 |
| Mossverse | Beta | beta | HTTP 200 · `ok` |
| Alpha | Beta | operational | HTTP 200 · `ok` · 기본 호출은 `worst_status: not_evaluated`, 상세 호출은 `warn` |
| SignalMap | Beta | operational | HTTP 200 · `ok` |
| Signal | Lab | beta | HTTP 200 · `ok` · AI 안내 반영, 실험 칩 유지 중 |
| City | Lab | operational | HTTP 200 · 자체 `status` 없이 자매 서비스 6개 상태 집계 · Algora는 `archived: true` |
| NPC | Lab | operational | HTTP 200 · `ok` |
| Recipe | Lab | operational | HTTP 200 · `ok` |
| MOSS.AO | Lab | operational | HTTP 200 · `ok` · 등재 주소의 하위 구성요소 점검 부재는 계속됨 |
| BRIDGE | Lab | operational | HTTP 200 · `ok` · 수집 `enabled: true`, 최근 처리 시각 있음 |
| Governance Monitor | Lab | operational | HTTP 200 · `ok` · 응답 시각은 빌드 시각 |
| Media | Archive | deprecated | statusUrl 없음 · 종료 기록으로 유지 |
| Algora | Archive | deprecated | HTTP 200 · `ok` · `archived: true`, 정지 시각 `2026-10-12T03:04:37Z` |

HTTP 200과 `ok`는 조회 시점의 응답이며, 월간 가동률이나 모든 작업의 성공을 뜻하지 않습니다. 10월 20일 01시께~04시 반께(KST) 일부 서비스가 네트워크 문제로 응답하지 않았다가 복구됐습니다(내부 기록 기준). 이 검토는 서비스별 가동 이력을 집계하지 않습니다. links와 Monitor의 `timestamp`는 각각의 `buildTime`과 같고, Algora는 아카이브 응답입니다. Alpha 상세 점검은 12개 중 11개 `ok`·1개 `warn`이며, 경고 항목은 호스트 밖 사본이 없는 `db_backup`입니다.

### 2. 제3조 부담당자 예외

Beta 8개는 모두 `secondMaintainer`가 지정되지 않았고, 각 `lifecycleReason`에 제3조 예외 사유가 남아 있습니다. 9월 이후 registry에 부담당자 지정이나 Core 승격은 없습니다.

| 대상 | 현재 기록 | 10월 검토 결정 |
|---|---|---|
| Mossland · Disclosure · Passport · Agora · links | 부속서 A의 Core 후보, 부담당자 미지정 시 Beta 게시 | Beta와 제3조 예외 유지 |
| Mossverse · Alpha | 부속서 A의 Beta, 부담당자 미지정 | Beta와 제3조 예외 유지 |
| SignalMap | 부속서 A의 Beta, Core 지향, 부담당자 미지정 | Beta와 제3조 예외 유지 |

10월 검토에서는 Beta 8개의 기존 분류와 제3조 예외를 유지합니다. 담당자·부담당자의 배포·복구 권한 요건을 확인하기 전에는 Core로 승격하지 않습니다.

### 3. 9월에 남긴 차이의 처리 결과

아래 표는 [9월 월검토](https://github.com/mossland/Disclosure-and-Materials/blob/main/disclosures/2026/2026-09-30_lifecycle-monthly-review.md) §5·§6의 후속입니다.

| 항목 | 11월 2일까지 확인한 조치 | 남은 차이 또는 확인 사항 |
|---|---|---|
| Algora의 Archive 분류와 실제 동작 | 10/12 12:04 KST 실시간 앱 정지·읽기 전용 아카이브 전환. 10,734개 공개 경로와 기존 인용 URL의 보존 검증. 홈페이지·links·Monitor·City의 관련 표시 반영. Algora 화면의 `Running`·`LIVE` 표시는 아카이브 안내로 대체(11/2 공개 HTML 기준) | 이전 보존 정리·내용 가림과 정책의 관계, 재시작 때 사라진 결론 문서 목록은 아래 별도 기록. registry `lifecycleReason`의 `best-effort-frozen` 표현과 links Algora 카드의 ‘실험’ 칩은 남아 있음. Algora 안에서 자동 생성된 기존 제안의 `passed`(표결 없음)·`voting` 표기는 읽기 전용 기록에 그대로 보존(아카이브 안내: 자동 처리로 정해진 상태이고, MOC 보유자의 투표 기록은 없으며, 모스랜드의 공식 거버넌스 결정이 아님) |
| Alpha 호스트 밖 백업 | 11/2 상세 health에서 `db_backup: warn`, 호스트 밖 사본 없음 표시를 재확인 | 호스트 밖 사본 없음 재확인. 복원 시험 완료 근거는 확인하지 못함. 9월의 Q4 이월 상태 유지 |
| Alpha brief와 registry note | 영문 9/28·9/29 페이지는 11/2 기준 HTTP 200이고 sitemap 등재 확인 | 영문 9/14는 여전히 404. 11/2 관측에서 registry note는 8/23의 `worst_status: ok` 관측을 유지해 현재 `warn`과 차이. note 정정은 §6의 links 반영에 포함 |
| BRIDGE 홈 고정 예시 | 9월 정정은 기존 완료로 유지. 11/2 health에서 수집 활성 확인. 11/2 홈에서 고정 데모 활동 미노출 재확인 | 공개 [README](https://github.com/MosslandOpenDevs/bridge-2026#readme)의 운영 방향 검토 일정 가운데 지난 10월 20일 항목이 11/2 현재 그대로 남아 있음 |
| Signal 카운터·실험 칩·AI 안내 | 설명·출처 정정 10/12, 기본 AI 안내·정책 링크 10/15 반영. 이번 회차는 Lab 등급의 실험 서비스임을 알리기 위해 ‘실험’ 칩 유지. 과거 홈의 빈 피드·카운터 미표시를 유지 사유로 삼지 않음 | 11/2 페이지 원문(초기 HTML)은 `00`이나 브라우저에서는 실제 값과 피드가 표시됨. [links README](https://github.com/MosslandOpenDevs/links#readme)의 빈 피드·데이터 등장 후 칩 제거 예시는 현재 결정에 맞춘 정정이 남음 |
| City 일일 기록 안내 | 10/9 실제 기록 방식에 맞춰 안내·시뮬레이션 표시 정정. 10/12 Algora 아카이브 대응 별도 배포. 11/2 홈의 자동 기록 미운영·Algora 읽기 전용 안내 유지 확인 | 자정 기록 기능을 새로 가동한 것으로 세지 않음 |
| Media의 `Absorbed` 표현 | Archive와 종료 기록 유지 | registry에 `Absorbed into SignalMap` 표현이 남음. 서비스 전체 이전과 편집 원칙 계승을 구별하는 문구 정정 미반영 |
| AO 등재 상태 주소 | 기본 AI 안내는 10/21 반영. 11/2 등재 health 응답 재확인 | 등재 `/api/health`가 하위 구성요소 점검을 보여주지 않는 한계 유지. 별도 `/api/status`의 처리 지표는 Q3 §12.1에 10/16 관측으로 기록되어 있으며, 이번 회차에 재관측하지 않음 |
| 공시 대시보드 표기 5곳 | 10/23 화면 배포와 유통 일정 영문 설명 반영 | 당시 지적 5곳은 수정. 새로 확인한 시장 영역·다른 일정 행의 차이는 §4에 기록 |
| registry 검토 시각 | 이 문서 병합 전에 갱신해 links에 반영(§6) | 10월 안의 검토 시각은 없음 |

#### Algora 전환과 과거 기록의 범위

10월 12일 전환은 신호 수집·대화 기록 생성·보존 정리 작업이 계속되던 실시간 앱을 정지하고, 전환 시점의 공개 응답을 읽기 전용으로 제공한 조치입니다. 11월 2일 health에서도 `archived: true`와 같은 정지 시각을 확인했습니다. MIP-1의 기존 Archive 분류와 현재 운영 동작 사이의 차이를 줄였으나, 과거 삭제와 수정의 정책상 취급까지 일괄 해결한 것으로 판단하지 않습니다.

[공개 아카이브의 보존 정리 기록](https://algora.moss.land/api/activity?type=SYSTEM_STATUS)에서 확인 가능한 10월 1~11일 11회 실행은 보존 기간이 지난 행 합계 **171,041행**을 삭제했다고 보고합니다. 대부분(133,112행)은 실행 기록이 `noise`로 구분한 활동 로그이고, 나머지는 그 밖의 활동 로그·신호·에이전트 대화이며, 제안·이슈·세션 기록은 이 실행 기록의 대상 목록에 없습니다. 공개 응답에 10월 12일 실행 기록이 없어 이 합계를 정지 시점까지의 전체 삭제량으로 확정하지 않으며, 삭제의 적합성을 뜻하지도 않습니다.

이번 회차는 현재의 읽기 전용 전환과 관련 화면 반영을 완료로 기록하되, 9월에 기록한 내용 가림(실존 인물 이름 가림·중립 안내문 전환)과 과거 보존 정리에 대한 MIP-1 적용 판단은 별도 미결 항목으로 남깁니다. 9월에 10월 회차 확인 사항으로 남긴 이 판단을 이번 회차에도 결론 내지 못했습니다. 관련 조항과 당시 기록을 대조해 삭제·개인정보 정정의 처리 기준을 검토하며, 다음 회차까지 결론을 확정하겠다는 새 기한은 두지 않습니다. 이 쟁점과 별도로, 앞선 재시작 때 소실된 메모리 결론 문서 공개 목록은 아카이브 전환으로 복원되지 않았습니다.

### 4. Q3 보고서에서 넘겨받은 공개 후속

#### AI 표시와 설명 정정

| 서비스 또는 발행물 | 실제 반영일 | 반영 범위 | 남은 조치 |
|---|---|---|---|
| Signal 설명 | 10/12 | 화면·소개·방법론·공유 설명을 Manifold의 플레이머니 기반 공개 확률과 AI 추정 비교로 정정. 현재 피드에 연결된 온체인 시장·고래 포지션이 없음을 설명. 게시 전 사람 검토를 보장하는 표현도 정정 | 모델·채점 로직 변경으로 세지 않음 |
| Signal 기본 AI 안내 | 10/15 | 한국어·영어·일본어 안내와 정책 링크 | 실험 칩은 Lab 성격을 이유로 유지(§3) |
| Alpha | 10/21 | 답글의 AI 페르소나 표시, Ask의 자동 생성 예시 질문 안내 | 사이트 전역의 정책 §4 표준 안내는 이 정정 범위에 포함되지 않았고, 11/2 확인한 5개 페이지의 공개 HTML 기준 미반영(정책 §9 순차 반영 대상). 페르소나 가격 설명의 추가 안내도 미반영 |
| MOSS.AO 웹 | 10/21 | 기본 AI 안내와 정책 링크, 한국어·영어 화면 확인 | 점수에 따라 자동으로 붙는 `approved` 등 상태 표현과 실제 사람 판단의 구별은 추가 정정 대상 |
| 8/28 MOSS.AO 소개글 [국문](https://medium.com/p/7d2175e1714f)·[영문](https://medium.com/p/3081df113e3e) | 11/6 | 두 글 본문 끝(관련 링크 앞)에 정정 안내를 붙임([공개 RSS](https://medium.com/feed/mossland-blog)로 확인): 공개 코드 기준으로 아이디어 승격과 계획의 `approved` 표시는 자동으로 처리되고, 자동 승인 점수에 못 미친 계획만 사람의 승인을 기다림 | 9월 26일 점검에서 확인한 표현으로 정책 §7의 7일 기준을 넘겨 안내함(아래). 제목·본문의 ‘사람이 선택하는’ 취지 표현은 고치지 않고 그대로 남아 있음 |
| Medium 글 4건: 10/23 Signal 소개글 [국문](https://medium.com/p/001f5d3a6198)·[영문](https://medium.com/p/71d44a793891), 10/30 Q3 요약 [국문](https://medium.com/p/fbea7e65bfb0)·[영문](https://medium.com/p/e3940ffd5b7b) | 11/2 | Q3에서 넘겨받은 항목이 아닌 10월 발행물의 정정. AI 보조로 작성했으나 발행 때 말미 작성 방식 표시가 없었음. 11/2 네 글 모두 표시와 정책 링크, 표시 추가 안내를 넣음(공개 RSS로 확인) | 작성 방식 표시 건의 남은 조치 없음 |

Alpha의 두 표시 오류는 9월 26일 인지했으며, 정책 §7의 인지 후 7일 기한을 넘겨 10월 21일(인지 후 25일) 정정했습니다. Signal의 사람 검토 관련 설명은 10월 12일 정정했습니다. 8월 28일 MOSS.AO 소개글의 표현도 같은 9월 26일 점검에서 확인했으며(Q3 §B), 정책 §7의 7일 기준을 넘겨 11월 6일 두 글 본문 끝(관련 링크 앞)에 정정 안내를 붙였습니다. 기본 AI 안내의 순차 적용에는 정책 §9에 따른 별도 일괄 기한이 없으므로, 이 기한 초과와 구별합니다.

추가 설명 정정 일부는 11월 2일 현재 반영되지 않았습니다. Alpha 페르소나 가격 설명의 추가 안내는 확인한 페이지의 공개 HTML에 없고 AO의 `approved` 표현은 그대로이며, 완료한 AI 안내와 분리해 기록합니다. 그 밖의 문구는 화면을 항목별로 재확인하지 못해 완료로 기록하지 않습니다.

#### ④-1 대시보드와 보고서의 공통 데이터

**공개 반영일은 2026-10-23입니다.** 대시보드 Q3 분기 카드가 보고서의 [development-data.json](https://mossland.github.io/Disclosure-and-Materials/disclosures/2026-q3/development-data.json)을 읽도록 반영했습니다. 배포 당시 확인한 값은 전체 3,409 · 공개 1,232 · 비공개 2,177커밋과 공개 저장소 PR 477건(봇 PR 포함, Q3 §6.3 기준)입니다.

11월 2일 재확인에서 공개 JSON은 HTTP 200이고, 공개 [해시 파일](https://mossland.github.io/Disclosure-and-Materials/disclosures/2026-q3/development-data.json.sha256) 및 승인된 파일과 일치했습니다. 같은 시각 대시보드 배포 파일에도 해당 URL과 동일한 해시 고정값이 있었습니다.

`SHA-256: bbc756a2135a2904b1ac1775d1fd85bd81a7feb53c166117fdc53aa9d4fde4f5`

Q3 분기 카드와 기존 개발 지표는 집계 기간·공개 범위·집계 방식이 다르므로 두 수치를 같은 모집단으로 해석하지 않습니다. 이번 후속 반영은 Q3 말 ④-1 미완료 판정을 소급 변경하지 않으며, Q4의 새 과제로 다시 세지 않습니다.

대시보드의 유통계획상 월말 상한·재단 지갑 설명·유통계획 일정·개발 지표 표기와 2026년 11월 일정의 영문 설명은 10월 23일 수정했습니다. 같은 배포에서 9월 목록 밖의 표기도 일부 정리했습니다. **시장 영역의 ‘유통량/총발행량 (24h)’ 표기는 남아 있습니다(24시간 값이 아닌 비율에 붙은 표기, 11/2 배포 파일 기준).** 유통 일정의 영문 설명은 11월 2일 공개 응답 5개 행에 누락이 없습니다. 응답에 나오지 않는 다른 일정 행의 누락은 10월 23일 기록이며 이번에 재확인하지 못했습니다. 이번 완료를 대시보드 모든 표시의 정합 완료로 확대하지 않습니다. 유통계획 일정은 실제 온체인 이체나 지급 예고와 구별합니다.

#### ④-4 온체인 산출 근거의 공개 확인

**공개 후속 완료일은 2026-10-19입니다.** 기준 블록·공개 지갑 목록·정수 산식·결과값을 담은 [onchain-supply.json](https://mossland.github.io/Disclosure-and-Materials/disclosures/2026-q3/onchain-supply.json)을 Q3 보고서와 함께 공개했습니다. 이 자료의 산출 대상은 Q3에서 정의한 재단 지갑 밖 수량이며, 시장 전체의 유통량과 동일한 개념으로 넓히지 않습니다.

11월 2일 재확인에서 보고서와 근거 6개, 총 7개 파일은 모두 HTTP 200이었고 승인된 공개 파일과 SHA-256이 일치했습니다. 온체인 근거 파일의 값은 다음과 같습니다.

`SHA-256: 4504006265e1f5fdc7bac92dc67c789f7aba18a3be378cbf44dd58dbe3a53225`

이 재확인은 파일 일치 확인이며 새로운 온체인 재산출이 아닙니다.

### 5. MIP-1 이행 기록과 Q4 과제

#### MIP-1 사후 사례 갱신

이번 기록은 [Q3 보고서 §A.6](https://mossland.github.io/Disclosure-and-Materials/disclosures/2026-q3/)의 MIP-1 수동 사후 사례 1건을 갱신합니다. 의결 뒤 작성한 사후 기록이라는 성격을 유지하며, 신규 live 사례나 ④-2 에이전트 결정 사례에 더하지 않습니다.

| 항목 | 이번 회차 기록 |
|---|---|
| 의도한 변화 | 생명주기 등급·운영 책임·공개 설명의 연결 |
| 추가 확인된 이행 | Algora 읽기 전용 전환 및 관련 화면 대응, City·Signal 설명 정정, 대시보드 표기 후속 반영 |
| 남은 부분 | 부담당자 예외, Media 설명, AO 상태 확인 범위, 과거 Algora 삭제·내용 수정의 정책상 취급 등 |
| 실행과 검증 | AI 보조로 내부 실행 기록과 공개 응답을 대조함. 별도 검증자가 확인한 사례로 표시하지 않음 |
| 갱신 범위 | 확인된 이행과 잔여 사항을 추가 기록. 과거 삭제·가림의 정책상 처리는 미결로 유지하며, MIP-1 전체 조항의 이행 완료로 확대하지 않음 |

#### Q4 서비스 정리와 표시 정합

Q3 §13이 내부 목표로 정한 Q4 과제는 **공통 데이터 소비와 제품 전환**, **서비스 정리와 표시 정합**의 두 개입니다. 이 월검토는 두 번째 과제 가운데 이번 회차에 확인한 항목의 처리 결과를 남기며, 첫 번째 과제는 이번 회차에 판정하지 않습니다. Q3 §13의 기준에 따라 10월에 이미 마친 정정은 과제 ②의 새 성과로 다시 세지 않습니다.

| 검토 범위 | 현재 처리 결과 |
|---|---|
| 9월 월검토 §5·§6의 표기 차이 | §3·§4에 항목별 완료일과 잔여 차이 기록 |
| 이미 공개한 registry 밖 호스트 5곳(comply · flow · null · pf · sv) | 9/27~29 정리 사실은 9월 결과로 유지. 10월 새 정리 실적으로 세지 않음 |
| 그 밖의 registry 밖 서비스와 관련 기록 | 새 대상 이름 공개는 보류. 이번 회차에 처리 결과를 확정한 대상은 없으며, 처리 방침과 조치는 검토 중(아래 문단) |

Q3 §13.1의 인증서 투명성 기록 기준 전수 대조와 공식 안내 설명의 전면 대조는 이번 회차에 하지 않았습니다. 달성 여부는 Q4 리포트의 스코어카드에서 판정합니다.

Alpha의 핵심 작업·MCP를 SignalMap으로 이전하는 검토(Q3 §13의 다섯 조건 기준)와 Alpha의 공개 release 읽기는 이번 회차에 확인하지 않았습니다.

**registry 밖 대상과 관련 문서.** 9월에 이름을 공개한 5곳 밖의 registry 밖 대상은 내부 목록으로 관리하며, 이번 회차에 처리 결과를 확정해 완료로 기록한 대상은 없습니다. 처리 방침과 조치는 검토 중이고, 관련 공개 문서의 오래된 링크·상태 표현 정리도 아직 반영하지 않았습니다. 처리 결과가 확정된 대상은 그 회차의 월검토에 기록하고, 이름의 공개 범위는 처리 결과를 확인한 뒤 정합니다(Q3 §13.1). 이 문단은 현재 가동 중인 호스트 전체 목록이나 서비스 개수를 뜻하지 않습니다.

Q3 §7.2에 적은 대로 Passport의 분기 후 인증 지갑 증가에는 자동화 관련 분류 기록이 포함되므로 이용 증가로 해석하지 않습니다(이번 회차에 재측정하지 않음).

### 6. registry 갱신과 다음 회차

11월 2일 15:57 KST 공개 registry의 `lifecycleReviewedAt`은 `2026-09-30T06:40:00Z`이고, 파일 SHA-256은 아래와 같습니다. 이 값은 이번 갱신 전 관측입니다.

`494a509c5f7ea851415a11be068c553adfae44041482512af499fa1ad20b0681`

이 값은 `MosslandOpenDevs/links`에서 이 파일을 마지막으로 바꾼 [PR #38](https://github.com/MosslandOpenDevs/links/pull/38)(병합 커밋 `c7e7583`, 10월 12일 14:42 KST)의 파일과 같습니다. 9월 검토 뒤의 파일 변경은 [PR #37](https://github.com/MosslandOpenDevs/links/pull/37)(병합 커밋 `ac397b1`, 10월 12일 12:05 KST, Algora 상태)과 PR #38(Signal 설명)입니다.

이 문서를 병합하기 전에 `lifecycleReviewedAt`을 이번 회차 registry 관측 시각 `2026-11-02T06:57:06Z`로 갱신해 links에 반영했습니다(`MosslandOpenDevs/links` [PR #39](https://github.com/MosslandOpenDevs/links/pull/39), 커밋 `0b67119`, 2026-11-06 20:12 KST 배포 확인). 반영 뒤 공개 파일 SHA-256은 아래와 같습니다.

`69d78556da441f63fddc55dffb144cfa8f55c348becbc2f24dc3bf097892e056`

이 시각은 이전 값 `2026-09-30T06:40:00Z`에서 33일 뒤이고(links 저장소 검증 스크립트의 월 1회 기준 35일 이내), 10월 안의 검토 시각은 없습니다. 10월 31일이나 그 이전 시각으로 소급하지 않습니다. 같은 반영에서 Alpha note의 8월 23일 관측값을 이번 관측값(상세 호출 `worst_status: warn`, `seo_pages` 2,540)으로 정정했고, Signal의 ‘실험’ 칩은 이번 결정에 따라 유지합니다. 그 밖의 등급·칩·`statusUrl`·다른 서비스의 note는 바꾸지 않았습니다.

| 공개 의무 | 현재 회차 기한 | 이 문서의 처리 |
|---|---|---|
| TRACKING #5 생명주기 월검토 | 기한 2026-10-31 초과 | 이 문서와 같은 PR에서 초과 표기·사유와 10월분 이행 링크, 11월분 기한 2026-11-30을 반영 |
| TRACKING #3 10월 시즌 요약 | 2026-11-07 | 별도 발행. 이 월검토로 대체하지 않음 |
| TRACKING #2 Season 1 최종 보고 | 2026-11-19 | 별도 발행 |

차기 월검토에서는 §3·§4의 잔여 항목과 Q4 서비스 정리 결과를 다시 확인합니다. 기한이 별도로 정해지지 않은 실행 항목을 다음 월검토일까지 모두 완료하겠다는 새 약속으로 해석하지 않습니다. MIP-1 제4조에 따라 이 검토 결과를 2026 Q4 리포트에도 기재합니다.

### 7. 기한 초과에 대하여

10월분 검토 결과의 공개 기한은 [공시 예고 관리 목록](https://github.com/mossland/Disclosure-and-Materials/blob/main/disclosures/TRACKING.md) #5의 **2026-10-31**이었습니다. 이 문서는 그 기한을 넘겨 발행했습니다. 초안은 기한 전에 준비했으나 발행 전 사람 검토·승인이 기한 안에 끝나지 않았습니다. 발행은 병합 시점이고, 정확한 초과 일수는 병합 기록의 KST 날짜 기준으로 확정해 TRACKING #5에 적습니다.



### 8. 확인 경로와 관련 링크

* [links.moss.land](https://links.moss.land/) · [registry JSON](https://links.moss.land/ecosystem-registry.json) · [registry 스키마](https://links.moss.land/ecosystem-registry.schema.json)
* [MosslandOpenDevs/links](https://github.com/MosslandOpenDevs/links) — registry 변경 이력: [PR #37](https://github.com/MosslandOpenDevs/links/pull/37) · [PR #38](https://github.com/MosslandOpenDevs/links/pull/38) · [PR #39](https://github.com/MosslandOpenDevs/links/pull/39)
* 서비스별 statusUrl: registry의 `statusUrl` 필드(16개). 하위 점검: `https://alpha.moss.land/api/health?detail=1&strict=1`
* [Algora 보존 정리 기록](https://algora.moss.land/api/activity?type=SYSTEM_STATUS) · [Medium RSS](https://medium.com/feed/mossland-blog)
* [2026 Q3 리포트](https://mossland.github.io/Disclosure-and-Materials/disclosures/2026-q3/) §13·§B · [9월 월검토](https://github.com/mossland/Disclosure-and-Materials/blob/main/disclosures/2026/2026-09-30_lifecycle-monthly-review.md) · [MIP-1 결과 공시](https://github.com/mossland/Disclosure-and-Materials/blob/main/disclosures/2026/2026-09-02_mip-1-lifecycle-policy-vote-results.md)
* [공시 예고 관리 목록(TRACKING)](https://github.com/mossland/Disclosure-and-Materials/blob/main/disclosures/TRACKING.md) #5 · [AI 생성 콘텐츠 표시 정책 v1.0](https://github.com/mossland/Disclosure-and-Materials/blob/main/disclosures/2026/2026-09-16_ai-content-labelling-policy.md)

---

### English Summary

**MIP-1 Lifecycle Monthly Review — October 2026**

This is the October round of the monthly registry review required by MIP-1 Article 4. Values are as of 2 November 2026, 15:41–16:41 KST, except the links update record and the MOSS.AO correction notice, which are later. Times ending in Z are UTC; add nine hours for KST.

- **This review was published after its public deadline of 31 October 2026.** The draft was prepared before the deadline, but human review and approval before publication were not completed by the deadline (§7). Values come from the 2 November observation and are not backdated to 31 October. Publication is the merge time, and the exact number of days over is set by the merge date (KST) and recorded in TRACKING #5.
- The review covers the 17 services with a lifecycle classification in the official registry: 8 Beta, 7 Lab, 2 Archive and no Core. There was no lifecycle classification change. Algora's operational status changed to `deprecated` on 12 October ([links PR #37](https://github.com/MosslandOpenDevs/links/pull/37)); its Archive classification was already in place.
- Algora, an experimental AI-agent deliberation service separate from Mossland Agora where MOC holders vote, was converted to a read-only archive on 12 October. City’s notice about its daily records and its simulation labels were corrected on 9 October to match how records actually work, and its Algora archive support followed on 12 October. This does not mean the midnight record feature was started; the home page still said dated automatic records are not running on 2 November. Signal’s descriptions and sources were corrected on 12 October, followed by its AI notice on 15 October.
- Alpha’s AI persona reply labels and automatically generated Ask example labels, and MOSS.AO’s basic AI notice, were deployed on 21 October. Alpha’s two labelling errors were identified on 26 September and corrected on 21 October, 25 days later and past policy §7’s seven-day deadline. Signal’s wording on human review was corrected on 12 October. The phased rollout of basic AI notices has no blanket deadline under policy §9. Alpha’s site-wide standard notice is outside the completed changes and was not in the public HTML of the five pages checked on 2 November. Some further explanatory corrections were not yet reflected on 2 November: the additional notice on Alpha’s persona price commentary was not in the public HTML of those pages, AO’s `approved` wording was unchanged, and other wording was not rechecked screen by screen and is not recorded as completed. The 28 August MOSS.AO introductory articles ([Korean](https://medium.com/p/7d2175e1714f), [English](https://medium.com/p/3081df113e3e)), whose wording was identified in the 26 September check (Q3 §B), received a correction notice at the end of the body, before the links section, on 6 November (confirmed via the public RSS), past policy §7’s seven-day standard: in the public code, ideas are promoted and plans marked `approved` automatically, and only plans below the auto-approval score wait for a person to approve them. The original wording about human selection, including the English title’s ‘Keeping Humans in the Loop’, remains unchanged.
- Four Medium articles were AI-assisted but carried no authoring line at the end when published: the Signal introduction of 23 October ([Korean](https://medium.com/p/001f5d3a6198), [English](https://medium.com/p/71d44a793891)) and the Q3 summary of 30 October ([Korean](https://medium.com/p/fbea7e65bfb0), [English](https://medium.com/p/e3940ffd5b7b)). The line, the policy link and a note about the addition were added to all four on 2 November (confirmed via the public RSS). These are October publications rather than items carried over from Q3, and no further action remains on this labelling issue.
- The disclosure dashboard’s five September findings and its Q3 shared-data card were addressed on 23 October. Some labels outside the September list were also tidied in the same deployment. The market label ‘Circ / Total Supply (24h)’ remains (a ratio that is not a 24-hour value, per the deployed file on 2 November). The five supply-plan schedule rows in the 2 November public response have no missing English (plan entries, not on-chain transfers or payment notices); missing English in other rows that response does not show is a 23 October record and could not be rechecked. The on-chain evidence was published with Q3 on 19 October. It measures the amount outside the Foundation wallet as defined in Q3, rather than total market circulating supply. On 2 November, the report and six supporting files returned HTTP 200 and matched the approved files by SHA-256. These later completion dates do not revise the quarter-end assessment.
- Algora’s archived retention records report 171,041 deleted rows past their retention period across 11 runs dated 1–11 October; most (133,112) are activity-log rows the job labels `noise`, the rest are other activity-log rows, signals and agent chatter, and proposals, issues and sessions are not in those runs’ target list. The public response has no run for 12 October, so this is not presented as the complete deletion total up to shutdown, and it does not establish that the deletions were appropriate. This review records the read-only conversion as completed while keeping the policy treatment of the earlier retention deletions and content masking open; the check that September left for the October round did not reach a conclusion in this round. The relevant provisions and historical records will be compared without setting a new deadline for a conclusion. The conversion did not restore the in-memory public Decision Packet list emptied at earlier restarts. The `Running` and `LIVE` labels have been replaced by the archive notice. The registry reason’s `best-effort-frozen` wording and the ‘experimental’ chip on Algora’s links card remain, and Algora’s auto-generated proposals keep their `passed` (no votes) and `voting` labels in the read-only record (the archive notice says these were set by an automated process, that no MOC holder vote was ever recorded, and that none of this is official Mossland governance).
- All eight Beta services still lack a designated second maintainer. This review retains their Beta classifications and Article 3 exceptions; Core promotion requires the maintainer and second-maintainer deployment and recovery rights to be confirmed. Signal retains its experimental chip to show that it is a Lab-class experimental service. The past empty feed and undisplayed counters are not the reason for keeping it. The home page’s initial HTML still showed `00`, while the loaded page displayed real values and a feed on 2 November. The links README example still says to remove the chip when real data appears and needs to be aligned with this decision.
- On 2 November, BRIDGE’s status response showed collection active; its public [README](https://github.com/MosslandOpenDevs/bridge-2026#readme) still lists the past 20 October item in its direction-review schedule and has not been updated. Alpha’s off-host backup warning remains and September’s carry-over of that item to Q4 stands; completion of a restore test has not been verified. The English brief for 14 September is still missing, and those for 28 and 29 September are now listed in its sitemap. Media’s wording and AO’s limited registered health response also remain open. AO has a separate processing-metrics endpoint documented in Q3’s 16 October observation; it was not rechecked in this round.
- The five previously disclosed hosts—comply, flow, null, pf and sv—retain their names and September clean-up records. Naming additional items is on hold. Beyond the five hosts named in September, items outside the registry are tracked in an internal list; no item reached a confirmed outcome in this round, their handling is under review, and outdated links and status wording in related public documents have not yet been corrected. Confirmed outcomes will be recorded in the monthly review of the round in which they are confirmed, and the scope of naming will be decided after outcomes are confirmed (Q3 §13.1). This is not a census of current hosts or a count of services. Of Q3 §13’s two Q4 tasks, which are internal goals, this review records only the items checked under the second (service clean-up and consistency of displays), and corrections already finished in October are not counted as new results for it. The full comparison against certificate-transparency records and the full comparison of official service descriptions named in Q3 §13.1 were not done in this round. The first task, including the review of moving Alpha’s core tasks and MCP to SignalMap, is not assessed here. Achievement will be judged in the Q4 report’s scorecard.
- All 16 registered status URLs returned HTTP 200 at the 15:57 KST observation on 2 November. That does not establish monthly uptime or the success of all work. On 20 October, from about 01:00 to 04:30 KST, some services stopped responding because of a network problem and then recovered (per internal records). This review does not tally service availability history. The existing MIP-1 retrospective case is updated without adding a new live or agent-decision case.
- At the 2 November 15:57 KST observation, the registry review timestamp was still `2026-09-30T06:40:00Z`, with file SHA-256 `494a509c5f7ea851415a11be068c553adfae44041482512af499fa1ad20b0681`, which matches the file as last changed by links [PR #38](https://github.com/MosslandOpenDevs/links/pull/38) (merge commit `c7e7583`, 12 October). The file’s changes since the September review are [PR #37](https://github.com/MosslandOpenDevs/links/pull/37) and PR #38. Before this document was merged, the timestamp was updated to this round’s registry observation time, `2026-11-02T06:57:06Z`, and reflected in links (`MosslandOpenDevs/links` [PR #39](https://github.com/MosslandOpenDevs/links/pull/39), commit `0b67119`, deployment confirmed 2026-11-06 20:12 KST; file SHA-256 after deployment `69d78556da441f63fddc55dffb144cfa8f55c348becbc2f24dc3bf097892e056`). That is 33 days after the previous value, within the 35 days the repository’s validator uses as its monthly-cadence threshold; no review timestamp falls within the October calendar month, and it is not backdated to 31 October or earlier. The same change corrected the Alpha note to this round’s observed values (detailed call `worst_status: warn`, `seo_pages` 2,540), and Signal’s experimental chip is kept under this round’s decision. Other classifications, chips, `statusUrl` values and other services’ notes were not changed.
- TRACKING #5’s October item missed its 31 October deadline. The same pull request as this document records the overrun and its reason, the fulfilment link and the November deadline of 30 November. As stated in Q3 §7.2, the post-quarter increase in Passport verified wallets includes records classified as automation-related, so it is not read as an increase in use (not re-measured in this round). The separate October season summary (TRACKING #3) and Season 1 final report (TRACKING #2) are due on 7 and 19 November, respectively, and this review does not replace them. The next monthly review rechecks the remaining items; this is not a new commitment to finish by then those with no deadline of their own. Under Article 4, this review will also be reported in the 2026 Q4 report.

작성 방식: **AI 보조 · 사람 검토** · 영문 요약 **AI 번역 · 사람 검토** · [AI 생성 콘텐츠 표시 정책 v1.0](./2026-09-16_ai-content-labelling-policy.md) / Authoring: **AI-assisted · human-reviewed** · English summary **AI-translated · human-reviewed** · [AI-Generated Content Labelling Policy v1.0](./2026-09-16_ai-content-labelling-policy.md)

**모스랜드**
**Mossland**
