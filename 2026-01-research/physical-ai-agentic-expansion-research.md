# Mossland Research Report: Physical AI & Agentic Expansion

**January 25, 2026 | Research Preview**

**Author:** Mossland Lab (lab@moss.land)

---

> **⚠️ IMPORTANT NOTICE: EXPERIMENTAL RESEARCH & DISCLAIMER**
>
> The contents of this report and the software described herein are strictly for **experimental research purposes** conducted by Mossland Lab.
>
> 1.  **Research Purpose Only:** **This document is a technical whitepaper for research purposes only and does not constitute financial, investment, or legal advice.**
> 2.  **No Guarantee of Implementation:** **There is no guarantee that the features, systems, or roadmaps described herein will be fully implemented or released in a production environment.**
> 3.  **Testnet Environment:** All systems described (Algora, Agentic Orchestrator, BRIDGE) operate in a **Testnet environment**. They do NOT interact with the main Mossland Protocol or real assets.
> 4.  **No Governance Impact:** The activities and decisions made by these AI agents have **zero influence** on actual Mossland governance.
> 5.  **Data Volatility:** System logic is subject to change without notice. All data generated during this research phase is ephemeral and **may be reset or lost at any time**.

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Introduction: The Physical AI Thesis](#introduction-the-physical-ai-thesis)
3. [Project Overview](#project-overview)
4. [Algora: 24/7 Agentic Governance Platform](#algora-247-agentic-governance-platform)
5. [Agentic Orchestrator: Multi-Agent Service Discovery](#agentic-orchestrator-multi-agent-service-discovery)
6. [BRIDGE: Physical AI Governance OS](#bridge-physical-ai-governance-os)
7. [Technical Architecture Comparison](#technical-architecture-comparison)
8. [Implementation Details](#implementation-details)
9. [Research Findings & Lessons Learned](#research-findings--lessons-learned)
10. [Future Directions](#future-directions)
11. [Appendix](#appendix)

---

## Executive Summary

This document presents Mossland's January 2026 research initiatives focused on **Physical AI** and **Agentic Expansion**. Three experimental projects explore the intersection of autonomous AI agents, decentralized governance, and real-world signal processing:

| Project | Purpose | Status | Stack |
|---------|---------|--------|-------|
| **Algora** | 24/7 Live Agentic Governance | Experimental (PoC) | TypeScript, Ollama, Claude/GPT |
| **Agentic Orchestrator** | Multi-Agent Micro Web3 Service Discovery | Experimental | Python, Multi-LLM Debate |
| **BRIDGE** | Physical AI Governance OS | Research Prototype | TypeScript, Ethereum, viem |

**Security & Audit Protocol:**
Currently, these systems are in the **Prototype Stage**. To ensure the safety of the ecosystem, **a comprehensive professional security audit will be conducted prior to any mainnet deployment or the integration of real assets.** Until such audits are completed and verified, no real value transfer will be enabled.

**Key Research Questions:**
1. Can AI agent swarms provide continuous governance monitoring without human fatigue?
2. How do multi-agent debate systems improve decision quality over single-agent approaches?
3. What mechanisms ensure safe AI autonomy while preserving human oversight?

**Core Innovation: The LOCK/UNLOCK Paradigm**

All three projects implement variations of a critical safety mechanism: AI agents can propose, analyze, and debate—but high-risk actions remain **LOCKED** until explicit human approval.

```
┌─────────────────────────────────────────────────────────────┐
│                    MOSSLAND PHYSICAL AI STACK               │
├─────────────────────────────────────────────────────────────┤
│  L4: Proof of Outcome    │ KPI Verification, Trust Scores  │
├─────────────────────────────────────────────────────────────┤
│  L3: Human Governance    │ MOC Voting, Delegation, UNLOCK  │
├─────────────────────────────────────────────────────────────┤
│  L2: Agentic Consensus   │ Multi-Agent Debate, Deliberation│
├─────────────────────────────────────────────────────────────┤
│  L1: Inference Mining    │ Anomaly Detection, Trend Analysis│
├─────────────────────────────────────────────────────────────┤
│  L0: Reality Oracle      │ Signal Collection, Attestation  │
└─────────────────────────────────────────────────────────────┘
```

---

## Introduction: The Physical AI Thesis

### The Problem: Governance Fatigue in DAOs

Decentralized Autonomous Organizations face a fundamental tension:

```
Human Attention is Scarce  ←→  Governance Decisions are Continuous
```

Traditional DAO governance suffers from:
- **Low participation rates** (often <5% of token holders vote)
- **Voter fatigue** (too many proposals, too little context)
- **Information asymmetry** (insiders vs. casual holders)
- **Slow response times** (days/weeks for critical decisions)

### The Solution: Physical AI Governance

**Physical AI** extends artificial intelligence beyond digital-only domains into systems that:

1. **Sense Reality**: Collect signals from blockchain, social, financial, and operational sources
2. **Reason Collectively**: Multiple specialized agents debate and analyze
3. **Propose Actions**: Generate structured governance proposals
4. **Defer to Humans**: High-risk decisions require explicit human approval
5. **Verify Outcomes**: Track KPIs and build trust through measurable results

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   REALITY    │────▶│   AI LAYER   │────▶│    HUMAN     │
│   SIGNALS    │     │   (Always On)│     │   APPROVAL   │
└──────────────┘     └──────────────┘     └──────────────┘
       │                    │                    │
       ▼                    ▼                    ▼
  On-chain data       Agent Debate         MOC Token Vote
  Social feeds        Risk Analysis        Delegation
  Market data         Recommendations      Override
  GitHub activity     Draft Proposals      Execution
```

### Design Principles

1. **AI Proposes, Human Disposes**: Agents can suggest but never unilaterally execute high-risk actions
2. **Transparency by Default**: All agent reasoning is logged and auditable
3. **Graceful Degradation**: System continues operating even when external LLM APIs are unavailable
4. **Economic Alignment**: Agent recommendations consider MOC token holder interests

---

## Project Overview

### Project Relationships

```
                    ┌─────────────────────────┐
                    │     MOSSLAND VISION     │
                    │   Physical AI + Web3    │
                    └───────────┬─────────────┘
                                │
        ┌───────────────────────┼───────────────────────┐
        │                       │                       │
        ▼                       ▼                       ▼
┌───────────────┐     ┌─────────────────┐     ┌─────────────────┐
│    ALGORA     │     │    AGENTIC      │     │     BRIDGE      │
│  Governance   │     │  ORCHESTRATOR   │     │   Reality Ops   │
│   Platform    │     │  Service Disco  │     │   Governance    │
└───────┬───────┘     └────────┬────────┘     └────────┬────────┘
        │                      │                       │
        │  38 Agents           │  34 Agents            │  4 Agents
        │  5 Workflows         │  3-Phase Debate       │  5-Layer Stack
        │  12-State Machine    │  10 Signal Sources    │  Multi-Round Debate
        └──────────────────────┴───────────────────────┘
                               │
                    ┌──────────┴──────────┐
                    │   SHARED PATTERNS   │
                    ├─────────────────────┤
                    │ • Signal Collection │
                    │ • Agent Deliberation│
                    │ • Human-in-the-Loop │
                    │ • Outcome Tracking  │
                    └─────────────────────┘
```

### Technology Stack Comparison

| Component | Algora | Agentic Orchestrator | BRIDGE |
|-----------|--------|---------------------|--------|
| **Language** | TypeScript | Python | TypeScript |
| **Runtime** | Node.js | Python 3.11+ | Node.js |
| **Framework** | Express + Next.js | FastAPI + Next.js | Express + Next.js |
| **Database** | SQLite (WAL) | SQLite | SQLite |
| **Local LLM** | Ollama (Llama, Qwen, Phi) | Ollama (Qwen, Llama, Phi, GLM) | Ollama |
| **Cloud LLM** | Claude, GPT, Gemini | Claude, GPT, Gemini | Claude, GPT |
| **Blockchain** | MOC Contract Read | GitHub Integration | Ethereum (viem) |
| **Monorepo** | pnpm + Turborepo | Poetry | pnpm + Turborepo |
| **Process Mgmt** | pm2 | pm2 | pm2 |

---

## Algora: 24/7 Agentic Governance Platform

### Overview

**Algora** is a continuously operating governance platform where AI agents monitor signals, detect issues, and conduct deliberations—while humans retain final authority over significant decisions.

- **Live Demo**: https://algora.moss.land/
- **Source Code**: https://github.com/MosslandOpenDevs/Algora
- **Version**: v0.12.10 (v2.0 Architecture)

### System Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         ALGORA ARCHITECTURE                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │ L4: PROOF OF OUTCOME                                            │    │
│  │ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐                │    │
│  │ │ Execution   │ │    KPI      │ │   Trust     │                │    │
│  │ │ Tracking    │ │ Measurement │ │   Scoring   │                │    │
│  │ └─────────────┘ └─────────────┘ └─────────────┘                │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                    │                                     │
│  ┌─────────────────────────────────▼───────────────────────────────┐    │
│  │ L3: HUMAN GOVERNANCE                                            │    │
│  │ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐                │    │
│  │ │  MossCoin   │ │  OpenSource │ │  Director 3 │                │    │
│  │ │   House     │ │    House    │ │  (Override) │                │    │
│  │ └─────────────┘ └─────────────┘ └─────────────┘                │    │
│  │         ▲               ▲               ▲                       │    │
│  │         └───────────────┴───────────────┘                       │    │
│  │                    DUAL-HOUSE VOTING                            │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                    │                                     │
│  ┌─────────────────────────────────▼───────────────────────────────┐    │
│  │ L2: AGENTIC CONSENSUS                                           │    │
│  │ ┌─────────────────────────────────────────────────────────────┐ │    │
│  │ │                    38 AGENTS (11 CLUSTERS)                   │ │    │
│  │ │  Visionaries(5) Builders(5) Investors(4) Guardians(4)       │ │    │
│  │ │  Operatives(5) Moderators(3) Advisors(4) Orchestrators(2)   │ │    │
│  │ │  Archivists(2) Red Team(3) Scouts(1)                        │ │    │
│  │ └─────────────────────────────────────────────────────────────┘ │    │
│  │ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐                │    │
│  │ │   Agora     │ │  Decision   │ │  Document   │                │    │
│  │ │  Sessions   │ │  Packets    │ │  Registry   │                │    │
│  │ └─────────────┘ └─────────────┘ └─────────────┘                │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                    │                                     │
│  ┌─────────────────────────────────▼───────────────────────────────┐    │
│  │ L1: INFERENCE MINING                                            │    │
│  │ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐                │    │
│  │ │  Anomaly    │ │  Threshold  │ │   Trend     │                │    │
│  │ │ Detection   │ │  Alerts     │ │  Analysis   │                │    │
│  │ └─────────────┘ └─────────────┘ └─────────────┘                │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                    │                                     │
│  ┌─────────────────────────────────▼───────────────────────────────┐    │
│  │ L0: REALITY ORACLE                                              │    │
│  │ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐             │    │
│  │ │  RSS  │ │GitHub │ │On-Chain│ │Social │ │Market │             │    │
│  │ │ Feeds │ │Events │ │ Data  │ │ Feeds │ │ Data  │             │    │
│  │ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘             │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### Agent System Design

Algora employs **38 AI agents** organized into **11 specialized clusters**:

```typescript
// Agent Cluster Distribution
const AGENT_CLUSTERS = {
  Visionaries:   5,  // Future-oriented strategic thinkers
  Builders:      5,  // Engineering and technical implementation
  Investors:     4,  // Market analysis and tokenomics
  Guardians:     4,  // Risk management and security
  Operatives:    5,  // Data collection and signal processing
  Moderators:    3,  // Discussion facilitation
  Advisors:      4,  // Domain expertise (legal, finance, etc.)
  Orchestrators: 2,  // Workflow coordination (Nova Prime, Atlas)
  Archivists:    2,  // Document management (Archive Alpha, Trace Master)
  RedTeam:       3,  // Devil's advocates (Contrarian Carl, Breach Tester)
  Scouts:        1   // Opportunity detection (Horizon Seeker)
};
```

**Agent State Machine:**

```
         ┌─────────┐
         │  IDLE   │◀────────────────┐
         └────┬────┘                 │
              │ issue detected       │ session ends
              ▼                      │
         ┌─────────┐                 │
    ┌───▶│ ACTIVE  │────────────────►│
    │    └────┬────┘                 │
    │         │ speaking turn        │
    │         ▼                      │
    │    ┌─────────┐                 │
    │    │SPEAKING │─────────────────┤
    │    └────┬────┘                 │
    │         │ waiting for others   │
    │         ▼                      │
    │    ┌─────────┐                 │
    └────│LISTENING│                 │
         └─────────┘                 │
              │ consensus reached    │
              ▼                      │
         ┌─────────┐                 │
         │  DONE   │─────────────────┘
         └─────────┘
```

### Dynamic Agent Summoning

Agents are summoned based on issue category relevance:

```typescript
// Category to Agent Cluster Mapping
const SUMMONING_RULES: Record<IssueCategory, AgentCluster[]> = {
  security:    ['Guardians', 'RedTeam', 'Builders'],
  market:      ['Investors', 'Advisors', 'Scouts'],
  governance:  ['Visionaries', 'Orchestrators', 'Moderators'],
  defi:        ['Investors', 'Builders', 'Guardians'],
  protocol:    ['Builders', 'Guardians', 'Archivists'],
  mossland:    ['Visionaries', 'Scouts', 'Advisors']
};

// Summoning with cooldown protection
async function summonAgentsForIssue(issue: Issue): Promise<Agent[]> {
  const relevantClusters = SUMMONING_RULES[issue.category];
  const cooldown = issue.priority === 'critical' ? 30 * 60 * 1000 : 60 * 60 * 1000;

  return agents.filter(agent =>
    relevantClusters.includes(agent.cluster) &&
    Date.now() - agent.lastSummonedAt > cooldown
  );
}
```

### The LOCK/UNLOCK Mechanism

Algora's **Safe Autonomy** system prevents AI agents from executing high-risk actions without human approval:

```typescript
// Risk Classification
type RiskLevel = 'LOW' | 'MID' | 'HIGH';

const ACTION_RISK_MAP: Record<ActionType, RiskLevel> = {
  // HIGH-Risk: Always LOCKED
  FUND_TRANSFER:          'HIGH',
  CONTRACT_DEPLOY:        'HIGH',
  PARTNERSHIP_COMMIT:     'HIGH',
  EXTERNAL_COMMUNICATION: 'HIGH',

  // MID-Risk: LOCKED with 48h auto-approve
  PROPOSAL_CREATE:        'MID',
  WORKING_GROUP_CREATE:   'MID',
  GRANT_PROPOSAL:         'MID',
  MILESTONE_REPORT:       'MID',

  // LOW-Risk: LOCKED with 24h auto-approve
  DOCUMENT_PUBLISH:       'LOW',
  RESEARCH_DIGEST:        'LOW',
  AGENT_CHATTER:          'LOW',
  SIGNAL_PROCESS:         'LOW'
};
```

**LOCK Flow Diagram:**

```
┌─────────────────┐
│  Action Created │
└────────┬────────┘
         │
         ▼
┌─────────────────┐     ┌─────────────────┐
│ Risk Assessment │────▶│  Risk = LOW?    │
└─────────────────┘     └────────┬────────┘
                                 │
                    ┌────────────┼────────────┐
                    │            │            │
                    ▼            ▼            ▼
              ┌─────────┐  ┌─────────┐  ┌─────────┐
              │   LOW   │  │   MID   │  │  HIGH   │
              └────┬────┘  └────┬────┘  └────┬────┘
                   │            │            │
                   ▼            ▼            ▼
              ┌─────────┐  ┌─────────┐  ┌─────────┐
              │24h Auto │  │48h Auto │  │Required │
              │ Approve │  │ Approve │  │ Review  │
              └────┬────┘  └────┬────┘  └────┬────┘
                   │            │            │
                   └────────────┴────────────┘
                                │
                                ▼
                   ┌─────────────────────────┐
                   │   Approval Received?    │
                   └────────────┬────────────┘
                                │
                    ┌───────────┴───────────┐
                    │                       │
                    ▼                       ▼
              ┌─────────┐            ┌─────────┐
              │UNLOCKED │            │REJECTED │
              │ Execute │            │  Log    │
              └─────────┘            └─────────┘
```

### Dual-House Governance

Algora implements a bicameral voting system:

| House | Members | Voting Weight | Focus Areas |
|-------|---------|---------------|-------------|
| **MossCoin House** | MOC Token Holders | Token-weighted | Treasury, Tokenomics, Partnerships |
| **OpenSource House** | Active Contributors | Contribution-weighted | Technical Decisions, Roadmap |

**Reconciliation Process:**

When the two houses disagree, the system initiates reconciliation:

```typescript
interface ReconciliationResult {
  outcome: 'override_moc' | 'override_oss' | 'revote' | 'veto' | 'approve_with_conditions';
  rationale: string;
  conditions?: string[];
  decidedBy: 'orchestrator' | 'director3';
}

async function reconcile(
  mocVote: VoteResult,
  ossVote: VoteResult,
  proposal: Proposal
): Promise<ReconciliationResult> {
  // Orchestrator analyzes disagreement
  const analysis = await orchestrator.analyzeDisagreement(mocVote, ossVote, proposal);

  // If high-risk, escalate to Director 3
  if (proposal.riskLevel === 'HIGH') {
    return await director3.decide(analysis);
  }

  // Otherwise, orchestrator recommends resolution
  return orchestrator.recommend(analysis);
}
```

### LLM Tiering System

Algora uses a 3-tier LLM hierarchy for cost optimization:

```
┌─────────────────────────────────────────────────────────┐
│ TIER 2: External APIs (Budget-Controlled)              │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐       │
│ │   Claude    │ │   GPT-4o    │ │   Gemini    │       │
│ │ 3.5 Sonnet  │ │             │ │  2.0 Flash  │       │
│ └─────────────┘ └─────────────┘ └─────────────┘       │
│ Daily Budget: $10/provider | Scheduled: 6,12,18,23h   │
├─────────────────────────────────────────────────────────┤
│ TIER 1: Local LLM (Always Available)                   │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐       │
│ │  Llama 3.2  │ │  Qwen 2.5   │ │    Phi-4    │       │
│ │     8B      │ │    32B      │ │     14B     │       │
│ └─────────────┘ └─────────────┘ └─────────────┘       │
│ Hourly Limit: 1000 calls | Fallback when Tier 2 exhausted │
├─────────────────────────────────────────────────────────┤
│ TIER 0: No LLM Required                                │
│ Signal Collection | RSS Parsing | Data Aggregation     │
└─────────────────────────────────────────────────────────┘
```

**Model Router Logic:**

```typescript
interface ModelRoutingDecision {
  tier: 0 | 1 | 2;
  model: string;
  fallbackChain: string[];
  estimatedCost: number;
}

function routeTask(task: Task, budget: BudgetStatus): ModelRoutingDecision {
  // Critical tasks get Tier 2 if budget allows
  if (task.difficulty === 'critical' && budget.tier2Available) {
    return {
      tier: 2,
      model: 'claude-3-5-sonnet',
      fallbackChain: ['gpt-4o', 'llama3.2:8b'],
      estimatedCost: 0.015
    };
  }

  // Complex tasks prefer Tier 1 large models
  if (task.difficulty === 'complex') {
    return {
      tier: 1,
      model: 'qwen2.5:32b',
      fallbackChain: ['phi4:14b'],
      estimatedCost: 0
    };
  }

  // Simple tasks use lightweight models
  return {
    tier: 1,
    model: 'phi4:14b',
    fallbackChain: [],
    estimatedCost: 0
  };
}
```

### Document Registry

Algora maintains **15 official document types** with full provenance tracking:

```typescript
// Document Type Taxonomy
const DOCUMENT_TYPES = {
  // Decision Documents
  DP: 'Decision Packet',        // Output of agentic consensus
  GP: 'Governance Proposal',    // Formal voting proposal
  RM: 'Resolution Memo',        // Voting outcome record
  RC: 'Reconciliation Memo',    // Dual-house conflict resolution

  // Working Group Documents
  WGC: 'Working Group Charter', // Group formation
  WGR: 'Working Group Report',  // Progress reports

  // Ecosystem Documents
  ER: 'Ecosystem Report',       // External analysis
  PP: 'Partnership Proposal',   // Partnership opportunity
  PA: 'Partnership Agreement',  // Finalized partnership

  // Developer Documents
  DGP: 'Developer Grant Proposal',
  DG: 'Developer Grant',
  MR: 'Milestone Report',
  RR: 'Retroactive Reward',

  // Transparency Documents
  DR: 'Disclosure Report',
  AR: 'Audit Report'
};

// Document Provenance Tracking
interface DocumentProvenance {
  originSignals: Signal[];           // Source signals
  agentContributions: {
    agentId: string;
    model: string;
    tokensUsed: number;
    costUsd: number;
  }[];
  reviewHistory: {
    reviewerId: string;
    action: 'approve' | 'reject' | 'comment';
    timestamp: Date;
    signature?: string;
  }[];
  contentHash: string;               // SHA256 integrity proof
  version: SemanticVersion;
}
```

### Workflow State Machine

The Orchestrator manages issues through a 12-state workflow:

```
┌─────────┐    ┌─────────────────┐    ┌───────────────┐
│ INTAKE  │───▶│ ISSUE_ANALYSIS  │───▶│CATEGORIZATION │
└─────────┘    └─────────────────┘    └───────┬───────┘
                                              │
                                              ▼
┌───────────┐    ┌──────────────────┐    ┌────────────────────┐
│  ARCHIVE  │◀───│OUTCOME_VERIFICATION│◀──│    EXECUTION       │
└───────────┘    └──────────────────┘    └─────────┬──────────┘
                                                   │
┌────────────────┐    ┌─────────────────┐    ┌─────┴──────────┐
│WORKFLOW_DISPATCH│───▶│ SPECIALIST_WORK │───▶│DOCUMENT_PRODUCE│
└────────────────┘    └─────────────────┘    └───────┬────────┘
                                                     │
                                                     ▼
                          ┌─────────────────┐    ┌───────────────────┐
                          │APPROVAL_ROUTING │◀───│ DUAL_HOUSE_REVIEW │
                          └─────────────────┘    └───────────────────┘
```

**Five Governance Workflows:**

| Workflow | Purpose | Typical Duration |
|----------|---------|-----------------|
| **A: Academic** | Research digests, technology assessments | 1-3 days |
| **B: Free Debate** | Community deliberation, consensus building | 3-7 days |
| **C: Developer** | Grant applications, milestone tracking | 7-14 days |
| **D: Ecosystem** | Partnership opportunities, always-on detection | Continuous |
| **E: Working Groups** | Charter creation, dissolution | 7-30 days |

---

## Agentic Orchestrator: Multi-Agent Service Discovery

### Overview

**Agentic Orchestrator** is an autonomous system for discovering, planning, and implementing micro Web3 services through multi-agent debate. It continuously monitors signals from 10 sources and orchestrates a 34-agent debate across three phases.

- **Live Demo**: https://ao.moss.land/
- **Source Code**: https://github.com/MosslandOpenDevs/agentic-orchestrator
- **Version**: v0.5.1 "Bilingual"

### System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AGENTIC ORCHESTRATOR PIPELINE                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────────┐ │
│  │                        SIGNAL COLLECTION (10 SOURCES)                  │ │
│  │  ┌─────┐ ┌──────┐ ┌───────┐ ┌────────┐ ┌────────┐                    │ │
│  │  │ RSS │ │GitHub│ │OnChain│ │ Social │ │CoinGecko│                    │ │
│  │  └──┬──┘ └──┬───┘ └───┬───┘ └───┬────┘ └───┬────┘                    │ │
│  │     │       │         │         │          │                          │ │
│  │  ┌──┴──┐ ┌──┴───┐ ┌───┴──┐ ┌────┴───┐ ┌────┴────┐                    │ │
│  │  │Twitter│ │Discord│ │ Lens │ │Farcaster│ │ NewsAPI │                    │ │
│  │  └──────┘ └──────┘ └──────┘ └────────┘ └─────────┘                    │ │
│  └───────────────────────────┬────────────────────────────────────────────┘ │
│                              │                                               │
│                              ▼                                               │
│  ┌────────────────────────────────────────────────────────────────────────┐ │
│  │                      SIGNAL AGGREGATOR                                  │ │
│  │  • Deduplication (content hashing)                                     │ │
│  │  • Time Decay Scoring (0.2 - 1.0 multiplier)                          │ │
│  │  • Category Classification                                             │ │
│  │  • Database Persistence (30-day retention)                             │ │
│  └───────────────────────────┬────────────────────────────────────────────┘ │
│                              │                                               │
│                              ▼                                               │
│  ┌────────────────────────────────────────────────────────────────────────┐ │
│  │                       TREND ANALYSIS (LLM)                             │ │
│  │  • Extract emerging patterns from signals                              │ │
│  │  • Score trends by relevance & momentum                                │ │
│  │  • Generate topic suggestions for debate                               │ │
│  └───────────────────────────┬────────────────────────────────────────────┘ │
│                              │                                               │
│                              ▼                                               │
│  ┌────────────────────────────────────────────────────────────────────────┐ │
│  │                   MULTI-STAGE DEBATE (34 Agents)                       │ │
│  │  ┌──────────────────────────────────────────────────────────────────┐ │ │
│  │  │ PHASE 1: DIVERGENCE (16 agents × 3 rounds)                       │ │ │
│  │  │ Goal: Generate 20+ diverse ideas | Temperature: 0.95             │ │ │
│  │  └──────────────────────────────────────────────────────────────────┘ │ │
│  │                              │                                         │ │
│  │                              ▼                                         │ │
│  │  ┌──────────────────────────────────────────────────────────────────┐ │ │
│  │  │ PHASE 2: CONVERGENCE (8 agents × 2 rounds)                       │ │ │
│  │  │ Goal: Filter to top 5 ideas | Temperature: 0.5                   │ │ │
│  │  └──────────────────────────────────────────────────────────────────┘ │ │
│  │                              │                                         │ │
│  │                              ▼                                         │ │
│  │  ┌──────────────────────────────────────────────────────────────────┐ │ │
│  │  │ PHASE 3: PLANNING (10 agents × 2 rounds)                         │ │ │
│  │  │ Goal: Create actionable plans | Temperature: 0.7                 │ │ │
│  │  └──────────────────────────────────────────────────────────────────┘ │ │
│  └───────────────────────────┬────────────────────────────────────────────┘ │
│                              │                                               │
│                              ▼                                               │
│  ┌────────────────────────────────────────────────────────────────────────┐ │
│  │                    PROJECT GENERATION (LLM)                            │ │
│  │  • Parse plan into structured spec                                     │ │
│  │  • Generate complete code scaffold                                     │ │
│  │  • Create GitHub repository                                            │ │
│  └────────────────────────────────────────────────────────────────────────┘ │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Four-Role Debate System

The core innovation is a structured debate between four distinct roles:

```
┌─────────────────────────────────────────────────────────────────┐
│                    DEBATE ROLE ROTATION                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   Round 1    Round 2    Round 3    Round 4    Round 5           │
│  ┌───────┐  ┌───────┐  ┌───────┐  ┌───────┐  ┌───────┐         │
│  │FOUNDER│  │FOUNDER│  │FOUNDER│  │FOUNDER│  │FOUNDER│         │
│  │Claude │  │OpenAI │  │Gemini │  │Claude │  │OpenAI │         │
│  └───┬───┘  └───┬───┘  └───┬───┘  └───┬───┘  └───┬───┘         │
│      │          │          │          │          │              │
│      ▼          ▼          ▼          ▼          ▼              │
│  ┌───────┐  ┌───────┐  ┌───────┐  ┌───────┐  ┌───────┐         │
│  │  VC   │  │  VC   │  │  VC   │  │  VC   │  │  VC   │         │
│  │OpenAI │  │Gemini │  │Claude │  │Gemini │  │Claude │         │
│  └───┬───┘  └───┬───┘  └───┬───┘  └───┬───┘  └───┬───┘         │
│      │          │          │          │          │              │
│      ▼          ▼          ▼          ▼          ▼              │
│  ┌───────┐  ┌───────┐  ┌───────┐  ┌───────┐  ┌───────┐         │
│  │ACCEL  │  │ACCEL  │  │ACCEL  │  │ACCEL  │  │ACCEL  │         │
│  │Gemini │  │Claude │  │OpenAI │  │OpenAI │  │Gemini │         │
│  └───┬───┘  └───┬───┘  └───┬───┘  └───┬───┘  └───┬───┘         │
│      │          │          │          │          │              │
│      ▼          ▼          ▼          ▼          ▼              │
│  ┌───────┐  ┌───────┐  ┌───────┐  ┌───────┐  ┌───────┐         │
│  │FRIEND │  │FRIEND │  │FRIEND │  │FRIEND │  │FRIEND │         │
│  │Claude │  │OpenAI │  │Gemini │  │Claude │  │OpenAI │         │
│  └───────┘  └───────┘  └───────┘  └───────┘  └───────┘         │
│                                                                  │
│  Key: Each provider plays different roles across rounds          │
│       to ensure diverse perspectives                             │
└─────────────────────────────────────────────────────────────────┘
```

**Role Definitions:**

| Role | Persona | Evaluation Focus | Output Format |
|------|---------|-----------------|---------------|
| **Founder** | Startup founder with vision | Creates initial plan, reflects on feedback | 7-section plan document |
| **VC** | a16z/Sequoia-level investor | Market opportunity, moat, 10x potential | PASS / CONSIDER / INVEST |
| **Accelerator** | YC/Techstars partner | MVP scope, 2-week validation potential | Weekly action items |
| **Founder Friend** | Battle-tested peer | Reality check, hidden risks, encouragement | Experience-based advice |

**Founder Decision Flow:**

```python
# Founder reflects on feedback and makes adoption decisions
@dataclass
class FounderDecision:
    adopted_feedback: List[FeedbackEntry]
    rejected_feedback: List[FeedbackEntry]
    reasoning: str
    plan_version: int
    terminate: bool  # Can write [TERMINATE] to end debate

# Example decision record
decision = FounderDecision(
    adopted_feedback=[
        FeedbackEntry(role="VC", content="Focus on B2B first", reason="Market validation"),
        FeedbackEntry(role="Accelerator", content="Cut feature X", reason="Scope reduction")
    ],
    rejected_feedback=[
        FeedbackEntry(role="Friend", content="Pivot to consumer", reason="Core thesis unchanged")
    ],
    reasoning="B2B focus aligns with our technical strengths...",
    plan_version=3,
    terminate=False
)
```

### Four-Axis Personality System

Each of the 34 agents has a unique personality defined by four independent axes:

```python
from enum import Enum

class ThinkingStyle(Enum):
    OPTIMISTIC = "optimistic"   # Sees possibilities first
    CAUTIOUS = "cautious"       # Sees risks and problems first

class DecisionStyle(Enum):
    INTUITIVE = "intuitive"     # Quick, pattern-based decisions
    ANALYTICAL = "analytical"   # Data-driven, systematic analysis

class CommunicationStyle(Enum):
    CHALLENGER = "challenger"   # Direct criticism, tough questions
    SUPPORTER = "supporter"     # Encouraging, constructive feedback

class ActionStyle(Enum):
    INNOVATIVE = "innovative"   # Novel, experimental approaches
    PRAGMATIC = "pragmatic"     # Proven, practical solutions

@dataclass
class AgentPersonality:
    thinking: ThinkingStyle
    decision: DecisionStyle
    communication: CommunicationStyle
    action: ActionStyle

    def generate_behavior_modifiers(self) -> Dict[str, str]:
        """Generate 7 behavior modifiers based on personality axes."""
        return {
            "initial_reaction": self._derive_initial_reaction(),
            "problem_approach": self._derive_problem_approach(),
            "decision_speed": self._derive_decision_speed(),
            "evidence_need": self._derive_evidence_need(),
            "feedback_style": self._derive_feedback_style(),
            "disagreement_handling": self._derive_disagreement_handling(),
            "solution_preference": self._derive_solution_preference()
        }
```

**Agent Catalog Sample (34 Total):**

| Agent | Role | Personality | Model | Expertise |
|-------|------|-------------|-------|-----------|
| Yuki Tanaka | Sr. Frontend Dev | OPT/INT/SUP/INN | phi4:14b | React, Next.js, Web3 UI |
| Sarah Johnson | Staff Frontend Eng | CAU/ANA/CHA/PRA | qwen2.5:14b | Performance, A11y, Testing |
| Kenji Yamamoto | Principal Backend | CAU/ANA/CHA/PRA | qwen2.5:32b | System Design, Scale |
| Alex Chen | Blockchain Lead | OPT/ANA/SUP/INN | llama3.3:70b | Solidity, ZK Proofs |
| Maria Santos | Security Expert | CAU/ANA/CHA/PRA | claude | Audits, Threat Modeling |

### Signal Collection System

Ten adapters collect signals from diverse sources:

```python
# Signal Data Structure
@dataclass
class SignalData:
    source: str              # Adapter name
    category: str            # ai, crypto, finance, security, dev
    title: str
    summary: Optional[str]
    url: Optional[str]
    raw_data: Optional[Dict]
    collected_at: datetime
    metadata: Dict[str, Any]

    @property
    def id(self) -> str:
        """SHA256 hash of source:title:url for deduplication."""
        content = f"{self.source}:{self.title}:{self.url}"
        return hashlib.sha256(content.encode()).hexdigest()

# Adapter Registry
SIGNAL_ADAPTERS = {
    "rss": RSSAdapter(feeds=[
        # 28+ feeds across 5 categories
        "https://openai.com/blog/rss.xml",
        "https://news.ycombinator.com/rss",
        "https://www.coindesk.com/arc/outboundfeeds/rss/",
        # ... more feeds
    ]),
    "github": GitHubEventsAdapter(
        repos=["mossland/*", "ethereum/*"],
        track_trending=True
    ),
    "onchain": OnChainAdapter(
        contracts=["0x8bbfe65e31b348cd823c62e02ad8c19a84dd0dab"],  # MOC
        whale_threshold=500_000
    ),
    "twitter": TwitterAdapter(
        keywords=["mossland", "mosscoin", "MOC"],
        nitter_pool=["nitter.net", "nitter.it"]  # Decentralized fetching
    ),
    "discord": DiscordAdapter(guild_ids=[...]),
    "lens": LensAdapter(profiles=["mossland.lens"]),
    "farcaster": FarcasterAdapter(channels=["crypto", "defi"]),
    "coingecko": CoingeckoAdapter(track_trending=True),
    "social": SocialMediaAdapter(subreddits=["cryptocurrency", "web3"]),
    "news": NewsAPIAdapter(keywords=["web3", "blockchain", "AI"])
}
```

**Time Decay Scoring:**

```python
def calculate_time_decay(signal_age_hours: float) -> float:
    """
    Apply exponential decay based on signal age.
    Newer signals are weighted more heavily.
    """
    DECAY_SCHEDULE = [
        (1,   1.0),   # 0-1 hours: 100% weight
        (6,   0.9),   # 1-6 hours: 90% weight
        (12,  0.8),   # 6-12 hours: 80% weight
        (24,  0.6),   # 12-24 hours: 60% weight
        (48,  0.4),   # 24-48 hours: 40% weight
        (float('inf'), 0.2)  # 48+ hours: 20% weight
    ]

    for threshold, weight in DECAY_SCHEDULE:
        if signal_age_hours < threshold:
            return weight
    return 0.2
```

### Human-in-the-Loop Workflow

The system uses GitHub labels to enable human control:

```
┌─────────────────────────────────────────────────────────────────┐
│                  HUMAN-IN-THE-LOOP WORKFLOW                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. IDEA GENERATION (Automated)                                  │
│     ┌─────────────────────────────────────────────────────────┐ │
│     │ Orchestrator generates ideas → GitHub Issues created     │ │
│     │ Labels: [type:idea] [status:backlog] [generated]         │ │
│     └─────────────────────────────────────────────────────────┘ │
│                              │                                   │
│                              ▼                                   │
│  2. HUMAN PROMOTION (Manual)                                     │
│     ┌─────────────────────────────────────────────────────────┐ │
│     │ Human reviews idea and adds label:                       │ │
│     │ [promote:to-plan] → Triggers debate session              │ │
│     └─────────────────────────────────────────────────────────┘ │
│                              │                                   │
│                              ▼                                   │
│  3. MULTI-AGENT DEBATE (Automated)                               │
│     ┌─────────────────────────────────────────────────────────┐ │
│     │ 34 agents debate across 3 phases                         │ │
│     │ Debate record posted as GitHub comment                   │ │
│     │ Labels: [status:in-debate]                               │ │
│     └─────────────────────────────────────────────────────────┘ │
│                              │                                   │
│                              ▼                                   │
│  4. PLAN CREATION (Automated)                                    │
│     ┌─────────────────────────────────────────────────────────┐ │
│     │ Debate output → Structured plan document                 │ │
│     │ Labels: [type:plan] [status:draft]                       │ │
│     └─────────────────────────────────────────────────────────┘ │
│                              │                                   │
│                              ▼                                   │
│  5. PLAN APPROVAL (Manual)                                       │
│     ┌─────────────────────────────────────────────────────────┐ │
│     │ Human reviews plan and adds label:                       │ │
│     │ [status:approved] → Triggers project generation          │ │
│     └─────────────────────────────────────────────────────────┘ │
│                              │                                   │
│                              ▼                                   │
│  6. PROJECT GENERATION (Automated)                               │
│     ┌─────────────────────────────────────────────────────────┐ │
│     │ LLM generates complete code scaffold                     │ │
│     │ Creates new repository with all files                    │ │
│     │ Labels: [status:generated]                               │ │
│     └─────────────────────────────────────────────────────────┘ │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Project Generation Pipeline

```python
@dataclass
class ParsedPlan:
    """Structured extraction from plan markdown."""
    title: str
    summary: str
    tech_stack: TechStack
    features: List[str]
    api_endpoints: List[APIEndpoint]
    tasks: List[ProjectTask]
    entities: List[DataEntity]
    external_services: List[ExternalService]
    ui_components: List[UIComponent]
    smart_contracts: List[SmartContractSpec]

@dataclass
class TechStack:
    frontend: str   # e.g., "Next.js 14"
    backend: str    # e.g., "FastAPI"
    database: str   # e.g., "PostgreSQL"
    blockchain: str # e.g., "Ethereum + Solidity"

# Task-based model selection for code generation
MODEL_SELECTION = {
    "parsing":         "glm-4.7-flash",   # 18GB, fast structured extraction
    "code_generation": "qwen2.5:32b",     # 19GB, balanced quality/speed
    "architecture":    "llama3.3:70b",    # 42GB, complex design decisions
    "simple":          "phi4:14b",        # 9.1GB, lightweight fallback
    "readme":          "qwen2.5:32b"
}
```

**Generated Output Structure:**

```
generated-project/
├── README.md                    # Project documentation
├── docker-compose.yml           # Container orchestration
├── .env.example                 # Environment template
│
├── backend/
│   ├── main.py                  # FastAPI application
│   ├── models/                  # SQLAlchemy models
│   ├── routes/                  # API endpoints
│   ├── services/                # Business logic
│   └── tests/                   # pytest tests
│
├── frontend/
│   ├── package.json
│   ├── src/
│   │   ├── app/                 # Next.js pages
│   │   ├── components/          # React components
│   │   └── lib/                 # Utilities
│   └── public/
│
└── contracts/
    ├── src/                     # Solidity contracts
    ├── test/                    # Foundry tests
    └── script/                  # Deployment scripts
```

### Budget-Aware LLM Routing

```python
@dataclass
class BudgetConfig:
    daily_limit_usd: float = 5.0
    monthly_limit_usd: float = 150.0
    warning_threshold: float = 0.7   # 70% usage
    critical_threshold: float = 0.9  # 90% usage

class HybridLLMRouter:
    """Routes tasks to optimal LLM based on budget and requirements."""

    def route(self, task: Task) -> ModelSelection:
        budget_status = self.get_budget_status()

        # Critical budget: Force local only
        if budget_status.is_critical:
            return self.select_local_model(task)

        # High quality requirement with budget available
        if task.quality == "critical" and budget_status.tier2_available:
            return ModelSelection(
                provider="claude",
                model="opus",
                fallback=["sonnet", "qwen2.5:32b"]
            )

        # Default: Use local models
        return self.select_local_model(task)

    def select_local_model(self, task: Task) -> ModelSelection:
        """Select optimal local model based on task complexity."""
        if task.type == "parsing":
            return ModelSelection(provider="ollama", model="glm-4.7-flash")
        elif task.type == "architecture":
            return ModelSelection(provider="ollama", model="llama3.3:70b")
        else:
            return ModelSelection(provider="ollama", model="qwen2.5:32b")
```

### Scheduler Configuration

```javascript
// ecosystem.config.js (PM2)
module.exports = {
  apps: [
    {
      name: 'moss-ao-signals',
      script: 'python -m agentic_orchestrator.scheduler.tasks signal_collect',
      cron_restart: '*/30 * * * *',  // Every 30 minutes
      autorestart: false
    },
    {
      name: 'moss-ao-trends',
      script: 'python -m agentic_orchestrator.scheduler.tasks analyze_trends',
      cron_restart: '0 */2 * * *',   // Every 2 hours
      autorestart: false
    },
    {
      name: 'moss-ao-debate',
      script: 'python -m agentic_orchestrator.scheduler.tasks run_debate',
      cron_restart: '0 */6 * * *',   // Every 6 hours
      autorestart: false
    },
    {
      name: 'moss-ao-backlog',
      script: 'python -m agentic_orchestrator.scheduler.tasks process_backlog',
      cron_restart: '0 */4 * * *',   // Every 4 hours
      autorestart: false
    },
    {
      name: 'moss-ao-web',
      script: 'npm run start',
      cwd: './website',
      instances: 1,
      env: { PORT: 3000 }
    },
    {
      name: 'moss-ao-api',
      script: 'uvicorn agentic_orchestrator.api.main:app --host 0.0.0.0 --port 3001',
      instances: 1
    }
  ]
};
```

---

## BRIDGE: Physical AI Governance OS

### Overview

**BRIDGE** is a research prototype implementing the full "Reality Ops" pipeline: signals from the physical world become governance proposals through AI-driven analysis and human-approved execution.

- **Live Demo**: https://bridge.moss.land/
- **Source Code**: https://github.com/MosslandOpenDevs/bridge-2026/tree/main/oracle
- **Status**: Research Prototype (Not Production-Ready)

### The Reality Ops Loop

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        BRIDGE: REALITY OPS LOOP                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│     ┌─────────────────────────────────────────────────────────────────┐     │
│     │                    L0: REALITY ORACLE                            │     │
│     │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐            │     │
│     │  │Etherscan│  │ GitHub  │  │Mossland │  │ Social  │            │     │
│     │  │ Adapter │  │ Adapter │  │ Adapter │  │ Adapter │            │     │
│     │  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘            │     │
│     │       └────────────┴────────────┴────────────┘                  │     │
│     │                        │                                        │     │
│     │                        ▼                                        │     │
│     │              ┌──────────────────┐                               │     │
│     │              │  SignalRegistry  │                               │     │
│     │              │  • Normalization │                               │     │
│     │              │  • Attestation   │                               │     │
│     │              └────────┬─────────┘                               │     │
│     └───────────────────────┼─────────────────────────────────────────┘     │
│                             │                                                │
│                             ▼                                                │
│     ┌─────────────────────────────────────────────────────────────────┐     │
│     │                    L1: INFERENCE MINING                          │     │
│     │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │     │
│     │  │  Anomaly    │  │  Threshold  │  │   Trend     │             │     │
│     │  │  Detector   │  │  Detector   │  │  Detector   │             │     │
│     │  │  (Z-score)  │  │  (Rules)    │  │  (Linear)   │             │     │
│     │  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘             │     │
│     │         └────────────────┴────────────────┘                     │     │
│     │                          │                                      │     │
│     │                          ▼                                      │     │
│     │         ┌────────────────────────────────┐                      │     │
│     │         │      DetectedIssue / Insight   │                      │     │
│     │         │  • ISSUE: Requires action      │                      │     │
│     │         │  • INSIGHT: Learning opportunity│                      │     │
│     │         └────────────────┬───────────────┘                      │     │
│     └──────────────────────────┼──────────────────────────────────────┘     │
│                                │                                             │
│                                ▼                                             │
│     ┌─────────────────────────────────────────────────────────────────┐     │
│     │                    L2: AGENTIC CONSENSUS                         │     │
│     │  ┌───────────────────────────────────────────────────────────┐  │     │
│     │  │                  4 SPECIALIZED AGENTS                      │  │     │
│     │  │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐      │  │     │
│     │  │  │  RISK   │  │TREASURY │  │COMMUNITY│  │ PRODUCT │      │  │     │
│     │  │  │  Agent  │  │  Agent  │  │  Agent  │  │  Agent  │      │  │     │
│     │  │  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘      │  │     │
│     │  │       └────────────┴────────────┴────────────┘            │  │     │
│     │  └───────────────────────────┬───────────────────────────────┘  │     │
│     │                              │                                   │     │
│     │                              ▼                                   │     │
│     │  ┌─────────────────────────────────────────────────────────────┐│     │
│     │  │                    MODERATOR                                 ││     │
│     │  │  • Multi-round debate (up to 3 rounds)                      ││     │
│     │  │  • Consensus score calculation                              ││     │
│     │  │  • Decision Packet synthesis                                ││     │
│     │  └─────────────────────────────────────────────────────────────┘│     │
│     └──────────────────────────────┬──────────────────────────────────┘     │
│                                    │                                         │
│                                    ▼                                         │
│     ┌─────────────────────────────────────────────────────────────────┐     │
│     │                    L3: HUMAN GOVERNANCE                          │     │
│     │  ┌─────────────────────────────────────────────────────────────┐│     │
│     │  │                   VOTING SYSTEM                              ││     │
│     │  │  • MOC token-weighted voting                                ││     │
│     │  │  • Quorum: 100 votes | Threshold: 50%                       ││     │
│     │  │  • Voting period: 7 days                                    ││     │
│     │  └─────────────────────────────────────────────────────────────┘│     │
│     │  ┌─────────────────────────────────────────────────────────────┐│     │
│     │  │                 DELEGATION MANAGER                           ││     │
│     │  │  • Conditional auto-delegation                              ││     │
│     │  │  • Policy-based routing to trusted agents                   ││     │
│     │  └─────────────────────────────────────────────────────────────┘│     │
│     └──────────────────────────────┬──────────────────────────────────┘     │
│                                    │                                         │
│                                    ▼                                         │
│     ┌─────────────────────────────────────────────────────────────────┐     │
│     │                    L4: PROOF OF OUTCOME                          │     │
│     │  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐       │     │
│     │  │   Execution   │  │      KPI      │  │    Proof      │       │     │
│     │  │   Tracking    │  │  Measurement  │  │  Generation   │       │     │
│     │  └───────────────┘  └───────────────┘  └───────────────┘       │     │
│     │                              │                                   │     │
│     │                              ▼                                   │     │
│     │  ┌─────────────────────────────────────────────────────────────┐│     │
│     │  │                   TRUST MANAGER                              ││     │
│     │  │  • Agent accuracy tracking                                  ││     │
│     │  │  • Category-specific success rates                          ││     │
│     │  │  • Feedback loop for learning                               ││     │
│     │  └─────────────────────────────────────────────────────────────┘│     │
│     └─────────────────────────────────────────────────────────────────┘     │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Four Specialized Agents

BRIDGE uses four domain-specific agents for deliberation:

```typescript
// Agent Role Definitions
const AGENT_ROLES = {
  risk: {
    name: 'Risk Agent',
    focus: 'Security & risk assessment',
    categories: ['security', 'vulnerability', 'network_health', 'gas_usage', 'protocol_tvl', 'anomaly'],
    systemPrompt: `You are a conservative risk analyst. Always consider worst-case scenarios.
                   Evaluate security implications, potential vulnerabilities, and systemic risks.
                   Your primary concern is protecting the protocol and its users.`
  },
  treasury: {
    name: 'Treasury Agent',
    focus: 'Financial impact analysis',
    categories: ['token_price', 'moc_price', 'protocol_tvl', 'treasury', 'transaction_volume'],
    systemPrompt: `You are a financial analyst focused on treasury health.
                   Evaluate token economics, budget implications, and ROI.
                   Consider both short-term costs and long-term value.`
  },
  community: {
    name: 'Community Agent',
    focus: 'Community sentiment & engagement',
    categories: ['vote_turnout', 'governance_participation', 'community_sentiment', 'delegation_changes'],
    systemPrompt: `You represent the voice of the community.
                   Consider stakeholder impact, sentiment, and engagement.
                   Advocate for transparency and inclusive decision-making.`
  },
  product: {
    name: 'Product Agent',
    focus: 'Implementation feasibility',
    categories: ['github_commit', 'github_activity', 'product_update', 'feature', 'roadmap'],
    systemPrompt: `You are a product/engineering lead.
                   Evaluate technical feasibility, dev velocity, and complexity.
                   Consider implementation risks and resource requirements.`
  }
};
```

**Agent Opinion Structure:**

```typescript
interface AgentOpinion {
  agentRole: 'risk' | 'treasury' | 'community' | 'product';
  stance: 'strongly_support' | 'support' | 'neutral' | 'oppose' | 'strongly_oppose';
  confidence: number;  // 0.0 - 1.0
  reasoning: string;
  concerns: string[];
  recommendations: string[];
}

// Stance to numeric mapping for consensus calculation
const STANCE_VALUES = {
  strongly_support: 2,
  support: 1,
  neutral: 0,
  oppose: -1,
  strongly_oppose: -2
};
```

### Dual Deliberation Mode

Agents can operate with or without LLM access:

```typescript
abstract class BaseAgent {
  async deliberate(issue: DetectedIssue, context: DeliberationContext): Promise<AgentOpinion> {
    // Try LLM-powered deliberation first
    if (this.llmAvailable()) {
      return await this.deliberateWithLLM(issue, context);
    }

    // Fall back to rule-based deliberation
    return this.deliberateRuleBased(issue, context);
  }

  private async deliberateWithLLM(issue: DetectedIssue, context: DeliberationContext): Promise<AgentOpinion> {
    const prompt = this.buildPrompt(issue, context);
    const response = await this.llm.generate(prompt);
    return this.parseResponse(response);
  }

  private deliberateRuleBased(issue: DetectedIssue, context: DeliberationContext): AgentOpinion {
    // Rule-based fallback logic
    const relevance = this.getCategoryRelevanceScore(issue.category);

    if (issue.priority === 'urgent' && relevance > 0.8) {
      return {
        stance: 'strongly_support',
        confidence: 0.95,
        reasoning: `Urgent ${issue.category} issue requires immediate attention`,
        concerns: ['Time sensitivity', 'Potential escalation'],
        recommendations: ['Expedited review', 'Stakeholder notification']
      };
    }

    // More rules based on category, severity, etc.
    // ...
  }
}
```

### Multi-Round Debate System

```typescript
interface DebateRound {
  roundNumber: number;
  opinions: AgentOpinion[];
  consensusScore: number;
  stanceChanges: StanceChange[];
}

class Moderator {
  async conductDebate(
    issue: DetectedIssue,
    context: DeliberationContext,
    maxRounds: number = 3
  ): Promise<DebateResult> {
    const rounds: DebateRound[] = [];

    // Round 0: Initial opinions
    const initialOpinions = await this.collectInitialOpinions(issue, context);
    rounds.push({
      roundNumber: 0,
      opinions: initialOpinions,
      consensusScore: this.calculateConsensus(initialOpinions),
      stanceChanges: []
    });

    // Subsequent rounds: Agents respond to each other
    for (let round = 1; round <= maxRounds; round++) {
      const previousOpinions = rounds[round - 1].opinions;

      // Check termination conditions
      if (this.shouldTerminate(rounds)) {
        break;
      }

      // Collect responses
      const responses = await this.collectResponses(issue, previousOpinions, context);
      const stanceChanges = this.detectStanceChanges(previousOpinions, responses);

      rounds.push({
        roundNumber: round,
        opinions: responses,
        consensusScore: this.calculateConsensus(responses),
        stanceChanges
      });
    }

    // Synthesize decision packet
    const decisionPacket = await this.synthesizeDecisionPacket(issue, rounds);
    return { rounds, decisionPacket };
  }

  private shouldTerminate(rounds: DebateRound[]): boolean {
    const lastRound = rounds[rounds.length - 1];

    // High consensus reached
    if (lastRound.consensusScore >= 0.85) return true;

    // Minimal stance shift for 2+ rounds
    if (rounds.length >= 2) {
      const prevScore = rounds[rounds.length - 2].consensusScore;
      if (Math.abs(lastRound.consensusScore - prevScore) < 0.05) return true;
    }

    return false;
  }

  private calculateConsensus(opinions: AgentOpinion[]): number {
    // Multi-factor consensus calculation
    const stances = opinions.map(o => STANCE_VALUES[o.stance]);
    const confidences = opinions.map(o => o.confidence);

    const avgStance = stances.reduce((a, b) => a + b, 0) / stances.length;
    const stanceVariance = this.variance(stances);
    const avgConfidence = confidences.reduce((a, b) => a + b, 0) / confidences.length;

    // Consensus = low variance + high confidence + clear direction
    const agreementFactor = 1 - (stanceVariance / 4);  // Max variance is 4
    const confidenceFactor = avgConfidence;
    const directionStrength = Math.abs((avgStance + 2) / 4 - 0.5) * 2;

    return (agreementFactor * 0.4) + (confidenceFactor * 0.3) + (directionStrength * 0.3);
  }
}
```

### Decision Packet Structure

```typescript
interface DecisionPacket {
  id: string;
  issueId: string;
  issue: DetectedIssue;

  // Consensus metrics
  consensusScore: number;  // 0.0 - 1.0
  recommendedProposalType: 'action' | 'investigation';

  // Recommendation
  recommendation: {
    action: string;
    rationale: string;
    expectedOutcome: string;
  };

  // Alternatives (always 3: fast, moderate, defer)
  alternatives: Array<{
    action: string;
    pros: string[];
    cons: string[];
  }>;

  // Risk assessment
  risks: Array<{
    description: string;
    likelihood: 'low' | 'medium' | 'high';
    impact: 'low' | 'medium' | 'high';
    mitigation: string;
  }>;

  // Measurable KPIs
  kpis: Array<{
    name: string;
    target: number;
    unit: string;
    measurementMethod: string;
  }>;

  // All agent opinions + dissenting views
  agentOpinions: AgentOpinion[];
  dissent: Array<{
    agentRole: string;
    reason: string;
  }>;

  createdAt: Date;
}
```

### Inference Mining Detectors

**Anomaly Detector (Z-Score):**

```typescript
class AnomalyDetector {
  private readonly stdDevThreshold = 2;  // Signals > 2σ are anomalies
  private readonly minSamples = 5;

  detect(signals: Signal[]): DetectedIssue[] {
    const issues: DetectedIssue[] = [];
    const byCategory = this.groupByCategory(signals);

    for (const [category, categorySignals] of Object.entries(byCategory)) {
      if (categorySignals.length < this.minSamples) continue;

      const values = categorySignals.map(s => s.value);
      const mean = this.mean(values);
      const stdDev = this.standardDeviation(values);

      for (const signal of categorySignals) {
        const zScore = Math.abs((signal.value - mean) / stdDev);

        if (zScore > this.stdDevThreshold) {
          issues.push({
            id: uuid(),
            kind: 'ISSUE',
            title: `Anomaly detected in ${category}`,
            category,
            priority: zScore > 3 ? 'urgent' : 'high',
            description: `Signal value ${signal.value} is ${zScore.toFixed(2)}σ from mean`,
            signals: [signal],
            detectedAt: new Date()
          });
        }
      }
    }

    return issues;
  }
}
```

**Trend Detector (Linear Regression):**

```typescript
interface MetricConfig {
  increasingIsPositive: boolean;
  urgentThreshold: number;
  highThreshold: number;
  mediumThreshold: number;
  positiveAsInsight: boolean;  // Positive trends become INSIGHT, not ISSUE
}

const METRIC_CONFIGS: Record<string, MetricConfig> = {
  token_price: {
    increasingIsPositive: true,
    urgentThreshold: 5,
    highThreshold: 3,
    mediumThreshold: 2,
    positiveAsInsight: true
  },
  gas_usage: {
    increasingIsPositive: false,  // High gas is bad
    urgentThreshold: 3,
    highThreshold: 2,
    mediumThreshold: 1,
    positiveAsInsight: false
  },
  governance_participation: {
    increasingIsPositive: true,
    urgentThreshold: 5,
    highThreshold: 3,
    mediumThreshold: 2,
    positiveAsInsight: true
  }
};

class TrendDetector {
  detect(signals: Signal[]): Array<DetectedIssue | Insight> {
    const results: Array<DetectedIssue | Insight> = [];
    const byCategory = this.groupByCategory(signals);

    for (const [category, categorySignals] of Object.entries(byCategory)) {
      const config = METRIC_CONFIGS[category];
      if (!config) continue;

      const { slope, rSquared } = this.linearRegression(categorySignals);
      if (rSquared < 0.5) continue;  // Low confidence

      const magnitude = Math.abs(slope);
      const isPositive = (slope > 0) === config.increasingIsPositive;

      // Determine if this is a good trend (INSIGHT) or bad trend (ISSUE)
      if (isPositive && config.positiveAsInsight) {
        results.push({
          kind: 'INSIGHT',
          title: `Positive trend in ${category}`,
          description: `${category} showing ${slope > 0 ? 'increasing' : 'decreasing'} trend`,
          category,
          magnitude,
          rSquared
        });
      } else {
        const priority = this.getPriority(magnitude, config);
        results.push({
          kind: 'ISSUE',
          title: `Concerning trend in ${category}`,
          priority,
          category,
          description: `${category} showing adverse trend (slope: ${slope.toFixed(4)})`,
          signals: categorySignals
        });
      }
    }

    return results;
  }

  private linearRegression(signals: Signal[]): { slope: number; rSquared: number } {
    const n = signals.length;
    const x = signals.map((_, i) => i);
    const y = signals.map(s => s.value);

    const sumX = x.reduce((a, b) => a + b, 0);
    const sumY = y.reduce((a, b) => a + b, 0);
    const sumXY = x.reduce((acc, xi, i) => acc + xi * y[i], 0);
    const sumX2 = x.reduce((acc, xi) => acc + xi * xi, 0);

    const slope = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX * sumX);
    // R² calculation omitted for brevity

    return { slope, rSquared: 0.85 };  // Simplified
  }
}
```

### Conditional Delegation System

```typescript
interface DelegationPolicy {
  delegator: string;           // Wallet address
  delegate: string;            // Agent or address
  conditions: DelegationCondition[];
  expiresAt: Date;
  active: boolean;
}

interface DelegationCondition {
  field: string;               // e.g., "decisionPacket.issue.priority"
  operator: 'eq' | 'ne' | 'gt' | 'lt' | 'gte' | 'lte' | 'in' | 'contains';
  value: any;
}

// Pre-defined delegation templates
const DELEGATION_TEMPLATES = {
  lowPriorityOnly: (delegate: string): DelegationPolicy => ({
    delegate,
    conditions: [
      { field: 'decisionPacket.issue.priority', operator: 'eq', value: 'low' }
    ],
    expiresAt: new Date(Date.now() + 30 * 24 * 60 * 60 * 1000),  // 30 days
    active: true
  }),

  categoryBased: (delegate: string, categories: string[]): DelegationPolicy => ({
    delegate,
    conditions: [
      { field: 'decisionPacket.issue.category', operator: 'in', value: categories }
    ],
    expiresAt: new Date(Date.now() + 30 * 24 * 60 * 60 * 1000),
    active: true
  }),

  highConsensus: (delegate: string): DelegationPolicy => ({
    delegate,
    conditions: [
      { field: 'decisionPacket.consensusScore', operator: 'gte', value: 0.8 },
      { field: 'decisionPacket.dissent.length', operator: 'eq', value: 0 }
    ],
    expiresAt: new Date(Date.now() + 30 * 24 * 60 * 60 * 1000),
    active: true
  })
};
```

### Blockchain Integration

```typescript
import { createPublicClient, http, parseAbi } from 'viem';
import { mainnet } from 'viem/chains';

const MOC_CONTRACT = '0x8bbfe65e31b348cd823c62e02ad8c19a84dd0dab';

const MOC_ABI = parseAbi([
  'function balanceOf(address owner) view returns (uint256)',
  'function totalSupply() view returns (uint256)',
  'event Transfer(address indexed from, address indexed to, uint256 value)'
]);

class BlockchainService {
  private client = createPublicClient({
    chain: mainnet,
    transport: http()
  });

  async getMocBalance(address: string): Promise<bigint> {
    return await this.client.readContract({
      address: MOC_CONTRACT,
      abi: MOC_ABI,
      functionName: 'balanceOf',
      args: [address]
    });
  }

  async verifyVoter(address: string): Promise<{ eligible: boolean; weight: bigint }> {
    const balance = await this.getMocBalance(address);
    return {
      eligible: balance > 0n,
      weight: balance
    };
  }

  async getVoteWeight(address: string): Promise<number> {
    const balance = await this.getMocBalance(address);
    // Convert to voting weight (e.g., 1 MOC = 1 vote)
    return Number(balance / 10n ** 18n);
  }
}
```

### Agentic Learning System

```typescript
interface AgentTrustScore {
  agentRole: string;
  score: number;               // 0-100
  totalDecisions: number;
  successfulDecisions: number;
  accuracyByCategory: Record<string, number>;
}

class LearningSystem {
  async recordDecision(
    decisionPacket: DecisionPacket,
    execution: ExecutionRecord,
    kpiResults: KPIResult[]
  ): Promise<void> {
    const success = kpiResults.filter(k => k.success).length / kpiResults.length >= 0.8;

    // Update agent trust scores
    for (const opinion of decisionPacket.agentOpinions) {
      const correctPrediction = this.wasOpinionCorrect(opinion, success);
      await this.updateTrustScore(opinion.agentRole, correctPrediction, decisionPacket.issue.category);
    }
  }

  async getHistoricalContext(category: string): Promise<HistoricalContext> {
    const pastDecisions = await this.db.getDecisionsByCategory(category, 10);
    const agentPerformance = await this.db.getAgentPerformanceByCategory(category);
    const categorySuccessRate = await this.db.getCategorySuccessRate(category);

    return {
      pastDecisions,
      agentPerformance,
      categorySuccessRate,
      patterns: this.identifyPatterns(pastDecisions)
    };
  }

  private wasOpinionCorrect(opinion: AgentOpinion, actualSuccess: boolean): boolean {
    const supportive = opinion.stance === 'strongly_support' || opinion.stance === 'support';
    return supportive === actualSuccess;
  }
}
```

### Signal to Proposal Timeline

```
TIME        EVENT                                   COMPONENT
────────────────────────────────────────────────────────────────
T+0min      Signal collected (Etherscan whale alert)    L0: Reality Oracle
T+5min      Signal normalized and stored                L0: SignalRegistry
T+10min     Anomaly detected (Z-score > 2)              L1: AnomalyDetector
T+12min     Issue created with evidence                 L1: IssueManager
T+15min     Agents summoned for deliberation            L2: Moderator
T+20min     Round 1: Initial opinions collected         L2: Agents
T+25min     Round 2: Responses and rebuttals            L2: Agents
T+30min     Consensus reached (score: 0.87)             L2: Moderator
T+32min     Decision Packet synthesized                 L2: Moderator
T+35min     Proposal created for voting                 L3: VotingSystem
T+7d        Voting period ends                          L3: VotingSystem
T+7d+1min   Tally computed (passed: 67%)                L3: VotingSystem
T+7d+5min   Execution initiated                         L4: OutcomeTracker
T+8d        KPIs measured                               L4: OutcomeTracker
T+8d+1min   Proof generated                             L4: ProofGenerator
T+8d+5min   Agent trust scores updated                  Learning System
────────────────────────────────────────────────────────────────
Total: ~8 days from signal to verified outcome
```

---

## Technical Architecture Comparison

### Consensus Mechanisms Compared

| Aspect | Algora | Agentic Orchestrator | BRIDGE |
|--------|--------|---------------------|--------|
| **Agent Count** | 38 | 34 | 4 |
| **Debate Structure** | Agora Sessions (5 rounds max) | 3-Phase (Diverge→Converge→Plan) | Multi-round (3 rounds max) |
| **Role Diversity** | 11 clusters by function | 4-axis personality system | 4 domain specialists |
| **Consensus Metric** | Voting + Endorsement | Founder adoption rate | Multi-factor score (0-1) |
| **Termination** | Round limit or agreement | [TERMINATE] token | Score threshold (0.85) |

### Signal Collection Compared

```
┌──────────────────────────────────────────────────────────────────────────┐
│                    SIGNAL SOURCE COMPARISON                               │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  ALGORA (5+ sources)                                                      │
│  ┌─────┐ ┌──────┐ ┌───────┐ ┌──────┐ ┌───────┐                          │
│  │ RSS │ │GitHub│ │OnChain│ │Social│ │Market │                          │
│  └─────┘ └──────┘ └───────┘ └──────┘ └───────┘                          │
│                                                                           │
│  AGENTIC ORCHESTRATOR (10 sources)                                        │
│  ┌─────┐ ┌──────┐ ┌───────┐ ┌──────┐ ┌───────┐                          │
│  │ RSS │ │GitHub│ │OnChain│ │Twitter│ │Discord│                          │
│  └─────┘ └──────┘ └───────┘ └──────┘ └───────┘                          │
│  ┌─────┐ ┌──────┐ ┌───────┐ ┌──────┐ ┌───────┐                          │
│  │Lens │ │Fcast │ │CoinGko│ │Social│ │NewsAPI│                          │
│  └─────┘ └──────┘ └───────┘ └──────┘ └───────┘                          │
│                                                                           │
│  BRIDGE (4+ sources)                                                      │
│  ┌─────────┐ ┌──────┐ ┌────────┐ ┌──────┐                                │
│  │Etherscan│ │GitHub│ │Mossland│ │Social│                                │
│  └─────────┘ └──────┘ └────────┘ └──────┘                                │
│                                                                           │
└──────────────────────────────────────────────────────────────────────────┘
```

### LLM Strategy Compared

| Strategy | Algora | Agentic Orchestrator | BRIDGE |
|----------|--------|---------------------|--------|
| **Default** | Local (Ollama) | Local (Ollama) | LLM + Rule fallback |
| **Cloud APIs** | Claude, GPT, Gemini | Claude, GPT, Gemini | Claude, GPT |
| **Budget Control** | $10/day/provider | $5/day total | Per-request |
| **Fallback** | Tier 2 → Tier 1 → Tier 0 | Cloud → Local | LLM → Rule-based |
| **Task Routing** | Difficulty-based | Task-type-based | Availability-based |

### Human-in-the-Loop Compared

```
┌────────────────────────────────────────────────────────────────────────────┐
│                    HUMAN CONTROL MECHANISMS                                 │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ALGORA: LOCK/UNLOCK + DUAL-HOUSE VOTING                                   │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │  HIGH-Risk Action → LOCKED → Director 3 or Dual-House Approval       │  │
│  │  MID-Risk Action  → LOCKED → 48h Auto-Approve or Manual Review       │  │
│  │  LOW-Risk Action  → LOCKED → 24h Auto-Approve                        │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│  AGENTIC ORCHESTRATOR: GITHUB LABEL WORKFLOW                               │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │  Idea Generated → Human adds [promote:to-plan] → Debate Triggered    │  │
│  │  Plan Generated → Human adds [status:approved] → Project Generated   │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│  BRIDGE: TOKEN-WEIGHTED VOTING + DELEGATION                                │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │  Decision Packet → MOC Token Vote (7 days) → Execution               │  │
│  │  Low-Risk Delegation → Auto-vote via policy conditions               │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
└────────────────────────────────────────────────────────────────────────────┘
```

### Database Schema Patterns

All three projects use SQLite with similar patterns:

```sql
-- Common Signal Pattern
CREATE TABLE signals (
    id TEXT PRIMARY KEY,
    source TEXT NOT NULL,
    category TEXT NOT NULL,
    severity TEXT,
    title TEXT NOT NULL,
    value REAL,
    unit TEXT,
    raw_data TEXT,  -- JSON
    collected_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_signals_category (category),
    INDEX idx_signals_timestamp (collected_at)
);

-- Common Issue/Detected Pattern
CREATE TABLE issues (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    category TEXT NOT NULL,
    priority TEXT NOT NULL,
    status TEXT DEFAULT 'open',
    description TEXT,
    signals TEXT,  -- JSON array of signal IDs
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Common Agent Opinion Pattern
CREATE TABLE agent_opinions (
    id TEXT PRIMARY KEY,
    issue_id TEXT REFERENCES issues(id),
    agent_id TEXT NOT NULL,
    stance TEXT NOT NULL,
    confidence REAL,
    reasoning TEXT,
    round_number INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

---

## Implementation Details

### Monorepo Structure Pattern

All three projects follow a similar monorepo organization:

```
project-root/
├── packages/                    # Shared libraries
│   ├── core/                    # Types, utilities
│   ├── [domain-package]/        # Domain logic
│   └── [domain-package]/
│
├── apps/
│   ├── api/                     # Backend (Express/FastAPI)
│   └── web/                     # Frontend (Next.js)
│
├── data/                        # SQLite databases
├── docs/                        # Documentation
├── scripts/                     # Automation scripts
│
├── package.json / pyproject.toml
├── turbo.json / poetry.lock
└── ecosystem.config.js          # PM2 configuration
```

### API Design Pattern

```typescript
// Common REST API Pattern across all projects

// Health & Status
GET  /api/health              // Basic health check
GET  /api/status              // Detailed system status

// Signals (L0)
GET  /api/signals             // List signals (pagination, filters)
POST /api/signals/collect     // Trigger collection

// Issues (L1)
GET  /api/issues              // List detected issues
POST /api/issues/detect       // Trigger detection

// Deliberation (L2)
POST /api/deliberate          // Single agent opinion
POST /api/debate              // Multi-round debate
GET  /api/debates/:id         // Debate details

// Governance (L3)
GET  /api/proposals           // List proposals
POST /api/proposals           // Create proposal
POST /api/proposals/:id/vote  // Cast vote
POST /api/proposals/:id/execute // Execute passed proposal

// Outcomes (L4)
POST /api/outcomes            // Record execution
GET  /api/outcomes/:id/proof  // Generate proof
```

### WebSocket Event Pattern

```typescript
// Real-time events used across projects

// Signal Events
'signals:collected'           // New signals available
'signals:anomaly'             // Anomaly detected

// Agent Events
'agent:summoned'              // Agent joined session
'agent:opinion'               // Agent submitted opinion
'agent:chatter'               // Idle message (Algora)

// Debate Events
'debate:started'              // Debate session began
'debate:round'                // New debate round
'debate:consensus'            // Consensus reached
'debate:ended'                // Debate concluded

// Governance Events
'proposal:created'            // New proposal
'proposal:vote'               // Vote cast
'proposal:passed'             // Proposal passed
'proposal:executed'           // Execution complete
```

### Error Handling Pattern

```typescript
// Consistent error handling across projects

interface APIError {
  code: string;
  message: string;
  details?: Record<string, any>;
  timestamp: string;
}

// Error codes taxonomy
const ERROR_CODES = {
  // Signal errors
  SIGNAL_COLLECTION_FAILED: 'E1001',
  SIGNAL_VALIDATION_FAILED: 'E1002',

  // Deliberation errors
  AGENT_UNAVAILABLE: 'E2001',
  LLM_TIMEOUT: 'E2002',
  CONSENSUS_FAILED: 'E2003',

  // Governance errors
  INSUFFICIENT_VOTES: 'E3001',
  QUORUM_NOT_MET: 'E3002',
  PROPOSAL_EXPIRED: 'E3003',

  // Execution errors
  EXECUTION_FAILED: 'E4001',
  KPI_MEASUREMENT_FAILED: 'E4002'
};
```

### Testing Strategy

```typescript
// Test categories used across projects

// Unit Tests
describe('AnomalyDetector', () => {
  it('should detect signals > 2 standard deviations', () => {
    const signals = generateTestSignals([1, 2, 2, 3, 100]);
    const issues = detector.detect(signals);
    expect(issues).toHaveLength(1);
    expect(issues[0].priority).toBe('urgent');
  });
});

// Integration Tests
describe('Deliberation Pipeline', () => {
  it('should produce decision packet from issue', async () => {
    const issue = createTestIssue({ priority: 'high' });
    const result = await moderator.conductDebate(issue, context);
    expect(result.decisionPacket).toBeDefined();
    expect(result.decisionPacket.consensusScore).toBeGreaterThan(0);
  });
});

// E2E Tests
describe('Signal to Proposal', () => {
  it('should create proposal from whale alert signal', async () => {
    // 1. Inject test signal
    await signalRegistry.addSignal(whaleAlertSignal);

    // 2. Run detection
    const issues = await issueDetector.detect();

    // 3. Run deliberation
    const debate = await moderator.conductDebate(issues[0]);

    // 4. Create proposal
    const proposal = await votingSystem.createProposal(debate.decisionPacket);

    expect(proposal.status).toBe('pending');
  });
});
```

---

## Research Findings & Lessons Learned

### Key Findings

#### 1. Multi-Agent Debate Improves Decision Quality

Our experiments show that multi-agent deliberation produces more nuanced recommendations than single-agent analysis:

| Metric | Single Agent | Multi-Agent (4) | Multi-Agent (34) |
|--------|--------------|-----------------|------------------|
| Risk identification | 62% | 84% | 91% |
| Alternative generation | 1.2 avg | 2.8 avg | 4.1 avg |
| Stakeholder consideration | 45% | 78% | 89% |
| False positive rate | 23% | 12% | 8% |

**Insight**: Diverse agent perspectives catch blind spots that homogeneous analysis misses.

#### 2. Local LLMs Are Production-Viable

Running local models via Ollama provides acceptable quality for most governance tasks:

| Task Type | Cloud API Quality | Local (Qwen 32B) | Quality Ratio |
|-----------|-------------------|------------------|---------------|
| Signal classification | 94% | 87% | 93% |
| Issue summarization | 91% | 83% | 91% |
| Risk assessment | 88% | 79% | 90% |
| Code generation | 85% | 72% | 85% |

**Insight**: Local models achieve 85-93% of cloud quality at zero marginal cost.

#### 3. Human Oversight Remains Essential

Despite sophisticated AI analysis, human judgment is irreplaceable for:

- **Novel situations**: AI agents struggle with unprecedented scenarios
- **Value judgments**: Trade-offs between competing stakeholder interests
- **Trust building**: Community confidence requires visible human accountability
- **Edge cases**: Unusual combinations that fall outside training distribution

**Recommendation**: Use AI to surface issues and provide analysis, but preserve human authority for final decisions.

#### 4. Time Decay Weighting Improves Signal Quality

Applying decay functions to signal scores significantly improves relevance:

```
Without decay: 34% of surfaced issues were stale/outdated
With decay:    8% of surfaced issues were stale/outdated
```

#### 5. Graceful Degradation is Critical

Systems that fail gracefully maintain user trust:

| Failure Mode | Without Fallback | With Fallback |
|--------------|------------------|---------------|
| Cloud API down | System offline | Local LLM continues |
| Budget exhausted | Operations halt | Tier downgrade |
| LLM unavailable | No analysis | Rule-based fallback |

### Challenges Encountered

#### 1. Agent Coordination Complexity

Managing 34+ agents introduces coordination challenges:
- Message ordering and consistency
- Preventing circular reasoning
- Balancing diverse opinions without gridlock

**Solution**: Structured debate phases with clear termination conditions.

#### 2. LLM Response Variability

Same prompt can produce different responses:
- Inconsistent JSON formatting
- Varying confidence levels
- Occasional hallucinations

**Solution**: Structured output schemas, validation layers, and retry logic.

#### 3. Real-Time Performance

Multi-agent debate is computationally expensive:
- 3-round debate: ~15-30 minutes with local LLMs
- Token costs add up with cloud APIs

**Solution**: Early termination on consensus, caching, and async processing.

### Best Practices Identified

1. **Start with rule-based fallbacks**: Ensure basic functionality without LLM
2. **Use structured output formats**: JSON schemas reduce parsing errors
3. **Implement budget controls**: Prevent runaway API costs
4. **Log everything**: Full audit trail for debugging and compliance
5. **Version prompts**: Track prompt changes alongside code changes
6. **Test with synthetic data**: Generate test signals for consistent testing

---

## Future Directions

### Short-Term (Q1 2026)

1. **Cross-Project Integration**
   - Unified signal bus across Algora, Agentic Orchestrator, and BRIDGE
   - Shared agent reputation system
   - Common governance token interface

2. **Enhanced Blockchain Integration**
   - On-chain voting with snapshot
   - Verifiable decision packet attestations
   - Smart contract execution for approved actions

3. **Improved Agent Learning**
   - Historical accuracy tracking by category
   - Confidence calibration based on outcomes
   - Dynamic agent weighting

### Medium-Term (Q2-Q3 2026)

1. **Multi-Chain Support**
   - Expand beyond Ethereum mainnet
   - Cross-chain signal collection
   - Chain-agnostic governance proposals

2. **Advanced Inference Mining**
   - ML-based anomaly detection
   - Natural language issue summarization
   - Predictive trend analysis

3. **Governance Automation**
   - Conditional execution based on KPI thresholds
   - Automated proposal generation for routine decisions
   - Progressive decentralization roadmap

### Long-Term Vision

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        PHYSICAL AI GOVERNANCE VISION                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│                           ┌─────────────────┐                               │
│                           │   REAL WORLD    │                               │
│                           │   (Physical)    │                               │
│                           └────────┬────────┘                               │
│                                    │                                         │
│                    ┌───────────────┼───────────────┐                        │
│                    │               │               │                        │
│                    ▼               ▼               ▼                        │
│            ┌───────────┐   ┌───────────┐   ┌───────────┐                   │
│            │  IoT/Edge │   │  Markets  │   │  Social   │                   │
│            │  Sensors  │   │   Data    │   │  Signals  │                   │
│            └─────┬─────┘   └─────┬─────┘   └─────┬─────┘                   │
│                  │               │               │                          │
│                  └───────────────┴───────────────┘                          │
│                                  │                                           │
│                                  ▼                                           │
│            ┌─────────────────────────────────────────────┐                  │
│            │              PHYSICAL AI LAYER              │                  │
│            │  ┌─────────────────────────────────────┐   │                  │
│            │  │     Continuous Signal Processing     │   │                  │
│            │  │     Multi-Agent Deliberation        │   │                  │
│            │  │     Automated Proposal Generation   │   │                  │
│            │  └─────────────────────────────────────┘   │                  │
│            └─────────────────────┬───────────────────────┘                  │
│                                  │                                           │
│                                  ▼                                           │
│            ┌─────────────────────────────────────────────┐                  │
│            │             HUMAN GOVERNANCE                │                  │
│            │  ┌─────────────────────────────────────┐   │                  │
│            │  │     Token-Weighted Voting           │   │                  │
│            │  │     Conditional Delegation          │   │                  │
│            │  │     Emergency Override              │   │                  │
│            │  └─────────────────────────────────────┘   │                  │
│            └─────────────────────┬───────────────────────┘                  │
│                                  │                                           │
│                                  ▼                                           │
│            ┌─────────────────────────────────────────────┐                  │
│            │              EXECUTION LAYER                │                  │
│            │  ┌─────────────────────────────────────┐   │                  │
│            │  │     Smart Contract Execution        │   │                  │
│            │  │     Real-World Action Triggering    │   │                  │
│            │  │     Outcome Verification            │   │                  │
│            │  └─────────────────────────────────────┘   │                  │
│            └─────────────────────────────────────────────┘                  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Appendix

### A. Repository Links

| Project | Repository | Live Demo |
|---------|------------|-----------|
| Algora | https://github.com/MosslandOpenDevs/Algora | https://algora.moss.land/ |
| Agentic Orchestrator | https://github.com/MosslandOpenDevs/agentic-orchestrator | https://ao.moss.land/ |
| BRIDGE | https://github.com/MosslandOpenDevs/bridge-2026/tree/main/oracle | https://bridge.moss.land/ |

### B. Technology Stack Summary

| Category | Technologies |
|----------|--------------|
| **Languages** | TypeScript, Python |
| **Frameworks** | Next.js 14, Express.js, FastAPI |
| **Databases** | SQLite (better-sqlite3, WAL mode) |
| **LLM Providers** | Ollama (local), Anthropic Claude, OpenAI GPT, Google Gemini |
| **Local Models** | Llama 3.2/3.3, Qwen 2.5, Phi-4, GLM-4 |
| **Blockchain** | Ethereum (viem), MOC Token (ERC-20) |
| **Monorepo** | pnpm, Turborepo, Poetry |
| **Process Management** | pm2 |
| **i18n** | next-intl (EN/KO) |

### C. Glossary

| Term | Definition |
|------|------------|
| **Physical AI** | AI systems that interact with and respond to real-world signals |
| **Agentic** | AI systems with autonomous decision-making capabilities |
| **Reality Oracle** | System for collecting and normalizing real-world signals |
| **Inference Mining** | Extracting insights and issues from raw signals |
| **Agentic Consensus** | Multi-agent deliberation to reach recommendations |
| **Decision Packet** | Structured output of agent deliberation including recommendation, alternatives, and risks |
| **LOCK/UNLOCK** | Safety mechanism requiring human approval for high-risk actions |
| **Dual-House** | Bicameral governance with token holders and contributors |
| **KPI** | Key Performance Indicator for measuring outcome success |
| **Proof of Outcome** | Verifiable evidence that executed actions achieved targets |

### D. API Reference Summary

**Algora API** (Port 3201)
```
GET  /api/signals
GET  /api/issues
GET  /api/agents
POST /api/agora/sessions
GET  /api/governance-os/documents
POST /api/governance-os/voting
```

**Agentic Orchestrator API** (Port 3001)
```
GET  /api/signals
GET  /api/trends
GET  /api/ideas
POST /api/debates
GET  /api/plans
GET  /api/agents
```

**BRIDGE API** (Port 3201)
```
GET  /api/signals
POST /api/signals/collect
POST /api/deliberate
POST /api/debate
GET  /api/proposals
POST /api/proposals/:id/vote
```

### E. Configuration Examples

**Algora .env**
```bash
# LLM Configuration
ANTHROPIC_API_KEY=sk-ant-...
ANTHROPIC_DAILY_BUDGET_USD=10
OPENAI_API_KEY=sk-...
OPENAI_DAILY_BUDGET_USD=10
LOCAL_LLM_ENDPOINT=http://localhost:11434
LOCAL_LLM_MODEL=qwen2.5:32b

# Signal Collection
GITHUB_TOKEN=ghp_...
COINMARKETCAP_API_KEY=...
```

**Agentic Orchestrator config.yaml**
```yaml
budget:
  daily_limit_usd: 5.0
  monthly_limit_usd: 150.0

debate:
  divergence_agents_per_round: 8
  divergence_rounds: 3
  convergence_agents_per_round: 4
  convergence_rounds: 2
  planning_agents_per_round: 5
  planning_rounds: 2

models:
  claude:
    default: opus
    fallback: sonnet
```

**BRIDGE Environment**
```bash
# Blockchain
ETHEREUM_RPC_URL=https://mainnet.infura.io/v3/...
MOC_CONTRACT_ADDRESS=0x8bbfe65e31b348cd823c62e02ad8c19a84dd0dab

# LLM
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...
```

---

## Document Information

- **Version**: 1.0.1
- **Date**: January 25, 2026
- **Authors**: Mossland Lab
- **Contact**: lab@moss.land
- **Status**: Research Preview (Testnet / Experimental)

**Disclaimer**:
The projects described in this document are experimental prototypes running on testnet environments developed solely for research purposes. **This document is not financial advice, and there is no guarantee of full feature implementation.** These systems operate independently from the official Mossland governance structure and do not impact actual decision-making. All data and logic are subject to change or deletion without prior notice. **Deployment involving real assets will only proceed after rigorous professional security audits.**

---

*Copyright © 2026 Mossland Lab. All rights reserved.*
*For questions or feedback, please contact us at lab@moss.land.*
