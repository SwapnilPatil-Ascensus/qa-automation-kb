# Standard Story template (Jira-ready)

Copy into Jira **Description** (Markdown if enabled) or split across **Description** + **Acceptance Criteria** field.

---

## Summary line

```text
[Epic tag] Imperative outcome — scope boundary
Example: [V3-IDP] Stabilize IDP login suite — Stage 1 nightly green 5/5 runs
```

---

## Fields

| Jira field | Value |
|------------|--------|
| **Issue type** | Story |
| **Epic Link** | *(required)* |
| **Component** | Automation-V2 / Automation-V3 / Performance / Platform / Governance |
| **Labels** | `needs-estimate`, `offshore-friendly` *(optional)* |

---

## Description

### Context
[Link Epic. One paragraph: system, env, suite name.]

### Business context
[Why now: risk, release, offshore unblock, leadership ask.]

### Scope
- **In:** …
- **Out:** …

### Dependencies
- [ ] None
- [ ] [Team/system] — owner — needed by [date]

---

## Acceptance criteria (Gherkin)

```gherkin
Scenario: Happy path
  Given …
  When …
  Then …

Scenario: Failure / edge
  Given …
  When …
  Then …
```

---

## Subtasks (create in Jira)

Map each subtask to AC or execution lane.

| Subtask title | Type | Done when |
|---------------|------|-----------|
| Implement / update automation | Dev | Merged; CI green |
| Add / update test data & config | Dev | Documented in repo or secure store |
| Peer review | Dev | PR approved |
| Execute validation run (target env) | QA | Pass + evidence linked |
| Update regression suite / XML | QA | Nightly includes scenario |
| Update documentation / Confluence | Either | Link in Story comment |

---

## Definition of Done

- [ ] All acceptance scenarios pass in **target Stage** (name env).
- [ ] Code merged to **integration branch**; pipeline green.
- [ ] No open **Sev1/Sev2** defects on Story scope.
- [ ] **TestNG/JUnit** report or job link attached or linked in comment.
- [ ] **Pipeline** job updated if applicable (name job).
- [ ] **Documentation** updated (path or Confluence URL in comment).
- [ ] **qTest** cycle linked *(if in scope for Performance or mandated)*.

---

**Version:** 1.0
