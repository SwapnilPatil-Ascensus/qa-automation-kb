PART A of 2. Create a polished SharePoint Site Page titled "08 Coverage, Traceability and Sign-off".

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

Quick links row for this page: Parent: Unite MSC API Automation | Previous: 07 Enrollment Automation | Next: 09 Reporting and Troubleshooting

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.
- Build only this part. Leave the page ready for the next part; do not add the Source and ownership band.

CONTENT:

# 08 Coverage, Traceability and Sign-off
Purpose: Where coverage lives, how to trace an endpoint to evidence, and what the sign-off boundary means.

## Coverage sources
| Source | System of record |
|---|---|
| Mobile 1 | mobile1-endpoint-current-state.csv |
| Mobile 2 | mobile2-endpoint-current-state.csv |
| Enrollment | enrollment-endpoint-current-state.csv and the coverage workbook |
| Legacy to canonical | legacy-to-canonical-traceability.csv |
| Automated implementation | https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/mobile?ref_type=heads |
| Manual API collection | https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/bruno/Mobile/mobile-msc/Unite-MSC-Bruno_collection?ref_type=heads |
| Manual test cases | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212334&object=0&tab=testdesign |
| Delivery scope and stories | https://ascensuscollegesavings.atlassian.net/browse/QA-796 |

Publish under "Unite MSC API Automation", then continue with Part B.
