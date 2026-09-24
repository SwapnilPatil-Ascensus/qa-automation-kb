# QA-893 — Enrollment API handover package

**Jira:** [QA-893](https://ascensuscollegesavings.atlassian.net/browse/QA-893)  
**Epic:** QA-796  
**Sprint:** AMSQUAD 26.15  
**Module:** Unite MSC Enrollment API (`api-test-automation/mobile/enrollment`)  
**Location:** `programs/unite-msc/enrollment/` — **do not** put these files in the API GitLab repo.

Coding for Mobile 1, Mobile 2, and Enrollment happy path is done. This pack is the **Enrollment** support handoff (same job Mobile 1 / Mobile 2 Word packs already did).

## What to hand to the receiving team

| # | Word (formal) | Markdown (SharePoint / Git) | QA-893 subtask |
|---|----------------|-----------------------------|----------------|
| 1 | [Enrollment-API-Documentation-Index.docx](./deliverables/Enrollment-API-Documentation-Index.docx) | [docs/00-index.md](./docs/00-index.md) | QA-2039 |
| 2 | [Enrollment-Architecture-Setup-Environments.docx](./deliverables/Enrollment-Architecture-Setup-Environments.docx) | [docs/01-architecture-setup.md](./docs/01-architecture-setup.md) | QA-2040 |
| 3 | [Enrollment-Execution-Troubleshooting.docx](./deliverables/Enrollment-Execution-Troubleshooting.docx) | [docs/02-execution-troubleshooting.md](./docs/02-execution-troubleshooting.md) | QA-2041 |
| 4 | [Enrollment-Reporting-Triage.docx](./deliverables/Enrollment-Reporting-Triage.docx) | [docs/03-reporting.md](./docs/03-reporting.md) | QA-2042 |
| 5 | [Enrollment-API-Automation-Sign-Off.docx](./deliverables/Enrollment-API-Automation-Sign-Off.docx) | [docs/04-sign-off.md](./docs/04-sign-off.md) | QA-2043 |
| 6 | [Enrollment-Handoff-DB-Refresh-Checklist.docx](./deliverables/Enrollment-Handoff-DB-Refresh-Checklist.docx) | [docs/05-handoff-checklist.md](./docs/05-handoff-checklist.md) | QA-2044 |
| 7 | [Enrollment-AI-Scenario-Guide.docx](./deliverables/Enrollment-AI-Scenario-Guide.docx) | [docs/06-ai-scenario-guide.md](./docs/06-ai-scenario-guide.md) | QA-2046 |
| 8 | (section in index) | [docs/07-secrets-and-review.md](./docs/07-secrets-and-review.md) | QA-2045, QA-2047 |

## SharePoint (API documentation project)

Do **not** upload every KB file. Use [sharepoint/README.md](./sharepoint/README.md): four pages + attach the matching DOCX.

## Regenerating Word files

```powershell
python programs/unite-msc/enrollment/tools/generate_enrollment_handoff_pack.py
```

Requires: `python-docx`, `matplotlib`

## Also in this folder

| Path | What |
|------|------|
| [coverage/](./coverage/) | Status MD, matrix XLSX, endpoint CSV, Excel catalog |
| [sql/](./sql/) | Step SQL (no credentials) |

Mobile 1 / Mobile 2 Word packs: `../mobile-1/signoff/`, `../mobile-2/signoff/`.  
Legacy → Java matrix: `../traceability/`.

**Approvals and ACM names:** `[NEED_INPUT]` on the sign-off page until Rajib/Henry name owners.
