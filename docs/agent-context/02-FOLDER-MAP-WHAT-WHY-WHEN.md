# Folder Map — What, Why, When

Complete guide to every top-level area. **~780 files total, ~246 markdown.**

---

## Numbered curated folders (`00`–`11`)

### `00_SYSTEM/` — Core system

| File | What | Why | When |
|------|------|-----|------|
| `ROLE.md` | AI/human role definition, non-negotiables, tech scope | Sets output expectations for Cursor | Every new session; before generating docs |
| `CONSTRAINTS.md` | Security, env limits, redaction rules | Prevent secrets/PII in repo | Before any commit or doc with env details |
| `PROMPTS.md` | **Primary daily tool** — prompts A through J + helpers | Automate bug reports, leadership updates, regression refresh | Daily repetitive tasks |
| `GLOSSARY.md` | Term definitions (Stage1, POM, flakiness, etc.) | Shared vocabulary | When terms are unclear |
| `SOURCES.md` | Import tracking for Confluence/chats | Audit trail of ingested content | After imports (currently stale — needs update) |

---

### `01_CONTEXT/` — Current reality

| File | What | Why | When |
|------|------|-----|------|
| `CURRENT_STATE.md` | What's true today: team, envs, metrics | Leadership context | Weekly refresh (**mostly placeholders**) |
| `STACK_AND_TOOLS.md` | Technology stack inventory | Onboarding, architecture talks | When stack changes |
| `ENVIRONMENTS.md` | Stage1/Stage2/QA/PRO/DR details | Test planning, troubleshooting | Before env-specific work |
| `OWNERSHIP_RACI.md` | Who owns test dev, defects, docs | Clarify responsibilities | Escalations, staffing |

---

### `02_STANDARDS/` — Rules for code and docs

| File | What | When |
|------|------|------|
| `DOC_STANDARDS.md` | Markdown format, placeholders, headers | Writing any new KB doc |
| `CODE_STANDARDS.md` | Java/test conventions (for external repos) | Code review in automation repos |
| `NAMING_CONVENTIONS.md` | Test/page/feature naming | New test creation |
| `SECURITY_AND_DATA.md` | PII, credentials, test data policy | Before sharing test data |

---

### `03_ARCHITECTURE/` — Technical design (templates + patterns)

| File | What | When |
|------|------|------|
| `OVERVIEW.md` | Layered architecture, design patterns | High-level framework understanding |
| `UI_AUTOMATION.md` | POM, Selenium, waits | UI test design |
| `API_AUTOMATION.md` | REST Assured patterns | API test design |
| `PERFORMANCE_TESTING.md` | Load/stress types | Perf planning |
| `CI_CD.md` | Jenkins pipeline skeleton | Pipeline discussions |
| `TEST_DATA_STRATEGY.md` | Data sources, refresh | Data setup planning |
| `OBSERVABILITY.md` | Logging, monitoring | Debugging failures |

---

### `04_EXECUTION/` — How tests run and fail get handled

| File | What | When |
|------|------|------|
| `DAILY_REGRESSION.md` | Nightly schedule, triage | Morning regression review |
| `RELEASE_REGRESSION.md` | Release gate process | Pre-release |
| `SMOKE_SANITY.md` | Quick validation scope | Post-deploy |
| `DEFECT_LIFECYCLE.md` | Bug workflow end-to-end | Logging/tracking defects |
| `TRIAGE_RULES.md` | Real bug vs flaky vs env | After failures |
| `RCA_PROCESS.md` | Root cause analysis steps | Post-incident |
| `FLAKINESS_PLAYBOOK.md` | Fix intermittent tests | Recurring flaky failures |
| `regression/` | **Pipeline 1**: evidence → area docs | See `regression/README.md` |

**`04_EXECUTION/regression/` subfolder:**

| File | What | When |
|------|------|------|
| `PIPELINE_PROMPT.md` | Fixed Cursor prompt (no improvisation) | Convert evidence to structured regression docs |
| `_template.md` | Fixed template — do not modify structure | Base for generated reports |
| `summary.md`, `enrollment.md`, etc. | Generated outputs | After running pipeline |

---

### `05_ONBOARDING/` — Getting started + repetitive tasks

| File | What | When |
|------|------|------|
| `HOW_TO_REPETITIVE_TASKS.md` | **Step-by-step bug + leadership update** | When you forget locations/steps |
| `KT_INDEX.md` | Master index to all KB areas | Finding anything |
| `ONBOARDING_7_DAY.md` | New hire first week | Onboarding |
| `LOCAL_SETUP.md`, `ACCESS_SETUP.md` | Environment and access | Day 1 setup |
| `FIRST_5_TASKS.md`, `COMMON_FAILURES.md` | Early tasks and troubleshooting | First weeks |

---

### `06_TEMPLATES/` — Reusable output structures

| File | What | When |
|------|------|------|
| `PERSISTENT_LEADERSHIP_UPDATE_TEMPLATE.md` | Bi-weekly client update structure | Prompt F2 |
| `JIRA_TICKET_TEMPLATE.md` | Generic Jira story/bug | Manual ticket creation |
| `CONFLUENCE_PAGE_TEMPLATE.md` | Standard page structure | New Confluence pages |
| `LEADERSHIP_UPDATE_TEMPLATE.md` | Short weekly status | Quick leadership brief |
| `EXEC_REPORT_TEMPLATE.md` | Test execution report | Post-run reporting |
| `RCA_TEMPLATE.md` | Formal RCA doc | Incidents |
| `TEST_PLAN_TEMPLATE.md` | Test plan structure | New feature planning |

---

### `07_GOVERNANCE_VISIBILITY/` — Metrics and status

| File | What | When |
|------|------|------|
| `METRICS_CATALOG.md` | QA metrics to track | Dashboard design |
| `COVERAGE_MATRIX.md` | Test coverage matrix | Coverage planning |
| `DASHBOARD_REQUIREMENTS.md` | Dashboard specs | Jira/qTest dashboards |
| `STATUS_RULES.md` | RAG/status definitions | Consistent reporting |

---

### `08_MEETINGS_NOTES/` — Meeting archive

| Path | What | When |
|------|------|------|
| `2026/README.md` | Naming convention `YYYY-MM-DD_TOPIC.md` | After meetings (**folder mostly empty**) |

---

### `09_DECISIONS_WORKLOG/` — Memory replacement

| File | What | When |
|------|------|------|
| `DECISIONS.md` | ADR-lite decision log | **After every significant decision**; read at session start |
| `WORKLOG.md` | Dated work bullets | Track completed work |
| `RISKS.md` | Risk register | Program risks |

---

### `11_BACKLOG/` — Doc gaps and actions

| File | What | When |
|------|------|------|
| `DOC_GAPS.md` | Missing pages/sections | Weekly via Prompt D |
| `ACTION_ITEMS.md` | Meeting follow-ups | After meetings |

---

## `docs/` — Extended program documentation

### `docs/agent-context/` (this folder)

Agent bootstrap docs for context recovery after chat wipe.

### `docs/jira-governance/` (~45 markdown files)

| Section | What | When |
|---------|------|------|
| `00-overview/` | Scope, operating model, rollout enforcement | Program kickoff |
| `01-requirement-intake/` | Aha → Jira intake | New work entering backlog |
| `02-backlog-management/` | Epic structure, health rules | Grooming |
| `03-story-standards/` | DoR, DoD, AC templates | Story writing |
| `04-sprint-execution/` | Sprint lifecycle, standup script | Scrum ceremonies |
| `05-communication/` | Email, Teams, escalation templates | Stakeholder comms |
| `06-jira-usage-guides/` | Boards, JQL, dashboards | Daily Jira use |
| `07-reporting/` | Sprint + leadership reporting | Sprint review |
| `08-roadmap/` | 90-day plan | Quarterly planning |
| `backlog/` | 9 epics + 32 synthetic stories | Jira seeding |
| `upcoming-stories/` | Copy-paste story drafts (MEMCONTRIB, UEPIPE, etc.) | Pre-Jira writing |
| `data/` | CSV exports, feature files, meeting notes | Reference data |

**Start:** `docs/jira-governance/README.md`

### `docs/mobile-automation-program-hub/` (18 files)

Mobile MSC API test migration program (UniteMSC → centralized framework).

| File | When |
|------|------|
| `01-program-overview-and-plan-of-action.md` | Program kickoff |
| `05-07-*-migration-tracker.md` | Daily migration status |
| `status-summary.md`, `action-items.md` | Leadership briefs |
| `jira-stories/` | Bulk Jira import |

**Start:** `docs/mobile-automation-program-hub/README.md`

### `docs/DB Refresh/`

SQL scripts for test account setup (IDP password, MFA disable). **No markdown index** — harder to discover.

| When | Use |
|------|-----|
| Resetting IDP test accounts | `SQL Files/2. IDP - Update Password & MFA Disable.sql` |

---

## `10_IMPORTS_RAW/` — Raw imports and working artifacts (~577 files)

**Purpose:** Preserve originals; hold evidence; host the **primary regression documentation KB**.

### Key subfolders

| Subfolder | What | Why | When |
|-----------|------|-----|------|
| `AM_Regression_Reports/docs/` | **Canonical regression docs** (V2/V3/CICD) | Confluence-ready suite documentation | Regression doc work, coverage reviews |
| `AM_Regression_Reports/suites/` | TestNG XML (v2 daily/smoke/release, v3 stage1) | Reference suite definitions | Prompt I, pipeline troubleshooting |
| `AM_Regression_Reports/reports/` | TestNG HTML exports | Latest run evidence | **Gitignored** — regenerable |
| `regression_reports/MMDDYYYY/` | Bug evidence + generated bug `.md` | Audit trail per failure | Every regression bug (Prompt H) |
| `confluence_exports/auto-qa-dochub/` | Confluence PDF archive | Historical reference | Finding legacy PDFs |
| `confluence_exports/Demand Planning Reports/` | Leadership working updates | Format reference for F2 | Bi-weekly updates |
| `confluence_exports/Bug Handling/` | Bug email process PDFs | Failure/resolution email templates | Bug reporting |
| `AM Troubleshooting Guide/` | Stage DB, schema, PuTTY SQL guides | Offshore troubleshooting | Env/schema issues |
| `AMSquad Team Reports/` | Team status examples | Reference for team comms | Status reporting |
| `Performance QA …/` | JMeter/Taurus/Lighthouse snapshot | Perf test reference (may drift from live repo) | Performance work |

### Canonical vs duplicate

| Canonical | Duplicate (reference only) |
|-----------|---------------------------|
| `AM_Regression_Reports/docs/CICD/` | `confluence_exports/auto-qa-dochub/regression-master-overview/CICD/` |

---

## Quick lookup: "I need to find…"

| Looking for… | Path |
|--------------|------|
| Bug prompt + steps | `00_SYSTEM/PROMPTS.md` § H · `05_ONBOARDING/HOW_TO_REPETITIVE_TASKS.md` |
| Leadership prompt | `PROMPTS.md` § F2 |
| V2 module list (14 modules) | `AM_Regression_Reports/docs/v2/modules/` |
| V3 Stage1 (UE + IDP) | `AM_Regression_Reports/docs/v3/modules/` |
| CI/CD master landscape | `AM_Regression_Reports/docs/CICD/01-master-qa-automation-cicd-landscape.md` |
| Full regression TOC + mermaid | `AM_Regression_Reports/docs/00-automation-regression-master-overview.md` |
| TestNG export cleanup guide | `AM_Regression_Reports/docs/GUIDE_TESTNG_REPORT_EXPORT_AND_CLEANUP.md` |
| Jira DoR/DoD | `docs/jira-governance/03-story-standards/` |
| Mobile migration | `docs/mobile-automation-program-hub/` |
