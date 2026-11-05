PART A of 3. Create a polished SharePoint Site Page titled "09 Reporting and Troubleshooting".

Site: API Testing Documentation Hub. Publish it under the parent page "Unite MSC API Automation", not at the hub root.

DESIGN:
- Full-width deep-teal hero: white title, one-line purpose, then "Owner: QA Automation | Internal - no credentials or PII".
- Breadcrumb: API Testing Documentation Hub > Unite MSC API Automation > this page.
- Navigation: Quick Links tiles/grid, not plain bullets.
- Alternate white/light-gray sections with dividers.
- Tables: navy header, bold white text, zebra rows, left-aligned, no merged cells.
- Callouts: info blue, caution amber, prohibition red.
- Two columns for short guidance + small table; full width for wide tables/code.
- Monospace code blocks; real checkbox lists.
- End with gray Source and ownership band: QA Automation owner; GitLab api-test-automation is executable source of truth.
- No emoji, stock photos, or clip art.

Quick links row for this page: Parent: Unite MSC API Automation | Previous: 08 Coverage, Traceability and Sign-off | Next: 10 Test Data, DB Refresh and Security

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.
- Build only this part. Leave the page ready for the next part; do not add the Source and ownership band.

CONTENT:

# 09 Reporting and Troubleshooting
Purpose: How to read the generated reporting portal, isolate the first real failure, distinguish environment/data/automation/product issues, rerun safely, and capture useful evidence.

## 1. Reporting outputs
| Output | Location | Use |
|---|---|
| Portal landing page | <module>/target/mobile-ms-report/index.html | Overall status, counts, suite/module/environment |
| Extent detail | target/mobile-ms-report/extent/detail.html | Per-test steps, duration, sanitized failure |
| Portal pages | target/mobile-ms-report/pages/ | details, categories, logs, history, about |
| Summary/history JSON | target/mobile-ms-report/data/ | machine-readable run and trend data |
| Surefire/TestNG | <module>/target/surefire-reports/ | stack trace, skipped dependency, JUnit XML |
| GitLab job log and artifacts | CI environment and command |
| Jira or bug evidence folder | Product or recurring automation defect |

## 2. Read the run in this order
1. Confirm module, suite, environment, and branding are what you intended.
2. Check passed/failed/skipped counts in index.html.
3. Open the earliest failed class in the ordered chain.
4. Read the HTTP status, assertion, sanitized failure reason, and duration.
5. Treat later Enrollment skips as downstream symptoms until the first failed wizard step is resolved.
6. Cross-check Surefire only when the portal lacks the compile/setup stack trace.
7. Check recent deployment or database-refresh timing before changing code.

Publish under "Unite MSC API Automation", then continue with Part B.
