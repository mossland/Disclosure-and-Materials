## MIP-1 생명주기 월 1회 검토 결과 — 2026년 9월

**작성일: 2026-09-30** · **관측 시각: 2026-09-30 15:35~16:25 KST** (항목별 시각은 본문에 적었습니다)

> 발행일은 본 문서를 포함한 커밋이 이 저장소의 기본 브랜치에 병합된 시각입니다. 작성·관측 시각과 발행 시각이 다를 수 있으며, 본문은 관측 시각을 기준으로 씁니다.

**근거:** MIP-1 (2026-09-02 비준) 제4조 — "links.moss.land registry를 상태의 유일한 기준으로 삼아 월 1회 검토한다. 상태 변경(특히 Archive 지정)은 근거와 함께 기록하고, 검토 결과는 분기 리포트에 기재한다."

**용어:** registry = links.moss.land가 공개하는 공식 서비스 목록 파일 · lifecycle = MIP-1이 정한 등급(Core 상시 운영 / Beta 운영 중·변동 가능 / Lab 실험 / Archive 종료·보존) · 부담당자 = 담당자와 함께 배포·복구 권한을 갖는 두 번째 담당자(MIP-1 제2조) · statusUrl = 서비스별 상태 확인 주소 · note = registry에 적는 서비스별 메모. 끝에 Z가 붙은 시각은 UTC이며, 한국 시각은 9시간을 더합니다.

### 핵심 요약

* MIP-1 제4조에 따라 links.moss.land registry의 9월 생명주기 검토를 했습니다. 검토 대상은 `lifecycle` 값이 있는 **17개 서비스**(Beta 8 · Lab 7 · Archive 2 · Core 0)이며, 이번 달 lifecycle 변경은 없습니다.
* registry의 검토 시각 필드 `lifecycleReviewedAt`을 `2026-08-23T06:30:00Z`에서 `2026-09-30T06:40:00Z`로 갱신했습니다(`MosslandOpenDevs/links` 커밋 `509a146`). 이 필드는 2026-08-23 이후 이번 검토 전까지 갱신되지 않은 상태였습니다.
* Beta 8개는 모두 부담당자가 아직 지정되지 않아, 비준된 MIP-1 부속서 A의 분류대로 Beta를 유지하고 제3조 예외 기록을 그대로 둡니다(§4). 부담당자가 지정된 서비스가 없어 Core로 게시한 서비스는 없습니다.
* 확인된 차이 8건을 §5에 적었습니다. BRIDGE 홈의 고정 예시 활동은 2026-09-26 수정으로 해소했습니다. 이번 검토로 해소되지 않은 것은 Algora(AI 에이전트 실험 서비스로 Mossland Agora와 별개. Archive 분류 — 제안·이슈 자동 생성은 2026-09-26 멈췄고 신호 수집·에이전트 대화 기록 생성과 보존 기간이 지난 로그의 일일 삭제는 2026-09-30 관측 시점에도 계속됨. MIP-1의 '읽기 전용 보존'과 '삭제는 별도 안건'을 여기에 어떻게 적용할지는 확정하지 못함, §5-①), Alpha(호스트 밖 백업 없음 — **미조치, Q4 이월**), 공시 대시보드 표기 5곳(유통량 관련 표기 4곳 · 개발 지표 표기 1곳 — 수량이 아니라 표기의 차이이며 2026-09-30 관측 시점까지 고치지 않음, §5-⑧), City의 일일 기록 안내, Signal의 AI 안내 미반영, Media의 'Absorbed' 문구(표현 차이로 유지)입니다. 이 8건과 별도로, AO의 등재 상태 주소가 하위 구성요소를 점검하지 않는 점을 §1과 §6에 적었습니다.
* statusUrl 16개가 정상 응답을 준다는 사실만으로는 가동을 확인할 수 없습니다. 두 곳(links · monitor)은 조회 시각이 아니라 빌드 시각을 돌려주고, 최근 처리 시각을 함께 내는 곳은 4곳입니다(§1).

### 1. 검토 대상과 분모

registry(`https://links.moss.land/ecosystem-registry.json`, `version` 1.1.1)에 `lifecycle` 값이 있는 **17개 서비스**가 이번 검토의 분모입니다. Beta 8 · Lab 7 · Archive 2 · Core 0입니다.

`services` 배열에는 30개 항목이 있으나 13개는 외부 링크·자료 항목(GitHub, registry JSON, llms.txt, sitemap, Medium, X, 시세·거래소 링크)이라 `lifecycle` 값이 없고 MIP-1 제1조의 적용 범위 밖입니다. 17개 가운데 `statusUrl`이 있는 서비스는 16개(media 제외)이고, Monitor 화면에 표시되는 서비스는 15개입니다(2026-09-30 15:40 KST 화면 관측). 세 숫자는 분모가 서로 다릅니다.

registry에 없는 `*.moss.land` 공개 호스트는 이 분모 밖입니다. 그 가운데 5곳(comply · flow · null · pf · sv)은 2026-09-27~29에 해당 하위 호스트의 DNS 레코드와 서버의 인증서를 삭제하고 웹 서버 설정을 꺼 정리했습니다. 다섯 곳 모두 registry에 등재된 적이 없는 호스트입니다.

- comply · flow: 둘 다 2026년 5월에 만든 호스트입니다. comply는 외부 AI 사업자의 인공지능 기본법 대응(AI 생성물 표시 · 기록 · 보고서 초안)을 돕는 도구로 구상한 시제품이며, 재단의 준법 기능이 아닙니다. flow는 업무 자동화 서비스 구상을 보여 주는 정적 화면 목업으로 제품 코드가 없습니다. 두 곳 모두 가입 · 결제 기능과 MOC를 쓰는 기능은 만들어지지 않았습니다.
- null · pf · sv: 2026년 2월에 MosslandOpenDevs 공개 저장소의 개발 단계 프로젝트 세 개를 올려 두었던 웹 주소입니다. 공개된 코드 기준으로 지갑 연결 · 결제 기능이 없고 실제 자금이나 토큰을 다루지 않습니다. 세 곳 모두 정리 시점에는 이미 응답하지 않던 상태였습니다.

comply의 코드와 flow의 화면 자료는 보존하고 있고, null · pf · sv의 코드는 공개 저장소에 남아 있습니다. `moss.land` 도메인과 registry에 등재된 서비스는 이 정리의 대상이 아닙니다.

#### statusUrl 응답이 뜻하는 것

**statusUrl 16개가 모두 HTTP 200으로 응답한다는 사실을 가동 증거로 쓰지 않습니다.** 응답은 세 갈래로 나뉩니다(2026-09-30 15:36~15:37 KST, 약 30초 간격 2회 조회).

| 갈래 | 서비스 | 응답이 보증하는 것 |
| --- | --- | --- |
| 1. 응답이 조회마다 바뀜 | 14개 | 요청 시점에 웹 프로세스가 응답했다는 것. 어느 하위 구성요소까지 점검한 결과인지는 서비스마다 다릅니다. 최근 처리 시각을 함께 내는 곳은 4개(bridge · npc · signal · signalmap), 최근 24시간 처리량까지 내는 곳은 1개(npc)입니다. ao의 등재 주소는 `status` · `timestamp` · `version` · `service` 네 필드만 돌려주며 하위 구성요소를 점검한 결과를 담지 않습니다 |
| 2. 빌드 시각 반향 | links · monitor | 정적 응답이 서빙되고 있다는 것뿐입니다. 두 엔드포인트 모두 `timestamp`가 `buildTime`과 같은 값에 고정돼 있고(관측 시 links `2026-09-12T23:20:06.261Z` · monitor `2026-09-22T03:26:31.131Z`), 두 번 조회한 응답이 바이트 단위로 같았습니다(나머지 14개는 모두 달라졌습니다). 두 응답은 `pipeline: "none"`(자체 처리 작업 없음)을 함께 돌려주며, health 규약도 정적 산출물에 이 방식을 허용합니다. 다만 값이 재배포 때만 바뀌므로 **이 응답만으로는 배포 뒤 서비스가 제대로 동작하는지 알 수 없습니다** |
| 3. 요약값이 따로 있음 | alpha | registry가 가리키는 쿼리 없는 주소는 `status: ok`와 함께 `worst_status: not_evaluated`를 돌려줍니다. 하위 항목을 평가하는 호출(`?strict=1`, `?detail=1&strict=1`)에서만 `worst_status: warn`이 보입니다(§5-⑥). 상위 필드만 보면 경고를 놓칩니다 |

`status` 값도 서로 같지 않습니다. 14개는 `ok`를 돌려주고, algora는 health 규약(links 저장소 `HEALTH_CONTRACT.md`)이 정한 세 값(`ok` · `degraded` · `down`) 밖의 값인 `running`을, city는 자체 `status` 필드 없이 자매 서비스 6개의 집계(`summary`)를 돌려줍니다. links 저장소의 일일 health 규약 점검(GitHub Actions `health conformance`)은 2026-09-29 18:24 KST 실행에서 12개 준수 · 4개 알려진 예외(city · npc · recipe · algora) · 실패 0을 보고했습니다. 이 점검은 응답 형식을 보는 것이며 가동을 보증하지 않습니다.

MIP-1 안건 본문은 배경으로 "화면상 정상인 서비스가 실제로는 멈춰 있던 사례가 반복 확인되었습니다"라고 적었습니다. 위 구조가 그런 사례가 다시 생길 수 있는 지점입니다. §2 표에 각 서비스의 갈래를 함께 적었습니다.

### 2. 검토 결과

statusUrl 응답과 갈래 열: 2026-09-30 15:36~15:37 KST 관측. 9월 lifecycle 변경 열: 2026-09-30 기준. registry `status` 열은 lifecycle과 별개로 registry가 적는 운영 상태 값입니다(operational · beta · deprecated 등).

| # | 서비스 | lifecycle | registry `status` | statusUrl 응답 | 갈래 | 9월 lifecycle 변경 | 비고 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | moss | beta | operational | `ok` | 1 | 없음 | |
| 2 | disclosure | beta | operational | `ok` | 1 | 없음 | 공시 대시보드 표기 (§5-⑧) |
| 3 | passport | beta | beta | `ok` | 1 | 없음 | |
| 4 | agora | beta | operational | `ok` | 1 | 없음 | |
| 5 | links | beta | operational | `ok` | 2 | 없음 | 이번 검토로 `lifecycleReviewedAt` 갱신 (§3) |
| 6 | wa | beta | beta | `ok` | 1 | 없음 | |
| 7 | alpha | beta | operational | `ok` · `worst_status: not_evaluated` | 1 · 3 | 없음 | strict 호출 `worst_status: warn` (§5-⑥) |
| 8 | signalmap | beta | operational | `ok` | 1 | 없음 | |
| 9 | signal | lab | beta | `ok` | 1 | 없음 | 홈 카운터 · 실험 칩 · AI 안내 (§5-⑤) |
| 10 | city | lab | operational | `status` 필드 없음 · 집계 6/6 ok | 1 | 없음 | 일일 기록 안내와 실제 기록 (§5-④) |
| 11 | npc | lab | operational | `ok` | 1 | 없음 | |
| 12 | recipe | lab | operational | `ok` | 1 | 없음 | |
| 13 | ao | lab | operational | `ok` | 1 | 없음 | 등재 주소는 하위 구성요소 점검 없음 (§1 · §6) |
| 14 | bridge | lab | operational | `ok` | 1 | 없음 | 홈 고정 예시 활동 (§5-③) |
| 15 | monitor | lab | operational | `ok` | 2 | 없음 | |
| 16 | media | archive | deprecated | — (statusUrl 없음) | — | 없음 | §5-② |
| 17 | algora | archive | operational | `running` | 1 | 없음 | **Archive 분류와 자동 생성 범위 (§5-①)** |

2026-09-29 20시께~23시 반께(KST) statusUrl이 있는 16곳 가운데 9곳(BRIDGE · Signal · AO 등)이 응답하지 않다가 회복했습니다. 보유자 접점인 moss.land · 공시 대시보드 · Passport · Agora는 그 시간대의 확인(21:05 KST)에서 응답했습니다. links 저장소의 일일 health 규약 점검은 2026-09-29에는 그보다 앞선 18:24 KST에 실행돼 이 일을 기록하지 못했습니다. 원인은 확인되지 않았습니다. 2026-09-30 15:36 KST 관측에서는 16곳 모두 응답했습니다. 이 문단은 검토 직전에 있었던 한 건을 적은 것이며, 9월 중의 무응답이나 서비스 자료의 갱신 지연·실패를 모두 집계한 것은 아닙니다(이 검토는 서비스별 가동 이력을 집계하지 않습니다).

### 3. registry 갱신

이번 검토의 registry 갱신은 아래 순서로 했습니다.

1. **변경 전 원문 기록.** 갱신 직전 공개본 `ecosystem-registry.json`의 sha256은 `f897a6254d3284eec2a41a31bdcca96ed2446467cde2ad4378b57d46c1781dd8`입니다(2026-09-30 15:35 KST 기록, 31,135 bytes). 이 값은 `MosslandOpenDevs/links` 저장소에서 이 파일을 마지막으로 바꾼 커밋 `be8b78f`(2026-09-10)의 파일과 같습니다.
2. **갱신 내용.** `lifecycleReviewedAt`을 `2026-08-23T06:30:00Z`에서 `2026-09-30T06:40:00Z`로 바꿨습니다. 같은 변경에 Signal note의 2026-09-30 관측값 갱신을 넣었습니다(§5-⑤). 그 밖의 항목(등급 · 칩 · statusUrl · 다른 서비스의 note)은 바꾸지 않았습니다.
3. **기록.** 갱신은 `MosslandOpenDevs/links` 저장소 [PR #36](https://github.com/MosslandOpenDevs/links/pull/36)(병합 커밋 `509a146`, 2026-09-30 16:19 KST 병합)으로 남겼습니다. 반영 뒤 공개본의 sha256은 `ba6cb8f0fe4870a8904fbe067b371c0697c4f046a0cd02b0e2c67b570228fb18`(31,512 bytes), links health의 `buildTime`은 `2026-09-30T07:19:44.261Z`입니다(2026-09-30 16:22 KST 확인).

`lifecycleReviewedAt`은 registry 스키마가 월 1회 검토의 시각("this field is that review's timestamp")으로 정의한 필드이며, MIP-1 결과 공시의 이행 현황표가 9월 검토의 표지로 지목한 값입니다. 그래서 이번 검토에서 이 필드를 갱신했고, 갱신 내용은 links 저장소의 커밋 이력으로 확인할 수 있습니다.

### 4. 제3조 예외 기록 — 8건

MIP-1 제2조는 Core 등급에 담당자와 부담당자를 두고 둘 다 배포·복구 권한을 갖도록 정합니다. 제3조는 부담당자가 없는 서비스를 원칙적으로 Lab 이하로 표시하고, 예외는 사유와 함께 registry에 기록하도록 정합니다.

**Beta 8개 모두 부담당자가 지정되지 않았습니다.** registry의 `maintainer` 값은 8개 모두 조직 계정 `MosslandOpenDevs`이고 부담당자(`secondMaintainer`)는 지정돼 있지 않으며, 8개 각각의 `lifecycleReason`에 제3조 예외가 기록돼 있습니다. 이번 검토에서 8건 각각을 예외로 유지합니다.

| 서비스 | registry에 기록된 사유 (`lifecycleReason` 요지) | 이번 달 처리 | 다음 검토 |
| --- | --- | --- | --- |
| moss · disclosure · passport · agora · links (5) | 부속서 A의 Core 후보. 부담당자 미지정으로 부속서 A 규정대로 Beta 게시(제3조 예외) | Beta 유지 · 예외 유지 | 2026년 10월 회차 |
| wa · alpha (2) | 부속서 A Beta. 부담당자 미지정(제3조 예외) | Beta 유지 · 예외 유지 | 2026년 10월 회차 |
| signalmap (1) | 부속서 A Beta, Core 지향. 부담당자 미지정(제3조 예외) | Beta 유지 · 예외 유지 | 2026년 10월 회차 |

**예외를 유지하는 근거.** 8개의 Beta 분류는 2026-09-02 비준된 MIP-1 부속서 A의 최초 분류 그대로입니다(Core 후보 5개는 부속서 A의 '미지정 시 Beta로 게시' 규정, 나머지 3개는 부속서 A Beta). 그 뒤 부담당자가 지정되지 않아 이번 달은 분류와 예외 기록을 그대로 둡니다. 부담당자가 지정되기 전에는 Core로 올리지 않습니다.

제3조는 예외를 사유와 함께 registry에 기록하도록 정하며 별도의 승인 절차는 두지 않습니다. 이번 달의 유지 판단은 재단이 이 검토에서 한 것이고, 그 기록이 이 공시와 registry의 `lifecycleReason`입니다.

### 5. 확인된 차이와 처리

#### ① Algora — Archive 분류와 자동 생성의 범위

- **무엇인가:** Algora는 AI 에이전트가 거버넌스 주제를 자동으로 토론하고 제안을 만들던 실험 서비스입니다(registry 설명: 'AI 에이전트 거버넌스 토론장'). 모스코인 보유자가 안건을 올리고 투표하는 Mossland Agora(agora.moss.land)와는 별개이며, 아래의 제안 · `passed` · `voting`은 모두 Algora 안의 자동 생성 기록입니다. 자동 제안자 이름 `agora-orchestrator`도 Algora 내부 구성요소의 이름입니다.
- **분류:** `lifecycle: archive`, `status: operational`. registry는 Passport 적격 대상 제외(2026-08-23 — 새 Passport 생태계 스탬프의 근거 서비스에서 뺌)와 정기 자동 보고 생성 중지(2026-09-02, 마지막 자동 보고는 2026년 8월 월간)를 기록하고 있습니다.
- **관측** (2026-09-30 15:35~15:38 KST, 화면은 16:24 KST):
  - statusUrl은 `status: "running"`과 `timestamp` 두 필드만 돌려줍니다. `running`은 health 규약의 세 값(`ok` · `degraded` · `down`) 밖의 값이며, 이 응답만으로는 Archive인지, 활동이 계속되는지 알 수 없습니다.
  - `/api/stats`: `totalAgents` 38 · `activeAgents` 0 · `signalsToday` 387 · `openIssues` 123. `/api/activity`의 최신 항목은 `2026-09-30T06:37:09Z`(조회 시각과 같은 분)의 에이전트 대화 기록입니다.
  - `/api/proposals?limit=5000`(954건 전체) 가운데 최근 생성 200건(2026-09-16~09-26)이 모두 자동 제안자 `agora-orchestrator`가 만든 것이며 `passed` 133 · `voting` 67이고, 200건 모두 표결 집계(`tally`)가 비어 있습니다. 가장 최근 제안의 생성 시각은 `2026-09-26T07:47:02Z`입니다.
  - 영문 화면은 브라우저에서 `System Status: Running`과 `LIVE` 표시를 함께 보입니다. 화면 맨 위에는 실험 환경이라는 안내("Experimental Environment")가 있습니다.
  - 보존 정리 작업(보존 기간이 지난 행을 자동으로 지우는 작업)이 매일 03:00Z(한국 시각 12:00)에 활동 로그 · 에이전트 대화 기록 · 신호 가운데 보존 기간이 지난 행을 지웁니다. 2026-09-30T03:00:55Z 실행에서 지워진 것은 활동 로그 12,279행(이 가운데 12,145행은 실행 기록이 `noise`로 구분한 행) · 에이전트 대화 1,357행 · 신호 1,846행, 합쳐 15,482행입니다(공개 `/api/activity?type=SYSTEM_STATUS`). 제안 · 이슈 · 세션 기록은 이 실행 기록의 대상 목록에 없습니다. 이 작업은 아래 9월 중 조치(PR #52)의 대상이 아니어서 2026-09-30 현재 돌고 있습니다.
- **9월 중 조치:** 2026-09-26 Algora 저장소 [PR #52](https://github.com/MosslandOpenDevs/Algora/pull/52)(병합 커밋 `efae806`)로 이슈 탐지, 자동 제안 생성, 투표 자동 종결을 기본값 꺼짐으로 바꾸고, 표결 없이 `passed`로 처리하던 경로를 없앴습니다. 2026-09-30 관측에서 가장 최근 제안의 생성 시각은 `2026-09-26T07:47:02Z`, 가장 최근 이슈의 생성 시각은 `2026-09-26T09:45:40Z`입니다. `voting` 상태 제안은 67건이며 모두 투표 기간이 끝났고 기록된 표는 0입니다. 신호 수집과 에이전트 대화 기록 생성은 이 변경의 대상이 아니어서 2026-09-30 관측 시점에도 계속되고 있었습니다.
- **기존 기록:** PR #52는 기존 기록을 다시 쓰지 않았습니다. 그래서 비준 이후 표결 없이 `passed`로 기록된 기존 제안의 표기는 그대로 남아 있습니다. 한편 배포에 따른 재시작으로 메모리에만 있던 결론 문서(Decision Packet) 공개 목록이 비었습니다(함께 발행한 [에이전트 결정 사례 공시](./2026-09-30_agent-decision-cases-definition-q3.md) §6). 2026-09-26 운영자가 실존 인물 관련 뉴스를 잘못 분류한 자동 생성 기록 1묶음의 제목에 철회 표시를 하고 이름을 가렸습니다. 이 수정으로 수집기가 같은 기사인지 판별하는 데 쓰는 값이 바뀌어 같은 기사가 두 차례 다시 수집됐고, 다시 들어온 신호 2건에 든 그 이름은 2026-09-27과 2026-09-30(16:57 KST, 이 문서의 관측 시각 뒤)에 1건씩 가렸습니다. 2026-09-30 21:28 KST(역시 관측 시각 뒤)에는 그 기록 묶음에서 기사의 나머지 내용(회사 이름 · 경위 · 기사 주소)과 에이전트가 쓴 토론 본문을 중립 안내문으로 바꿨습니다. 기록 id · 상태 · 시각 · 건수와 결론 문서 생성 문구 · 수치 결과는 그대로이고, 원본은 운영자가 비공개로 보관합니다. 2026-09-30 현재 운영자가 고친 기존 기록은 이것뿐입니다. 이 수정들이 아래의 '읽기 전용 보존'과 어떻게 맞는지도 10월 회차 검토에서 함께 확인합니다.

**MIP-1은 Archive의 기록을 읽기 전용으로 보존하도록 정합니다. 다만 이를 지금 계속되는 자동 생성과 삭제 작업에 어떻게 적용할지는 이 검토에서 확정하지 못했습니다.** MIP-1의 상태 표는 Archive를 '종료·보존 — 신규 개발 중단 · 기록은 읽기 전용으로 보존'으로 정하고, 표 아래에 "Archive는 삭제가 아닙니다. 도메인·데이터·저장소 기록은 보존되며, 삭제는 별도 안건을 요구합니다"라고 적습니다(안건 본문과 2026-09-02 결과 공시). registry의 Archive 설명도 "Development ended; the record is preserved read-only. Archive is not deletion — removing a domain, its data, or its repository requires its own proposal."이고, 스키마는 "an archived service can still be reachable"이라고 적어 접속 가능성은 허용합니다. Archive 상태의 서비스가 자동 생성을 멈춰야 한다고 따로 명시한 조항은 제1~4조와 스키마에 없습니다. 삭제에 대해서는 위 문장이 별도 안건을 요구하며, 보존 기간이 지난 기록을 자동으로 지우는 작업을 따로 다룬 조항은 없습니다. 그래서 두 가지가 확정되지 않은 채 남습니다. 새 기록이 계속 생기는 현재 상태가 '읽기 전용 보존'에 맞는지, 그리고 보존 정리 작업이 활동 로그 · 에이전트 대화 기록 · 신호를 지우는 것이 '삭제는 별도 안건을 요구합니다'에 맞는지입니다. 이 검토는 둘 다 판정하지 않고 차이로 기록하며, 10월 회차 검토에서 확인할 사항으로 남깁니다(아래 ⓐ · ⓔ).

**이번 달 처리:** lifecycle과 registry 표기는 바꾸지 않고, 위 관측 사실과 확정하지 못한 두 가지를 차이로 기록합니다.

**이번 검토로 이 차이가 해소된 것으로 보지 않습니다.** 남은 확인 사항은 다섯 가지입니다: ⓐ '읽기 전용 보존'을 계속되는 자동 생성(신호 수집 · 에이전트 대화 기록)에 어떻게 적용할지 ⓑ 서비스 전체의 읽기 전용 전환 시점 ⓒ 화면·registry 표기(`Running` · `LIVE`, registry 사유의 'best-effort-frozen')와 Archive 분류 · 실제 생성 상태의 정합성 ⓓ 메모리에만 있어 배포 재시작마다 비워지는 결론 문서 공개 목록(에이전트 결정 사례 공시 §6) ⓔ 보존 정리 작업의 일일 삭제(활동 로그 · 에이전트 대화 기록 · 신호)와 'Archive는 삭제가 아닙니다 … 삭제는 별도 안건을 요구합니다' 문장의 관계.

#### ② Media — 'Absorbed' 문구

registry note는 "Absorbed into SignalMap 2026-08-21"과 DNS 삭제 · 저장소 archive를 적고, 편집 원칙은 signalmap.moss.land에 이어진다고 적고 있습니다. `lifecycle: archive` / `status: deprecated`로 분류는 일치하며, `statusUrl`이 없어 자동 관측 대상이 아닙니다. 차이는 표현입니다: 'Absorbed'(흡수)는 실제로 일어난 일(서비스 종료와 편집 원칙의 SignalMap 계승)보다 넓게 읽힐 수 있습니다. 처리: note가 서비스 종료와 기록 보존을 함께 적고 있어 이번 달은 문구를 그대로 두고, 표현 차이로만 기록합니다.

#### ③ BRIDGE — 홈의 고정 예시 활동

Lab 등급, `status: operational`. 9월 점검에서 공개 홈의 활동 영역이 고정 예시(제안 통과 1시간 전, 결과 검증 1일 전 등)를 실제 기록처럼 보여 주는 문제를 확인했습니다. 공개 통계(`/api/stats`)상 통과한 제안과 검증된 결과는 모두 0건입니다(2026-09-30 15:37 KST 관측: 실제 제안 21건 중 진행 0 · 만료 21 · 통과 0 · 부결 0, 합성 제안 143건 별도, `totalProofs` 0).

처리: 2026-09-26 BRIDGE 저장소 [PR #32](https://github.com/MosslandOpenDevs/bridge-2026/pull/32)(병합 커밋 `4c35a4d`)로 홈 활동 영역을 관측 데이터만 보이도록 바꾸고, 모든 페이지 하단에 AI 생성 콘텐츠 안내(정책 §4 문구)를 달았으며, 공식 의사결정 안내를 Agora로 바꿨습니다. 같은 날 [PR #29](https://github.com/MosslandOpenDevs/bridge-2026/pull/29)(병합 커밋 `9c65c20`)로 자동 심의 · 자동 제안 생성 · 결과 자동 평가를 기본값 꺼짐으로 바꾸고, 정족수를 채우지 못하고 끝난 투표를 `rejected`(부결)가 아니라 `expired`(만료)로 기록하게 했습니다(기존 건 포함). [PR #31](https://github.com/MosslandOpenDevs/bridge-2026/pull/31)(병합 커밋 `1741dab`)로는 제안 목록에서 데모(합성) 제안을 기본으로 숨기고, 표결 없이 기한이 지난 제안을 '정족수 미달로 만료'로 표시하도록 고쳤습니다. 2026-09-30 관측에서도 이 변경은 공개 화면과 공개 통계에 그대로 반영돼 있었습니다. 홈의 고정 예시 활동이라는 차이는 해소된 것으로 기록합니다.

이와 별도로, 2026-09-27 BRIDGE 저장소 [PR #34](https://github.com/MosslandOpenDevs/bridge-2026/pull/34)(병합 커밋 `14a6ea4`)로 BRIDGE의 자체 투표·위임 기능(BRIDGE 안의 실험 기능)을 껐고, 투표와 위임은 Agora에서 하도록 안내하고 있습니다. Agora의 투표·위임은 이 변경의 대상이 아닙니다. 기능을 끌 때까지 BRIDGE의 실제 제안 21건에 기록된 표는 0이었습니다. 신호 수집과 공개 화면 · 공개 통계는 2026-09-30 관측 시점에도 동작하고 있었습니다(15:36 KST 상태 응답: 수집 켜짐, 최근 수집 `2026-09-30T06:36:26Z`).

공개 통계(`/api/stats`)의 신호 수(`signals.total`)는 같은 값으로 반복 저장된 행을 2026-09-27에 정리해 줄었습니다(정리 전 사본 보존). 2026-09-23 855,132건에서 2026-09-30 15:37 KST 104,776건이 됐습니다.

BRIDGE의 예시·데모(합성) 데이터는 재단 공시에서 실제 제안 수나 실제 결과 수로 세지 않습니다.

#### ④ City — 일일 기록 안내와 실제 기록

Lab 등급, `status: operational`. City 사이트는 "매일 자정 도시의 상태가 박물관에 영구 기록됩니다"라고 안내하지만, 공개 상태 화면(`city.moss.land/status`)은 매일 자정 기록 작업 항목에 'archive 폴더 없음'을 표시하고, 기록 목록 API(`/api/archive`)는 `count: 0`(항목 없음)을 돌려줍니다(2026-09-30 15:37 KST 관측). 여기서 'archive'는 City의 일일 기록 기능 이름이며 MIP-1의 Archive 등급과는 관계가 없습니다. 처리: 안내와 실제 기록이 맞지 않는 상태로 기록합니다. 관측 시점까지 고친 것은 없고 lifecycle 변경도 없습니다.

#### ⑤ Signal — registry note의 관측 시점, 홈 카운터, AI 안내

`lifecycle: lab` · `status: beta` · registry 칩 `실험`. 검토 시점의 registry note는 2026-08-21 브라우저 관측(홈 카운터 `00`, 빈 시그널 피드)을 담고 있었고, 홈이 실제 데이터를 보일 때까지 칩을 유지한다고 적고 있었습니다.

2026-09-30 15:36~15:39 KST 관측:

- **피드:** `/api/health`는 `status` ok · `sourceBlocked` false · `signalCount` 54 · `forecastCount` 54입니다. 홈의 시그널 목록은 실제 질문을 렌더합니다.
- **홈 카운터:** 서버가 보내는 초기 HTML에는 카운터 4곳이 `00`으로 렌더되고, 같은 페이지 데이터에는 54 · 54 · 54 · 6이 들어 있습니다. 브라우저에서의 최종 표시값은 실제 값(54 · 54 · 54 · 06)입니다.
- **분모:** 같은 시각 `/api/health`는 `signalCount` 54, 성적표(`/accuracy`)는 '87 추적 중 · 7 해소됨'입니다. 두 값은 서로 다른 모집단이고 계속 움직이는 값입니다.
- **AI 안내:** 홈, 성적표, 방법론 페이지에서 정책 §4의 자동 산출 서비스 안내 문구와 정책 링크를 찾지 못했습니다. 방법론 페이지에는 에이전트가 사람의 검토를 위한 예측을 '제안'하며 무엇을 노출할지는 사람이 결정한다는 설명이 있습니다.

처리:
- registry note: 2026-09-30 관측값으로 갱신해 §3의 변경에 함께 넣었습니다. 브라우저에서의 카운터 미표시는 해소됐으므로 note의 해당 서술을 고쳤습니다.
- 실험 칩: 홈이 브라우저에서 실제 값을 보이므로, 칩을 붙였던 사유(홈이 비어 있음)는 더 이상 해당하지 않습니다. 다만 Signal의 lifecycle이 Lab이어서 이번 달은 칩을 유지하고, 뗄지는 10월 검토에서 정합니다. note에 그렇게 적었습니다. links 저장소 README의 Signal 예시 문장(홈 카운터 `00`)은 아직 고치지 않았습니다.
- 정책 §4 안내: '미반영'으로 기록합니다. 정책 §9는 운영 중인 서비스의 AI 안내를 기존 수정 작업에서 순차 반영하며 별도 일괄 적용 기한을 두지 않습니다.

#### ⑥ Alpha — 하위 점검 `db_backup` warn (호스트 밖 사본 없음)

registry가 가리키는 쿼리 없는 주소는 `worst_status: not_evaluated`를 돌려주고, 하위 항목을 평가하는 호출에서 `worst_status: warn`이 나옵니다. 하위 점검 12개 가운데 11개가 `ok`, 1개가 `warn`입니다(2026-09-30 15:37 KST 관측).

- **`warn`: `db_backup`.** 일일 백업은 정상 실행되고 있으나(마지막 실행 2026-09-30 03:00 KST, 23.0MB, 무결성 검사 ok) 서비스가 돌아가는 서버(호스트) 밖에 둔 사본이 없습니다(`offhost=none`). 그 서버에 사고가 나면 Alpha(크립토·매크로·국제정세 큐레이션 서비스) 데이터베이스의 원본과 백업이 함께 사라집니다.
- **brief 게시:** 공개 sitemap(2026-09-30 15:37 KST, URL 1,564개)에는 9월 한국어 brief가 9/1~9/27 날마다 있고, 영어 brief는 같은 기간 가운데 **2026-09-14 하루가 빠졌습니다**(해당 주소는 404). 9/28 · 9/29 brief는 한국어·영어 페이지가 모두 게시돼 있으나(16:19 KST 확인) sitemap에는 아직 실리지 않았습니다. health의 brief 하위 점검은 `ok`이고 최신 자료일은 2026-09-29입니다(15:37 KST). 따라서 이 항목은 "영어 brief 2026-09-14 1건 누락, 최근 2일분 sitemap 미반영"으로 기록합니다. 하위 점검 `macro`는 `ok`이며, 자료일이 2~3일 늦는 것은 평상 상태입니다(2026-09-30 관측 최신 자료일 2026-09-28).
- **registry note:** alpha note는 2026-08-23 확인값(strict 호출에서 `worst_status: ok`, 색인 페이지 1,642개)을 담고 있어, 현재 strict 호출 결과(`warn`, 2,299개)와 다릅니다. 처리: 이번 달은 차이를 이 공시에 기록하고, note는 백업 상태를 다시 보는 10월 회차에서 고칩니다.
- **처리: 미조치 — Q4 이월**(이번 분기에는 하지 않기로 2026-09-22에 결정). 호스트 밖 사본 확보와 복원 시험은 2026-09-30 관측 시점까지 하지 않았습니다. 이월은 Q4에 다시 판단한다는 뜻이며, 확보 시점을 정한 것은 아닙니다. 남는 위험은 호스트 사고 시 원본과 일일 백업이 함께 사라진다는 것입니다. Alpha의 호스트 밖 백업을 약속한 공시는 없으며, MIP-1 제2조의 배포·복구 권한은 Core 등급의 요건입니다(Alpha는 Beta). 다음 달 검토에서 다시 봅니다.

#### ⑦ registry 갱신 시각

`lifecycleReviewedAt`이 2026-08-23 이후 갱신되지 않아 9월 검토의 표지가 없었습니다. 그 사이 registry 내용은 바뀌었으므로(마지막 변경 커밋 `be8b78f`, 2026-09-10) 시각 필드로는 검토 여부를 판단할 수 없었습니다. §3의 절차로 이번 검토와 함께 해소했습니다(links 커밋 `509a146`). 직전 검토 시각과의 간격은 38일로, links 저장소의 검증 스크립트가 월 1회 주기의 기준으로 두는 35일을 넘겼습니다(오류가 아닌 알림 대상). 달력 월로는 8월과 9월에 한 번씩입니다(registry 검토 시각 기준). 이 검토 결과 공시의 기한은 공시 예고 관리 목록(TRACKING) #5가 정한 매월 말일입니다.

#### ⑧ 공시 대시보드(disclosure) 표기

공시 대시보드의 표기 가운데 실제로 가리키는 값과 다른 곳 5곳을 확인했습니다(2026-09-30 15:37~16:24 KST 배포본에 그대로).

- 토큰 절 4곳:
  - ⓐ '현재 유통량'(450,489,688 MOC)은 실시간 유통량이 아니라 유통계획상 해당 월말의 상한입니다.
  - ⓑ '유통되지 않는 모스코인을 보관하는 지갑'이라는 설명이 붙은 지갑은 재단 보유 지갑(대시보드에 공개된 1개)이며, 그 잔액은 계획상 비유통 수량과 같은 값이 아닙니다. 2026-09-30 16:24 KST 온체인 잔액은 약 8,037만 MOC로, 계획상 비유통 수량(총 발행 한도 5억 − 위 표시값 = 49,510,312 MOC)보다 약 3,086만 MOC 많습니다. 유통계획상 유통 가능으로 분류됐으나 재단 지갑에 남아 있는 수량이 잔액에 함께 들어 있기 때문이며, 유통계획의 분류 변경은 온체인 거래가 아닙니다(2026 Q2 리포트 §2.7 각주 2 · §C). 곧 이 지갑 밖에 있는 수량은 ⓐ의 표시값(450,489,688 MOC)보다 적으며, ⓐ의 표시값은 계획상 상한입니다.
  - ⓒ '최근 유통량 변동'은 유통계획 일정이며 온체인 이체 기록이 아닙니다.
  - ⓓ 유통 일정 설명의 영문에 국문의 '인건비 포함'이 빠져 있습니다(2026-11 항목 — 국문 "…사업운영(인건비 포함) 목적의 유통", 영문 "…and business operation").
- 개발 지표 절 1곳: '(비공개 포함)' 표기는 현재 집계 범위와 다릅니다(비공개 저장소 기여분이 집계에 들어가 있지 않습니다).

처리: 2026-09-30 관측 시점(15:37~16:24 KST)까지 고치지 않았습니다. 토큰 절 4곳은 분기말(2026-09-30) 화면 기록을 남긴 뒤에 고치기로 한 것이고, 개발 지표 절 1곳은 9월 안에 고치려 했으나 관측 시점까지 고치지 못했습니다. 관측 시점 뒤의 변경과 고친 결과는 다음 월 검토에 기록합니다.

### 6. 남은 차이 요약

| 항목 | 이번 달 처리 | 실행 증거 | 남은 차이 | 다음 검토 |
| --- | --- | --- | --- | --- |
| Beta 8 부담당자 미지정 | 제3조 예외 유지 | registry `lifecycleReason` 8건 | 부담당자 미지정 | 2026년 10월 회차 |
| Algora 자동 생성 범위 | 관측 기록 | PR #52 (`efae806`) | '읽기 전용 보존'의 적용 미확정 · 서비스 전체의 읽기 전용 전환 시점 · 표기 정합성 · 결론 문서 공개 목록 · 보존 정리 작업의 일일 삭제 — **해소로 보지 않음** | 2026년 10월 회차 |
| Alpha 호스트 밖 백업 부재 | **미조치 — Q4 이월** (2026-09-22 결정) | — | 호스트 사고 시 원본·백업 동시 소실 위험 · registry note가 2026-08-23 값 · 영어 brief 2026-09-14 누락 | 2026년 10월 회차 |
| BRIDGE 홈 고정 예시 활동 | 수정 — 해소 | PR #29 (`9c65c20`) · #31 (`1741dab`) · #32 (`4c35a4d`) | 없음 | 2026년 10월 회차 |
| Signal 홈 카운터 · 실험 칩 · AI 안내 | 카운터 표시 해소 · registry note 갱신 · 칩 유지 · §4 안내 미반영 | links 커밋 `509a146` | §4 안내 미반영 · 초기 HTML의 `00` · 칩을 뗄지 · README 예시 문장 | 2026년 10월 회차 |
| City 일일 기록 안내와 실제 기록 0건 | 불일치로 기록 (관측 시점까지 수정 없음) | — | 안내 문구와 실제 기록의 불일치 | 2026년 10월 회차 |
| Media 'Absorbed' 문구 | 유지 | — | 표현이 실제(종료 · 편집 원칙 계승)보다 넓음 | 2026년 10월 회차 |
| AO 등재 상태 주소 | 변경 없음 | — | 등재 주소가 하위 구성요소를 점검하지 않음 | 2026년 10월 회차 |
| 공시 대시보드 표기 5곳 | 2026-09-30 관측 시점까지 미수정 — 토큰 절 4곳은 분기말 기록 뒤 수정 예정 · 개발 지표 절 1곳은 9월 안에 고치려 했으나 관측 시점까지 미수정 · 고친 결과는 다음 월 검토에 기록 | — | 표기 5곳 | 2026년 10월 회차 |
| registry `lifecycleReviewedAt` | 이번 검토로 갱신 | links 커밋 `509a146` | 없음 | 매월 |

다음 검토는 [공시 예고 관리 목록](../TRACKING.md) #5의 10월 회차(기한: 매월 말일)입니다. MIP-1 제4조에 따라 이 검토 결과를 2026 Q3 리포트에도 기재합니다.

### 7. 확인 경로와 관련 링크

* [links.moss.land](https://links.moss.land/) · [registry JSON](https://links.moss.land/ecosystem-registry.json) · [registry 스키마](https://links.moss.land/ecosystem-registry.schema.json)
* [MosslandOpenDevs/links](https://github.com/MosslandOpenDevs/links) — registry 변경 이력([PR #36](https://github.com/MosslandOpenDevs/links/pull/36)), health 규약(`HEALTH_CONTRACT.md`), 일일 health 규약 점검(Actions `health conformance`)
* 서비스별 statusUrl: registry의 `statusUrl` 필드(16개). 하위 점검: `https://alpha.moss.land/api/health?detail=1&strict=1`
* Algora [PR #52](https://github.com/MosslandOpenDevs/Algora/pull/52) · BRIDGE [PR #29](https://github.com/MosslandOpenDevs/bridge-2026/pull/29) · [PR #31](https://github.com/MosslandOpenDevs/bridge-2026/pull/31) · [PR #32](https://github.com/MosslandOpenDevs/bridge-2026/pull/32) · [PR #34](https://github.com/MosslandOpenDevs/bridge-2026/pull/34)
* [MIP-1 결과 공시 (2026-09-02)](./2026-09-02_mip-1-lifecycle-policy-vote-results.md)
* [공시 예고 관리 목록 (TRACKING)](../TRACKING.md) #5
* [AI 생성 콘텐츠 표시 정책 v1.0](./2026-09-16_ai-content-labelling-policy.md)
* [관찰 가능한 에이전트 결정 사례 — 집계 정의 고정과 2026 Q3 집계 (2026-09-30)](./2026-09-30_agent-decision-cases-definition-q3.md)

---

### English Summary

**MIP-1 Lifecycle Monthly Review — September 2026**

This is the September round of the monthly registry review required by MIP-1 Article 4 (ratified 2026-09-02). Values are as of 2026-09-30 15:35–16:25 KST.

* **Scope (§1):** The denominator is the **17 services** that carry a `lifecycle` value in the links.moss.land registry (Beta 8 · Lab 7 · Archive 2 · Core 0). The other 13 registry entries are external links or data files and fall outside MIP-1 Article 1. Of the 17, 16 have a `statusUrl`; the Monitor screen shows 15. The three figures are different denominators.
* **Hosts outside the registry (§1):** Public `*.moss.land` hosts that are not in the registry fall outside this denominator; five of them (comply, flow, null, pf, sv) were cleaned up on 2026-09-27–29 by removing those sub-hosts' DNS records and the certificates on the server and disabling the web server configuration. None of the five was ever listed in the registry. comply and flow were both set up in May 2026: comply was a prototype of a tool conceived to help outside AI service providers respond to Korea's AI Framework Act (labelling AI-generated content, keeping records and drafting reports) — not a compliance function of the Foundation — and flow was a set of static screen mock-ups for a workflow-automation concept, with no product code; neither had sign-up or payment functions built, nor any function that used MOC. null, pf and sv were the web addresses where three development-stage projects whose code is in public MosslandOpenDevs repositories had been deployed in February 2026; based on the published code they have no wallet-connection or payment features and handle no real funds or tokens, and all three had already stopped responding by the time of the clean-up. comply's code and flow's screen files have been kept, and the code of null, pf and sv remains in the public repositories. The `moss.land` domain and the registered services were not part of this clean-up.
* **What status endpoints show (§1):** An HTTP 200 from the 16 status URLs is not treated as evidence of operation. 14 responses change per request, but only 4 report a recent processing time and 1 a 24-hour volume; AO's registered URL returns four fields and no subsystem checks. links and monitor return their build time as `timestamp` (with `pipeline: "none"`, which the health contract allows for static artifacts) and were byte-identical across two requests, so the response alone does not show whether the service works after deployment. Alpha's registered URL reports `worst_status: not_evaluated`; only the strict call shows `warn`. Status values also differ: 14 return `ok`, algora returns `running` (outside the health contract's three values `ok` / `degraded` / `down`), and city returns an aggregate without its own `status`.
* **Results (§2):** No lifecycle changes this month. Between about 20:00 and 23:30 KST on 2026-09-29, 9 of the 16 status URLs (BRIDGE, Signal, AO and six others) did not respond and then recovered; the holder-facing services moss.land, the disclosure dashboard, Passport and Agora responded when checked during that period (21:05 KST). The links repository's daily health conformance check had already run at 18:24 KST on 2026-09-29, before this happened, and did not record it. The cause has not been identified. All 16 responded at the 2026-09-30 15:36 KST observation. This paragraph records the one event closest to the review; it is not a tally of every non-response or failed data refresh in September.
* **Registry update (§3):** `lifecycleReviewedAt`, unchanged since 2026-08-23, was updated to `2026-09-30T06:40:00Z` in `MosslandOpenDevs/links` PR #36 (merge commit `509a146`), together with the Signal note. The pre-change file's SHA-256 was `f897a6254d3284eec2a41a31bdcca96ed2446467cde2ad4378b57d46c1781dd8`, matching the file as last changed in links commit `be8b78f` (2026-09-10); after deployment it is `ba6cb8f0fe4870a8904fbe067b371c0697c4f046a0cd02b0e2c67b570228fb18`. The gap since the previous review timestamp was 38 days, above the 35 days the repository's validator uses as its monthly-cadence threshold (a non-fatal notice, not an error); by calendar month there was one review each in August and September (by the registry review timestamp); the TRACKING #5 deadline is the last day of each month.
* **Article 3 exceptions (§4):** All 8 Beta services still have no second maintainer (the "second owner" of MIP-1 Articles 2–3). Their Beta classification is the original one in MIP-1 Annex A as ratified on 2026-09-02 (for the five Core candidates, under Annex A's rule that a candidate is published as Beta while no second maintainer is designated), and each is recorded as an Article 3 exception in the registry's `lifecycleReason`. No second maintainer has been designated since, so the classification and the exception records stay as they are; no service is promoted to Core until a second maintainer is designated. Article 3 requires the exception to be recorded with its reason and sets no separate approval step; this month's decision to keep them was made by the Foundation in this review.
* **Differences found (§5):**
  * ① **Algora (Archive):** Algora is an experimental AI-agent deliberation service, separate from Mossland Agora where MOC holders vote; its proposals and `passed` / `voting` statuses are auto-generated records inside Algora. Scheduled reports stopped on 2026-09-02. On 2026-09-26 (PR #52) issue detection, automatic proposal generation and vote resolution were switched off by default and the path that marked proposals `passed` without votes was removed; proposal and issue generation has been stopped since then. Signal collection and agent chatter logging were outside that change and continued (2026-09-30 observation: latest proposal created 2026-09-26T07:47:02Z, latest issue 2026-09-26T09:45:40Z, latest agent chatter 2026-09-30T06:37:09Z; the 67 proposals still marked `voting` are all past their voting period with zero votes recorded). Existing records were not rewritten, so proposals marked `passed` without votes keep that label. The deploy restart also emptied the in-memory public Decision Packet list (see the agent decision cases disclosure published together with this one, Limits). A daily retention job deletes rows past their retention period from the activity log, agent chatter and signals (15,482 rows on 2026-09-30, of which 12,145 are activity-log rows the job itself labels `noise`; proposals, issues and sessions are not in that run's target list). On 2026-09-26 the operator added a retraction mark to the titles of one batch of auto-generated records that had misclassified news about a real person and masked the name. Masking the name changed the value the collector uses to detect duplicates, so the same article was collected again twice; the operator masked the name in those two re-collected signals, one on 2026-09-27 and one on 2026-09-30 (at 16:57 KST, after the observation window stated above). At 21:28 KST on 2026-09-30 (also after that window) the operator replaced the remaining details of the report (firm, circumstances, article link) and the agent-authored discussion text in that batch of records with neutral notices; record ids, statuses, timestamps and counts, the decision-packet creation line and numeric results are unchanged, and the original is retained privately by the operator. As of 2026-09-30 these are the only existing records the operator has edited; how these edits relate to read-only preservation is also left for the October review. MIP-1 requires an Archive service's record to be preserved read-only, and the proposal text as passed (Korean) states that Archive is not deletion: domains, data and repository records are preserved, and deletion requires a separate proposal — the registry's Archive description says the same in English ("Archive is not deletion — removing a domain, its data, or its repository requires its own proposal"). Neither Articles 1–4 nor the registry schema expressly says that an Archive service must stop automated generation, and no provision deals separately with a job that automatically deletes records past a retention period. This review could not settle how those provisions apply to the automated generation that continues or to the daily retention deletions, so it rules on neither, records both as differences between the Archive description and the current state, and leaves them for the October review. This month only the observation is recorded. **Not counted as resolved.** Five items remain open: (a) how the read-only preservation requirement applies to the automated generation that continues (signal collection and agent chatter logging); (b) when the service as a whole becomes read-only; (c) whether the wording on the screen and in the registry is consistent with the Archive classification and the actual generation state — in a browser the English page shows `System Status: Running` and `LIVE`, with an "Experimental Environment" notice at the top, and the registry reason says 'best-effort-frozen'; (d) the public Decision Packet list, which is held only in memory and is emptied at each deploy restart; (e) how the retention job's daily deletions relate to the requirement that deletion needs a separate proposal.
  * ② **Media:** classification is consistent; the registry wording "Absorbed into SignalMap" reads wider than what happened (the service was retired and its editorial principles carried over) and is kept this month as a wording difference.
  * ③ **BRIDGE:** the home page showed fixed example activity as if it were real. On 2026-09-26 it was changed to show observed data only, with the policy's AI notice on every page and Agora named as the place of official decisions (PR #32); automatic deliberation, proposal generation and outcome evaluation were switched off by default and votes that end without quorum are recorded as `expired` rather than `rejected`, including earlier ones (PR #29); the proposal list hides demo proposals by default (PR #31). Recorded as resolved. Separately, on 2026-09-27 (PR #34) BRIDGE's own voting and delegation functions (an experimental feature inside BRIDGE) were switched off, and voting and delegation are directed to Agora; Agora's voting and delegation were not part of this change. No votes had been recorded on BRIDGE's 21 real proposals when these functions were switched off. Signal collection, the public pages and the public statistics were still running at the 2026-09-30 observation (status response at 15:36 KST: collection enabled, latest signal `2026-09-30T06:36:26Z`). BRIDGE's public signal count (`signals.total` in `/api/stats`) fell because rows stored repeatedly with the same value were compacted on 2026-09-27 (a pre-compaction copy is kept): from 855,132 on 2026-09-23 to 104,776 at 2026-09-30 15:37 KST. Example and demo (synthetic) data are not counted as real proposals or real outcomes in the Foundation's disclosures.
  * ④ **City:** the site says the city's state is recorded every midnight, but its public status page shows the daily-record folder as missing and `/api/archive` returns `count: 0` (observed 2026-09-30 15:37 KST). Recorded as a mismatch between the notice and the actual records; nothing had been changed as of the observation. This "archive" feature is unrelated to the MIP-1 Archive state.
  * ⑤ **Signal:** the feed is live (54 signals); the home counters render as `00` in the initial HTML and show the real values (54 · 54 · 54 · 06) in a browser. The policy §4 service notice and policy link were not found — recorded as "not yet applied"; under policy §9 such service notices are added during normal maintenance, with no separate deadline for applying them across all services. The registry note was updated with the 2026-09-30 observation. The original reason for the experimental chip (an empty home view) no longer applies; the chip is kept this month because Signal's lifecycle is Lab, and whether to drop it is left to the October review.
  * ⑥ **Alpha:** 11 of 12 subsystem checks are `ok`; `db_backup` is `warn` because daily backups have no off-host copy. **No action — carried over to Q4** (decided 2026-09-22); the carry-over means the question is revisited in Q4, not that a date for an off-host copy has been set. The remaining risk is losing both the original and the backups in a host incident. No disclosure has committed to an off-host backup for Alpha. Per the public sitemap, Korean briefs were published every day from 9/1 to 9/27 and the English brief is missing for 2026-09-14 only; the 9/28 and 9/29 brief pages exist but were not yet in the sitemap. The registry's alpha note still carries the 2026-08-23 values and will be corrected at the October round.
  * ⑦ **Registry review timestamp:** resolved by the update in §3.
  * ⑧ **Disclosure dashboard labels:** five labels do not match what they show. In the token section: (a) "Circulating Supply" (450,489,688 MOC) is the supply plan's month-end ceiling, not a live figure; (b) the wallet described as "holding non-circulating MOC" is the Foundation wallet (the one wallet published on the dashboard), whose on-chain balance (about 80.37 million MOC at 2026-09-30 16:24 KST) is about 30.86 million MOC larger than the plan's non-circulating amount (max supply 500,000,000 − the displayed figure = 49,510,312 MOC), because tokens the supply plan has reclassified as available to circulate but that remain in the Foundation wallet are part of that balance (a reclassification under the plan is not an on-chain transaction — 2026 Q2 report §2.7 note 2 and §C) — that is, the amount outside this wallet is below the displayed figure (450,489,688 MOC), which is the plan's ceiling; (c) "Recent Circulation Changes" is the plan schedule, not on-chain transfers; (d) the English schedule description omits the Korean text's "including personnel costs". In the development section, "(incl. private)" does not match the current aggregation scope (contributions to private repositories are not counted). None had been corrected as of the 2026-09-30 observations (15:37–16:24 KST): the four token-section labels are to be corrected after the quarter-end (2026-09-30) screen record is taken, and the development-section label, which was meant to be corrected in September, had not been corrected as of that observation either. The corrections will be recorded in the next monthly review.
* **Next review (§6):** remaining differences are reviewed in the October round (TRACKING #5, due the last day of each month). Under Article 4, this review is also reported in the 2026 Q3 report.

작성 방식: **AI 보조 · 사람 검토** · [AI 생성 콘텐츠 표시 정책 v1.0](./2026-09-16_ai-content-labelling-policy.md) / Authoring: **AI-assisted · human-reviewed** · [AI-Generated Content Labelling Policy v1.0](./2026-09-16_ai-content-labelling-policy.md)

**모스랜드**
**Mossland**
