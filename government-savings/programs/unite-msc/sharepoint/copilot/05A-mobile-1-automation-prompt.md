PART A of 3. Create a polished SharePoint Site Page titled "05 Mobile 1 Automation".

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

Quick links row for this page: Parent: Unite MSC API Automation | Previous: 04 Daily Run Playbook | Next: 06 Mobile 2 Automation

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.
- Build only this part. Leave the page ready for the next part; do not add the Source and ownership band.

CONTENT:

# 05 Mobile 1 Automation
Purpose: Complete operating guide for Mobile 1: delivered coverage, endpoint families, authentication/data model, suite design, execution, evidence, and safe extension.

## 1. What was delivered
| Metric | Delivered |
|---|---|
| Endpoint operations automated | 26 of 26 documented |
| TestNG @Test methods | 27 |
| Validation | L1-L4 lean assertions |
| Branding in current regression/integration XML | okdirect, newyork, nmdirect |
| Sign-off | COMPLETE |

This is a full canonical migration, not a wrapper around legacy Cucumber. It adds current TestNG, SQL-driven automation users, mobile/IDP authentication, multi-plan XML execution, and the shared HTML reporting portal.

## 2. Endpoint families
| Family | Coverage |
|---|---|
| Authentication | member session, username, CSR-as-member, IDP exchange, IDP-to-member token |
| Profile and beneficiary | owner/profile menus, owner update, beneficiary lookup, close-account checks |
| Security and device | biometric POST/GET/DELETE, phone authentication, devices, push tokens |
| Session | session by ID, biometric-token validation, session PIN |
| Account utility | routing-number bank info, password change and re-login |

The register assigns stable IDs M1-01 through M1-26 so an endpoint can be traced from sign-off CSV to Java method, suite, evidence, qTest, and Jira.

Publish under "Unite MSC API Automation", then continue with Part B.
