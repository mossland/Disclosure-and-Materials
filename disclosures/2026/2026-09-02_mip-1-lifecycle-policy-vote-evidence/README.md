# 증빙 자료 — MIP-1 공개 서비스·저장소 생명주기 정책 DAO 투표 (2026-09-02 공시)

본 폴더는 [2026-09-02 MIP-1 DAO 투표 결과 및 정책 채택 공시](../2026-09-02_mip-1-lifecycle-policy-vote-results.md)의 증빙입니다.
원본 증빙은 최초 공시와 **같은 커밋**에 포함되었습니다. 수집 시각은 `fetch-metadata.json`에 남긴 수집자의 기록입니다. SHA-256은 보존 파일이 기록된 해시와 일치하는지 확인하는 데 사용합니다. 원본 증빙을 포함한 GitHub의 최초 병합 기록은 해당 내용이 그 병합 시점까지 존재했음을 뒷받침하지만, 해시나 커밋·병합 기록만으로 정확한 API 수집 시각을 독립적으로 증명할 수는 없습니다.

The original evidence was committed alongside the initial disclosure. Collection times are recorded by the collector in `fetch-metadata.json`. SHA-256 checks whether the preserved files match the recorded hashes. GitHub's original merge record containing the evidence supports that the contents existed by that merge time; neither hashes nor commit or merge records independently establish the exact API collection time.

> **설명 보완:** 종전의 “수집 시점의 무결성을 뒷받침”한다는 표현을 파일 무결성 확인과 수집 시각 입증으로 구분했습니다. 원본 JSON과 해시는 유지합니다. 적용 시점은 [이 문서의 변경 이력](https://github.com/mossland/Disclosure-and-Materials/commits/main/disclosures/2026/2026-09-02_mip-1-lifecycle-policy-vote-evidence/README.md)에서 확인할 수 있습니다.
>
> **Clarification:** The former wording about supporting the integrity of collection time is clarified to distinguish file integrity from proof of collection time. Raw JSON and hashes are retained. See the [document history](https://github.com/mossland/Disclosure-and-Materials/commits/main/disclosures/2026/2026-09-02_mip-1-lifecycle-policy-vote-evidence/README.md) for when this clarification is applied.

| 파일 | 내용 | 출처 |
| --- | --- | --- |
| `proposal.json` | 안건 공식 레코드 (contentHash, snapshot block, 투표 규칙 포함) | `https://agora.moss.land/api/governance/proposals/6a85129f8be190cf5d2ebcc1` |
| `votes.json` | 전체 투표 export — 지갑 주소, 선택, voting power, **EIP-712 서명** 포함 | `https://agora.moss.land/api/proposal-votes/6a85129f8be190cf5d2ebcc1` |
| `transparency.json` | 공시 시점 Passport Transparency 스냅샷 (활성화·위임·보유 지표) | `https://passport.moss.land/api/transparency` |
| `ecosystem-registry.json` | 부속서 A 상태 필드가 반영된 links.moss.land registry (v1.1.0) — MIP-1이 정한 외부 확인 가능 증거 | `https://links.moss.land/ecosystem-registry.json` |
| `fetch-metadata.json` | 수집 시각(UTC)과 원본 URL | — |
| `SHA256SUMS.txt` | 위 파일들의 SHA-256 해시 | — |

## 재검증 방법

```bash
# 1) 해시 검증 — 이 폴더에서
shasum -a 256 -c SHA256SUMS.txt

# 2) 원본 대조 — API는 살아 있는 공개 엔드포인트다
curl -s https://agora.moss.land/api/governance/proposals/6a85129f8be190cf5d2ebcc1
curl -s https://agora.moss.land/api/proposal-votes/6a85129f8be190cf5d2ebcc1
curl -s https://links.moss.land/ecosystem-registry.json
```

주의: 살아 있는 API 응답에는 조회수 등 시간에 따라 변하는 필드가 있어 바이트 단위로 같지 않을 수 있습니다.
검증 대상은 **투표 데이터의 실질 내용**(지갑, 선택, voting power, 서명, snapshot block)과 **registry의 `lifecycle` 값**입니다.
각 투표의 EIP-712 서명은 서명자 지갑 주소로 온체인 데이터 없이도 독립 검증이 가능합니다.
registry의 이후 판(version)은 월간 검토로 바뀔 수 있으며, 여기 보존된 사본은 가결 당일(2026-09-02)의 v1.1.0입니다.
