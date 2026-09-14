# 01 — Source inventory (local, already preserved)

We do **not** need to download SharePoint to start rewriting. The hub was already exported from Confluence into this repo.

## Counts (2026-09-03)

| Source | Location | What it is | Publish? |
|--------|----------|------------|----------|
| Automation QA hub | `qa-knowledge-base/10_IMPORTS_RAW/confluence_exports/auto-qa-dochub/` | **110 PDFs** + 12 markdown (CI/CD rewrite) | Rewrite a **subset** |
| Demand planning / leadership | `qa-knowledge-base/10_IMPORTS_RAW/confluence_exports/Demand Planning Reports/` | Recurring leadership PDFs/md | Keep in Archive / leadership program, not hub home |
| Clean-up screenshots | `.../CleanUp-Confluence-DocHub/` | 6 PNGs | Reference only |
| Performance hub | `qa-knowledge-base/10_IMPORTS_RAW/Performance QA – Home & Documentation Hub/` | **42 PDFs**, 4 Word, plus Jenkins/JMeter/GitLab dump | Docs yes; **scripts/keys no** |
| Regression markdown (curated) | `qa-knowledge-base/10_IMPORTS_RAW/AM_Regression_Reports/docs/` | V2/V3 module pages already rewritten | **Reuse** — better than PDFs |
| Evergreen KB | `qa-knowledge-base/00_SYSTEM` … `05_ONBOARDING` | Operating standards | **Reuse** as SharePoint “Start here” |
| Bug lifecycle | `automation-bug-lifecycle/` | Current defect SOP | Link, do not duplicate |
| CI/CD markdown | `auto-qa-dochub/regression-master-overview/CICD/` | Numbered pipeline pages | **Reuse** with SharePoint titles |

Full PDF path list: [inventory/auto-qa-dochub-pdfs.md](./inventory/auto-qa-dochub-pdfs.md).

## Hub dump — keep / rewrite / archive / drop

### Rewrite into numbered SharePoint pages (high value)

| Old dump | New SharePoint page |
|----------|---------------------|
| Master Onboarding Guide + Charter | `01` Start here |
| Environment Access & Setup + 2.1.x | `02` Access and environments |
| Tech stack, GitLab, IntelliJ/Maven/Cursor | `03` Tooling and local setup |
| Best practices, naming, GitLab standards | `04` Standards |
| Defect Management + bug lifecycle repo | `05` Defects and triage |
| DoR / DoD / Jira Kanban KT | `06` Ready, done, Jira |
| Regression Master Overview + V2/V3 suites | `07` Regression |
| CI/CD markdown already in repo | `08` Pipelines |
| Automation Execution Plan (current parts only) | `09` How we run |
| AM Troubleshooting Guide | `10` Troubleshooting |
| IDP reference + MFA | `11` IDP |
| Performance onboarding PDFs (not JMeter trees) | `12` Performance |
| Working agreement, Kanban hub | `13` Ways of working |
| qTest–Jira guide | `14` qTest |

### Archive (keep files, do not put on hub home)

- `regression-master-overview/Archival/` (duplicate PDFs)
- Hiring hub (`Sr. Automation Engineer hiring hub/` — 13 PDFs)
- Drafts (`DRAFT` in filename, SASVA research, 4-week new-hire roadmap unless refreshed)
- Plan conversion program pack (`3.0`–`3.6`) unless that program is still active — then a single program page, not six
- Demand Planning Reports (belongs with leadership updates)
- Execution dashboards dated Q2–Q3 2025

### Drop from SharePoint (never republish)

- Performance `Jenkins/setup/secretKeyStage.txt` and any CSV with live credentials
- JMeter `.jmx` / Taurus YAML / Jenkins artifacts (`kpi.jtl`) — those live in GitLab `performance-test-automation`, not a documentation hub
- Interview question banks and candidate resumes under AMSquad Team Reports

## What “download all” would add

Only **SharePoint-native pages created after the Confluence migration** (Copilot drafts, new libraries, dashboards). Until you drop a OneDrive/PnP export into `10_IMPORTS_RAW/sharepoint_exports/`, assume the local PDF tree **is** the dump.

## Script

```powershell
.\programs\sharepoint-qa-hub\scripts\inventory-local-sources.ps1
```
