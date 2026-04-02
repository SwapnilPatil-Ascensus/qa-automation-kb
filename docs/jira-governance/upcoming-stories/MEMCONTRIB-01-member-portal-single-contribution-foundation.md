# MEMCONTRIB-01 — Member portal: single contribution foundation (CSR parity)

**Status:** Draft · **Suggested Story Points:** **8** · **Epic:** `QA-E-V3-TXN` (confirm)

**Labels:** `automation`, `prime-v3`, `contributions`, `member-portal`, `idp`, `stage1`, `QA-Board-View`, `Contrib`, `intake-upcoming`

**Blocks / relates to:** CSR baseline `docs/jira-governance/data/MemberSingleContribution.feature` + `stage1-contributions.xml` (NYD/NYA/NYB examples).

---

## Copy — Jira Summary

```
[V3][Contributions] Member portal — single contribution automation (IDP member login)
```

---

## Copy — Description

```markdown
## Context
`stage1-contributions.xml` today runs **CSR** flows: CSR login → pull account → **jump to member** → complete **member** contribution *as CSR*. We need the **same business scenarios** executed from the **member portal** using **member credentials** and **IDP (or approved member) login** — *without* CSR impersonation — so nightly regression covers the path real members use.

**Baseline reference (CSR):** `MemberSingleContribution.feature` — Background uses `login` for `csr`; Examples include EBT existing bank, new bank, multiple beneficiaries, 3 funds, etc.

## User outcome
As **QA**, I want **automated member-portal single contributions** on Stage 1 for an agreed **pilot traunch**, so that **IDP-enabled member contribution** is regression-protected like the CSR suite.

## Scope — In
- New feature (or refactored flows) under **member/front office** path (not `frontoffice/csr/...`), e.g. `MemberSingleContributionMemberPortal.feature` — exact path per repo conventions.
- **Background:** `starting "login" URL for "member"` (or project-standard **IDP member** login step), load test cases, browser, DB, creator email.
- **Scenario outline** parity with CSR **Examples** for **slice 1** (minimum):
  - EBT - Existing Bank  
  - EBT w/ New Bank - Savings  
  - EBT - Multiple Beneficiaries  
- Step definitions / POM: **member navigates to contribution** and completes flow; **no** “jump to member account” CSR steps.
- Assertions: reuse or mirror CSR validation rules (`log and validate member contribution`) adapted for **member session** (SME confirms).

## Scope — Out
- Additional traunches beyond **one pilot** (Story 02).  
- AIP / recurring / negative feature files (Story 02).  
- Pipeline wiring (Story 03).

## Dependencies
- SME: pilot **traunch** (e.g. NYD), test users, bank/contribution rules, assertion expectations.  
- Stable **IDP member login** on Stage 1 for that traunch (no open Sev1 login blocker).

## Links
- CSR feature (KB copy): `docs/jira-governance/data/MemberSingleContribution.feature`  
- CSR suite: `docs/jira-governance/data/stage1-contributions.xml`
```

---

## Copy — Acceptance Criteria (paste into AC field or Description)

```markdown
h3. Must pass (checklist)

* ( ) New member-portal feature file exists on agreed path; **no CSR login** in Background for these scenarios.
* ( ) **IDP/member login** succeeds on Stage 1 for the **pilot traunch** using secured test credentials.
* ( ) **Three** scenario rows run green: *EBT - Existing Bank*, *EBT w/ New Bank - Savings*, *EBT - Multiple Beneficiaries* (same business intent as CSR Examples).
* ( ) Post-contribution **validation** passes per SME rules (DB/API/UI — same bar as CSR automation where applicable).
* ( ) Tags include `@regression` and `@dailyrun` (or team standard for nightly).
* ( ) MR merged; **local or MR pipeline** green for the module that owns the feature.
* ( ) SME or PO comment with **pilot traunch** name and **sign-off** on assertion scope.

h3. Gherkin (summary)

{code:gherkin}
Scenario Outline: Member portal single contribution - <test case name>
  Given member starts login for the member portal on Stage 1
  And test cases are loaded for <test case name>
  When the member completes a single contribution for <test case name>
  Then the contribution outcome is validated per automation rules

  Examples:
    | test case name               |
    | EBT - Existing Bank          |
    | EBT w/ New Bank - Savings    |
    | EBT - Multiple Beneficiaries |
{code}
```

---

## Copy — Definition of Done (comment or checklist)

```markdown
* Code review approved; no new critical Sonar/issues.
* Pilot traunch documented in Story comment.
* Follow-up Story 02 linked for multi-plan + AIP/negatives.
```

---

## Notes for implementers

- Reuse **test case JSON/DB** shape from CSR flows where possible; only **navigation and login** layers change.  
- If “member” uses **IDP**, align with existing IDP step defs from `unite-universal-enrollment` / IDP login modules.
