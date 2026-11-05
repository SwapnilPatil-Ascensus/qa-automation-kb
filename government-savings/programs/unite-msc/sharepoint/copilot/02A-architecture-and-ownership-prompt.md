PART A of 4. Create a polished SharePoint Site Page titled "02 Architecture and Ownership".

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
- Keep each diagram in one full-width monospace block, character for character; never redraw it.
- Build only this part. Leave the page ready for the next part; do not add the Source and ownership band.

CONTENT:

# 02 Architecture and Ownership
Purpose: A practical map of the canonical TestNG architecture, shared framework, module inheritance, test data, reporting, legacy references, and ownership.

## 1. Canonical runtime flow
Render this diagram as a full-width monospace block, exactly as written:

  [ mvn -P<suite-profile>,<environment-profile> ]
                    |
                    v
  [ TestNG suite XML ] -- branding parameter: okdirect | newyork | nmdirect
                    |
                    v
  [ module test class ]  mobile1 | mobile2 | enrollment
                    |
                    v
  [ module base class ] MobileBaseRequestTest | EnrollmentBaseTest
       |                                   |
       |                                   +-- Enrollment only:
       +-- Oracle: automation user,             GET certificate, AES key,
           app version, routing, fund,          @MobileEncrypt payloads
           contribution fixtures
                    |
                    v
  [ jsonapi-core BaseRequestTest + Rest Assured client ]
                    |
                    v
  [ Unite MSC BFF route ] <- environment.properties + host overlay
                    |
                    v
  [ downstream MSC services ] -> [ Oracle ]
                    |
                    v
  [ L1-L4 assertions ] -> [ HTML portal + Surefire ]

The canonical stack is JDK 17, Maven, TestNG, Rest Assured, jsonapi-core, Oracle-backed test data, and Extent-based HTML reporting. It replaces the legacy Cucumber implementation; do not add new API coverage to the V2 or V3 UI repositories.

Publish under "Unite MSC API Automation", then continue with Part B.
