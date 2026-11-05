PART A of 3. Create a polished SharePoint Site Page titled "10 Test Data, DB Refresh and Security".

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

Quick links row for this page: Parent: Unite MSC API Automation | Previous: 09 Reporting and Troubleshooting | Next: 11 Extend the Automation

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.
- Build only this part. Leave the page ready for the next part; do not add the Source and ownership band.

CONTENT:

# 10 Test Data, DB Refresh and Security
Purpose: Oracle-backed automation data, post-refresh recovery, safe fixture ownership, targeted SQL use, the L5 boundary, and strict secret/PII handling.

## 1. What Oracle is used for
| Use | Modules |
|---|---|
| Select approved automation member/account and IDP metadata | Mobile 1, Mobile 2, subsequent Enrollment |
| Resolve minimum supported app version | All mobile modules |
| Resolve account extension, member ID, routing/bank | Mobile 1 and Mobile 2 |
| Resolve recurring-contribution fixture ID | Mobile 2 |
| Resolve active fund/plan data and verify created account | Enrollment |

SQL is a controlled fixture/provider layer. It is not permission to browse or mutate arbitrary customer-like data.

## 2. Data rules
- Use only approved automation-owned member/account patterns.
- Generate unique Enrollment username and SSN values through framework placeholders.
- Never hardcode a password, account extension, member ID, bank/contribution ID, routing number, fund ID, or app version in Java.
- Mutating/delete cases must prove they own the record.
- Keep SQL in the module SQL file with a named key and branding placeholder.
- Record environment and branding with evidence; never publish returned rows.

Publish under "Unite MSC API Automation", then continue with Part B.
