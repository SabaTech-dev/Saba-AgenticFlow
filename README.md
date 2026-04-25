# Saba-AgenticFlow — Multi-Agent Orchestration Framework

![CI](https://github.com/SabaTech-dev/Saba-AgenticFlow/workflows/CI/badge.svg)
![Coverage](https://img.shields.io/codecov/c/github/SabaTech-dev/Saba-AgenticFlow)
![License](https://img.shields.io/badge/license-MIT-blue)

## Abstract
Saba-AgenticFlow is a production-grade multi-agent orchestration system for AI agent ecosystems. It implements a hierarchical delegation model with Alfred (CEO) + 5 specialists (coder, debug, security, research, qa-tester), supported by Kanban tracking, heartbeat autonomy, and PDCA continuous improvement. Unlike simple multi-agent systems, it provides a complete orchestration lifecycle: delegate → execute → review → improve. Built on OpenClaw, it powers complex autonomous workflows with clear ownership boundaries and quality gates.

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   Alfred (CEO Agent)                  │
│              Decision Maker + Delegator                    │
├─────────────────────────────────────────────────────────────┤
│         5 Specialists (bounded ownership)                 │
├──────────┬──────────┬──────────┬──────────┬─────────┤
│  Coder   │  Debug    │ Security   │ Research  │ QA-Test │
│ (impl)   │ (diag)   │ (audit)   │ (invest) │ (test)  │
├──────────┴──────────┴──────────┴──────────┴─────────┤
│                   Orchestration Primitives               │
│  Kanban + Heartbeat + OpenProse + sessions_spawn       │
└─────────────────────────────────────────────────────────────┘
```

### Orchestration Primitives

| Primitive | Purpose | Owner |
|-----------|---------|--------|
| **Kanban** | Task tracking, quality gates, async work | Alfred creates, specialists process |
| **Heartbeat** | Autonomous 30-min cycles, claim work, handoff | All agents run independently |
| **OpenProse** | Multi-agent parallel workflows | Alfred/cross-domain |
| **sessions_spawn** | Helper subtasks, bounded scope | Specialist with context |
| **sessions_yield** | Pass baton back to owner | Specialist preserving ownership |

## Production Metrics

6 months continuous operation with OpenClaw multi-agent ecosystem:

| Metric | Value |
|--------|--------|
| Total tasks processed | 847 |
| Tasks completed | 782 (92.3% completion rate) |
| Average cycle time | 45 min |
| Handoffs between agents | 156 |
| PDCA iterations | 34 |
| Quality gates passed | 98.2% |

## Patterns

**Delegation Pattern:** Alfred delegates with explicit scope → Specialist claims → Specialist executes → Specialist yields back → Alfred reviews

**Autonomy Pattern:** Heartbeat every 30 min → Check Kanban → Claim if available → Execute → Handoff on completion

**Parallel Pattern:** OpenProse spawns parallel specialists → All run bounded tasks → Results aggregated → Continue flow

## Quick Start

```bash
# Clone repo
git clone https://github.com/SabaTech-dev/Saba-AgenticFlow.git
cd Saba-AgenticFlow

# Read architecture
cat docs/architecture.md

# Explore patterns
cat docs/patterns.md

# See [CHANGELOG.md](CHANGELOG.md) for version history
## Releases
See [CHANGELOG.md](CHANGELOG.md) for version history.
```

## API Reference

### Orchestration Operations

| Operation | Purpose | Flow |
|-----------|---------|-------|
| `delegate` | Alfred delegates to specialist | Alfred → specialist via sessions_spawn |
| `heartbeat` | Autonomous work cycle | All agents every 30 min |
| `handoff` | Return baton with summary | Specialist → Alfred via sessions_yield |
| `claim` | Take ownership of task | Specialist → Kanban |
| `review` | Quality gate before done | Debug/Security → Done |

### Example: Delegation

```markdown
# Alfred delegates to coder

**Goal:** Implement OAuth2 authentication

**Scope:** src/auth/, tests/auth/

**Acceptance Criteria:**
- Login/logout endpoints functional
- Token refresh mechanism
- All tests passing

**Constraints:**
- No DB schema changes
- Security audit before done
```

## Roadmap

### v1.1 (Next)
- [ ] Auto-discovery of specialist capabilities
- [ ] Dynamic task routing based on skills
- [ ] Metrics dashboard

### v1.2 (Future)
- [ ] Federated orchestration across clusters
- [ ] Multi-cloud deployment
- [ ] AI-powered task prioritization

## Documentation

- [Architecture](docs/architecture.md) - Delegation model, specialist matrix
- [Patterns](docs/patterns.md) - Reusable delegation, parallelization, PDCA
- [Contributing](CONTRIBUTING.md) - Development guidelines

## License
MIT License — see [LICENSE](LICENSE)
