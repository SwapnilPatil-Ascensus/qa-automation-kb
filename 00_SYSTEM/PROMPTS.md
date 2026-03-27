# Prompt Library

## Purpose

This document provides copy/paste-ready Cursor prompts for QA automation tasks. These are your "buttons" - use them directly in Cursor chat.

## How to Use

1. Copy the prompt you need
2. Paste into Cursor chat
3. Replace any `[PLACEHOLDER]` values with your specific information
4. Execute the prompt

**Regression KB extras:** **I)** refresh a V2/V3 module page from TestNG + PDF · **J)** sync parent/master indexes and the mermaid map after adding or renaming docs · TestNG export cleanup: `10_IMPORTS_RAW/AM_Regression_Reports/docs/GUIDE_TESTNG_REPORT_EXPORT_AND_CLEANUP.md`

**Step-by-step for repetitive tasks (bug report, leadership update):** See `05_ONBOARDING/HOW_TO_REPETITIVE_TASKS.md` for locations, templates, and plain-English steps.

---

## A) One-Time "Project Bootstrap" Prompt

**Use this in Cursor chat after opening the repo:**

```
You are the repo's documentation architect.

Task:
1) Read: 00_SYSTEM/ROLE.md, 00_SYSTEM/CONSTRAINTS.md
2) Create initial curated skeleton content for:
   - 01_CONTEXT/CURRENT_STATE.md
   - 03_ARCHITECTURE/OVERVIEW.md
   - 04_EXECUTION/DAILY_REGRESSION.md
   - 05_ONBOARDING/ONBOARDING_7_DAY.md
   - 06_TEMPLATES/LEADERSHIP_UPDATE_TEMPLATE.md
3) Keep each file concise and table-driven.
4) Insert placeholders where org-specific details are missing, tagged [NEED_INPUT].

Output: directly write the files in the repo.
```

---

## B) "Ingest Confluence Export → Curated Docs" Prompt

**After you drop exports into `10_IMPORTS_RAW/confluence_exports/`:**

```
Ingest task:
- Use ONLY the files under 10_IMPORTS_RAW/confluence_exports/.
- Extract and normalize content into the curated structure (03_ARCHITECTURE, 04_EXECUTION, 05_ONBOARDING, 07_GOVERNANCE_VISIBILITY).
- Do not copy raw text blindly. Rewrite into standardized format.

Rules:
- Any missing information becomes [NEED_INPUT].
- Any sensitive content becomes [REDACT_NEEDED].
- Update 00_SYSTEM/SOURCES.md with what was imported and mapped.

Start with onboarding and daily regression first.
```

---

## C) "Ingest Chats → Decisions + Worklog + Standards" Prompt

**After you paste chat exports/summaries into `10_IMPORTS_RAW/chats_exports/`:**

```
Ingest chats task:
- Read files under 10_IMPORTS_RAW/chats_exports/.
- Produce:
  1) 09_DECISIONS_WORKLOG/DECISIONS.md (bullet ADRs: Decision, Why, Options considered, Impact)
  2) 09_DECISIONS_WORKLOG/WORKLOG.md (dated bullets grouped by month)
  3) 02_STANDARDS/DOC_STANDARDS.md (rules implied by the chats)

Constraints:
- No names/PII unless already safe and required. Prefer roles over names.
- Keep it concise and auditable.
```

---

## D) "Gap Finder" Prompt (Find What's Missing)

**Run weekly:**

```
Gap analysis:
Scan curated docs (01-07 folders).
Create/refresh:
- 11_BACKLOG/DOC_GAPS.md with:
  - Missing pages
  - Missing sections within pages
  - Conflicts or outdated statements
  - Suggested owner (role) and priority (P0/P1/P2)

Output should be a table with: Area | Gap | Risk | Priority | Owner | Next action.
```

---

## E) "Confluence-Ready Page Generator" Prompt

**Use anytime:**

```
Create a Confluence-ready page for: [TOPIC]
Source: use only repository content.
Format:
- Purpose
- Scope
- Preconditions
- Step-by-step (table)
- Definition of Done
- Troubleshooting
- FAQs
- Links (repo paths)

Keep it short and execution-first.
```

---

## F) "Leadership Update" Prompt (1-Minute Status)

**Using repo facts only:**

```
Using repo facts only, generate a leadership update for: [WEEK/DATE].
Max 6 bullets:
- Progress
- Risks/blocks
- Decisions needed
- Next week focus
Also output a 1-line headline summary.
```

---

## F2) "Persistent Bi-Weekly Leadership Update" Prompt (Confluence + PSL)

**Use every alternate week when Persistent meets with the client. You provide a brief update; Cursor produces both deliverables.**

**Template to use:** `06_TEMPLATES/PERSISTENT_LEADERSHIP_UPDATE_TEMPLATE.md`  
**Reference example:** `10_IMPORTS_RAW/confluence_exports/Demand Planning Reports/14. QA Automation Program – Leadership Working Update (As of 02042026).md`

**Copy this prompt, then paste your brief update at the end:**

```
Persistent bi-weekly leadership update task.

I will give you a brief update on what has happened and what is happening with the QA Automation team. Produce two deliverables:

1. **Detailed Confluence page** – Full leadership working update using the structure in 06_TEMPLATES/PERSISTENT_LEADERSHIP_UPDATE_TEMPLATE.md (Part 1). Include: Executive Context, Prime V2, Prime V3, API & Performance, Cross-Team Support, Key Risk (if any), Leadership Discussion Points, Summary, One-Line Reference Snapshot. Use period dates [START] to [END] and "since last" date [LAST_SHARE_DATE].

2. **PSL page summary** – The "5. Automation Team" block for the main PSL page (MAIN - PSL - Persistent Updates), using the structure in the same template (Part 2). Include: Detailed Reference, One-Line Summary, Key Highlights (6 bullets with bold sub-headers), In Progress / Next Focus (4 bullets), Initiatives & Execution Highlights (5 bullets), Call-Out for Leadership. Match the format of the 02/04 example in the Demand Planning Reports folder.

Rules:
- Use ONLY the brief update I provide below; expand and categorize it into the right sections. Do not invent facts.
- Follow the template and reference example structure exactly. Be concise and leadership-ready.
- Save the Confluence page as: 10_IMPORTS_RAW/confluence_exports/Demand Planning Reports/[NEXT_NUMBER]. QA Automation Program – Leadership Working Update (As of [MMDDYYYY]).md
- Output the PSL block in the same file under a clear "PSL Page Summary" section for copy-paste.

Replace [START], [END], [LAST_SHARE_DATE], [MMDDYYYY], [NEXT_NUMBER] with the correct values for this update period.

---

[BRIEF UPDATE PASTE BELOW]
```

---

## G) "RCA from Evidence" Prompt

**Given evidence (logs/failed tests summary):**

```
RCA assistant:
Given this evidence (logs/failed tests summary pasted below), produce:
- Problem statement
- Likely causes (ranked)
- Validation steps
- Fix options (low-risk first)
- Prevent recurrence (standards + pipeline guards)
Then update 04_EXECUTION/RCA_PROCESS.md if a new pattern is discovered.

[PASTE EVIDENCE BELOW]
```

---

## H) "Bug Report: JIRA + Email + Teams" Prompt

**Use when:** A regression or test failure occurs and you need to log a bug and notify leads/dev. You have (or will put) failure artifacts in a date folder under `10_IMPORTS_RAW/regression_reports/[MMDDYYYY]/`.

**Templates to follow:**  
- Failure email: `10_IMPORTS_RAW/confluence_exports/Bug Handling/1. Handling Process When a Bug Is Found or Regression Fails (QA Automation).pdf`  
- Resolution email: `10_IMPORTS_RAW/confluence_exports/Bug Handling/1b. 🔁 Automation Bug Resolution Follow-Up Process & Resolution Notification.pdf`  
- Bug doc structure: existing bug docs in `10_IMPORTS_RAW/regression_reports/` (e.g. `02032026_UniversalEnrollment_BadSqlGrammarException.md`)

**Copy this prompt, then replace the placeholders and paste your details:**

```
Bug report task: create one markdown file that contains JIRA copy-paste content, failure email draft, and Teams message.

**Inputs (provide below):**
- Date (MMDDYYYY), e.g. 02032026
- Feature/area name (e.g. Universal Enrollment, IDP Login)
- Short summary of what failed and the main error (paste exact exception if available)
- TestNG or CI report URL (if any)
- Folder path where artifacts are saved, e.g. 10_IMPORTS_RAW/regression_reports/02032026/
- List of files in that folder (screenshots, exception .txt, test data, etc.)

**Output:**
1. Create ONE file in that folder, named: [MMDDYYYY]_[FeatureName]_[IssueType].md (e.g. 02032026_UniversalEnrollment_BadSqlGrammarException.md).
2. File must include:
   - Context/Background, Issue Summary, Steps to Reproduce, Error Message (exact), JIRA Bug link placeholder
   - **JIRA block (copy-paste ready):** Summary, Description, Steps, Expected/Actual, Environment, Priority/Severity, Attachments/Links, Test Data, Labels, Components
   - **Email draft (failure):** To: AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk. **Cc (always):** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>. Subject, body with Bug Summary (error, JIRA, report link, exception, screenshot, test data, env, priority), Change Set placeholder, CI/CD policy line. Concise.
   - **Teams message:** Short summary, links (JIRA, report, screenshot), priority/env, call-to-action
   - **Resolution section (placeholder):** Empty "Resolution Email Draft" for when the bug is fixed (use template from "1b. Automation Bug Resolution Follow-Up..." PDF). **Cc (same as failure, always):** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>
3. Follow the structure and tone of existing bug docs in 10_IMPORTS_RAW/regression_reports/ (e.g. 02032026 or 02022026). Be concise; no long paragraphs.
4. Naming: [MMDDYYYY]_[FeatureName]_[IssueType].md — e.g. 02032026_UniversalEnrollment_BadSqlGrammarException.md

---

**Date (MMDDYYYY):** [FILL]
**Feature/area:** [FILL]
**Summary of failure + main error:** [FILL or paste exception]
**Report URL:** [FILL]
**Artifacts folder path:** [FILL]
**Files in folder:** [FILL – list screenshots, .txt, etc.]
```

---

## I) "Regression suite module – Confluence page refresh" (V2 / V3)

**How to use (one line):** Fill in **V2 or V3**, **module name**, and the three paths below (latest TestNG HTML, suite XML, Confluence PDF), paste into Cursor chat, and ask it to update the matching file under `AM_Regression_Reports/docs/v2/modules/` or `docs/v3/modules/`.

**Template (section order & tables):** `10_IMPORTS_RAW/AM_Regression_Reports/docs/TEMPLATE_REGRESSION_MODULE_CONFLUENCE.md`  
**Format examples:** `10_IMPORTS_RAW/AM_Regression_Reports/docs/v2/modules/01-enrollment.md`, `docs/v3/modules/02-universal-enrollment-stage1.md`

**Copy-paste prompt (replace ALL caps placeholders):**

```
Regression suite module – Confluence page refresh.

Version & target folder: [V2 → docs/v2/modules/ | V3 → docs/v3/modules/]
Module to recreate: [e.g. enrollment | withdrawals | universal enrollment | idp login]
Output file: [e.g. 01-enrollment.md | 02-universal-enrollment-stage1.md] (full path under AM_Regression_Reports/docs/...)

Inputs (use repo paths or attach the HTML if not in repo):
- TestNG report used to create/update the doc: [PATH_OR_URL_TO_TESTNG_INDEX_HTML]
- TestNG runner suite (XML): [e.g. AM_Regression_Reports/suites/v2/daily/stage1-enrollments.xml]
- Refer existing PDF (Confluence export we are superseding / aligning to): [PATH_UNDER_10_IMPORTS_RAW/confluence_exports/...pdf]

Tasks:
1) Read TEMPLATE_REGRESSION_MODULE_CONFLUENCE.md and the current output file (if it exists) plus one sibling module in the same folder for tone.
2) Read the suite XML from the path above; list all active `<test>` blocks (note commented-out tests separately).
3) Read the TestNG HTML report: extract suite name, tests/methods counts, passed/failed/skipped, and any per-method detail needed for the “Latest report summary” and validation of counts.
4) Rewrite the output markdown to match the template sections: title block with module/XML/suite name/framework/env/pipeline; inputs table; suite at a glance; purpose; latest report summary; coverage summary; module & plan coverage table; test scenarios table; what’s covered; report & artifacts; notes.
5) Do NOT invent Jenkins job names, GitLab URLs, schedules, or durations—copy from existing docs in AM_Regression_Reports/docs/v2 or v3, or mark NEEDS_VALIDATION.
6) Keep tables Confluence-friendly (short cells, bullets where listed in examples).

Write/update the file in the repo at the Output file path.
```

**Optional – before step 3:** If the user saved HTML from a browser, remind them to follow `10_IMPORTS_RAW/AM_Regression_Reports/docs/GUIDE_TESTNG_REPORT_EXPORT_AND_CLEANUP.md` (remove duplicate downloads, `_files` policy, rename, move under `reports/v2` or `v3`).

---

## J) "Parent / master docs sync" (new or moved Markdown pages)

**How to use (one line):** After you add or rename any file under `AM_Regression_Reports/docs/` (or `reports/` README paths), paste this prompt and list what changed so every **parent** index and the **mermaid** map stay accurate.

**Copy-paste prompt:**

```
Parent / master documentation sync (AM_Regression_Reports).

What changed (list paths or describe):
- [e.g. Added docs/v3/modules/03-new-module-stage1.md]
- [e.g. Renamed reports/v3/*.html to new convention]
- [e.g. New CICD child page]

Tasks:
1) Update ALL relevant index/parent files so links and tables match the repo:
   - 10_IMPORTS_RAW/AM_Regression_Reports/docs/README.md (Start here table, children at a glance)
   - 10_IMPORTS_RAW/AM_Regression_Reports/docs/00-automation-regression-master-overview.md (section 1.1–1.14 and/or 2.0 tables; **Documentation map** mermaid — add/remove nodes and edges to reflect new pages)
   - 10_IMPORTS_RAW/AM_Regression_Reports/docs/v2/README.md and/or docs/v3/README.md (module tables if applicable)
   - 10_IMPORTS_RAW/AM_Regression_Reports/docs/v2/modules/README.md and/or docs/v3/modules/README.md
   - 10_IMPORTS_RAW/AM_Regression_Reports/README.md (folder tree / Quick Start if structure changed)
   - 10_IMPORTS_RAW/AM_Regression_Reports/docs/CICD/README.md and 01-master-… only if CI/CD pages changed
2) If a new module page was added, add a row to the master overview tables AND extend the mermaid **Documentation map** (same subgraph as existing: V2 modules or V3 children).
3) Do not invent files — if unsure, add NEEDS_VALIDATION in the master page footnote.
4) Keep wording concise; preserve existing tone and table format.

Apply edits directly in the repo.
```

---

## Additional Quick Prompts

### Test Development

#### Create Page Object
```
Create a Page Object class for [page name] following POM pattern.
Include:
- WebElement locators
- Action methods
- Verification methods
- Follow naming conventions from 02_STANDARDS/NAMING_CONVENTIONS.md
```

#### Create Test Scenario
```
Create a Cucumber test scenario for [feature/functionality].
Follow BDD best practices and use Gherkin syntax.
Include:
- Given/When/Then steps
- Test data considerations
- Expected validations
```

#### Create API Test
```
Create a REST Assured API test for [endpoint].
Include:
- Request setup
- Response validation
- Error handling
- Test data management
```

### Test Execution

#### Analyze Test Results
```
Analyze the test execution results and identify:
- Failed tests and root causes
- Flaky tests
- Performance issues
- Recommendations for fixes
```

#### Generate Execution Report
```
Generate a test execution report using 06_TEMPLATES/EXEC_REPORT_TEMPLATE.md.
Include:
- Execution summary
- Pass/fail statistics
- Failed test details
- Recommendations
```

### Debugging

#### Investigate Flaky Test
```
Investigate the flaky test [test name].
Follow the process in 04_EXECUTION/FLAKINESS_PLAYBOOK.md.
Identify:
- Root cause
- Fix recommendations
- Prevention strategies
```

## Best Practices

1. **Be specific**: Include context about what you're working on
2. **Reference standards**: Always mention relevant standards documents
3. **Request templates**: Ask for templates when creating new documents
4. **Maintain consistency**: Use established patterns and conventions
5. **Use placeholders**: Replace `[PLACEHOLDER]` values before executing

## Notes

- All prompts assume you're working within this repository context
- Prompts follow the non-negotiables from `00_SYSTEM/ROLE.md`
- Output should be execution-ready (Confluence/Jira/pipeline ready)
- Prefer tables/checklists over paragraphs
