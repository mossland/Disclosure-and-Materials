# 증빙 자료 — MIP-1 공개 서비스·저장소 생명주기 정책 DAO 투표 (2026-09-02 공시)

본 폴더는 [2026-09-02 MIP-1 DAO 투표 결과 및 정책 채택 공시](../2026-09-02_mip-1-lifecycle-policy-vote-results.md)의 증빙입니다.
공시 문서와 **같은 커밋**에 포함되어, GitHub 커밋 타임스탬프가 수집 시점의 무결성을 뒷받침합니다.

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
