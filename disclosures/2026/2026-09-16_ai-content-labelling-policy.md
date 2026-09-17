## AI 생성 콘텐츠 표시 정책 v1.0

**작성일: 2026-09-16** · **버전: v1.0** · **발행·시행일: 2026-09-17 12:59 KST (병합 커밋 `50036b7`)**

> 본 정책은 이 문서를 포함한 커밋이 기본 브랜치에 병합된 시각에 발행·시행됩니다. 작성 시각과 발행 시각은 다를 수 있으며, 발행일은 병합 기록으로 확정합니다. 정책 URL과 파일명은 개정 후에도 바꾸지 않으며(파일명의 날짜는 최초 작성일이고, 파일명에는 버전을 넣지 않습니다), 현재 버전과 개정일은 이 헤더에 표시합니다. 한국어와 영어의 해석에 차이가 있으면 한국어판을 기준으로 합니다.

### 핵심 요약

- 재단 발행물에 AI가 작성·번역한 내용이 있으면 알리고, 담당자가 확인한 뒤 발행합니다.
- 자동으로 내용을 만드는 서비스에는 이용자가 볼 수 있는 AI 안내를 둡니다.
- 이미지·영상은 눈에 보이는 표시 하나를 기본으로 합니다. 별도 대장, 건수 집계, 워터마크·메타데이터 시스템을 새로 만들 의무는 없습니다.
- 이 정책은 Q2에 완료하지 못해 Q3로 이월한 운영 기준을 정리한 것입니다. 공개 문서와 실제 적용 사례를 확인한 뒤 이행 결과를 보고합니다.

### 1. 목적과 범위

2026-02-09 초안의 세 원칙인 **투명한 공개·안전 우선·책임 있는 운영**을 간단한 표시·검토 규칙으로 정합니다. 기존 문서의 ‘AI 활용 정책’, ‘AI 콘텐츠 표시 정책’도 이 정책을 가리킵니다.

| 구분 | 대상 | 적용 방식 |
| --- | --- | --- |
| 재단 발행물 | Medium KO/EN, 공시 md/PDF, 분기 리포트, X, 공식 웹사이트 카피, GitHub README·문서, Agora 재단 안건·포럼 글 | 발행물에 작성 방식을 표시하고 담당자가 검토 |
| 제품 출력 | AO·BRIDGE·Signal·Signal Map·Alpha·NPC·City·Recipe·Agora(AI 요약·이해 지원 기능) 등 운영 서비스의 자동 산출 | 서비스 안내, 대화 화면 안내, 필요한 이미지 표시 |
| 기존 기록·재표시 | Archive 서비스, Monitor 등 다른 서비스의 산출을 다시 보여주는 화면 | 아래 §5의 기존 기록 원칙 적용 |

재단 내부 문서는 대상이 아닙니다. 사람이 입력한 레지스트리·증빙 데이터와 AI가 아닌 코드로 만든 차트·OG 이미지는 그 이유만으로 AI 생성물로 분류하지 않습니다. 서비스 목록은 현재 운영 상태에 맞춰 갱신하되, 새 분류 체계를 만들지는 않습니다.

### 2. 작성 방식의 구분

| 구분 | 뜻 | 표시 |
| --- | --- | --- |
| 사람 작성 | 공개할 표현을 사람이 작성. AI를 맞춤법 확인·검색·참고에만 사용한 경우 포함 | 별도 AI 표시 불필요. 공시에는 ‘사람 작성’ 1줄 |
| AI 보조 | AI가 초안이나 일부 표현을 작성하고 사람이 검토·승인 | ‘AI 보조 · 사람 검토’ |
| AI 번역 | AI 번역문을 사람이 원문과 확인 | ‘AI 번역 · 사람 검토’ |
| AI 생성 이미지·영상 | 생성형 AI로 만든 이미지·영상. 사람이 선택·편집했어도 생성 사실은 유지 | ‘AI 생성 이미지’ 또는 ‘AI 생성 영상’ |
| 제품 출력 | 서비스가 자동 생성하며 항목마다 발행 전 사람 검토를 거치지 않는 내용 | 서비스의 AI 안내 |

글과 첨부 이미지는 각각 판단합니다. 사람이 쓴 글에 AI 이미지를 붙였다면 이미지에 표시하면 됩니다. 제품 출력을 재단의 설명 글로 다시 발행할 때는 그 글을 사람이 검토하고 작성 방식을 표시합니다.

### 3. 사람 검토와 승인

일반 AI 보조 발행물은 담당자가 **전체 내용을 읽고 주요 사실·수치·인용을 출처와 확인한 뒤** 승인합니다. 확인하지 못한 내용은 빼거나 불확실성을 밝힙니다. AI 번역은 원문의 의미와 사실이 달라지지 않았는지 확인합니다. **사람의 검토 없이 LLM 출력을 그대로 공개하지 않습니다.** 검토 후 문제가 없는 문장까지 반드시 다시 쓸 필요는 없습니다.

검증과 승인은 한 사람이 맡을 수 있으며 별도 결재를 추가하지 않습니다. 기존 발행·커밋 기록을 사용하고, 공개 담당 표기는 maintainer 핸들 `MosslandOpenDevs`로 둘 수 있습니다. 실제 검토가 끝나기 전에는 ‘사람 검토 완료’라고 표시하지 않습니다.

**분기 리포트는 기존 Q2 §B 절차를 유지합니다.** (1) 자동 메타데이터 수집(GitHub API·공시 대시보드·RSS) → (2) LLM 초안 작성 → (3) 담당 팀 사실 검증(초안의 검증 마커 전수 해소) → (4) 재단 검토·승인 → (5) 발행. 초안 단계의 모든 사실 서술 중 외부 검증이 불가한 항목에는 검증 마커를 붙이며, **마커가 남아 있는 버전은 발행하지 않습니다.** 검증·승인 역할은 한 사람이 맡을 수 있습니다. 다른 발행물에는 이 마커 절차를 의무로 확대하지 않습니다.

### 4. 어디에 어떻게 표시하는가

| 채널 | 최소 표시 | 위치 |
| --- | --- | --- |
| Medium·웹사이트 글·README·문서·Agora 재단 글 | AI 보조 또는 AI 번역이면 작성 방식 1줄과 정책 링크 | 본문 말미 |
| 공시 md/PDF | 사람 작성·AI 보조·AI 번역 중 해당 방식 1줄과 정책 링크 | 서명 위 또는 마지막 페이지 |
| 분기 리포트 | §B 작성 절차와 정책 링크, §1 말미 요약 1줄 | 매 호 |
| AI 생성 이미지·영상 | ‘AI 생성 이미지/영상’이라는 눈에 보이는 표시 하나 | 캡션·함께 게시한 본문·이미지나 영상 내부 중 한 곳 |
| X | AI 보조·번역 글에는 해당 문구, AI 이미지·영상에는 생성 표시 | 게시글 본문. 고지가 있는 원문을 연결하는 짧은 안내 글은 텍스트 표시 생략 가능 |
| 자동 산출 서비스 | ‘이 서비스에는 AI가 자동 생성한 내용이 포함됩니다. 사람이 검토하지 않은 내용이 있을 수 있으며, 참고용입니다.’ | 푸터·소개 페이지 등 이용자가 볼 수 있는 곳 |
| 대화형 화면 | ‘AI와 대화 중입니다.’ | 대화 화면 상단 또는 첫 응답 전 |
| 공식 웹사이트·공시 대시보드 | 정책 링크, AI 실험 산출을 보여주는 부분의 간단한 설명 | 푸터 또는 해당 섹션 |

이미지의 모델명을 알면 함께 적을 수 있습니다. alt 설명, 이미지 내 워터마크, 파일 메타데이터는 가능한 경우 추가하되 모두를 의무로 요구하지 않습니다. 플랫폼이 메타데이터를 제거했다는 이유만으로 재업로드하지 않습니다.

API·RSS·llms.txt·MCP에는 기존 설명이나 문서에 AI 사용 여부를 안내하는 것으로 충분합니다. 이 정책만을 위해 응답에 새 필드를 추가하거나 기존 형식을 바꿀 의무는 없습니다. 서비스의 출처 데이터와 AI 해석을 모두 ‘AI가 만든 사실’로 표시하지 않도록 구분합니다.

### 5. 기존 기록과 예외

- 시행 전 발행물을 일괄 재작성하거나 다시 올리지 않습니다. 기존 표시의 오류는 §7에 따라 정정합니다.
- Q1·Q2 리포트 본문은 당시 기록으로 보존합니다. 두 리포트 §B가 확정 정책 발행 후 부록을 갱신하겠다고 예고했으므로(Q1 §B 「확정 정책이 2026 Q2 발행되면 본 부록도 함께 갱신됩니다」, Q2 §B 「확정판 발행(§13) 후 그 기준으로 갱신합니다」), 정책 발행 후 30일 이내에 각 §B의 그 예고 문장 바로 뒤에 갱신일·정책 링크와 ‘확정 정책은 2026 Q2에 발행되지 못해 Q3로 이월되었다’는 사실, ‘이후 발행물은 확정 정책 적용’이라는 안내를 더합니다(수치·절차가 바뀌지 않는 표현 정합성 갱신이며, 리포트를 재발행하지는 않습니다). Q2는 자체 규정에 따라 v1.3 개정으로 기록하고, Q1은 §B에 갱신일이 표기된 문장을 더합니다. 담당은 `MosslandOpenDevs`입니다. Q3부터 새 기준을 적용합니다.
- Archive 서비스는 이 정책을 이유로 재배포하지 않습니다. 기존 레지스트리 설명이나 안내 페이지에 AI 산출을 포함한 기록임을 알릴 수 있습니다. Monitor 등 재표시 화면은 원본의 출처와 AI 표시를 함께 보여주는 것을 원칙으로 합니다.
- 코드의 AI 사용은 기존 커밋·PR의 AI 사용 표기나 `Co-Authored-By` 기록으로 갈음할 수 있습니다. README·문서 본문에는 독자가 볼 수 있는 작성 방식 표시를 둡니다.
- 시뮬레이션·목업 수치의 라벨은 AI 생성 표시와 별개로 유지합니다. AI 표시가 실제 관측 데이터라는 뜻은 아닙니다.
- 실제 인물·사건으로 오인하게 하는 기만적 합성 콘텐츠는 발행하지 않습니다. 그 밖의 예외가 필요하면 기존 발행 기록에 이유를 간단히 남깁니다.

### 6. 기록

발행물의 고지와 기존 커밋·PR 기록을 사용합니다. **별도 적용 대장과 건수 집계는 필수가 아닙니다.** 외부 채널의 대표 적용 사례와 주요 정정은 다음 분기 리포트에 링크로 정리합니다. 이미 있는 대장은 계속 써도 됩니다.

### 7. 정정과 문제 대응

일반적인 표시 누락·오분류는 인지 후 **7일 이내** 고치고 정정일과 사유를 간단히 남깁니다. 원문을 직접 수정하기 어려운 채널에서는 해당 글이나 답글에 정정 안내를 붙입니다.

개인정보 노출이나 유해한 내용은 즉시 비공개할 수 있습니다. 문제가 있는 원문을 공개 상태로 보존할 의무는 없으며, 민감한 내용을 제외한 정정 이력만 남깁니다. 공개 신고에는 민감한 정보를 적지 않도록 안내하고, 필요한 내용은 재단의 기존 비공개 연락 경로로 받습니다.

제품의 오류·악용·자동 실행 문제는 해당 서비스의 기존 대응 절차로 다룹니다. 이 표시 정책은 서비스의 안전장치가 구현되었다는 보증이나 배포·자금 사용의 승인을 대신하지 않습니다.

### 8. 법령·개정

이 정책은 재단이 채택하는 자발적 표시·검토 기준이며, 적용되는 법령을 배제하거나 대체·유예하지 않습니다. AI를 작성 도구로 이용하는 경우와 이용자에게 AI 서비스를 제공하는 경우를 구분해 서비스별로 판단하며, 무료 또는 Lab이라는 이유만으로 적용 제외를 단정하지 않습니다. 안내 문구만으로 법정 의무를 충족했다고 하거나 EU 규정의 준수·적용 면제를 주장하지 않습니다.

매년 9월 또는 운영상 문제가 확인될 때 검토합니다. 오탈자·링크·서비스 목록은 갱신일을 남기고 고칠 수 있습니다. 표시 문구·절차·예외를 바꾸면 버전과 개정 이유를 기록하고, 중요한 변경은 적용 전에 알립니다. 긴급 정정은 먼저 시행할 수 있습니다. MIP-1의 서비스 생명주기 분류는 변경하지 않습니다.

### 9. 이행 현황

Q2 리포트 §13.1의 완료 증거 「버전이 표기된 확정 문서의 공개 URL + 재단 발행물 적용 사례」에 대한 이행 현황입니다. **완료**로 적은 항목은 실제 URL·병합 기록으로 확인한 것이며, 나머지는 예정입니다. 갱신할 때는 이 표를 제자리에서 고치고 `(YYYY-MM-DD 갱신)`을 남깁니다.

| 항목 | 목표 | 현재 상태 |
| --- | --- | --- |
| 버전이 표기된 확정 문서의 공개 URL | 2026-09-30 (Q3 종료) | **완료** — 2026-09-17 12:59 KST 병합 ([PR #15](https://github.com/mossland/Disclosure-and-Materials/pull/15), 커밋 `50036b7`). 공개 URL: [disclosures/2026/2026-09-16_ai-content-labelling-policy.md](https://github.com/mossland/Disclosure-and-Materials/blob/main/disclosures/2026/2026-09-16_ai-content-labelling-policy.md) · README 공시 목록 등재 (2026-09-17 갱신) |
| 첫 적용 사례 | Q3 내 실제 재단 발행물 1건에 적용 | 예정 — 발행 후 링크 추가 |
| Q3 리포트 §B 적용 | Q3 리포트 발행 시 | 예정 |
| 운영 중인 서비스의 간단한 AI 안내 | 기존 수정 작업에서 순차 반영 | 예정 — 기존 표시를 확인하고 부족한 부분만 보완. 별도 일괄 적용 기한은 두지 않음 |
| Q1·Q2 리포트 §B 갱신 안내 (문구 1줄, 수치 무변경) | 정책 발행 +30일 = 2026-10-17 | **완료** — 2026-09-17 19:03 KST 병합 ([PR #17](https://github.com/mossland/Disclosure-and-Materials/pull/17), 커밋 `e535a10`). [Q1 §B](https://mossland.github.io/Disclosure-and-Materials/disclosures/2026-q1/#appB) · [Q2 v1.3 §B](https://mossland.github.io/Disclosure-and-Materials/disclosures/2026-q2/#appB) (2026-09-17 갱신) |

이 문서의 자체 표시도 적용 사례가 될 수 있지만, 문서 공개와 전 서비스 적용은 별개의 결과입니다. 완료한 항목만 실제 날짜와 링크로 갱신합니다.

### 10. 복사용 문구와 공시 연동

다음 문구는 **실제로 사람 검토를 마친 발행물**에 사용합니다. 초안에는 ‘발행 전 사람 검토 예정’이라고 씁니다.

- 일반 글: `작성 방식: AI 보조 · 사람 검토 · [AI 생성 콘텐츠 표시 정책 v1.0](정책 URL)`
- 번역: `작성 방식: AI 번역 · 사람 검토 · 원문 링크 · 정책 링크`
- 사람 작성 공시: `작성 방식: 사람 작성 · 정책 링크`
- 이미지·영상: `AI 생성 이미지` / `AI 생성 영상`
- 분기 리포트 §1: `본 리포트는 AI 보조 발행물이며, 작성·검토 절차는 §B에 설명합니다.`

분기 리포트 §B에는 §3의 기존 5단계와 마커 규칙, 실제 사용한 번역 방식, 정책 링크를 적습니다. 적용 건수를 세는 대신 대표 사례와 주요 정정 링크를 붙이면 됩니다.

본 정책을 발행하는 커밋에서 README 공시 목록에 정책 URL을 연결하고, TRACKING 목록에 첫 적용 사례, Q3 리포트 §B 갱신, Q1·Q2 리포트 §B 갱신 안내를 등록합니다. 이후 이행 상태와 링크는 TRACKING에서 갱신합니다. 새 대장·증빙 폴더·해시 목록을 의무로 만들지 않습니다. 실제 보존·확인하지 않은 증빙을 포함했다고 쓰지 않습니다.

### 11. 관련 기록

- [2026-02-09 초안 「AI가 만든 콘텐츠, 어디까지 표시해야 할까?」](https://medium.com/mossland-blog/ai%EA%B0%80-%EB%A7%8C%EB%93%A0-%EC%BD%98%ED%85%90%EC%B8%A0-%EC%96%B4%EB%94%94%EA%B9%8C%EC%A7%80-%ED%91%9C%EC%8B%9C%ED%95%B4%EC%95%BC-%ED%95%A0%EA%B9%8C-2f5f99dbc795) (Medium, KO) — §1 세 원칙의 출처
- [2026 Q2 리포트](https://mossland.github.io/Disclosure-and-Materials/disclosures/2026-q2/) §B·§13.1
- [2026 Q1 리포트](https://mossland.github.io/Disclosure-and-Materials/disclosures/2026-q1/) §B
- [MIP-1 결과 공시](./2026-09-02_mip-1-lifecycle-policy-vote-results.md)
- [공시 예고 관리 목록](../TRACKING.md)

---

## English — AI-Generated Content Labelling Policy v1.0

**Written: 2026-09-16 · Version: v1.0 · Published and effective: 2026-09-17 12:59 KST (merge commit `50036b7`)**

This policy takes effect when the commit containing it is merged into the default branch; the merge record fixes the publication date. The policy URL and file name stay fixed across revisions (the date in the file name is the original authoring date, and the file name carries no version); the current version and revision date are shown in this header. The Korean text governs where interpretations differ.

### Summary and 1. Purpose and scope

The policy turns the February draft's principles of **transparent disclosure, safety first and responsible operation** into simple labelling and review rules. It addresses the operating standard left incomplete in Q2 and carried into Q3. Completion is reported after the public policy and a real application are confirmed.

Foundation publications include Medium KO/EN, disclosure md/PDF, quarterly reports, X, website copy, GitHub READMEs/docs and Foundation posts on Agora. They carry an authoring notice and human review. Automatic outputs from services such as AO, BRIDGE, Signal, Signal Map, Alpha, NPC, City, Recipe and Agora's AI summarisation feature use service notices and, where relevant, chat or image notices. Archive and redisplay surfaces follow §5. Internal documents are excluded. Human-entered registry/evidence data and non-AI, code-generated charts or OG images are not classified as AI-generated merely because they are automated. Update the service list as operations change. Earlier references to an 'AI use policy' or 'AI content labelling policy' mean this policy; no new classification scheme is created.

### 2. Categories

- **Human-written:** a person wrote the published expression; AI used only for proofreading, search or reference is allowed. No AI label is needed; disclosures carry a human-written line.
- **AI-assisted:** AI drafted some or all wording and a person reviewed and approved it. Label: `AI-assisted · human-reviewed`.
- **AI-translated:** a person checked the AI translation against the source. Label: `AI-translated · human-reviewed`.
- **AI-generated image/video:** made using generative AI, even if a person selected or edited it. Label: `AI-generated image` or `AI-generated video`.
- **Product output:** generated automatically without human review before each item is published. Use the service notice.

Assess text and attached images separately. A human-written article with an AI image needs an image label. When product output is republished as a Foundation article, review that article and label its authoring method.

### 3. Human review and approval

For ordinary AI-assisted publications, the publisher reads the full content and checks key facts, figures and quotations against sources before approval. Remove unverified claims or state their uncertainty. Check translations for changes in meaning or fact. **Do not publish LLM output without human review.** Correct wording need not be rewritten simply because AI drafted it. One person may verify and approve; no extra sign-off is required. Use existing publication/commit records. The public responsible handle may be `MosslandOpenDevs`. Do not claim completed human review before it occurs.

Quarterly reports retain the Q2 §B process: (1) automated metadata collection (GitHub API, disclosure dashboard, RSS) → (2) LLM drafting → (3) responsible-team fact verification, resolving every verification marker → (4) Foundation review and approval → (5) publication. Every factual draft statement that cannot be verified externally receives a marker; **no version is published while markers remain**. One person may hold the verification and approval roles. Other publications need not adopt the marker process.

### 4. Placement

Articles, READMEs/docs and Foundation Agora posts carry an AI-assisted or AI-translated line and policy link at the end where applicable. Disclosure md/PDF carries the applicable human-written, AI-assisted or AI-translated line above the signature or on the last page. Quarterly reports carry §B and a short notice in §1.

AI images/videos need **one visible label**, in the caption, accompanying post or the artefact itself. On X, label AI-assisted/translated posts and AI images/videos; a short announcement linking to a source with its own notice may omit the text label. The model name may be added if known. Alt descriptions, in-image watermarks and file metadata are optional additions; platform metadata stripping alone does not require re-uploading.

Automatic-output services display: `This service includes AI-generated content. Some content may not have been reviewed by a person. For reference only.` Place it somewhere users can find, such as the footer or introduction. Chat displays `You are talking with an AI` at the top or before the first reply. The official website and the disclosure dashboard link the policy and briefly describe the sections that show AI-experiment output (footer or the relevant section). API/RSS/llms.txt/MCP can explain AI use in existing descriptions or documentation, without new response fields or format changes. Distinguish source data from AI interpretation.

### 5. Existing records and exceptions

Do not rewrite or re-upload earlier publications wholesale; correct inaccurate labels under §7. Preserve Q1/Q2 reports as historical records. Within 30 days of publication, add, immediately after the update notice in each §B of the Q1 and Q2 reports, a dated note, the policy link, the fact that the final policy was not published in Q2 and was carried into Q3, and a line explaining that subsequent publications follow the final policy — a wording-consistency update that changes no figure or procedure; the reports are not re-issued. Q2 records this as a v1.3 revision under its own versioning rule; Q1 adds a dated note to §B. Owner: `MosslandOpenDevs`. Apply the new standard from Q3.

Do not redeploy Archive services solely for this policy; existing registry descriptions or information pages can note that the archive contains AI output. Redisplay surfaces such as Monitor should show the original source and AI notice together. Code can use existing commit/PR AI-use notes or `Co-Authored-By`; READMEs/docs need a reader-visible authoring line. Keep simulation/mock-data labels separate from AI labels: an AI label does not mean a figure is observed data. Do not publish deceptive synthetic content that could be mistaken for real people or events. Explain other necessary exceptions briefly in existing publication records.

### 6. Records and 7. Corrections

Use notices and existing commit/PR records. **A separate ledger and entry counts are not mandatory.** Link representative external applications and significant corrections in the next quarterly report. Existing ledgers may continue to be used.

Correct ordinary missing or inaccurate labels within **7 days of awareness**, recording the date and a short reason. Where the original cannot readily be edited, add a notice to the post or a reply. Personal-data exposure or harmful content may be hidden immediately; the problematic original need not remain public. Retain only a correction record that excludes sensitive content. Ask reporters not to include sensitive information in public reports and use the Foundation's existing private contact route where needed. Product errors, abuse and automated actions follow the service's existing response procedures. This policy neither guarantees implemented safety controls nor authorises deployment or use of funds.

### 8. Law and revision

This is a voluntary labelling and review standard; it does not exclude, replace or defer applicable law. Assess tool use for drafting separately from providing AI services to users, service by service; free or Lab status alone does not establish an exemption. A notice alone is not claimed to fulfil statutory duties, and the policy claims neither EU compliance nor exemption from EU rules. Review every September or when operating problems arise. Date minor corrections and inventory/link updates; version changes to wording, procedure or exceptions and explain why. Announce important changes before application; urgent corrections may take effect first. MIP-1 lifecycle classifications remain unchanged.

### 9–11. Implementation, reusable notices and records

Implementation status: the versioned policy was published on 2026-09-17 12:59 KST (merge commit `50036b7`; see the §9 table); application to one actual Foundation publication follows within Q3; the Q3 §B update is made when that report is published; the dated note was added to §B of the Q1 and Q2 reports on 2026-09-17 (Q2 revised to v1.3; PR #17, commit `e535a10`), within the 30-day window; and simple service notices are added during normal maintenance, with no separate deadline for applying them across all services. Only confirmed items are marked complete, with actual dates and links. Update the status table in place and mark it (updated YYYY-MM-DD). This policy’s own notice can be an application, but policy publication and adoption across services are separate results.

After actual human review, use `Authoring: AI-assisted · human-reviewed · policy link`, `Authoring: AI-translated · human-reviewed · source and policy links`, or `Authoring: human-written · policy link`. Drafts say `human review pending before publication`. Image/video labels are `AI-generated image` / `AI-generated video`. Quarterly §1 can say: `This is an AI-assisted report; its authoring and review process is explained in §B.` §B retains the five steps and marker rule, explains translation actually used and links the policy, representative applications and significant corrections, without mandatory counts. The same commit that publishes this policy links it from the README disclosure index and registers its follow-up items — the first application, the Q3 §B update and the dated Q1/Q2 §B note — in the existing TRACKING list, where their status and links are maintained. No new ledger, evidence folder or hash list is mandatory, and no unverified preservation claim is made. Related links — the 2026-02-09 draft post on Medium (Korean), the Q1/Q2 reports, MIP-1 and TRACKING — are listed in §11 above.

---

작성 방식: **AI 보조 · 사람 검토** · [AI 생성 콘텐츠 표시 정책 v1.0](./2026-09-16_ai-content-labelling-policy.md) / Authoring: **AI-assisted · human-reviewed** · [AI-Generated Content Labelling Policy v1.0](./2026-09-16_ai-content-labelling-policy.md)
