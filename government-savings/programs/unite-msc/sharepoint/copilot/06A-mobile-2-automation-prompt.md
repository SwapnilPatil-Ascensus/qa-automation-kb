PART A of 3. Create a polished SharePoint Site Page titled "06 Mobile 2 Automation".

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
- Build only this part. Leave the page ready for the next part; do not add the Source and ownership band.

CONTENT:

# 06 Mobile 2 Automation
Purpose: Complete Mobile 2 guide: 96% signed-off business coverage, endpoint families, Mobile 1 reuse, suite separation, dynamic fixtures, execution, and evidence.

## 1. What was delivered
| Metric | Delivered |
|---|---|
| Catalog rows | 25 |
| In-scope business operations automated | 24 |
| Signed-off business coverage | 96.0% |
| Validation | L1-L4 lean assertions |
| Current regression/integration branding | okdirect, newyork, nmdirect |
| Sign-off | COMPLETE |

The only excluded catalog row is the acceptance harness GET mobilemembers/{planId}/{username}; it is not a missing business API. Mobile 2 reuses Mobile 1 authentication instead of duplicating login code.

## 2. Endpoint families
| Family | Coverage |
|---|---|
| Account experience | dashboard, YTD summary, activity, transaction history |
| Portfolio | investments, balance trend, performance, stackup |
| Banks | list/detail, add, update, delete |
| Contributions | options/check/detail, create, update, delete |
| Reference/content | content and plans/list/detail |
| Engagement | UGift page and UGift assignment |

IDs M2-01 through M2-25 trace each row to its TestNG class, method, suite, plants, and legacy/Postman source.

Publish under "Unite MSC API Automation", then continue with Part B.
