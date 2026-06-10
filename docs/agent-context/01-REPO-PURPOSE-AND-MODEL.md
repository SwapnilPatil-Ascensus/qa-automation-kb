# Repo Purpose and Operating Model

## Why this repo exists

The user (Sr. QA Automation Architect / Principal SDET) runs **daily QA automation operations** across:

- Prime **V2** nightly regression (Jenkins, Ant, legacy Unite/CSR UI)
- Prime **V3** Stage1 regression (GitLab CI, Maven, UE + IDP)
- API, performance, platform support, and mobile MSC migration programs
- Jira/Scrum governance, leadership reporting, and client updates (Persistent)

This repo is the **single place** where:

1. **Process knowledge** lives (how to triage, report bugs, run sprints)
2. **Templates** produce stakeholder-ready output (JIRA, email, Confluence)
3. **Regression documentation** stays current (module pages, CI/CD landscape)
4. **Memory** survives chat wipes (`DECISIONS.md`, worklog, meeting notes)
5. **Cursor prompts** automate repetitive documentation work

> **This is not where tests are written or executed.** Test code is in external GitLab repos (primarily `prime-test-automation`, `performance-test-automation`).

---

## Four roles this repo plays

| Role | What it means | Examples |
|------|---------------|----------|
| **Source of truth** | Authoritative markdown for processes and regression docs | `AM_Regression_Reports/docs/`, `docs/jira-governance/` |
| **Memory** | Decisions and work history replace chat context | `09_DECISIONS_WORKLOG/DECISIONS.md` |
| **Prompt library** | Copy/paste Cursor instructions = "buttons" for tasks | `00_SYSTEM/PROMPTS.md` |
| **Output factory** | Generate Confluence/Jira/leadership content from evidence | Prompts H, F2, I, E |

---

## How / why / when — by activity

| Activity | How | Why | When |
|----------|-----|-----|------|
| Log regression bug | Put artifacts in date folder → Prompt **H** | Standard JIRA + comms in one file; audit trail | Any nightly/test failure needing dev attention |
| Leadership update | Brief bullets → Prompt **F2** | Bi-weekly Persistent client meeting deliverable | Alternate weeks before client PSL meeting |
| Refresh module doc | TestNG HTML + suite XML → Prompt **I** | Keep Confluence-ready regression pages accurate | After major suite changes or before sharing coverage |
| Sync doc indexes | List changes → Prompt **J** | Parent TOC + mermaid map stay correct | After adding/renaming files under `AM_Regression_Reports/docs/` |
| Sprint governance | Use DoR/DoD checklists + story drafts | Enforceable Jira standards | Sprint planning, refinement, story writing |
| Mobile program tracking | Update migration trackers | Central program status for UE → Mobile1 → Mobile2 | Weekly mobile MSC migration work |
| Ingest Confluence | Drop PDFs in `10_IMPORTS_RAW/confluence_exports/` → Prompt **B** | Normalize legacy docs into curated structure | When new Confluence exports arrive |
| Gap analysis | Prompt **D** | Find missing/stale docs | Weekly hygiene |

---

## Curated vs raw content

| Zone | Path pattern | Treatment |
|------|--------------|-----------|
| **Curated** | `00_SYSTEM/` … `11_BACKLOG/`, `docs/jira-governance/`, `docs/mobile-automation-program-hub/` | Edit carefully; follow `02_STANDARDS/DOC_STANDARDS.md` |
| **Working regression KB** | `10_IMPORTS_RAW/AM_Regression_Reports/docs/` | Primary regression documentation (Confluence-ready) |
| **Evidence archive** | `10_IMPORTS_RAW/regression_reports/MMDDYYYY/` | Bug artifacts + generated bug `.md` files — append-only per incident |
| **Raw imports** | `10_IMPORTS_RAW/confluence_exports/`, etc. | Reference/archive; don't blindly duplicate into curated folders |

**Decision (2026-01-25):** Numbered folders `00`–`11` for navigation; raw imports isolated in `10_IMPORTS_RAW/` to prevent distraction.

---

## Relationship to external systems

```
┌─────────────────────────────────────────────────────────────┐
│  LIVE AUTOMATION (external GitLab repos)                     │
│  prime-test-automation · performance-test-automation · …     │
└──────────────────────────┬──────────────────────────────────┘
                           │ runs in Jenkins / GitLab CI
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  EXECUTION OUTPUT                                            │
│  TestNG HTML · screenshots · exceptions · Jira tickets       │
└──────────────────────────┬──────────────────────────────────┘
                           │ user saves evidence
                           ▼
┌─────────────────────────────────────────────────────────────┐
│  qa-automation-kb (THIS REPO)                                │
│  Evidence → Prompts → Docs → Confluence/Jira/Email/Teams     │
└─────────────────────────────────────────────────────────────┘
```

---

## What "good output" looks like

From `00_SYSTEM/ROLE.md`:

- Confluence-ready tables and checklists
- JIRA copy-paste blocks with Summary, Steps, Expected/Actual, Environment
- Email drafts with correct To/Cc lists (see Prompt H)
- Leadership updates matching `PERSISTENT_LEADERSHIP_UPDATE_TEMPLATE.md` structure
- Regression module pages matching `TEMPLATE_REGRESSION_MODULE_CONFLUENCE.md`

---

## Maintenance expectations

| File | Update frequency |
|------|------------------|
| `01_CONTEXT/CURRENT_STATE.md` | Weekly (currently has placeholders — needs live data) |
| `09_DECISIONS_WORKLOG/DECISIONS.md` | After every significant decision |
| `09_DECISIONS_WORKLOG/WORKLOG.md` | Ongoing work bullets |
| `11_BACKLOG/DOC_GAPS.md` | Weekly via Prompt D |
| Regression module pages | After suite/report changes via Prompt I |
| `docs/agent-context/*` | When repo structure or workflows change |
