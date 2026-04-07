# Story QA-494 — Copy-paste pack (Description, AC, Sub-tasks)

**Jira:** [QA-494](https://ascensuscollegesavings.atlassian.net/browse/QA-494)  
**Title:** Transfer – UI Automation Regression Execution & Stabilization (CSR + Member)  
**Parent Epic:** [QA-493](https://ascensuscollegesavings.atlassian.net/browse/QA-493) — *Transfer Feature – End-to-End UI automation test case tuning and execution*  
**Export ref:** `docs/jira-governance/data/jira-export.csv` (Story `QA-494`, Parent `QA-493`)

| Field (from Jira / export) | Value |
|----------------------------|--------|
| **Issue type** | Story |
| **Project** | QA — QA Automation |
| **Story points** | 5 |
| **Priority** | Low |
| **Labels** | `QA-Board-View`, `Regression` |
| **AGS Scrum Team** | QA Automation |
| **Team** | Automation Squad |
| **Fix version** | Master Backlog (confirm if sprint-specific) |

---

## 1. Description (paste into Jira *Description*)

Use **Wiki markup** or **Markdown** per your Jira project settings. Below is plain structure you can paste as-is or convert.

```text
h2. Purpose
Deliver reliable *execution* and *stabilization* of UI automation for *Transfer* flows in both *CSR* and *Member* contexts, aligned with the Transfer epic (QA-493). Reduce noise from flaky or environment-driven failures so daily regression signal is trustworthy.

h2. Scope
* *In:*
** Execute Transfer-related UI regression for *CSR* and *Member* on agreed environment(s) (e.g. Stage 1).
** Triage failures: *product defect* vs *automation* vs *data* vs *environment* vs *intermittent/flaky*.
** Address stabilization: test fixes, waits/locators, data hygiene, or documented quarantine with PO/Tech Lead approval where appropriate.
** Correlate results with *qTest* (Test Cycle / Test Run IDs) and *Unite* daily report output where the team standard requires it.
* *Out:*
** New Transfer *product* features (belongs in separate Stories).
** Performance/load testing (separate Story/Epic unless explicitly in scope).

h2. Context
Parent epic QA-493 covers end-to-end UI automation tuning and execution for Transfer. This Story focuses on *running* those suites consistently, *stabilizing* flaky cases, and *closing the loop* with evidence (reports, qTest, brief summary in comments).

h2. Evidence & links (fill as you execute)
* Unite regression reports (folder per run day): http://seleniumhubnt2:8081/reports/unite/?C=M;O=D
* qTest: PRIME / frontoffice *csr* (and member) cycles — map Transfer test cases to CL-*/TR-* from daily PDFs.
* Confluence: Link *Product requirements* when available (field on Story).

h2. Dependencies
* Stable Stage 1 (or target env) for Transfer CSR + Member.
* Test data and accounts for Transfer scenarios — owner: [NEED_INPUT].
* Any suite XML / job names for Prime V2 Transfer modules — document in first sub-task.

h2. Definition of Done (summary)
See *Acceptance Criteria* below; all AC satisfied, sub-tasks closed or moved to follow-up with explicit parent comment.
```

---

## 2. Acceptance Criteria (paste into *Acceptance Criteria* field or Description)

Checklist form (testable):

```markdown
- [ ] **Coverage identified:** Documented list of *CSR Transfer* and *Member Transfer* automated scenarios (or suite XML / feature paths) in a Story comment or linked doc; mapped to qTest cycle(s) where applicable.
- [ ] **CSR execution:** At least one *full* scheduled (or agreed) regression run for CSR Transfer paths completed; link to Unite report folder for that date + TestNG/Surefire link if applicable.
- [ ] **Member execution:** At least one *full* scheduled (or agreed) regression run for Member Transfer paths completed; same evidence pattern as CSR.
- [ ] **Failure triage log:** For each failure in scope, Story comment (or table) records: date, test name, TR-/CL- id if available, category (Defect / Flaky / Data / Env / Unknown), and owner for follow-up.
- [ ] **Stabilization applied:** Known flaky or brittle cases either *fixed* (merged) or *explicitly quarantined* with approval note (PO/Tech Lead) — no silent ignores.
- [ ] **Post-stabilization check:** Re-run of affected Transfer CSR + Member subset (or full suite per team norm) shows *no unresolved* P1/P2 failures attributable to automation stability for Transfer.
- [ ] **Stakeholder visibility:** Short summary comment on QA-494: pass rate trend, open defects (Jira keys), and link to latest Unite day folder.
```

Optional Gherkin-style supplement (if your Jira uses it):

```gherkin
Scenario: Regression signal is trustworthy for Transfer
  Given CSR and Member Transfer UI suites are defined and linked to qTest
  When daily (or scheduled) regression runs complete
  Then failures are triaged and documented with category and evidence
  And stabilization fixes or approved quarantine are in place
  And a verification run confirms no critical automation noise remains for Transfer
```

---

## 3. Sub-tasks (create under QA-494 in Jira)

Create **Issue type: Sub-task** with **Parent = QA-494**. Use the summaries below; adjust assignee in Jira (export shows **Sunil Godiyal** on Story).

| # | Sub-task Summary | Done when (description snippet for Jira) |
|---|------------------|------------------------------------------|
| 1 | **Transfer automation — inventory & qTest mapping** | Table or comment: CSR + Member Transfer features/suites, job or XML name, env, qTest cycle IDs; gaps flagged as NEED_INPUT. |
| 2 | **CSR Transfer — regression run & evidence** | Run complete; Unite date-folder URL + screenshot or pass/fail counts in comment; list failed TR-/test names. |
| 3 | **Member Transfer — regression run & evidence** | Same as sub-task 2 for Member path. |
| 4 | **Failure triage — Transfer (CSR + Member)** | Each failure categorized (Defect / Flaky / Data / Env); defects logged as Bugs and linked; flaky list references Unite/qTest pattern. |
| 5 | **Stabilization — implement fixes & verification** | PRs merged or quarantine approved; re-run shows targeted scenarios green or defects owned; Story comment with before/after. |

**Optional 6th sub-task** (if 5 points feel tight — split 5 or carry to next sprint):

| 6 | **Confluence / requirements link** | *Product requirements* field populated; short “how to run Transfer regression” note linked for onboarding. |

### Copy-paste blocks for each Sub-task (minimal)

**Sub-task 1 — Summary:** `Transfer — inventory & qTest mapping (CSR + Member)`  
**Description:** Complete mapping of Transfer UI tests (CSR + Member) to suite XML, Jenkins/GitLab job if any, Stage 1 URLs, and qTest CL-/cycles. Post as comment on QA-494.

**Sub-task 2 — Summary:** `CSR Transfer — regression execution + report links`  
**Description:** Execute full CSR Transfer regression per team schedule; attach/link Unite report for run date; list failures with TR- ids.

**Sub-task 3 — Summary:** `Member Transfer — regression execution + report links`  
**Description:** Same as CSR for Member Transfer flows.

**Sub-task 4 — Summary:** `Transfer failures — triage and defect linkage`  
**Description:** Categorize each failure; create/link Bugs; document flaky candidates for stabilization.

**Sub-task 5 — Summary:** `Transfer — stabilization fixes + verification run`  
**Description:** Implement automation/data fixes or approved quarantine; re-run; update QA-494 with verification evidence.

---

## 4. Suggested Story comment (after first run)

```text
Regression execution kickoff — QA-494
* CSR run: [date] — [Unite folder link]
* Member run: [date] — [Unite folder link]
* Open failures: [count] — triage in sub-task 4
```

---

## 5. Link to flaky / concurrent-failure spike (optional)

If the team is running the Unite flaky analysis spike in parallel, link or mention:  
`docs/jira-governance/upcoming-stories/SPIKE-Prime-V2-Flaky-Regression-Unite-Reports.md` (internal); in Jira, reference only **seleniumhubnt2** URL and spike Jira key when created.

---

**Version:** 1.0  
**Last updated:** 2026-04-07
