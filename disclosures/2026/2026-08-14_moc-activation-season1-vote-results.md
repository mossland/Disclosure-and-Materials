## MOC Activation Season 1 — 자가지갑 참여 전환 (90일 파일럿) DAO 투표 결과 및 시즌 채택 공시

**작성일: 2026-08-14**

### 핵심 요약

* 2026년 7월 8일부터 8월 7일까지 Agora에서 진행된 「MOC Activation Season 1 — 자가지갑 참여 전환 (90일 파일럿)」 안건이 **찬성 100%로 가결**되었습니다.
* 이에 따라 안건이 제시한 **4가지 원칙이 비준**되고, **Season 1이 90일 공식 파일럿으로 채택**되었습니다. 시즌 기간은 비준일(투표 종료일) 기준 **2026-08-07 ~ 2026-11-05**입니다.
* 참여 규모는 **108,988.96676301 MOC / 2명**입니다. 안건 스스로 밝혔듯 참여율은 작게 시작하며, 본 공시는 이 수치를 시즌의 **baseline**으로 기록합니다.
* 결과 JSON, 전체 투표 서명 export, Passport Transparency 스냅샷, SHA-256 해시가 본 공시와 **같은 커밋**에 [증빙 폴더](./2026-08-14_moc-activation-season1-vote-evidence/)로 포함되어 있습니다.

### 1. 안건 개요

| 구분 | 내용 |
| --- | --- |
| 안건명 | MOC Activation Season 1 — 자가지갑 참여 전환 (90일 파일럿) |
| 안건 페이지 | <https://agora.moss.land/proposals/6a4decb73697e1a9d307e327> |
| 투표 기간 | 2026-07-08 16:57 ~ 2026-08-07 16:57 (KST) |
| 투표 방식 | 가스리스 EIP-712 서명 투표 · 1 MOC = 1 vote (위임 시 위임 파워) |
| 투표권 기준 | Ethereum mainnet (chainId 1) snapshot block **25,486,030** 시점의 자가지갑 MOC |
| MOC 컨트랙트 | `0x8bbfe65e31b348cd823c62e02ad8c19a84dd0dab` |
| 안건 본문 해시 | `sha256:490acdbc00a6e7303e1682dd9c00cd648c9fe90962429dff59f67d1d88c9ce78` |
| 최소 참여 요건 | 없음 (minimumMocRequired: 0) |

### 2. 최종 결과

| 선택 | MOC (가중) | 인원 | 비율 |
| --- | ---: | ---: | ---: |
| **For (찬성)** | **108,988.96676301** | **2** | **100%** |
| Against (반대) | 0 | 0 | 0% |
| Abstain (기권) | 0 | 0 | 0% |
| 합계 | 108,988.96676301 | 2 | 100% |

개별 투표 내역(전량 공개 — 서명 원문은 [증빙 `votes.json`](./2026-08-14_moc-activation-season1-vote-evidence/votes.json) 참조):

| 지갑 | 선택 | Voting Power (MOC) | 산정 방식 | 투표 시각 (KST) |
| --- | --- | ---: | --- | --- |
| `0xe645cd81…335c60b2` | For | 9,100.0 | onchain_votes_snapshot (위임) | 2026-07-08 17:25 |
| `0x1d67e226…4e59c464` | For | 99,888.96676301 | onchain_balance_snapshot | 2026-07-09 18:27 |

※ `0x1d67e226…4e59c464`는 본 안건의 제안자 지갑입니다.

### 3. 참여 규모의 맥락 (원칙 2 이행)

비준된 원칙 2(참여 지표 표시)에 따라, 참여 수치를 기준값과 함께 공개합니다.

| 지표 | 값 | 비고 |
| --- | ---: | --- |
| 참여 MOC (가중 합계) | 108,988.96676301 | |
| 참여 인원 | 2명 | |
| MOC 총공급 대비 참여율 | 0.0218% | 총공급 500,000,000 MOC |
| Passport 검증 홀더 잔고 대비 참여율 | 34.60% | 검증 홀더 잔고 314,988.96676301 MOC (2026-08-14 스냅샷) |
| 거래소 보관 MOC | 412,701,334.83 (총공급의 82.5%) | 원칙 3에 따라 구속 투표 밖 — 비구속 시그널·설문 대상 |

안건 본문의 표현대로, 본 안건은 "전체 MOC 보유자의 완성된 민의를 주장하지 않습니다." 위 수치는 Season 1의 출발점이며, 시즌 동안 제안을 거듭하며 이 참여율이 어떻게 변하는지를 이후 보고에서 같은 형식으로 추적합니다.

### 4. 비준된 4가지 원칙

1. **출금 비용 보전만** — MOC 직접 지급은 자가지갑 이전 시 출금 비용 상당액 보전으로만 한다. 투표·보유·매수 보상은 없다.
2. **참여 지표 표시** — 투표 결과 화면에 참여 MOC(가중 합계)와 참여 인원을 표기하고, 총공급·Passport 활성 MOC·voting power 대비 참여율(%)은 데이터 연동이 완료되는 대로 단계적으로 추가한다.
3. **구속 투표 = 자가지갑만** — 거래소 보관 MOC는 비구속 시그널·설문으로만 참여한다.
4. **지표 공개** — 인증·위임·참여·보전 집계를 [Passport Transparency](https://passport.moss.land/transparency)에 상시 공개하고, 시즌 요약은 월간 공시로 남긴다.

### 5. Season 1 기간 및 보고 일정

* **시즌 기간:** 2026-08-07 (비준일) ~ 2026-11-05 (90일)
* **Day 30 보고:** 2026-09-06 전후 — 공시 1건 + Agora 포럼 답글
* **Day 60 보고:** 2026-10-06 전후 — 동일 형식
* **최종 보고:** 시즌 종료(2026-11-05) 후 — 시즌 전체 지표 요약 및 Season 2 여부 판단 자료

각 보고는 본 공시와 동일한 형식(공시 문서 + 증빙 커밋 + Agora 포럼 답글)으로 이 저장소에 쌓입니다. 비준된 안건의 종료 처리는 "공시 1건 + 포럼 답글"을 관례로 합니다.

### 6. 증빙 (Evidence)

본 공시와 같은 커밋에 포함된 [증빙 폴더](./2026-08-14_moc-activation-season1-vote-evidence/)의 파일과 SHA-256 해시입니다. GitHub 커밋 타임스탬프가 수집 시점을 증명합니다.

| 파일 | 내용 | SHA-256 |
| --- | --- | --- |
| `proposal.json` | 안건 공식 레코드 (contentHash, snapshot block 포함) | `0aa62fe91d5f6653105c1b243fb29805cb5e0fb5e69c3fef36ea54d0b9b60d15` |
| `votes.json` | 전체 투표 export (EIP-712 서명 포함) | `8e3ad67884e2764dec1078b5f3df68fb7a225c0b4d34bdec4a9fbf8f7738c171` |
| `transparency.json` | Passport Transparency 스냅샷 (2026-08-14) | `1be89db384061517379fa09b09eb79b8484e176540e9be0e0b37ed01ab618b32` |
| `fetch-metadata.json` | 수집 시각·원본 URL | `37b52b8468993978aaa6fbec474c89089013aef71a9604341067f936162cbee0` |

재검증 절차는 증빙 폴더의 [README](./2026-08-14_moc-activation-season1-vote-evidence/README.md)를 참조하십시오.

### 7. 관련 링크

* [안건 페이지 (Agora)](https://agora.moss.land/proposals/6a4decb73697e1a9d307e327)
* [안건 토론 스레드 (Agora Forum)](https://agora.moss.land/forum/6a4decc73697e1a9d307e33a)
* [Passport Transparency](https://passport.moss.land/transparency)
* 선례: [2025-08-11 Ethereum Mainnet Migration DAO Vote: Conclusion & Results](https://agora.moss.land/forum/68881a427d3ee1bb1f129b54)

---

### English Summary

**MOC Activation Season 1 — Self-Custody Participation Transition (90-Day Pilot): DAO Vote Results & Season Adoption**

The proposal ["MOC Activation Season 1"](https://agora.moss.land/proposals/6a4decb73697e1a9d307e327) was **approved with 100% For** in a gasless EIP-712 signature vote on Agora (2026-07-08 → 2026-08-07 KST, Ethereum mainnet snapshot block **25,486,030**).

* **Results:** For 108,988.96676301 MOC (2 voters; one is the proposer's wallet) / Against 0 / Abstain 0.
* **Effect:** The four principles are ratified (compensation limited to withdrawal-fee reimbursement; participation metrics displayed; binding votes from self-custody wallets only; metrics published on Passport Transparency), and Season 1 is adopted as an official 90-day pilot: **2026-08-07 → 2026-11-05**.
* **Context:** Participation equals 0.0218% of total supply and 34.60% of Passport-verified holder balances — deliberately recorded as the season's baseline. As the proposal itself states, this vote does not claim a completed mandate of all MOC holders; participation is expected to grow proposal by proposal.
* **Reporting:** Day-30 (~2026-09-06), Day-60 (~2026-10-06), and final reports will each be published as one disclosure + one Agora forum reply, in this repository.
* **Evidence:** The vote-result JSON, the full signed-vote export, a Passport Transparency snapshot, and their SHA-256 hashes are committed [alongside this disclosure](./2026-08-14_moc-activation-season1-vote-evidence/); the GitHub commit timestamp attests the collection time.

**모스랜드**
**Mossland**
