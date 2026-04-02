# Jira Story Draft — V3 Member contributions (IDP-enabled plans)

> **Superseded for execution planning** by the split stories in [`../upcoming-stories/`](../upcoming-stories/) (`MEMCONTRIB-01` … `04`). Keep this file for a single-story rollup if PO prefers one ticket.

**Use:** Copy sections into Jira (Summary, Description, Acceptance Criteria custom field).  
**Aligns with:** `03-story-standards/jira-story-template.md`, `acceptance-criteria-template.md`, `backlog/stories.md` → **QA-S-V3-004** (narrower: **member** path only, **IDP-enabled** plans).  
**Data note:** `jira-export.csv` and backlog use labels such as `Contrib`, `Regression`, `QA-Board-View`; link this story to epic **QA-E-V3-TXN** when creating in Jira.

---

## Summary (Jira Summary field — ~80 chars)

`[V3][Contributions] Add member contribution automation for IDP-enabled plans`

---

## Description (paste into Jira Description)

```markdown
## Context
Prime V3 nightly regression covers Universal Enrollment, IDP login, and growing transaction areas. **Member contribution** flows for plans that use **IDP (member)** authentication are **under-covered** compared to legacy/V2-style paths. This gap increases release risk as more plans move to IDP.

**Relates to:** Backlog story **QA-S-V3-004** (V3 contribution flow automation post-IDP) — this story scopes explicitly to **member** + **IDP-enabled** traunches and lists concrete automation scenarios.

## User outcome
As a **QA automation engineer**, I want **automated member contribution scenarios on Stage 1 for IDP-enabled plans**, so that **nightly regression detects regressions before production** and **parity with legacy-covered plans improves**.

## Scope
**In:**
- **Member** portal contribution flows after **IDP** login (not legacy member login URL).
- **IDP-enabled** traunches agreed with SME (**minimum two** pilot plans in first slice; expand per second slice).
- Happy path + agreed **negative/validation** cases (see test case table).
- Cucumber/TestNG (or existing V3 pattern), POM/step defs, test data strategy documented in Story comments.
- Registration in **V3** contributions suite XML (e.g. `stage1-contributions` / master regression) when ready.

**Out:**
- CSR-only contribution flows (track under separate Story unless PO combines).
- Performance/load testing.
- Production execution; scope is **Stage 1** unless otherwise agreed.

## Dependencies
- [ ] SME — **IDP-enabled plan list**, funding rails in scope, assertion rules (DB/API) — owner: *[TBD]* — needed by: refinement
- [ ] Test data — accounts with contribution eligibility — owner: *[TBD]*
- [ ] No open **Sev1** IDP login blocker for in-scope plans (link bug if any)

## Links
- Design: *[Confluence / Figma if applicable]*
- Aha!/Confluence: *[Aha feature URL + ID if mapped]*
- KB: `10_IMPORTS_RAW/AM_Regression_Reports/docs/v3/` (V3 regression docs); `docs/jira-governance/backlog/stories.md` (QA-S-V3-004)

---
Source: *[Aha feature name]* — *[URL]*  
Aha ID: *[id or N/A]*
```

---

## Suggested Jira fields

| Field | Suggested value |
|-------|-----------------|
| **Issue type** | Story |
| **Epic link** | QA-E-V3-TXN (or program epic for V3 transactions) |
| **Component** | Prime V3 / Contributions / Automation (use project components) |
| **Labels** | `automation`, `prime-v3`, `contributions`, `idp`, `member`, `stage1`, `intake-2026-04` |
| **Team** | AMSquad (per `jira-export.csv` pattern) |

---

## Automation test cases (backlog for implementation)

*Finalize plan codes (traunch) with SME; below is a typical slice.*

| ID | Theme | Scenario (short) | Type | Notes |
|----|--------|------------------|------|--------|
| MC-IDP-01 | Happy path | Member logs in via **IDP**, navigates to contribution, completes **one-time** contribution (e.g. bank), reaches confirmation | Positive | Assert UI + agreed DB/API checks |
| MC-IDP-02 | Happy path | Same as MC-IDP-01 on **second** IDP-enabled traunch (different plan rules if any) | Positive | Proves plan-agnostic pattern |
| MC-IDP-03 | Funding rail | Contribution using **payroll** (or second rail in scope per SME) | Positive | Only if supported for IDP member on Stage 1 |
| MC-IDP-04 | Validation | Amount **below minimum** / invalid entry → expected inline error, **no** submit | Negative | |
| MC-IDP-05 | Validation | Exceeds **daily/limit** rule (if test data supports) → expected block message | Negative | Optional slice 2 |
| MC-IDP-06 | Session | Contribution after IDP login; **session** still valid through submit | Positive | |
| MC-IDP-07 | Regression tag | All in-scope scenarios tagged for **nightly** (`@regression` / `@dailyrun` per project standard) | N/A | |

*Add rows for plan-specific rules (state limits, holding period, etc.) per SME matrix.*

---

## Acceptance criteria

### A) Checklist (Jira AC field or Description)

- [ ] At least **two** IDP-enabled traunches have **passing** automated member contribution scenarios on **Stage 1** (SME-confirmed list in Story comment).
- [ ] **Happy path** contribution completes with **expected confirmation** and **assertions** (DB/API per SME sheet) **green**.
- [ ] At least **one negative** scenario (invalid amount or disallowed action) shows **expected validation** and **no partial commit** (per assertion rules).
- [ ] Scenarios merged to integration branch; **CI** green for the contributions module job.
- [ ] Scenarios added to the **agreed V3 suite XML** and appear in **nightly** (or scheduled) run; **TestNG** report linked in Story comment.
- [ ] **qTest** (or team test mgmt) mapping updated for new methods, if required by process.
- [ ] **No** dependency on legacy member-only login URL for in-scope cases (IDP entry only).

### B) Gherkin (optional second AC block)

```gherkin
Scenario: Member one-time contribution after IDP login
  Given a member account on an IDP-enabled plan with contribution eligibility
  And the member authenticates via IDP on Stage 1
  When the member completes a one-time contribution per approved test data
  Then the contribution completes with expected confirmation
  And post-conditions match SME database or API assertions

Scenario: Invalid contribution rejected
  Given a member authenticated via IDP on an IDP-enabled plan
  When the member enters contribution data that violates validation rules
  Then the application shows the expected validation message
  And no unintended transaction state is committed per assertions
```

---

## Sub-tasks (create in Jira)

| Summary | Done when |
|---------|-----------|
| Confirm IDP-enabled plan list & rails with SME | List + assertion rules pasted in Story comment |
| Implement MC-IDP-01 … MC-IDP-04 (adjust IDs) | MR merged; code review passed |
| Wire tests into V3 contributions suite XML | Nightly picks up new tests |
| Stage 1 validation run | TestNG link + pass/fail in comment |
| qTest / traceability | Updated if process requires |

---

## Definition of Done

- [ ] Meets all **Acceptance criteria** checkboxes above.  
- [ ] **Definition of Ready** satisfied at refinement (see `03-story-standards/definition-of-ready.md` if used).  
- [ ] SME sign-off or linked approval comment.  
- [ ] Related duplicate avoided: clarify vs **QA-S-V3-004** / **QA-522**-family (CSR/member investment) in Jira **linked issues** if overlap.

---

## Import / CSV hygiene (`docs/jira-governance/data`)

After creating the issue in Jira, export issues to `jira-export.csv` and merge into `docs/jira-governance/backlog/stories.md` per `data/README.md`.

**Version:** 1.0 · **Draft date:** 2026-04-02
