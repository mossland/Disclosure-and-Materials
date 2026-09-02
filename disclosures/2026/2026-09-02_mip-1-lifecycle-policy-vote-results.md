## MIP-1: 공개 서비스·저장소 생명주기 정책 DAO 투표 결과 및 정책 채택 공시

**작성일: 2026-09-02**

### 핵심 요약

* 2026년 8월 19일부터 9월 2일까지 Agora에서 진행된 「MIP-1: 공개 서비스·저장소 생명주기 정책」 안건이 **찬성 100%로 가결**되었습니다.
* 이에 따라 안건의 **4개 조항이 비준**되고, **부속서 A의 최초 분류가 적용**되었습니다. 모든 공개 서비스(`*.moss.land`)와 배포에 연결된 공개 저장소는 Core / Beta / Lab / Archive 중 하나의 상태를 links.moss.land와 저장소 README에 표시합니다.
* 참여 규모는 **108,988.96676301 MOC / 2명**으로, Season 1 안건(2026-08-07 가결)과 동일한 두 지갑이 참여했습니다. Season 1 공시가 기록한 baseline 대비 참여율 변화는 없습니다.
* **이행 현황(본 공시 시점):** links.moss.land registry에 상태 필드 반영 완료(2026-09-02, registry v1.1.0 — 17개 서비스, Beta 8 · Lab 7 · Archive 2 · Core 0). 각 저장소 README 상태 표시는 가결 후 14일 이내(2026-09-16)에 완료합니다.
* 결과 JSON, 전체 투표 서명 export, Passport Transparency 스냅샷, 반영된 registry 사본, SHA-256 해시가 본 공시와 **같은 커밋**에 [증빙 폴더](./2026-09-02_mip-1-lifecycle-policy-vote-evidence/)로 포함되어 있습니다.

### 1. 안건 개요

| 구분 | 내용 |
| --- | --- |
| 안건명 | MIP-1: 공개 서비스·저장소 생명주기 정책 |
| 안건 페이지 | <https://agora.moss.land/proposals/6a85129f8be190cf5d2ebcc1> |
| 투표 기간 | 2026-08-19 11:19 ~ 2026-09-02 11:19 (KST) |
| 투표 방식 | 가스리스 EIP-712 서명 투표 · 1 MOC = 1 vote (위임 시 위임 파워) |
| 투표권 기준 | Ethereum mainnet (chainId 1) snapshot block **25,786,120** 시점의 자가지갑 MOC |
| MOC 컨트랙트 | `0x8bbfe65e31b348cd823c62e02ad8c19a84dd0dab` |
| 안건 본문 해시 | `sha256:7d3cf4a440fdb055022e866b631be18433e80a7e28d6101e11ed9a5eff49bdf5` |
| 최소 참여 요건 | 없음 (minimumMocRequired: 0) |
| 본 안건이 승인하지 않는 것 | 신규 예산 · 투표·보유·매수 보상 · 도메인/데이터/저장소의 삭제 · 인력·조직 변경 · Season 2 |

### 2. 최종 결과

| 선택 | MOC (가중) | 인원 | 비율 |
| --- | ---: | ---: | ---: |
| **For (찬성)** | **108,988.96676301** | **2** | **100%** |
| Against (반대) | 0 | 0 | 0% |
| Abstain (기권) | 0 | 0 | 0% |
| 합계 | 108,988.96676301 | 2 | 100% |

개별 투표 내역(전량 공개 — 서명 원문은 [증빙 `votes.json`](./2026-09-02_mip-1-lifecycle-policy-vote-evidence/votes.json) 참조):

| 지갑 | 선택 | Voting Power (MOC) | 산정 방식 | 투표 시각 (KST) |
| --- | --- | ---: | --- | --- |
| `0x1d67e226…4e59c464` | For | 99,888.96676301 | onchain_votes_snapshot (자가 위임) | 2026-08-19 11:19 |
| `0xe645cd81…335c60b2` | For | 9,100.0 | onchain_votes_snapshot (자가 위임) | 2026-08-26 10:26 |

※ `0x1d67e226…4e59c464`는 본 안건의 제안자 지갑입니다. 안건 토론 스레드에는 투표 기간 중 댓글이 없었습니다.

### 3. 참여 규모의 맥락 (Season 1 원칙 2 이행)

Season 1에서 비준된 원칙 2(참여 지표 표시)에 따라, 참여 수치를 기준값과 함께 공개합니다.

| 지표 | 값 | 비고 |
| --- | ---: | --- |
| 참여 MOC (가중 합계) | 108,988.96676301 | Season 1 결과와 동일 |
| 참여 인원 | 2명 | Season 1과 동일한 두 지갑 |
| MOC 총공급 대비 참여율 | 0.0218% | 총공급 500,000,000 MOC |
| Passport 검증 홀더 잔고 대비 참여율 | 34.60% | 검증 홀더 잔고 314,988.96676301 MOC (2026-09-02 스냅샷) |
| 거래소 보관 MOC | 416,426,769.48 (총공급의 83.3%) | 원칙 3에 따라 구속 투표 밖 — 비구속 시그널·설문 대상 |

Season 1 공시(2026-08-14)가 baseline으로 기록한 참여 MOC·인원·검증 홀더 대비 참여율은 본 안건에서 그대로입니다. Season 1의 전제("참여는 제안을 거듭할수록 커진다")는 이번 안건에서는 아직 확인되지 않았으며, Day 30 보고(2026-09-06 전후)에서 같은 형식으로 다시 기록합니다.

### 4. 비준된 4개 조항

1. **상태 표시 의무** — 모든 공개 서비스와 배포 연결 공개 저장소는 Core / Beta / Lab / Archive 4단계 상태 중 하나를 links.moss.land와 저장소 README에 표시한다.
2. **Core의 요건** — Core는 담당자(owner)와 부담당자(second owner)를 지정하고, 두 사람 모두 배포·복구 권한을 가져야 한다.
3. **부담당자 없는 서비스** — second owner가 없는 서비스는 원칙적으로 Lab 이하로 표시한다. 예외는 사유와 함께 registry에 기록한다.
4. **Source of truth** — links.moss.land registry를 상태의 유일한 기준으로 삼아 월 1회 검토한다. 상태 변경(특히 Archive 지정)은 근거와 함께 기록하고, 검토 결과는 분기 리포트에 기재한다.

| 상태 | 의미 | 약속 |
| --- | --- | --- |
| Core | 상시 운영 | owner + second owner · 장애 대응 · 변경은 예고 후 |
| Beta | 운영 중, 변동 가능 | owner 지정 · 기능·데이터가 바뀔 수 있음 |
| Lab | 실험, best-effort | 예고 없이 변경·중단될 수 있음 |
| Archive | 종료·보존 | 신규 개발 중단 · 기록은 읽기 전용으로 보존 |

Archive는 삭제가 아닙니다. 도메인·데이터·저장소 기록은 보존되며, 삭제는 별도 안건을 요구합니다.

### 5. 부속서 A 적용 결과 — 최초 분류 게시

가결과 함께 부속서 A의 최초 분류를 links.moss.land registry(v1.1.0)에 반영했습니다. 반영된 registry 사본은 [증빙 `ecosystem-registry.json`](./2026-09-02_mip-1-lifecycle-policy-vote-evidence/ecosystem-registry.json)입니다.

| 상태 | 서비스 (registry id) | 비고 |
| --- | --- | --- |
| **Beta** (8) | moss.land (`moss`) · disclosure · links · agora · passport | 부속서 A의 **Core 후보 5개**. 부담당자(second owner)가 아직 지정되지 않아 부속서 A의 명문("미지정 시 Beta로 게시")대로 Beta로 게시 — 제3조 예외로 registry에 사유 기록. 담당자·부담당자가 개인으로 지정되는 즉시 Core로 승격 |
| | wa (Mossverse) · alpha | 부속서 A Beta. 부담당자 미지정(제3조 예외, registry에 기록) |
| | signalmap | 부속서 A Beta, Core 지향 — 승격 조건(담당자·부담당자 지정, 배포·복구 권한)을 registry에 기록 |
| **Lab** (7) | ao · bridge · monitor · city · npc · recipe | 부속서 A Lab |
| | signal | 부속서 A 미기재 — 안건 게시(8/19) 후 등록(8/21)된 서비스로, owner 결정에 따라 Lab |
| **Archive** (2) | media · algora | 부속서 A Archive. media 기능은 SignalMap으로 흡수(2026-08-21, DNS 삭제) · 기록 보존. algora는 Passport 적격 대상에서 제외 |
| **Core** (0) | — | 조항 2·3에 따라 부담당자 없는 Core는 게시하지 않음 |

registry 외 항목(제3자 마켓, 도메인 밖 채널, 데이터 산출물)은 MIP-1의 적용 범위 밖으로 상태를 갖지 않습니다.

### 6. 이행 현황 및 후속 절차

| 의무 (안건 본문) | 기한 | 현황 |
| --- | --- | --- |
| links.moss.land에 상태 필드 반영 · 최초 분류 적용 | 가결 후 14일 (2026-09-16) | **완료** — 2026-09-02, [MosslandOpenDevs/links PR #22](https://github.com/MosslandOpenDevs/links/pull/22) 병합(커밋 `e11f1c9`), registry v1.1.0 공개 |
| 각 저장소 README에 상태 표시 | 가결 후 14일 (2026-09-16) | **진행 중** — 본 공시 시점 links 저장소 README 반영, 나머지 배포 연결 저장소는 순차 반영 |
| 결과 처리: 공시 1건 + Agora 포럼 답글 | — | 본 공시 + [토론 스레드](https://agora.moss.land/forum/6a8512ad8be190cf5d2ebcd5) 답글 |
| registry 월 1회 검토 · 상태 변경 근거 기록 · 분기 리포트 기재 | 상시 | 다음 검토는 2026년 9월 중 (`lifecycleReviewedAt` 갱신), 결과는 2026 Q3 리포트에 기재 |

### 7. 증빙 (Evidence)

본 공시와 같은 커밋에 포함된 [증빙 폴더](./2026-09-02_mip-1-lifecycle-policy-vote-evidence/)의 파일과 SHA-256 해시입니다. GitHub 커밋 타임스탬프가 수집 시점을 증명합니다.

| 파일 | 내용 | SHA-256 |
| --- | --- | --- |
| `proposal.json` | 안건 공식 레코드 (contentHash, snapshot block, 투표 규칙 포함) | `04bf2e0a3f49161dc8219352e821f9c3077d94532e456344d1a86fc58bae4b68` |
| `votes.json` | 전체 투표 export (EIP-712 서명 포함) | `75aba3d37116db9b01e417d9dcdac3377f55a0e78d0022b7c416c5c18e56c447` |
| `transparency.json` | Passport Transparency 스냅샷 (2026-09-02) | `49534821f0f6fdbf2bfb62e7257a3a834aa228bfdc4352a72702c968f822842b` |
| `ecosystem-registry.json` | 상태 필드가 반영된 links.moss.land registry (v1.1.0) | `22ccd143794f84300d0d688a622573d5f99e12e71327dae9068c69e6d54da9cc` |
| `fetch-metadata.json` | 수집 시각·원본 URL | `ec7358eefeaded25b78b4fe47df811093a9240b70adb153a8323644f267d5457` |

재검증 절차는 증빙 폴더의 [README](./2026-09-02_mip-1-lifecycle-policy-vote-evidence/README.md)를 참조하십시오.

### 8. 관련 링크

* [안건 페이지 (Agora)](https://agora.moss.land/proposals/6a85129f8be190cf5d2ebcc1)
* [안건 토론 스레드 (Agora Forum)](https://agora.moss.land/forum/6a8512ad8be190cf5d2ebcd5)
* [links.moss.land — 상태가 표시된 서비스 목록](https://links.moss.land/) · [registry JSON](https://links.moss.land/ecosystem-registry.json)
* [MosslandOpenDevs/links PR #22 — 부속서 A 값 반영](https://github.com/MosslandOpenDevs/links/pull/22)
* [Passport Transparency](https://passport.moss.land/transparency)
* 선례: [2026-08-14 MOC Activation Season 1 DAO 투표 결과 및 시즌 채택 공시](./2026-08-14_moc-activation-season1-vote-results.md)

---

### English Summary

**MIP-1: Public Service & Repository Lifecycle Policy — DAO Vote Results and Policy Adoption**

The proposal ["MIP-1: 공개 서비스·저장소 생명주기 정책"](https://agora.moss.land/proposals/6a85129f8be190cf5d2ebcc1) was **approved with 100% For** in a gasless EIP-712 signature vote on Agora (2026-08-19 → 2026-09-02 KST, Ethereum mainnet snapshot block **25,786,120**).

* **Results:** For 108,988.96676301 MOC (2 voters; one is the proposer's wallet) / Against 0 / Abstain 0 — the same two wallets and the same weight as the Season 1 vote, so the participation baseline recorded on 2026-08-14 is unchanged.
* **Effect:** Four articles are ratified — every public `*.moss.land` service and deployment-linked public repository displays one of four lifecycle states (Core / Beta / Lab / Archive) on links.moss.land and in its README; Core requires a named owner and second owner with deploy and recovery rights; a service without a second owner is shown as Lab or below unless an exception is recorded; the links.moss.land registry is the single source of truth, reviewed monthly and reported quarterly. Annex A's initial classification is applied with the vote.
* **Initial classification (registry v1.1.0, live 2026-09-02):** Beta 8 (moss.land, disclosure, links, agora, passport — Annex A Core candidates published as Beta until a second owner is designated; wa, alpha, signalmap), Lab 7 (ao, bridge, monitor, city, npc, recipe, signal), Archive 2 (media, algora), Core 0. Archive is not deletion; domains, data and repositories are preserved.
* **Implementation:** the links.moss.land status field is live ([MosslandOpenDevs/links#22](https://github.com/MosslandOpenDevs/links/pull/22), commit `e11f1c9`); repository README status lines are being added within the 14-day window (by 2026-09-16).
* **Evidence:** the proposal record, the full signed-vote export, a Passport Transparency snapshot, the published registry, and their SHA-256 hashes are committed [alongside this disclosure](./2026-09-02_mip-1-lifecycle-policy-vote-evidence/); the GitHub commit timestamp attests the collection time.

**모스랜드**
**Mossland**
