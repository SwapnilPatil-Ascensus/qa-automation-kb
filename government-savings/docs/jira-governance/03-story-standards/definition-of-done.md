# Definition of Done (DoD)

**Governance:** No Story moves to **Done** unless **all** applicable items are satisfied.

## 1. DoD checklist (delivery Story)

| # | Criterion | WHO verifies | WHEN |
|---|-----------|--------------|------|
| O1 | All **acceptance criteria** met | PO or delegate | Before Done |
| O2 | **Code** merged to agreed branch; **CI** green | Author | Before Done |
| O3 | **Unit/integration** tests added/updated as agreed | Author + Tech Lead | Before Done |
| O4 | **Automation** updated if in scope (or explicit “N/A” with PO sign-off) | QA / Author | Before Done |
| O5 | **Peer review** completed (PR approved) | Reviewer | Before Done |
| O6 | **Docs/runbooks** updated if behavior changed | Author | Before Done |
| O7 | **Feature flag** / config documented if applicable | Author | Before Done |
| O8 | No **open Sev1/2** bugs on Story scope | QA | Before Done |

## 2. Bug DoD

| # | Criterion |
|---|-----------|
| B1 | Root cause noted in comment or linked doc |
| B2 | Fix + test (automated preferred) |
| B3 | Verified in target env by QA or author per policy |

## 3. Task / chore DoD

| # | Criterion |
|---|-----------|
| T1 | Stated outcome achieved |
| T2 | Stakeholder informed if cross-team |

## 4. Waivers

| Waiver | Requires |
|--------|----------|
| Skip O4 automation | PO + QA comment on ticket |
| Hotfix | Post-incident backlog item for tests/docs |

## 5. Jira transition

| Action | WHO |
|--------|-----|
| Move to **Done** only after checklist | Assignee |
| SM audits random sample weekly | Scrum Master |

**Version:** 1.0
