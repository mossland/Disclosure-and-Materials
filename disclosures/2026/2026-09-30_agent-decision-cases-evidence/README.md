# 증빙 자료 — 관찰 가능한 에이전트 결정 사례 (2026 Q3 집계)

본 폴더는 함께 발행한 공시 [관찰 가능한 에이전트 결정 사례 — 집계 정의 고정과 2026 Q3 집계](../2026-09-30_agent-decision-cases-definition-q3.md)의 증빙입니다. `cases.csv`와 `fetch-metadata.json`은 **2026-09-26T09:59:55Z**에 이 폴더의 것과 같은 판의 `reproduce.py`(sha256 `46811195…`)를 한 번 실행해 만든 것입니다(응답 원문을 재단 기록으로 함께 저장하려고 내려받기 함수만 감싼 래퍼로 실행 — 출력은 같음). 수집 시각은 운영자가 기록한 `fetch-metadata.json`의 `observed_at_utc`이며, 외부에서 따로 증명되지 않습니다. GitHub의 PR 병합 기록은 이 파일들이 늦어도 병합 시각에는 지금 내용 그대로 있었음을 보여 줍니다.

| 파일 | 내용 |
|---|---|
| `cases.csv` | 심의 완결 전수 건별 표. 10열: `system` · `input_id`(이슈/제안 식별자) · `output_id`(결론 산출물 id) · `n_outputs`(같은 입력에 붙은 결론 산출물 수) · `concluded_at_utc` · `grade` · `proposal_status`(수집 시점의 제안 상태) · `human_participation`(사람 참여 기록: `yes`/`no`/`unknown`) · `after_definition_date` · `path`(공개 조회 경로 — Algora 행은 2026-09-26T10:01:16Z 이후 404, 아래 '한계'). **제목·계정 핸들 등 개인 식별 문자열은 포함하지 않습니다** |
| `fetch-metadata.json` | 수집 시각(UTC) · 원본 URL 10개 · 각 응답의 SHA-256·바이트(받은 응답의 기록) · 전수 확인 결과 · 집계 요약. 응답 원문 일부(Algora 결론 문서·제안·세션 목록)에 개인 식별 문자열(계정 핸들 등)이 있어 원문은 넣지 않았습니다 |
| `reproduce.py` | 재현 스크립트(Python 3 표준 라이브러리만). 공개 API만 읽고 `cases.csv`·`fetch-metadata.json`과 표준 출력 요약을 만듭니다. 위 두 파일을 만든 판 그대로입니다 |
| `reproduce.sh` | `reproduce.py`를 이 폴더 안의 새 폴더 `재현_<실행 시각 UTC>/`로 실행하는 명령 |
| `재현_20260930T063522Z/` | 발행 전 재확인(2026-09-30T06:35:22Z)으로 같은 스크립트를 다시 실행한 결과(`cases.csv`·`fetch-metadata.json`). 결정 사례 0건 · 심의 완결 18건(Algora 0 · BRIDGE 18). 집계 표본이 아니라, 발행 시점에 공개 경로로 다시 세면 무엇이 나오는지의 기록입니다 |
| `SHA256SUMS.txt` | 위 파일들과 이 README의 SHA-256 해시 |

## 재현

```bash
# 1) 해시 검증 — 이 폴더에서
shasum -a 256 -c SHA256SUMS.txt

# 2) 재집계 — 공개 API를 다시 읽는다(읽기 전용). 결과는 새 폴더에 쓴다
sh reproduce.sh                       # 결과: ./재현_YYYYMMDDTHHMMSSZ/
python3 reproduce.py --out ./재현      # 출력 폴더를 직접 정할 때 (--out . 은 이 폴더의 파일을 덮어쓴다)
```

**2026-09-26T10:01:16Z 뒤에 재집계하면 Algora는 0건이 나옵니다.** Algora 결론 문서 목록(`governance-os/documents?type=DP`)이 그 시각의 서비스 재시작으로 비었기 때문입니다(아래 '한계'). 이때도 DP 전수 확인은 `[0, 0, true]`로 참이 되어 경고가 나지 않습니다. 발행 전 재확인 결과는 이 폴더의 `재현_20260930T063522Z/`에 있습니다.

| 대상 | 재집계로 | 비교 방법 |
|---|---|---|
| 결정 사례 0건 | 현재 값은 확인 가능 | 2026-09-26 관측과 2026-09-30 재확인에서 모두 0건입니다. `outcomes` 두 경로와 `totalProofs`는 기간 무관 전체 기록이지만, 재현 시각의 0건은 그 사이 기록이 삭제·변경되지 않았을 때에만 과거의 0건을 뜻합니다. 과거 관측값은 당시 수집 기록(`fetch-metadata.json`)에 의존합니다 |
| BRIDGE 18행 | 확인 가능 | `concluded_at_utc` < 관측 시각인 행만 비교하면 건수는 같고, `proposal_status`는 재현 시점의 값이라 달라질 수 있습니다(예: 투표 중이던 제안의 종결) |
| Algora 336행 | 다시 셀 수 없음 | 결론 문서(`output_id`·`n_outputs`·`path`)가 공개 경로에 없습니다. 아래 부분 확인만 할 수 있습니다 |

위 표의 '확인 가능'은 해당 서비스가 공개 경로를 제공하는 동안에 한합니다.

**Algora 행의 부분 확인.** 2026-09-27 현재 각 행의 입력(이슈)·완결 세션·결론 시각과, 세션 기록 안의 결론 문서 생성 메시지("A decision packet has been created for governance review.")는 공개 경로로 조회됩니다. 아래 경로의 `agora`는 Algora 내부 토론 모듈의 이름이며, 모스코인 보유자가 투표하는 Mossland Agora(agora.moss.land)와는 별개입니다.

```bash
curl -s 'https://algora.moss.land/api/agora/sessions?status=completed' -o /tmp/sessions.json
curl -s 'https://algora.moss.land/api/issues/<input_id>'              # 입력(이슈)
curl -s 'https://algora.moss.land/api/agora/sessions/<session_id>'    # 세션 기록과 결론 문서 생성 메시지
# <session_id>: /tmp/sessions.json 에서 issue_id 가 cases.csv 의 input_id 인 완결 세션의 id
#               (여럿이면 concluded_at 이 가장 늦은 세션. 그 concluded_at = cases.csv 의 concluded_at_utc)
```

Algora 336행의 입력 집합은, 완결 세션 목록에서 결론 시각이 Algora PR #49 병합 시각(2026-09-09T02:31:49Z) 이상 PR #52 병합 시각(2026-09-26T09:58:21Z) 미만인 세션들의 `issue_id` 집합과 같습니다. 두 병합은 각각 결론 문서 목록을 비운 배포 재시작으로 이어졌습니다(4분 44초 뒤·2분 55초 뒤). 각 병합과 그에 따른 재시작 사이에는 결론이 난 세션이 없어, 재시작 시각을 경계로 써도 같은 336개입니다. 이 폴더에서 실행합니다.

```bash
python3 - <<'EOF'
import csv, json
s = json.load(open('/tmp/sessions.json')); s = s['sessions'] if isinstance(s, dict) else s
lo, hi = '2026-09-09T02:31:49Z', '2026-09-26T09:58:21Z'
got = {x['issue_id'] for x in s if x.get('status') == 'completed' and x.get('issue_id')
       and x.get('concluded_at') and lo <= x['concluded_at'].replace('+00:00', 'Z') < hi}
rows = [r for r in csv.DictReader(open('cases.csv', newline='')) if r['system'] == 'algora']
want = {r['input_id'] for r in rows}
print(len(got), len(want), got == want)   # 2026-09-27 · 2026-09-30 실행: 336 336 True
# 결론 시각: 이슈별 완결 세션의 가장 늦은 concluded_at 이 cases.csv 의 concluded_at_utc 와 같은지
last = {}
for x in s:
    if x.get('status') == 'completed' and x.get('issue_id') and x.get('concluded_at'):
        last[x['issue_id']] = max(last.get(x['issue_id'], ''), x['concluded_at'].replace('+00:00', 'Z'))
print(sum(last.get(r['input_id']) == r['concluded_at_utc'] for r in rows), len(rows))   # 2026-09-30 실행: 336 336
EOF
```

이 확인은 입력 집합과 결론 시각이 공개 완결 세션 목록과 맞는다는 것만 보여 줍니다(첫째 줄이 입력 집합, 둘째 줄이 결론 시각). `output_id`·`n_outputs`와 결론 문서 자체는 확인하지 못합니다.

응답 해시(`fetch-metadata.json`)는 관측 시각에 받은 응답의 기록입니다. `algora_outcomes`(`{"outcomes":[]}`)와 `bridge_outcomes`(`{"outcomes":[],"count":0}`)는 2026-09-27에도 관측 시각과 같은 해시였습니다. 나머지 8건은 공개 응답이 그 뒤 바뀌어 같은 해시를 다시 받을 수 없습니다. 결론 문서 목록이 비었고, 일부 기록의 제목과 본문이 고쳐졌고, 통계는 수시로 바뀌기 때문입니다. `재현_20260930T063522Z/`의 응답 해시도 그 실행 시각의 기록이며, 같은 날 뒤의 위 수정으로 제안 목록 응답은 그때와 달라졌습니다. `algora.moss.land`는 분당 요청 수를 제한합니다. 제한에 걸리면(HTTP 429) 스크립트가 멈추고 빈 출력 폴더를 남기므로, 1분 뒤 다시 실행하십시오.

## 집계 로직 (공시 §2의 정의를 구현)

1. **Algora** — `governance-os/documents?type=DP`(Decision Packet 전수 — 관측 시각 기준. 이 경로는 2026-09-26T10:01:16Z 이후 비어 있습니다, '한계')의 `content`에서 `issueId`를 꺼내 이슈 단위로 묶습니다. `issueId`가 없는 문서는 `content`의 `sessionId`(없으면 `sourceId`)로 완결 세션 목록(`agora/sessions?status=completed`)에서 세션을 찾아 그 세션의 `issue_id`를 씁니다(역매핑). 어느 쪽으로도 이슈를 찾지 못한 문서는 세지 않습니다. 그다음 같은 `issue_id`의 완결 세션(`concluded_at` 있음)이 붙는 그룹만 남깁니다. 결론 시각 = 그 이슈의 완결 세션 `concluded_at` 최댓값. `output_id`는 그룹의 DP 문서 id를 정렬한 첫 번째, `n_outputs`는 그룹의 DP 문서 수입니다. `proposals`에서 같은 `issue_id`의 제안(여럿이면 응답 순서상 첫 번째) 상태를 `proposal_status`에 적습니다. `human_participants`가 하나라도 있으면 `human_participation = yes`.
2. **BRIDGE** — `proposals` 중 `decisionPacket`이 있는 것. `decisionPacket.issue.category`가 `stats.signals.synthetic.byCategory`의 카테고리에 속하면 synthetic으로 제외합니다. 결론 시각 = `decisionPacket.createdAt`. `issueId` 중복은 1건. `proposal_status`는 응답의 `status` 그대로입니다(BRIDGE는 2026-09-26부터 정족수 미달 종료를 `rejected`가 아니라 `expired`로 기록합니다). `proposer`가 `auto-system`이면 `human_participation = no`, 아니면 `unknown`.
3. **AO** — 공개 계획 목록이 최신 5건만 반환하고 토론 기록이 공개되지 않아 0건으로 보류합니다(`ao/pipeline`의 plans 건수만 기록).
4. **실행·검증(결정 사례)** — `algora/api/outcomes`의 항목 수 + `bridge/api/outcomes`의 `count`. `bridge/api/stats`의 `outcomes.totalProofs`로 교차 확인.
5. **창·정의일** — 결론 시각 UTC `2026-07-01T00:00Z ≤ t < 2026-10-01T00:00Z`. 정의일 `2026-09-18T00:00Z` 이후면 `after_definition_date = yes`.

## 전수 확인

Algora의 Decision Packet 목록과 제안 목록은 `limit=5000`으로 조회합니다(완결 세션 목록과 BRIDGE 제안 목록은 `limit` 인자 없이 조회합니다). 스크립트는 다음 네 가지를 검사해 `fetch-metadata.json`의 `completeness_checks`와 표준 출력 요약에 `[센 값, 기준 값, 일치 여부]`로 기록합니다: DP 수신 건수 = 응답 `total` · Algora 제안 수신 건수 = `proposals/stats`의 `proposals.total` · BRIDGE에서 `decisionPacket`이 있고 synthetic이 아닌 제안 수 = `stats.proposals.total` · 같은 방식으로 센 synthetic 제안 수 = `stats.proposals.synthetic.total`. BRIDGE의 두 수는 창 적용과 `issueId` 중복 제거 전의 수입니다. Algora의 두 검사 가운데 하나라도 일치하지 않으면 표준 오류에 경고를 냅니다. BRIDGE의 두 검사는 기록만 하고 경고를 내지 않습니다. 경고가 나도 실행은 멈추지 않고 집계와 출력을 마칩니다(종료 코드 0). 이 검사들은 목록이 잘렸는지만 가려내며, 목록이 통째로 빈 경우(DP `[0, 0, true]`)는 가려내지 못합니다.

## 한계

- **Algora 결론 문서(Decision Packet)의 공개 목록은 서비스 프로세스의 메모리에만 있어, 서비스가 재시작될 때마다 비워집니다**([`InMemoryDocumentStorage`](https://github.com/MosslandOpenDevs/Algora/blob/efae806/packages/document-registry/src/document.ts#L79-L82)). 관측 시각의 목록에는 2026-09-09T02:36:33Z 재시작 뒤에 만들어진 문서만 있어, 그 전에 결론이 난 Q3 Algora 심의는 셀 수 없었습니다. 관측 81초 뒤인 2026-09-26T10:01:16Z 재시작(재단이 병합한 Algora PR #52의 자동 배포)으로 목록이 비었고, 그 뒤로는 Algora 행의 결론 문서(`output_id`·`n_outputs`·`path`)를 공개 경로로 확인할 수 없습니다. 결론 문서 id는 재시작 뒤 같은 날짜 번호가 다시 쓰일 수 있어 영구 식별자가 아닙니다.
- 관측 뒤인 2026-09-26에 운영자가 입력 이슈 1건(실존 인물 관련 뉴스를 잘못 분류한 자동 생성 항목)과 그에 딸린 제안·세션 기록의 제목에 철회 표시를 하고 이름을 가렸습니다. 2026-09-30에는 그 이슈·제안의 설명과 세션 3건의 에이전트 토론 메시지 본문도 중립 안내문으로 바꿨습니다(원본은 운영자가 비공개로 보관). 기록 id · 상태 · 결론 시각 · 메시지 수와 결론 문서 생성 문구는 그대로여서, 이 행도 위 부분 확인은 그대로 됩니다(2026-09-30 수정 뒤 확인). `cases.csv`의 해당 행은 관측값 그대로 두었습니다(행에는 id만 있습니다).
- BRIDGE의 synthetic 분리는 카테고리 대조로 합니다. 개수가 `stats`와 일치하는 것을 확인 조건으로 둡니다. 관측 시각의 `/api/proposals` 응답에는 제안마다 `synthetic` 불리언이 있었고(true 143 · false 21), 카테고리 대조 결과와 164건 모두 일치했습니다.

---

작성 방식: **AI 보조 · 사람 검토** · [AI 생성 콘텐츠 표시 정책 v1.0](../2026-09-16_ai-content-labelling-policy.md)
