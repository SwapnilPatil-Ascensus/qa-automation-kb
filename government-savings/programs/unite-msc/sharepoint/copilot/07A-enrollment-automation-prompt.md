PART A of 5. Create a polished SharePoint Site Page titled "07 Enrollment Automation".

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
- Build only this part. Leave the page ready for the next part; do not add the Source and ownership band.

CONTENT:

# 07 Enrollment Automation
Purpose: End-to-end Enrollment operating guide: delivered coverage, ordered encrypted wizard, subsequent enrollment, suite/plants, data/session design, execution, and handoff evidence.

## 1. What was delivered
Handoff: Jira QA-893

| Metric | Position |
|---|---|
| Catalog rows | 28 |
| Automated | 25 |
| Deferred | 3 |
| Catalog coverage | 89.3% |
| Ordered regression/integration chain | 17 classes per plant |
| Current plants in XML | okdirect, newyork, nmdirect |
| Validation | L1-L4 + targeted post-account SQL verification |

Deferred partner submit, Upromise account, and OAuth token are explicit scope decisions tied to QA-1808/QA-1807—not missing MSC happy-path coding.

Publish under "Unite MSC API Automation", then continue with Part B.
