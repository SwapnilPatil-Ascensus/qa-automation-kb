Create a modern, visually polished SharePoint Site Page titled "07 Enrollment Automation".

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

Quick links row for this page: Parent: Unite MSC API Automation | Previous: 06 Mobile 2 Automation | Next: 08 Coverage, Traceability and Sign-off

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

PAGE CONTENT — build the page from exactly this material:

# 07 Enrollment Automation
Purpose: Scope, wizard flow, suites, and operational notes for Enrollment API automation handed over under QA-893.

## Scope and status
Code: api-test-automation/mobile/enrollment/ | Handoff: Jira QA-893

| Metric | Position |
|---|---|
| Catalog rows | 28 |
| Automated | 25 |
| Deferred | 3 |
| Core wizard | 15 of 15 documented happy-path steps |
| Primary plants | OK Direct, New York |
| Local-only plant | NM Direct example; not CI sign-off |

Deferred items are partner submit, Upromise account, and OAuth token. They are exclusions, not missing coding in the signed-off MSC happy path.

## Wizard flow
Certificate, prospect, enrollment started, owner, address, beneficiary, routing and bank, recurring contribution, allocations, review-confirm, then subsequent enrollment cases.

Prohibition callout: Enrollment POST bodies use encryption. Never paste plaintext sensitive payloads, certificate material, JWT, SSN, or environment JSON into SharePoint.

## Suites
| Profile | Purpose |
|---|---|
| mobile-ms-enrollment-smoke | Stage1 bootstrap and health |
| mobile-ms-enrollment-regression | Stage1 OK Direct and New York |
| mobile-ms-enrollment-integration | QC4 integration |

## Operational notes
- QC4 can be blocked by refresh, IDP or reverse proxy, plan metadata, or account and MFA prerequisites.
- The GitLab Enrollment nightly remains a follow-up unless it has since been implemented and verified.
- After a database refresh, use page 10 before classifying a product defect.

After generating, verify the page title, the breadcrumb, the quick links, and the Source and ownership band, then publish under "Unite MSC API Automation".
