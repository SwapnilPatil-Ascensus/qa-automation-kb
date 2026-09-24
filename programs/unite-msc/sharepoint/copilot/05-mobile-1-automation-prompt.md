Create a modern, visually polished SharePoint Site Page titled "05 Mobile 1 Automation".

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

PAGE CONTENT — build the page from exactly this material:

# 05 Mobile 1 Automation
Purpose: Scope, plants, artifacts, and known considerations for Mobile 1 API automation.

## Scope
Code: api-test-automation/mobile/mobile1/

Mobile 1 documents 26 coded operations covering member session and authentication, username, owner and profile, beneficiary and account closure, routing information, biometric, phone authentication, device and push tokens, password, CSR-as-member, IDP token exchange, session lookup, biometric validation, and session PIN.

## Plants and suites
- OK Direct is the primary non-IDP path.
- NM Direct is used on applicable authentication and IDP paths.
- Destructive updates and deletes belong in smoke or targeted suites, not an unattended master run unless explicitly designed.

## Support files
| Artifact | Use |
|---|---|
| Mobile 1 API Automation Sign-Off (DOCX) | Formal scope and completion record |
| mobile1-endpoint-current-state.csv | Endpoint to class to suite mapping |
| mobile1-signoff-summary.md | Quick status |
| Coverage chart image | Optional visual |

## Known considerations
Caution callout:
- IDP token tests exist in canonical TestNG; legacy Cucumber did not cover the IDP feature.
- QC4 automation JWT behavior can produce environment-dependent 401 responses.
- PATCH logout remains an enhancement candidate.
- L5 SQL analysis is not implemented as the completion gate.

When a case fails, record endpoint ID, class, method, plant, environment, and report - not only a screenshot.

After generating, verify the page title, the breadcrumb, the quick links, and the Source and ownership band, then publish under "Unite MSC API Automation".
