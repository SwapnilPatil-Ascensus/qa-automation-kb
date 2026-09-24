Create a modern, visually polished SharePoint Site Page titled "06 Mobile 2 Automation".

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

Quick links row for this page: Parent: Unite MSC API Automation | Previous: 05 Mobile 1 Automation | Next: 07 Enrollment Automation

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

PAGE CONTENT — build the page from exactly this material:

# 06 Mobile 2 Automation
Purpose: Scope, coverage position, artifacts, and known considerations for Mobile 2 API automation.

## Scope
Code: api-test-automation/mobile/mobile2/

Mobile 2 covers activity, transaction history, investments, banks, content, plans, contributions, dashboard and YTD summary, balance trend, performance, stackup, and UGift.

## Coverage position
| Item | Position |
|---|---|
| Documented rows | 25, including one acceptance harness endpoint |
| Business APIs in sign-off numerator | 24 |
| Intentional exclusion | GET mobilemembers/{planId}/{username} harness |
| Primary master-regression plants | OK Direct and New York |
| Additional smoke plant | NM Direct on selected stackup coverage |

## Support files
| Artifact | Use |
|---|---|
| Mobile 2 API Automation Sign-Off (DOCX) | Formal scope and completion record |
| mobile2-endpoint-current-state.csv | Endpoint to class to suite mapping |
| unite-msc-endpoint-summary.csv | Compact evidence register |
| Coverage chart image | Optional visual |

## Known considerations
Caution callout:
- Bank PUT and DELETE, and contribution DELETE, are destructive and intentionally separated from master coverage.
- Dynamic contribution fixtures can be environment-sensitive.
- POST mobilebanks with planId=upromise is a Postman-only enhancement candidate.
- Mobile 2 has the mature nightly pattern to reuse when adding other module jobs.

Use the current GitLab suite XML and POM for commands. SharePoint does not replace executable configuration.

After generating, verify the page title, the breadcrumb, the quick links, and the Source and ownership band, then publish under "Unite MSC API Automation".
