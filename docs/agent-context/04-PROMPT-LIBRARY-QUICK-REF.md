# Prompt Library Quick Reference

All prompts live in **`00_SYSTEM/PROMPTS.md`**. Copy the full block, replace placeholders, run in Cursor.

---

## Master table

| ID | Name | Use when | Output location |
|----|------|----------|-----------------|
| **A** | Project bootstrap | One-time repo skeleton setup | `01_CONTEXT/`, `03_ARCHITECTURE/`, etc. |
| **B** | Ingest Confluence export | PDFs dropped in `confluence_exports/` | Curated folders + `SOURCES.md` |
| **C** | Ingest chats | Chat exports in `chats_exports/` | `DECISIONS.md`, `WORKLOG.md`, `DOC_STANDARDS.md` |
| **D** | Gap finder | Weekly doc hygiene | `11_BACKLOG/DOC_GAPS.md` |
| **E** | Confluence page generator | Any topic from repo content | New Confluence-ready markdown |
| **F** | Leadership update (1-min) | Quick status from repo facts | Chat output |
| **F2** | Persistent bi-weekly leadership | **Alternate weeks** — client meeting | `Demand Planning Reports/[N]. …md` |
| **G** | RCA from evidence | Post-failure analysis | Updates `RCA_PROCESS.md` if new pattern |
| **H** | Bug report JIRA + email + Teams | **Daily** — regression failures | `regression_reports/MMDDYYYY/*.md` |
| **I** | Regression module refresh | TestNG + XML → module doc | `AM_Regression_Reports/docs/v2\|v3/modules/` |
| **J** | Parent/master docs sync | After add/rename regression docs | Index files + mermaid map |

---

## Most-used prompts (expanded)

### H — Bug Report

**Inputs required:**
- Date (MMDDYYYY)
- Feature/area name
- Failure summary + exact exception
- TestNG/CI report URL
- Artifacts folder path
- File list in folder

**Output naming:** `[MMDDYYYY]_[FeatureName]_[IssueType].md`

**Email templates (PDF):**
- Failure: `confluence_exports/Bug Handling/1. Handling Process When a Bug.pdf`
- Resolution: `…/1b. Automation Bug Resolution Follow-Up.pdf`

**Cc (always):** Rajib Akhter, Henry Dittmer, Phuong Huynh, Automation.Squad

---

### F2 — Persistent Leadership Update

**Inputs required:**
- `[START]`, `[END]`, `[LAST_SHARE_DATE]`, `[MMDDYYYY]`, `[NEXT_NUMBER]`
- Brief bullet update at bottom of prompt

**Template:** `06_TEMPLATES/PERSISTENT_LEADERSHIP_UPDATE_TEMPLATE.md`

**Output has two parts:**
1. Full Confluence page (sections 1–10)
2. PSL "5. Automation Team" block for copy-paste

---

### I — Regression Module Refresh

**Inputs required:**
- V2 or V3 + target module
- TestNG HTML path/URL
- Suite XML path (e.g. `suites/v2/daily/stage1-enrollments.xml`)
- Reference PDF path (optional)
- Output file path

**Template:** `AM_Regression_Reports/docs/TEMPLATE_REGRESSION_MODULE_CONFLUENCE.md`

**Rules:**
- Do NOT invent Jenkins job names — copy from existing docs or mark `NEEDS_VALIDATION`
- Match section order from template exactly

---

### J — Parent/Master Sync

**Run after:** Any add/rename under `AM_Regression_Reports/docs/`

**Updates:**
- `docs/README.md`
- `00-automation-regression-master-overview.md` (tables + mermaid)
- `v2/README.md`, `v3/README.md`, module READMEs
- `AM_Regression_Reports/README.md`
- CICD indexes if applicable

---

## Additional quick prompts (in PROMPTS.md)

| Category | Prompts for |
|----------|-------------|
| Test development | Page Object, Cucumber scenario, API test |
| Test execution | Analyze results, generate exec report |
| Debugging | Investigate flaky test |

All follow `02_STANDARDS/` and `03_ARCHITECTURE/` references.

---

## Separate fixed pipeline (not A–J)

| Pipeline | Prompt file | Purpose |
|----------|-------------|---------|
| Regression evidence → area docs | `04_EXECUTION/regression/PIPELINE_PROMPT.md` | Generate `summary.md`, `enrollment.md`, etc. |

**Rule:** Fixed template — no improvisation.

---

## Prompt selection cheat sheet

| User says… | Use |
|------------|-----|
| "Regression failed, need JIRA" | **H** |
| "Leadership update for Persistent" | **F2** |
| "Update enrollment module doc from last night's run" | **I** then **J** |
| "I added a new V3 module page" | **J** |
| "What's missing in our docs?" | **D** |
| "Root cause this failure" | **G** |
| "Convert Confluence PDFs" | **B** |
| "Quick status for this week" | **F** |
