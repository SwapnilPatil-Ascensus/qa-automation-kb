# UEPIPE-04 — UI smoke vs integration: criteria, ownership, time budgets

**Status:** Draft · **Suggested Story Points:** **3** · **Epic:** [QA-600](https://ascensuscollegesavings.atlassian.net/browse/QA-600)

**Labels:** `automation`, `env-pipeline`, `process`, `smoke`, `ENVP`, `QA-Board-View`

**Source:** `docs/jira-governance/data/Env-Pipeline-Project/Meeting minutes 04-01 @1.30PM.txt`, `Meeting minutes 04-09 @2PM.txt`

---

## Copy — Jira Summary

```
[ENVP] Align QA/Tech leads — UI smoke criteria, API vs UI, 3–5 min vs integration suites
```

---

## Copy — Description

```markdown
## Context
Meetings captured open questions:
- What belongs in **UI smoke** vs **API**; is **one UI scenario per URN/schema** enough?
- **Ownership:** QA Lead + Tech Lead decide inclusion and risk (Rajib).
- **Time:** Rajib noted **3–5 minutes** for some UI execution expectations; Nick noted practical limit **~10–15 parallel UI tests** (up to **~30** only with ideal grid). **UE integration** workstream separately targets **≤10 minutes** for the packaged UE suite (UEPIPE-01).

## Goal
Exit meeting(s) with **written decisions**:
- Definition of **smoke** vs **integration** vs **nightly/full** for ENVP
- **Maximum duration** per gate type (smoke 3–5 min vs integration budgets per product)
- **Plan/traunch coverage** expectations and risk acceptance
- **Pass/fail** meaning for deploy confidence (ties to UEPIPE-03)

## Outcome artifact
Bullet list of **decisions + owners** attached to Epic QA-600; inputs for Confluence taxonomy (UEPIPE-05).
```

---

## Copy — Acceptance Criteria

```markdown
h3. Must pass

* ( ) Documented answers to: inclusion criteria, UI vs API, ownership, time thresholds per suite **type**.
* ( ) Explicit reconciliation: **smoke (3–5 min)** vs **UE integration (≤10 min)** — both allowed as different gates if agreed.
* ( ) QA Lead + Tech Lead acknowledgment (comment or sign-off link).
```
