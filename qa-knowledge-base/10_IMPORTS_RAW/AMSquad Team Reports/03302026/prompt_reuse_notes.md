# Prompt reuse – QA Automation monthly AMSquad report (03/30/2026)

## What was generated this month

| File | Purpose |
|------|---------|
| `confluence_report.md` | Confluence-ready detailed monthly report (sections 1–7 per spec). |
| `teams_summary.md` | Short bullets for Teams under GitLab screenshot(s). |
| `leadership_email.md` | Manager-ready email with per-member detail and links. |
| `monthly_report_data.json` | Machine-readable snapshot for automation / next-month diff. |
| `prompt_reuse_notes.md` | This file – how to rerun next month. |

**Folder:** `10_IMPORTS_RAW/AMSquad Team Reports/03302026/`

## Inputs used

- Structured **member/workstream** text provided in the generation prompt (Venkatesh, Dinesh, Preeti, Sunil, Swapnil).
- **GitLab:** `https://gitlab.com/groups/ascensus-gs/products/depot/qa-automation/-/contribution_analytics?start_date=2026-02-28`
- **Jira:** Scrum [board 2515](https://ascensuscollegesavings.atlassian.net/jira/software/c/projects/QA/boards/2515), Kanban [board 1292](https://ascensuscollegesavings.atlassian.net/jira/software/c/projects/QA/boards/1292)

**Note:** No JPG/PNG/Word files were present in the folder at generation time. **Contribution counts were not invented**; Confluence §2 and JSON `contribution_summary` direct readers to the GitLab link and screenshots.

## How to reuse next month

1. **Create** a new folder: `10_IMPORTS_RAW/AMSquad Team Reports/[MMDDYYYY]/`.
2. **Drop in** GitLab contribution screenshots (and any Word/txt notes); optionally paste the same **full prompt** with updated **reporting date**, **reporting_period**, **GitLab start_date** URL, and **revised member bullets**.
3. **Run** the prompt in Cursor with the new folder as **source of truth** so OCR/screenshot text can fill **exact metrics** where visible.
4. **Copy** the five filenames unchanged (`confluence_report.md`, `teams_summary.md`, `leadership_email.md`, `monthly_report_data.json`, `prompt_reuse_notes.md`) into the new folder.
5. **After generation:** Append real screenshot/doc paths to `monthly_report_data.json` → `source_files` and mirror filenames in Confluence §7 References.
6. **Optional:** Diff `monthly_report_data.json` month-over-month for dashboards or scripts.

## Quality rules to preserve

- Do **not** invent GitLab numbers; use **visible** data or phrases like **“based on visible GitLab activity.”**
- Keep **Teams** bullet-heavy; **email/Confluence** more detailed.
- Always carry **gitlab_report_link** and updated **reporting_period** in JSON.
