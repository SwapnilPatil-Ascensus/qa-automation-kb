# Daily Workflows

Step-by-step for tasks the user runs **day to day**. For copy-paste prompts, see [04-PROMPT-LIBRARY-QUICK-REF.md](04-PROMPT-LIBRARY-QUICK-REF.md).

---

## Workflow 1: Morning regression review + bug report

**Trigger:** Nightly Jenkins/GitLab run has failures needing dev attention.

### Steps

1. **Check external CI** (Jenkins for V2, GitLab for V3) — not in this repo
2. **Create evidence folder:** `10_IMPORTS_RAW/regression_reports/MMDDYYYY/`
3. **Drop artifacts:**
   - Screenshots (`.png`)
   - Exception logs (`*.txt`, `*exception*`)
   - Test case info (`*testcase_information.txt`)
   - TestNG/CI report URL (paste in doc later)
4. **Run Prompt H** from `00_SYSTEM/PROMPTS.md`
   - Fill: date, feature, error, report URL, folder path, file list
5. **Output:** `[MMDDYYYY]_[Feature]_[IssueType].md` in same folder containing:
   - JIRA copy-paste block
   - Failure email draft (To/Cc from prompt)
   - Teams message
   - Empty resolution section
6. **Execute:**
   - Create JIRA ticket → paste JIRA block → attach screenshots
   - Send email with JIRA link
   - Post Teams message with JIRA link
7. **When fixed:** Fill resolution email in same `.md`; update JIRA status line

**Reference examples:** `10_IMPORTS_RAW/regression_reports/02032026/`, `02112026/`

**Process doc:** `10_IMPORTS_RAW/regression_reports/BUG_REPORTING_PROCESS.md`

---

## Workflow 2: Bi-weekly Persistent leadership update

**Trigger:** Alternate week before Persistent client PSL meeting.

### Steps

1. **Gather brief bullets** (2 weeks of work):
   - V2 progress, V3 progress, API/perf, platform support
   - In progress / next focus
   - Risks or leadership asks
2. **Open Prompt F2** in `00_SYSTEM/PROMPTS.md`
3. **Set placeholders:**
   - `[START]`, `[END]` — 2-week period
   - `[LAST_SHARE_DATE]` — previous share-out
   - `[MMDDYYYY]` — this update date
   - `[NEXT_NUMBER]` — next report number (e.g. 17)
4. **Paste bullets** at `[BRIEF UPDATE PASTE BELOW]`
5. **Run prompt**
6. **Output file:** `10_IMPORTS_RAW/confluence_exports/Demand Planning Reports/[N]. QA Automation Program – Leadership Working Update (As of MMDDYYYY).md`
7. **Publish:**
   - Part 1 → Confluence detailed page
   - Part 2 "PSL Page Summary" → paste into MAIN - PSL - Persistent Updates

**Template:** `06_TEMPLATES/PERSISTENT_LEADERSHIP_UPDATE_TEMPLATE.md`  
**Example:** `Demand Planning Reports/14. QA Automation Program – Leadership Working Update (As of 02042026).md`

---

## Workflow 3: Refresh regression module documentation

**Trigger:** Suite changed, new TestNG report downloaded, or Confluence page needs update.

### Steps

1. **Download TestNG HTML** from Jenkins/GitLab
2. **Clean/rename** per `AM_Regression_Reports/docs/GUIDE_TESTNG_REPORT_EXPORT_AND_CLEANUP.md`
3. **Identify:**
   - Version: V2 or V3
   - Module: e.g. enrollment, withdrawals, idp login
   - Suite XML path: e.g. `AM_Regression_Reports/suites/v2/daily/stage1-enrollments.xml`
   - Output file: e.g. `docs/v2/modules/01-enrollment.md`
4. **Run Prompt I** from `PROMPTS.md`
5. **Verify:** Template sections match `TEMPLATE_REGRESSION_MODULE_CONFLUENCE.md`
6. **Run Prompt J** to sync parent indexes and mermaid map

---

## Workflow 4: Regression evidence pipeline (Pipeline 1)

**Trigger:** Need structured area docs in `04_EXECUTION/regression/` (separate from bug reporting).

### Steps

1. Place in `10_IMPORTS_RAW/regression_reports/YYYY-MM-DD/`:
   - `test-engine.pdf`
   - `failures.csv`
   - Area screenshots (`enrollment.png`, etc.)
2. Copy fixed prompt from `04_EXECUTION/regression/PIPELINE_PROMPT.md`
3. Run with date — **no improvisation**
4. Check outputs: `summary.md`, `enrollment.md`, `withdrawals.md`, `login_idp.md`

**Note:** This is a different pipeline from Prompt H (bug docs).

---

## Workflow 5: Sprint / Jira work

**Trigger:** Sprint planning, refinement, story writing.

### Steps

1. **DoR gate:** `docs/jira-governance/03-story-standards/definition-of-ready.md`
2. **Story format:** `jira-story-template.md`, `acceptance-criteria-template.md`
3. **Pull drafts:** `docs/jira-governance/upcoming-stories/` (MEMCONTRIB, UEPIPE, Sprint_26.05, etc.)
4. **Backlog seed:** `docs/jira-governance/backlog/epics.md` + `stories.md`
5. **DoD gate:** `definition-of-done.md` before closing stories
6. **Log decisions:** `09_DECISIONS_WORKLOG/DECISIONS.md`

---

## Workflow 6: Mobile MSC migration program

**Trigger:** Weekly mobile program work.

### Steps

1. Update trackers: `05-unite-enrollment-migration-tracker.md`, `06-unite-mobile1-…`, `07-unite-mobile2-…`
2. Refresh `status-summary.md` and `action-items.md`
3. Use Jira import: `jira-stories/06-story-import-table.csv`
4. Regeneration notes: `11-technical-reference-and-cursor-execution-notes.md`

---

## Workflow 7: Troubleshooting

| Issue type | Go to |
|------------|-------|
| Stage DB / schema (`$$QA_SCHEMA$$`) | `10_IMPORTS_RAW/AM Troubleshooting Guide/guides/QA_FIN_TXN_user_schema/` |
| SQL via PuTTY on staging | `…/sql_staging_putty/` |
| IDP test account reset | `docs/DB Refresh/SQL Files/` |
| Flaky tests | `04_EXECUTION/FLAKINESS_PLAYBOOK.md` |
| Triage classification | `04_EXECUTION/TRIAGE_RULES.md` |

---

## Workflow 8: Weekly hygiene

| Task | How |
|------|-----|
| Gap analysis | Prompt **D** → update `11_BACKLOG/DOC_GAPS.md` |
| Current state | Refresh `01_CONTEXT/CURRENT_STATE.md` |
| Work log | Update `09_DECISIONS_WORKLOG/WORKLOG.md` |
| Import tracking | Update `00_SYSTEM/SOURCES.md` after new imports |

---

## Decision tree: which workflow?

```
Failure from nightly run?
├── Need JIRA + email + Teams?     → Workflow 1 (Prompt H)
├── Need area rollup docs?           → Workflow 4 (Pipeline 1)
└── Need module Confluence refresh?  → Workflow 3 (Prompt I + J)

Client meeting this week?
└── Persistent bi-weekly?            → Workflow 2 (Prompt F2)

Sprint ceremony?
└──                                    → Workflow 5

Mobile MSC work?
└──                                    → Workflow 6
```
