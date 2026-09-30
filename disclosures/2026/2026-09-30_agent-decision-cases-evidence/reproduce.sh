#!/bin/sh
# 관찰 가능한 에이전트 결정 사례 — 재현 (공개 API 읽기 전용)
cd "$(dirname "$0")" && python3 reproduce.py --out "./재현_$(date -u +%Y%m%dT%H%M%SZ)"
