# Unite MSC SharePoint upload manifest

Create one document-library folder:

`API Testing Documentation Hub / Unite MSC API Automation`

Use the library for approved support artifacts. The Site Pages contain the explanation and links.

Page bodies are **not** uploaded. SharePoint Copilot cannot read local files, so each page is created by pasting its self-contained prompt from `sharepoint/copilot/`.

## Upload — formal handoff and sign-off files

| Display name | Local source | Link from page |
|---|---|---|
| Mobile 1 API Automation Sign-Off | `mobile-1/signoff/Mobile-1-API-Automation-Sign-Off.docx` | 05, 08 |
| Mobile 2 API Automation Sign-Off | `mobile-2/signoff/Mobile-2-API-Automation-Sign-Off.docx` | 06, 08 |
| Enrollment Documentation Index | `enrollment/deliverables/Enrollment-API-Documentation-Index.docx` | 01, 07 |
| Enrollment Architecture, Setup and Environments | `enrollment/deliverables/Enrollment-Architecture-Setup-Environments.docx` | 02, 03, 07 |
| Enrollment Execution and Troubleshooting | `enrollment/deliverables/Enrollment-Execution-Troubleshooting.docx` | 04, 09 |
| Enrollment Reporting and Triage | `enrollment/deliverables/Enrollment-Reporting-Triage.docx` | 09 |
| Enrollment API Automation Sign-Off | `enrollment/deliverables/Enrollment-API-Automation-Sign-Off.docx` | 07, 08 |
| Enrollment DB Refresh Checklist | `enrollment/deliverables/Enrollment-Handoff-DB-Refresh-Checklist.docx` | 10 |
| Enrollment AI Scenario Guide | `enrollment/deliverables/Enrollment-AI-Scenario-Guide.docx` | 11 |
| Legacy-to-Canonical Traceability | `traceability/deliverables/Unite-MSC-Legacy-to-Canonical-Traceability.docx` | 08 |

## Upload — coverage and traceability data

| Display name | Local source | Link from page |
|---|---|---|
| Mobile 1 Endpoint Current State | `mobile-1/mappings/mobile1-endpoint-current-state.csv` | 05, 08 |
| Mobile 2 Endpoint Current State | `mobile-2/mappings/mobile2-endpoint-current-state.csv` | 06, 08 |
| Unite MSC Endpoint Summary | `mobile-2/mappings/unite-msc-endpoint-summary.csv` | 06, 08 |
| Enrollment Endpoint Current State | `enrollment/coverage/enrollment-endpoint-current-state.csv` | 07, 08 |
| Enrollment Coverage Matrix | `enrollment/coverage/Enrollment-Automation-Coverage-Matrix.xlsx` | 07, 08 |
| Enrollment Endpoint Catalog | `enrollment/coverage/Enrollment End Points.xlsx` | 07, 08 |
| Legacy-to-Canonical Full Matrix | `traceability/legacy-to-canonical-traceability.csv` | 08 |
| Enhancement Backlog | `traceability/enhancement-backlog.md` | 08, 11 |

## Optional visuals

Upload only if the pages need a chart:

- `mobile-1/signoff/mobile1_coverage.png`
- `mobile-2/signoff/mobile2_coverage.png`
- `enrollment/deliverables/_assets/enrollment_coverage.png`

Do not use stock images. These charts are supporting visuals, not source-of-truth data.

## Link from GitLab — do not upload

These belong in GitLab and should be linked:

- Java source, POMs, and TestNG XML.
- Postman collections.
- SQL and YAML mappings.
- Pipeline YAML, runner configuration, and secure files.
- Current reports and GitLab job artifacts.
- Jira and qTest records.

## Never upload

- `*.postman_environment.json`
- Personal or shared host/property overlays.
- Passwords, JWT, cookies, certificates, private keys, SSN, database credentials, or connection strings.
- `target/`, raw logs, or payloads with PII.
- The SQL-field-validation folder as a claim of implemented coverage.
- Leadership drafts, generators, archives, duplicate handoff folders, or the entire repository tree.

## Count

- 10 formal DOCX files.
- 8 coverage/traceability files.
- Up to 3 optional chart images.

**Required upload total: 18 files. Optional maximum: 21 files.**
