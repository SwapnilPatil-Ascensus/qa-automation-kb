# UEPIPE-03 — Retry, flakes, and pipeline pass/fail policy for UI gates

**Status:** Draft · **Suggested Story Points:** **3** · **Epic:** [QA-600](https://ascensuscollegesavings.atlassian.net/browse/QA-600)

**Labels:** `automation`, `env-pipeline`, `process`, `ENVP`, `QA-Board-View`

**Relates to:** Meeting notes (04-01, 04-09) — Nick’s feedback that pipelines need explicit process for instability; UE Foreign Phone retry did not clear build failure.

---

## Copy — Jira Summary

```
[ENVP] Define UI test retry / flake handling for pipeline quality gates
```

---

## Copy — Description

```markdown
## Context
UI tests under parallel Selenium are **non-deterministic** at times. ENVP discussions require clarity: when a test **fails then passes on retry**, does the **build** pass? Who **overrides** a gate?

**Example:** UE integration run — scenario passed on runs 1 and 3 but failed on run 2; Maven still reported **BUILD FAILURE**.

## Goal
Agreed **written policy** (Confluence + Jira template) covering:
- Retry count and **whether intermediate failures fail the job**
- When a failure is **flake** vs **regression** (triage checklist)
- **Escalation / risk acceptance** path when blocking deploy
- Relationship to **Sonar/Fortify/unit** gates (ACS-5289 dependency ACS-I-2271)

## Deliverables
- 1–2 page runbook section: “UI gate failures”
- Optional: GitLab job configuration guidance (fail fast vs retry plugin vs manual promote)

## Owners
QA Lead + Tech Lead (per Rajib/Nick alignment meetings).
```

---

## Copy — Acceptance Criteria

```markdown
h3. Must pass

* ( ) Document published and linked from Epic **QA-600** or ENVP hub.
* ( ) Explicit answer: **Does retry clear red build?** (yes/no/conditional).
* ( ) Escalation path named (roles, SLA for override).
* ( ) Referenced from UE integration CI job description (UEPIPE-01).
```
