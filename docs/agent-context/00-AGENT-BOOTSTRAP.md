# Agent Bootstrap — Read This First

## 30-second summary

| Question | Answer |
|----------|--------|
| **What is this repo?** | Documentation + operational memory for QA automation at Ascensus/AGS |
| **What is it NOT?** | The Java/Selenium test code (that lives in GitLab: `prime-test-automation`, etc.) |
| **Who uses it?** | Sr. QA Automation Engineer (you) + Cursor for daily doc generation |
| **Core rule** | If it isn't in the repo, it doesn't exist |
| **Primary daily tool** | `00_SYSTEM/PROMPTS.md` — copy/paste Cursor prompts |

---

## Mandatory behavior for agents

Read and follow **`00_SYSTEM/ROLE.md`** and **`00_SYSTEM/CONSTRAINTS.md`**.

| Rule | Detail |
|------|--------|
| Output style | Execution-ready: Confluence/Jira/email/Teams ready; **tables over paragraphs** |
| No theory | Skip generic QA theory unless asked |
| Always include | Assumptions (max 5), risks, next actions |
| Security | **Never** add secrets, credentials, tokens, or customer PII |
| Unknown facts | Mark `[NEED_INPUT]` or `[REDACT_NEEDED]` — do not invent |
| Source of truth | Prefer curated numbered folders (`00`–`11`); `10_IMPORTS_RAW/` is evidence/archive |

---

## Repo mental model

```
External systems (Jenkins, GitLab CI, Jira, Confluence)
        ↓ evidence / exports / failures
10_IMPORTS_RAW/          ← raw imports, bug artifacts, TestNG HTML, PDF exports
        ↓ Cursor prompts process & normalize
Curated KB (00–11, docs/) ← standards, templates, regression docs, governance
        ↓ prompts H, F2, I, J
Outputs                  ← JIRA blocks, emails, Teams, Confluence pages, leadership updates
```

---

## Top 5 user tasks (most common)

| # | Task | Prompt | Primary paths |
|---|------|--------|---------------|
| 1 | **Bug report** (JIRA + email + Teams) | **H** | `10_IMPORTS_RAW/regression_reports/MMDDYYYY/` |
| 2 | **Bi-weekly leadership update** (Persistent client) | **F2** | `06_TEMPLATES/PERSISTENT_LEADERSHIP_UPDATE_TEMPLATE.md` |
| 3 | **Refresh regression module doc** from TestNG | **I** | `AM_Regression_Reports/docs/v2|v3/modules/` |
| 4 | **Sync parent indexes** after doc changes | **J** | `AM_Regression_Reports/docs/00-automation-regression-master-overview.md` |
| 5 | **RCA** from failure evidence | **G** | `04_EXECUTION/RCA_PROCESS.md` |

Full steps: `05_ONBOARDING/HOW_TO_REPETITIVE_TASKS.md` and `docs/agent-context/03-DAILY-WORKFLOWS.md`.

---

## Two regression documentation pipelines (don't confuse them)

| Pipeline | Input | Output | Prompt |
|----------|-------|--------|--------|
| **Bug reporting** | Screenshots, exceptions, test data in date folder | One `.md` with JIRA + email + Teams | **H** in `PROMPTS.md` |
| **Evidence → area docs** | `regression_reports/YYYY-MM-DD/` with PDF/CSV/PNG | `04_EXECUTION/regression/*.md` | Fixed prompt in `04_EXECUTION/regression/PIPELINE_PROMPT.md` |
| **Module Confluence refresh** | TestNG HTML + suite XML + PDF | `AM_Regression_Reports/docs/v2|v3/modules/*.md` | **I** in `PROMPTS.md` |

---

## Tech stack (documented here; code elsewhere)

| Stream | Stack | CI platform |
|--------|-------|-------------|
| Prime V2 UI | Java, Ant, Selenium, Cucumber, TestNG | Jenkins (Stage1) |
| Prime V3 UI | Java, Maven, Selenium, Cucumber, TestNG | GitLab CI |
| API | REST Assured, Cucumber, Maven | In progress |
| Performance | JMeter, Taurus, BlazeMeter | Jenkins |
| Mobile MSC (target) | Java, Cucumber, Rest Assured, Maven | TBD |

---

## Before you edit anything

1. Check if content is **curated** (`00`–`11`) vs **raw import** (`10_IMPORTS_RAW/`)
2. For regression docs, confirm **canonical** path is `AM_Regression_Reports/docs/` (not duplicate under `confluence_exports/`)
3. After adding/moving regression markdown, run prompt **J**
4. Log significant decisions in `09_DECISIONS_WORKLOG/DECISIONS.md`

---

## Next reads

- Full purpose: [01-REPO-PURPOSE-AND-MODEL.md](01-REPO-PURPOSE-AND-MODEL.md)
- Folder guide: [02-FOLDER-MAP-WHAT-WHY-WHEN.md](02-FOLDER-MAP-WHAT-WHY-WHEN.md)
- Daily workflows: [03-DAILY-WORKFLOWS.md](03-DAILY-WORKFLOWS.md)
