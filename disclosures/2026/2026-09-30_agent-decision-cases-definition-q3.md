## 관찰 가능한 에이전트 결정 사례 — 집계 정의 고정과 2026 Q3 집계

**작성일: 2026-09-30** · **관측 시각: 2026-09-26T09:59:55Z** (한국 시각 18:59:55. 2026-09-27에 사후로 정함 — §6. 결정 사례 0건과 공개 경로 상태는 2026-09-30T06:35Z, 한국 시각 15:35에 재확인)

이 문서의 시각은 따로 적지 않으면 UTC(끝에 Z)입니다. 한국 시각은 9시간을 더합니다.

> 발행일은 본 문서를 포함한 커밋이 이 저장소의 기본 브랜치에 병합된 시각입니다. 작성·관측 시각과 발행 시각이 다를 수 있으며, 본문은 관측 시각을 기준으로 씁니다.

### 핵심 요약

1. AI 에이전트 기반 실험 시스템 세 곳(Algora · Agentic Orchestrator(AO) · BRIDGE)을 대상으로 아래 정의로 센 **결정 사례(에이전트의 결론이 실행되어 결과가 검증된 것)는 0건**입니다. 2026 Q2 리포트 §13.3이 정한 Q3 목표 "정의 고정 후 ≥ 10 재판정"에 미치지 못합니다. 모스코인 보유자가 투표하는 Mossland Agora의 안건·투표는 이 집계의 대상이 아닙니다.
2. **심의 완결 354건**(결론은 남았으나 실행·검증 기록이 없는 것, 2026-09-26T09:59:55Z 관측)은 결정 사례로 세지 않습니다. 전부 자동 파이프라인이 만든 것이고 사람의 개시·표결이 없습니다. 규모 참고용으로만 적습니다. 이 가운데 Algora 336건의 결론 문서는 관측 81초 뒤 재단이 배포한 Algora PR #52(자동 제안 생성과 무투표 통과 경로를 끄는 변경)에 따른 서비스 재시작으로 공개 경로에서 사라졌습니다(서비스 메모리에만 있던 목록이라 재시작 때 비워진 것이며, 각 건의 입력 식별자·완결 세션·결론 시각은 2026-09-30T06:35Z 재확인에서도 공개 완결 세션 목록으로 조회됩니다 — §6). 발행 전 2026-09-30T06:35Z에 같은 방법으로 다시 센 심의 완결은 18건(Algora 0)입니다(§6).
3. 정의는 §2, 건별 표본과 재현 명령은 증빙 폴더(§5)에 있습니다. 분기 목표의 달성 여부 판정은 Q2 §13.1이 정한 대로 2026 Q3 리포트의 스코어카드에서 합니다.

### 1. 배경

2026 Q1 리포트 §11.3은 "관찰 가능한 에이전트 결정 사례"를 Q2 지표 목표 "≥ 10 (Algora+AO+BRIDGE)"로 두었으나 무엇을 1건으로 셀지는 정하지 않았습니다. 2026 Q2 리포트는 집계 정의가 고정되지 않았다는 이유로 판정을 유보하고(§1.2·§13.3), 정의를 고정한 뒤 판정을 재개하는 것을 Q3 과제로 두었습니다(§13.1 ④-2, 완료 증거 "정의 문서 + 해당 정의로 집계한 표본"). 이 문서는 그 정의와 표본입니다.

Q2 §1.2가 참고로 적은 관측치(2026-08-03: Algora 완결 세션 10건 · AO 누적 완성 프로젝트 66건)는 정의 이전의 다른 단위이며 이 문서의 수와 비교하지 않습니다.

### 2. 집계 정의

| 항목 | 내용 |
|---|---|
| 대상 | Algora · Agentic Orchestrator(AO) · BRIDGE. 사람이 내린 결정의 이행 기록은 대상이 아닙니다 |
| 집계 단위 (1건) | 하나의 식별 가능한 입력(이슈·신호 묶음)에 대해 복수 에이전트의 심의가 끝나 구조화된 결론 산출물이 남은 것. Algora는 완결 세션에 Decision Packet이 연결된 이슈, BRIDGE는 Decision Packet이 있는 제안, AO는 토론을 거쳐 승격·기각 판정이 기록된 계획 |
| 등급 | **심의 완결** — 위 단위를 충족하고 로그인 없이 URL·공개 API로 조회 가능 / **실행·검증** — 심의 완결에 더해, 그 결론에 대한 실행·검증 기록이 공개 API의 outcome·proof로 조회되는 것 |
| **결정 사례** | **실행·검증 등급만** 결정 사례로 부르고 목표 "≥ 10"은 이 수로 판정합니다 |
| 제외 | 결론 산출물 없이 닫힌 세션 · synthetic/mock 라벨 데이터 · 테스트·재시도 중복 · 에이전트 심의 없이 사람이 결정한 건 |
| 기간·중복 | 결론 시각 기준 UTC 2026-07-01T00:00Z ≤ t < 2026-10-01T00:00Z. 같은 입력 식별자는 1건 |
| 정의일 | 2026-09-18 (UTC 자정 기준). 정의일 이전 발생분은 '사후 판정'으로 구분해 셉니다 |

**문턱을 실행·검증에 둔 이유.** Q1 리포트는 목표를 "실험 단계 내에서 관찰 가능한 의사결정 사례를 늘리고"(§11.1)와 "≥ 10"(§11.3)으로만 적고 1건의 정의는 두지 않았습니다. 같은 리포트 §6은 당시 상태를 "Algora · Agentic Orchestrator · BRIDGE 세 개의 에이전트 기반 시스템은 모두 실험(Experimental) 단계이며, 분기 중 MOC 거버넌스 실운영에 직접적 영향을 미친 의사결정 사례는 없습니다"라고 적었습니다. 재단은 이 서술을 기준으로, 결론이 실제로 실행되고 검증된 것만 결정 사례로 세기로 했습니다. 심의만 끝난 산출물을 세면 자동 파이프라인의 출력만으로 목표가 채워지기 때문입니다.

### 3. 집계 결과

아래 값은 2026-09-26T09:59:55Z에 증빙 폴더의 것과 같은 판의 `reproduce.py`(sha256 `46811195…`)를 한 번 실행해 얻은 것입니다(공개 GET 10건, 로그인 없음). 응답 원문을 재단 기록으로 함께 저장하려고 내려받기 함수만 감싼 래퍼로 실행했으며 출력은 같습니다. 원문은 일부에 개인 식별 문자열이 있어 공개하지 않습니다(§5). Algora 결론 문서 목록이 비기 전에 그 목록 전체(1,358건, 응답 `total`과 일치)를 받은 마지막 관측이며, 이 시각을 공시 관측으로 정한 것은 2026-09-27입니다(§6). §2의 "로그인 없이 조회 가능"은 관측 시각을 기준으로 판단했습니다.

| 항목 | 값 |
|---|---|
| **결정 사례 (실행·검증)** | **0건** |
| 심의 완결 — 결정 사례로 세지 않음 | 354건 (Algora 336 · AO 0 · BRIDGE 18) |
| 심의 완결 중 정의일(2026-09-18, UTC) 이후 발생 | 165건 |
| 심의 완결 중 정의일 이전 발생 (사후 판정) | 189건 (Algora는 2026-09-09 이후 결론분만 — §6) |
| 참고: 같은 정의·스크립트로 2026-09-30T06:35Z 재실행 | 결정 사례 0건 · 심의 완결 18건 (Algora 0 · BRIDGE 18). Algora 결론 문서 목록이 비어 §2의 공개 조회 조건을 충족하지 못함(§6) |

**0건의 확인 경로** (2026-09-26T09:59:55Z, 2026-09-30T06:35Z 재확인): `algora.moss.land/api/outcomes` → `{"outcomes":[]}` · `bridge.moss.land/api/outcomes` → `count 0` · `bridge.moss.land/api/stats` → `outcomes.totalProofs 0`. 이 세 경로는 기간에 무관한 전체 기록이며, 결론 문서 목록과 달리 데이터베이스에 저장된 기록을 읽어 서비스 재시작의 영향을 받지 않습니다.

**심의 완결 354건의 성격.** Algora · AO · BRIDGE는 AI 에이전트 기반의 실험 시스템이며, 아래의 제안과 `passed` · `voting` · `expired`는 각 시스템 안의 자동 생성 기록입니다. 모스코인 보유자가 투표하는 Mossland Agora의 안건·투표와는 별개이고, Agora의 투표는 이 집계에 들어가지 않습니다. 354건은 전부 자동 파이프라인이 만든 것으로, 사람이 개시하거나 표결한 건은 없습니다(완결 세션의 `human_participants`가 전부 비어 있음). Algora 336건은 관측 시각에 공개 목록 API(`algora.moss.land/api/governance-os/documents?type=DP`)에서 로그인 없이 받은 결론 문서(Decision Packet)로 센 것입니다. 그 가운데 269건은 대응 제안의 상태가 `passed`였고 67건은 `voting`이었습니다(건별 확인, 관측 시각 값). 건별 득표 필드는 비어 있으며, 제안 시스템 전체 집계(`disclosure.moss.land/api/algora/proposals/stats`)가 총 투표 0 · 투표자 0을 보이므로 `passed`는 투표 없는 통과로 판단합니다. `passed`는 제안의 상태값일 뿐 실행·반영을 뜻하지 않습니다(outcomes 비어 있음). 관측 81초 뒤인 2026-09-26T10:01:16Z에 Algora 저장소 [PR #52](https://github.com/MosslandOpenDevs/Algora/pull/52)(자동 파이프라인 기본 꺼짐, 무투표 통과 경로 제거)가 배포되었고, 그 뒤로 투표 기간이 끝난 제안도 `voting`에 머물러 있습니다(2026-09-30T06:35Z 재확인: 제안 전체 `passed` 887 · `voting` 67 · 총 투표 0, 그중 투표 기간이 끝난 `voting` 67건). BRIDGE 18건은 전부 0표입니다. 17건은 정족수(100)에 미달해 `expired`(정족수 미달로 만료)로 끝났고, 1건은 관측 시각에 `active`(투표 종료 2026-09-27T09:04Z)였으며 2026-09-30T06:35Z 재확인에서 `expired`입니다. 이 1건의 투표 종료 전인 2026-09-27T01:14Z에 BRIDGE 자체 투표·위임을 끄는 변경([PR #34](https://github.com/MosslandOpenDevs/bridge-2026/pull/34))이 병합되었습니다(그때까지 기록된 표는 0). BRIDGE는 2026-09-26 [PR #29](https://github.com/MosslandOpenDevs/bridge-2026/pull/29)로 자동 심의 · 자동 제안 생성 · 결과 자동 평가를 기본값 꺼짐으로 바꾸고, 정족수를 채우지 못하고 끝난 제안을 `rejected`(부결)가 아니라 `expired`(만료)로 기록하게 했습니다(기존 건 포함). BRIDGE의 공개 통계상 실제 제안은 21건이며, 결론 시각이 집계 기간 시작(2026-07-01T00:00Z) 전인 3건을 뺀 18건을 셌습니다.

### 4. 판정

- 이 정의로 센 결정 사례는 **0건**으로, Q2 §13.3의 Q3 목표 "≥ 10"에 미치지 못합니다.
- 심의 완결 354건을 결정 사례로 부르지 않습니다.
- 기간 창(2026-10-01T00:00Z) 종료 후의 판정은 Q2 §13.1의 기존 판정 절차(2026 Q3 리포트 스코어카드)에 따릅니다.

### 5. 증빙 (Evidence)

본 공시와 함께 발행한 [증빙 폴더](./2026-09-30_agent-decision-cases-evidence/)의 파일과 SHA-256 해시입니다. `cases.csv`와 `fetch-metadata.json`은 2026-09-26T09:59:55Z에 `reproduce.py`를 한 번 실행해 만든 것입니다. 수집 시각은 운영자가 기록한 `observed_at_utc`이며 외부에서 따로 증명되지 않습니다. GitHub의 PR 병합 기록은 이 파일들이 늦어도 병합 시각에는 지금 내용 그대로 있었음을 보여 줍니다.

| 파일 | 내용 | SHA-256 |
| --- | --- | --- |
| `README.md` | 재현 절차와 집계 로직(DP 문서 → `issueId`, 없으면 세션을 거쳐 역매핑 → 완결 세션 결합, synthetic 분리 규칙, UTC 창), 관측 뒤 재집계로 확인할 수 있는 것과 없는 것, Algora 행의 부분 확인 방법 | `f3cb1b91d27029423b4d5106eb64fbe6e3b0b6d0e306c0fbc08abdc5a2214e68` |
| `cases.csv` | 심의 완결 전수 건별 표(10열) — 시스템 · 입력 식별자 · 결론 산출물 id · 결론 산출물 수 · 결론 시각(UTC) · 등급 · 제안 상태(조회 시점) · 사람 참여 여부 · 정의일 이후 여부 · 조회 경로. **제목·GitHub 핸들 등 개인 식별 문자열은 넣지 않음.** Algora 행의 조회 경로는 2026-09-26T10:01:16Z 이후 404입니다(§6) | `b16b9f667bd09a1546c38f1554081c8264b52dd2f7fb25d0c72a66b94f01e780` |
| `reproduce.py` | 재현 스크립트(Python 3 표준 라이브러리만, 공개 API 읽기 전용). `cases.csv`·`fetch-metadata.json`과 요약을 만듭니다. 위 두 파일을 만든 판 그대로이며, 2026-09-26T10:01:16Z 뒤에 실행하면 Algora는 0건이 나오고 경고가 나지 않습니다(§6) | `46811195ad93ec19356f9c7edf539e52b4f59c18f5d5a2dd8b6d46badf38660e` |
| `reproduce.sh` | `reproduce.py`를 실행 시각(UTC)을 붙인 새 폴더로 실행하는 명령 | `358630bbfe685146e990aa2f5ecee9b6eddc1ed89796520af94b4675ed13e445` |
| `fetch-metadata.json` | 수집 시각(UTC) · 원본 URL 10개 · 각 응답의 SHA-256·바이트(받은 응답의 기록. 일부 응답 원문에 개인 식별 문자열이 있어 원문은 싣지 않음. `outcomes` 두 응답은 2026-09-27에도 같은 해시였고, 나머지 8건은 공개 응답이 그 뒤 바뀌어 같은 해시를 다시 받을 수 없음) · 응답 건수와 `total`(또는 stats) 대조 결과 · 집계 요약 | `59512648007c3e7ca9188791e7952eb540e5285fb61517f7b46135737aa1da73` |
| `재현_20260930T063522Z/cases.csv` · `재현_20260930T063522Z/fetch-metadata.json` | 발행 전 2026-09-30T06:35Z 재확인으로 같은 스크립트를 다시 실행한 결과. 집계 표본이 아니라, 발행 시점에 공개 경로로 다시 세면 무엇이 나오는지의 기록입니다 | `a0230739620cb4ed81c332d82f8ee22bc8fe7d5411fe10761723360d22394701` · `d4ca6679ad4683b5f71970109ee707dcb4d6cc65208f801073b3cb0db5ece308` |

재검증 절차는 증빙 폴더의 [README](./2026-09-30_agent-decision-cases-evidence/README.md)를 참조하십시오. 해시 목록은 같은 폴더의 `SHA256SUMS.txt`에도 있습니다.

재현 명령의 목록 조회는 `limit=5000`으로 하고, 결론 문서(DP)는 응답의 `total`과 수신 건수가, Algora 제안은 `proposals/stats`의 `proposals.total`과 수신 건수가 같은지 확인합니다(관측 시각 결론 문서 1,358건 = `total` 1,358). 이 대조는 목록이 잘리지 않았는지만 확인하며, 목록이 통째로 빈 경우(0 = 0)는 가려내지 못합니다. 2026-09-26T10:01:16Z 이후의 재실행이 그 경우입니다(§6).

### 6. 한계

- 위 수치는 라이브 누적 집계를 **2026-09-26T09:59:55Z 한 번의 관측으로 고정한 값**이며, 제안 상태(`passed`·`voting`·`active` 등)도 그 시각의 값입니다. 그 뒤 공개 경로를 다시 조회하면 BRIDGE는 관측 시각 이전에 결론 난 행의 수가 같고 상태만 달라질 수 있으며, 관측 뒤 새 행이 생길 수 있습니다(2026-09-30T06:35Z 재확인: 새 행 0건 — BRIDGE의 자동 제안 생성은 2026-09-26부터 기본값 꺼짐입니다). Algora 행은 다시 셀 수 없습니다(다음 세 항목). 관측 뒤로 새로 결론이 난 Algora 세션은 없습니다(공개 완결 세션 목록의 `concluded_at` 최댓값 2026-09-26T07:47:02Z — 2026-09-27 확인, 2026-09-30T06:35Z 재확인에서도 같음). 결정 사례 0건의 세 경로는 기간 무관 전체 기록이며 2026-09-30T06:35Z 재확인에서도 0건입니다.
- **Algora의 결론 문서(Decision Packet) 공개 경로는 서비스 프로세스의 메모리에만 있는 목록을 보여 주며, 서비스가 재시작될 때마다 비워집니다**([`InMemoryDocumentStorage`](https://github.com/MosslandOpenDevs/Algora/blob/efae806/packages/document-registry/src/document.ts#L79-L82)). 2026년 9월 한 달 동안 배포에 따른 재시작이 네 번 있었습니다(09-02 05:21Z · 09-09 02:36Z · 09-26 10:01Z · 09-26 14:06Z — 운영 서버 기록. 모두 재단이 Algora 저장소에 병합한 변경의 자동 배포로, 각 병합 약 3~7분 뒤입니다. 이 가운데 이 집계와 관련된 것은 PR #49 병합 뒤의 09-09 재시작과 PR #52 병합 뒤의 09-26 10:01Z 재시작입니다. 같은 달 문서만 바꾼 병합은 재시작으로 이어지지 않았습니다). 그래서 관측 시각의 목록에는 2026-09-09T02:36:33Z 재시작 뒤에 만들어진 문서만 있었고, Algora 336건은 그 뒤에 결론이 난 건입니다. Algora의 정의일 이후 164건은 빠진 건 없이 센 값입니다(정의일 이후 결론이 난 세션은 모두 관측 시각의 목록 범위 안이고, 관측 뒤 2026-09-30T06:35Z 재확인까지 새 결론 없음). 정의일 이전 Algora 172건은 실제보다 적게 센 값입니다. 2026-09-09T02:36:33Z 재시작 전에 결론이 난 Q3 Algora 심의는 결론 문서가 있었더라도 관측 시각에 공개 경로에 없어 이 정의로 셀 수 없었습니다. 공개 완결 세션 목록에는 그 기간(2026-07-01T00:00Z 이상 2026-09-09T02:36:33Z 미만)에 결론이 난 세션이 2,129건(입력 이슈 2,079개) 있어 이 172건의 약 12배입니다(결론 문서가 있었는지는 공개 경로로 확인할 수 없어 세지 않음). 관측 시각의 결론 문서는 전부 `state: draft`였습니다.
- **관측 81초 뒤인 2026-09-26T10:01:16Z 재시작(재단이 배포한 Algora PR #52)으로 이 목록이 비었고**, 그 뒤 새 결론 문서는 만들어지지 않았습니다(2026-09-30T06:35Z 재확인: 목록 total 0). 그래서 `cases.csv` Algora 336행의 `path`는 404를 돌려주고, 이 336건은 발행 시점에는 §2의 "로그인 없이 조회 가능" 조건을 충족하지 못합니다. 제3자는 공개 API로 Algora 행을 다시 셀 수 없습니다(같은 스크립트를 다시 돌린 결과는 §3 참고 행). 2026-09-27 현재 각 행의 입력(이슈)·완결 세션·결론 시각과 세션 기록 안의 결론 문서 생성 메시지는 공개 경로로 조회되며, 입력 집합이 공개 완결 세션 목록과 일치하는지 확인하는 방법을 증빙 README에 적었습니다(이 대조는 2026-09-30T06:35Z에 받은 완결 세션 목록으로도 336건 모두 일치). 결론 문서 자체(`output_id`·`n_outputs`)는 재단 기록으로만 뒷받침됩니다. 결론 문서 id는 재시작 뒤 같은 날짜의 번호가 다시 쓰일 수 있어 영구 식별자가 아닙니다.
- **관측 시각은 사후에 정했습니다.** 원래 계획은 2026-09-30 재관측 값을 싣는 것이었고, 2026-09-26T09:59:55Z 실행은 2026-09-23의 시험 실행과 대조하려던 사전 실행이었습니다(재단이 병합한 Algora PR #52[09:58:21Z]의 자동 배포 재시작 전). 이 재시작이 결론 문서 목록을 비운다는 것은 2026-09-27에 확인했고, 그 뒤 목록이 비기 전에 목록 전체를 받은 마지막 관측인 이 실행을 공시 관측으로 정했습니다. §2의 "로그인 없이 조회 가능"을 관측 시각 기준으로 읽는 것도 이때 정했습니다(§2 문구에는 판단 시점이 없습니다). 같은 정의·같은 스크립트로 2026-09-30T06:35Z에 다시 센 결과는 §3 참고 행과 증빙 폴더의 `재현_20260930T063522Z/`에 그대로 싣습니다. 결정 사례는 어느 쪽이든 0건입니다.
- AO는 공개 계획 목록이 파라미터와 무관하게 최신 5건만 반환해 전수·상태별 건수를 공개 경로로 셀 수 없고, 토론 기록도 공개되지 않아 판정을 보류했습니다(0건으로 셈). 포함하더라도 결정 사례 수는 바뀌지 않습니다.
- **집계 정의는 공개 경로의 표본을 조회한 뒤에 고정했습니다.** 정의일(2026-09-18)은 표본을 본 뒤에 정한 날짜이고, 결정 사례의 문턱(실행·검증, §2)은 2026-09-23에 확정했습니다. 그래서 정의가 표본에 맞춰졌다고 읽힐 수 있습니다. 다만 이 문턱에서는 정의일이나 집계 단위를 어떻게 잡아도 결정 사례는 0건입니다(§3의 확인 경로는 기간에 무관한 전체 기록입니다). 심의 완결 건수는 정의일 이전(사후 판정)과 이후로 나눠 적었습니다(§3).

---

### English Summary

**Observable Agent Decision Cases — Definition Fixed and 2026 Q3 Count**

* **Result:** Under the definition in §2, the number of **decision cases (deliberation concluded *and* executed with a verified outcome) is 0** — below the Q3 target "≥ 10, reassessed once the definition is fixed" set in the 2026 Q2 report §13.3.
* **Not counted as decisions:** Algora, AO and BRIDGE are experimental AI-agent systems; their proposals and `passed` / `voting` / `expired` statuses are auto-generated records inside those systems and are separate from Mossland Agora, where MOC holders vote (Agora votes are not part of this count). 354 *deliberation-concluded* items (Algora 336 · AO 0 · BRIDGE 18) were observed at 2026-09-26T09:59:55Z, all produced by automated pipelines with no human initiation or votes. At that time 269 of the Algora items carried a `passed` proposal status and 67 were `voting`, while Algora's own proposal statistics record zero votes in total; after Algora PR #52 was deployed 81 seconds later, proposals whose voting period ended have stayed `voting` (re-checked 2026-09-30T06:35Z). BRIDGE's 18 received no votes: 17 ended as `expired` (the quorum of 100 was not reached; since 2026-09-26, under BRIDGE PR #29, such closures, including earlier ones, are recorded as `expired` rather than `rejected`, and automatic deliberation, proposal generation and outcome evaluation are off by default) and 1 was `active` at the observation time (voting ended 2026-09-27T09:04Z; `expired` on re-check). Before that voting period ended, a change switching off BRIDGE's own voting and delegation (BRIDGE PR #34) was merged at 2026-09-27T01:14Z; no vote had been recorded by then. BRIDGE's public statistics show 21 proposals excluding synthetic ones; the 18 whose conclusion time falls within the counting period (2026-07-01T00:00Z onward) are counted here. They are reported for scale only. Recounted the same way at 2026-09-30T06:35Z, the figure is 18 (Algora 0), because Algora's public Decision Packet list had been emptied (see Limits).
* **Verification paths:** `algora.moss.land/api/outcomes` (empty), `bridge.moss.land/api/outcomes` (count 0), `bridge.moss.land/api/stats` (`totalProofs 0`), observed at 2026-09-26T09:59:55Z and re-checked 2026-09-30T06:35Z. These read stored database records and are not affected by service restarts. The per-case table and fetch metadata in the [evidence folder](./2026-09-30_agent-decision-cases-evidence/) are the output of a single run of `reproduce.py` (sha256 46811195…) at the observation time (run through a wrapper that additionally saved the response bodies to the Foundation's own records — not published, because some contain personal identifiers; the output is unchanged); the folder also holds the publication-day re-run.
* **Limits:** The figures are fixed at that single observation. Algora's public Decision Packet list was held only in the service's process memory and was emptied at every restart; the four deploy restarts in September 2026 each followed one of the Foundation's own merges to the Algora repository (the two relevant to this count followed PR #49 and PR #52; docs-only merges that month did not restart the service). At the observation time the list held only documents created after the 2026-09-09T02:36:33Z restart (all in `draft` state), so earlier Q3 Algora deliberations could not be counted: the before-definition Algora figure (172) is an undercount (the public completed-session list shows 2,129 sessions on 2,079 input issues concluded in Q3 before that restart — about twelve times the 172 — not counted because whether they had Decision Packets cannot be checked publicly), while the after-definition figure is not truncated. The restart at 2026-09-26T10:01:16Z, from the Foundation's deployment of Algora PR #52 81 seconds after the observation, emptied the list: the 336 Algora rows cannot be recounted from public APIs, their `path` links return 404, and at publication they no longer meet §2's public-queryability test, which was applied at the observation time. As of 2026-09-27 their input issues, completed sessions, conclusion times and the session messages recording each packet's creation were public, and the evidence README shows how to check the input set (the same check against the completed-session list fetched at 2026-09-30T06:35Z also matched all 336); the packets themselves (`output_id`, `n_outputs`) rest on the Foundation's record alone, and packet ids are not permanent identifiers. The collection time is the operator's record (`observed_at_utc`); the PR merge record only shows that the files existed by merge time. **The observation time was chosen after the fact:** the plan was to publish a 2026-09-30 re-observation; the 09:59:55Z run was a pre-run, chosen on 2026-09-27, once the wipe was found, as the last observation that received the full list before it was emptied. Applying §2's public-queryability test at the observation time was decided at the same point; §2 itself names no time. The decision-case count is 0 either way. AO exposes only its latest five plans. The definition was fixed after the public sample had been viewed: the definition date (2026-09-18) was set after viewing it, and the decision-case threshold (execution and verification) was confirmed on 2026-09-23. At that threshold the count is 0 whatever the date or unit, because the verification paths are all-time records. Final judgment against the target is made in the 2026 Q3 report scorecard, as Q2 §13.1 prescribes.

작성 방식: **AI 보조 · 사람 검토** · [AI 생성 콘텐츠 표시 정책 v1.0](./2026-09-16_ai-content-labelling-policy.md) / Authoring: **AI-assisted · human-reviewed** · [AI-Generated Content Labelling Policy v1.0](./2026-09-16_ai-content-labelling-policy.md)

**모스랜드**
**Mossland**
