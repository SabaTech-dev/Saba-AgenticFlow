# Saba-AgenticFlow Patterns

This document describes reusable patterns for multi-agent orchestration.

## Pattern 1: Delegation with Explicit Scope

**Use Case:** Alfred delegates task to specialist

**Flow:**
1. Alfred creates task in Kanban with:
   - Goal
   - Scope (files, areas affected)
   - Acceptance criteria
   - Constraints
   - Deadline

2. Specialist claims task (heartbeat)

3. Specialist executes bounded work

4. Specialist yields back with:
   - Executive summary (1-3 lines)
   - Files changed
   - Tests run
   - Risks

**Example:**
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

---

## Pattern 2: Autonomy via Heartbeat

**Use Case:** Specialists work autonomously

**Flow:**
Every 30 min:

1. Check Kanban for tasks assigned to me
2. If available:
   - Claim task
   - Execute bounded work
   - Handoff on completion
3. If not available:
   - Continue previous work
   - Report progress

**Key Principle:** No manual intervention required for task claiming and execution.

---

## Pattern 3: Parallel Workflows (OpenProse)

**Use Case:** Alfred needs parallel work from multiple specialists

**Flow:**
1. Alfred spawns parallel specialists via OpenProse
2. Each specialist runs bounded task
3. Results aggregated by coordinator
4. Flow continues with combined results

**Example:** Investigation that needs:
- Coder: Check code
- Debug: Diagnose issue
- Research: Explore alternatives

**Result:** All three specialists run in parallel, Alfred aggregates findings.

---

## Pattern 4: PDCA Continuous Improvement

**Use Case:** Improving processes based on feedback

**Flow:**
1. **Plan:** Create design and implementation plan
2. **Do:** Implement with TDD (RED-GREEN-REFACTOR)
3. **Check:** Review and validate (debug/security)
4. **Act:** Improve based on feedback

**Key Principle:** Every improvement is small, reversible, and measurable.

---

## Pattern 5: Quality Gates

**Use Case:** Ensuring quality before task completion

**Gate Conditions by Specialist:**

| Specialist | Gate Condition |
|------------|---------------|
| Coder | All tests passing, code reviewed |
| Debug | Findings documented, recommendations clear |
| Security | Audit complete, risks identified |
| Research | Investigation thorough, next steps defined |
| QA-Tester | Tests executed, results reported |

**Enforcement:** Debug and Security agents must approve before task moves to done.

---

## See Also

- [Architecture](architecture.md) - Delegation model and primitives
- [README.md](../README.md) - Quick start
