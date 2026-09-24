Create a modern, visually polished SharePoint Site Page titled "09 Reporting and Troubleshooting".

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

PAGE CONTENT — build the page from exactly this material:

# 09 Reporting and Troubleshooting
Purpose: Where to find evidence and how to classify a failure before escalating it.

## Where to look
| Evidence | Use |
|---|---|
| Surefire and TestNG output | Class and assertion failure |
| Module HTML report | Shareable sanitized run summary |
| GitLab job log and artifacts | CI environment and command |
| Jira or bug evidence folder | Product or recurring automation defect |

## First-failure classification
| Symptom | Likely class | First action |
|---|---|---|
| 401 or IDP token error | Auth, environment, or data | Confirm plant, account, token path, IDP availability |
| Enrollment decrypt error | Encryption or session | New certificate and prospect; avoid double encryption |
| 426 | App-version metadata | Confirm approved x-app-version |
| Oracle timeout | Access or environment | Confirm VPN, Frogger, and port |
| Empty SQL fixture | Data refresh | Recreate approved automation data |
| Class never ran | Suite or group wiring | Check XML, profile, groups, exclusions |
| 404 or 503 across tests | Environment or routing | Check service health before editing tests |

## Triage steps
1. Preserve timestamp, environment, plant, endpoint, class, and report.
2. Re-run targeted once only when safe.
3. Compare with service health and any recent refresh or deploy.
4. Classify as environment, data, automation, product, or expected exclusion.
5. For defects, use the automation bug lifecycle with sanitized evidence.

## Evidence rules
Prohibition callout: never attach bearer tokens, passwords, SSN, raw personal payloads, host properties, Postman environment JSON, or database credentials. Redact account identifiers unless the approved internal process requires them.

After generating, verify the page title, the breadcrumb, the quick links, and the Source and ownership band, then publish under "Unite MSC API Automation".
