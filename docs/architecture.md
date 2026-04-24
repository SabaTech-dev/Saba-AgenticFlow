# Saba-AgenticFlow Architecture

## Overview

Saba-AgenticFlow implements a hierarchical multi-agent orchestration system with Alfred (CEO) + 5 specialists, supported by orchestration primitives for autonomous operation.

## Delegation Model

### Alfred (CEO Agent)

**Role:** Decision maker and delegator

**Responsibilities:**
- Create tasks in Kanban with explicit scope
- Delegate to specialists with acceptance criteria
- Review results and close tasks
- Coordinate parallel workflows via OpenProse

**Key Files:**
- `WORKING-CONVENTIONS.md` - Shared conventions
- `DELEGATION-PROTOCOL.md` - Handoff protocol

### 5 Specialists

**Role:** Bounded ownership of specialist domains

| Specialist | Domain | Superpowers |
|------------|---------|-------------|
| **Coder** | Implementation | brainstorming → plans → TDD |
| **Debug** | Diagnostics | Investigate, diagnose, recommend |
| **Security** | Audits | Review, validate, approve/reject |
| **Research** | Investigation | Explore, experiment, report findings |
| **QA-Tester** | Validation | Test, verify, report results |

## Orchestration Primitives

| Primitive | Description | Trigger |
|-----------|-------------|----------|
| **Kanban** | Task tracking with quality gates (backlog → in_progress → review → done) | Alfred creates tasks, specialists process |
| **Heartbeat** | Autonomous 30-min work cycles | All agents run every 30 min |
| **OpenProse** | Multi-agent parallel workflows | Alfred spawns parallel specialists |
| **sessions_spawn** | Bounded subtasks with context | Specialist spawns helper subagent |
| **sessions_yield** | Pass baton back to owner with summary | Specialist returns to Alfred |

## Delegation Matrix

| Alfred → | Purpose | Handoff → |
|------------|---------|-------------|
| Coder | Implementation tasks | Code ready for review |
| Debug | Diagnostic tasks | Findings + recommendations |
| Security | Security audits | Audit results + approval/rejection |
| Research | Investigation tasks | Findings + next steps |
| QA-Tester | Testing tasks | Test results + pass/fail |

## Autonomy Model

Every specialist runs **heartbeat** every 30 min:

1. **Check Kanban** for tasks assigned to me
2. **If available:**
   - Claim task
   - Execute bounded work
   - Handoff on completion
3. **If not available:**
   - Continue previous work
   - Report progress if applicable

## Quality Gates

Before marking task as **review**:

1. Coder: All tests passing, code reviewed
2. Debug: Findings documented, recommendations clear
3. Security: Audit complete, risks identified
4. Research: Investigation thorough, next steps defined
5. QA-Tester: Tests executed, results reported

## See Also

- [README.md](../README.md) - Quick start and API reference
- [Patterns](patterns.md) - Reusable patterns
