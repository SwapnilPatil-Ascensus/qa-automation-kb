# UEPIPE-05 — Confluence: ENVP test taxonomy — features, APIs, UI suites

**Status:** Draft · **Suggested Story Points:** **3** · **Epic:** [QA-600](https://ascensuscollegesavings.atlassian.net/browse/QA-600)

**Labels:** `automation`, `documentation`, `env-pipeline`, `ENVP`, `confluence`

---

## Copy — Jira Summary

```
[ENVP][Docs] Confluence — map Aha/MFE features to API vs UI tests and suite types
```

---

## Copy — Description

```markdown
## Context
[Aha ACS-5289](https://acscensus.aha.io/features/ACS-5289) requires **clarity of test intent**: suites must state whether they validate **UI (MFE)** vs **API/service** behavior. ENVP will onboard many MFEs/microservices; a single **mapping page** prevents ambiguity.

## Goal
Create a **Confluence space page** (or section under existing ENVP hub) with tables:

| Dimension | Example columns |
|-----------|-----------------|
| Product / feature | Aha link, owning team |
| Gate type | Unit, API, UI smoke, UI integration, nightly |
| Suite / job | Maven profile, GitLab job, TestNG/XML name |
| Duration budget | e.g. 3–5 min smoke, ≤10 min UE integration |
| Traunch/env | Stage1, etc. |

**Pilot row:** Universal Enrollment — `stage1-ue-integration-test`, `stage1-universal-enroll-integration.xml`, tags `@integration` `@intrun`.

## Dependencies
UEPIPE-01 (accurate job names) and UEPIPE-04 (naming and budgets).

## Links
- Epic: https://ascensuscollegesavings.atlassian.net/browse/QA-600  
- Aha: https://acscensus.aha.io/features/ACS-5289
```

---

## Copy — Acceptance Criteria

```markdown
h3. Must pass

* ( ) Confluence page published; URL in Story comment and linked from QA-600.
* ( ) UE row complete (suite name, profile, tags, approximate duration).
* ( ) Template reusable for next MFE (empty rows or “TBD” owners).
```
