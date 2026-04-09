# UEPIPE-07 — Spike: test data lifecycle and cleanup for pipeline UI tests

**Status:** Draft · **Suggested Story Points:** **5** · **Epic:** [QA-600](https://ascensuscollegesavings.atlassian.net/browse/QA-600)

**Issue type:** **Spike** (time-box; output = recommendation)

**Labels:** `automation`, `env-pipeline`, `spike`, `test-data`, `ENVP`

**Source:** Meeting 04-01 — Nick: data management/cleanup; “automation nor pipelines have this concept of cleanup right now.”

---

## Copy — Jira Summary

```
[ENVP][Spike] Test data + cleanup strategy for UI tests in automated pipelines
```

---

## Copy — Description

```markdown
## Problem
Pipeline UI tests (e.g. UE enrollments) may create **persistent data** in Stage 1. Without cleanup or idempotent data strategy, tests **collide**, **pollute**, or become **order-dependent**.

## Goal (spike)
Time-box (**2–3 days**) to produce:
- Current state: how UE (and similar) tests obtain data today
- Options: **per-run unique data**, **scheduled cleanup**, **DB reset** (if allowed), **API teardown**
- Risks and **non-goals** for Stage 1
- Recommendation + rough effort for a **follow-up Story**

## Stakeholders
QA automation, owning product QA, DBA/Infra if DB scope.

## Out of scope
Implementing full cleanup automation (separate Story after spike).
```

---

## Copy — Acceptance Criteria

```markdown
h3. Spike outputs

* ( ) Written summary (Confluence or Story comment) with **recommended approach**.
* ( ) List of **risks** (PII, shared env, flakiness).
* ( ) One **follow-up Story** drafted or created for implementation (if warranted).
```
