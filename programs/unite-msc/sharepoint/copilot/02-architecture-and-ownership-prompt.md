Create a modern, visually polished SharePoint Site Page titled "02 Architecture and Ownership".

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

Quick links row for this page: Parent: Unite MSC API Automation | Previous: 01 KT and Onboarding | Next: 03 Access, Setup and Environments

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

PAGE CONTENT — build the page from exactly this material:

# 02 Architecture and Ownership
Purpose: How the canonical automation is built, which repository owns what, and where the validation boundary sits.

## Runtime model
Render as a preformatted code block:

TestNG test class
  -> module base test / shared jsonapi framework
  -> Rest Assured request and L1-L4 assertions
  -> Unite MSC BFF endpoint
  -> downstream account, profile, bank, metadata, transaction, auth services

The canonical automation is Java 17, Maven, TestNG, and Rest Assured. It is not the legacy Cucumber implementation.

## Repository map
Mobile root: https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/mobile?ref_type=heads

| Area | GitLab path | Purpose |
|---|---|---|
| Mobile parent | mobile/pom.xml | Shared module build |
| Mobile 1 | mobile/mobile1/ | Authentication, profile, device, biometric, session APIs |
| Mobile 2 | mobile/mobile2/ | Dashboard, bank, contribution, activity, plans, performance APIs |
| Enrollment | mobile/enrollment/ | Encrypted enrollment wizard and subsequent enrollment |
| Shared reporting | mobile/reporting/ or module report wiring | HTML and test evidence |
| Manual API testing | https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/bruno/Mobile/mobile-msc/Unite-MSC-Bruno_collection?ref_type=heads | Unite MSC Bruno collection |

## Validation boundary
| Layer | Meaning | Sign-off |
|---|---|---|
| L1 | HTTP status and transport | Required |
| L2 | Contract and response shape | Required |
| L3 | Schema and typed payload | Required where supported |
| L4 | Business assertions | Required |
| L5 | API-to-database field reconciliation | Optional enhancement; not the completion gate |

## Ownership
- QA Automation owns framework patterns, TestNG tests, suite XML, reports, and coverage registers.
- DevOps owns or partners on runners, schedules, secure files, and pipeline hard gates.
- Product and development SMEs own service behavior and approve unknown API-to-database mappings.
- The receiving team owns steady-state runs, triage, test-data upkeep, and approved enhancements after handoff.

Caution callout: named approvers remain required wherever sign-off documents still contain [NEED_INPUT].

After generating, verify the page title, the breadcrumb, the quick links, and the Source and ownership band, then publish under "Unite MSC API Automation".
