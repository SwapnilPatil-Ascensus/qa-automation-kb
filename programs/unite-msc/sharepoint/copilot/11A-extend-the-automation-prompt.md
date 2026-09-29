PART A of 4. Create a polished SharePoint Site Page titled "11 Extend the Automation".

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

Quick links row for this page: Parent: Unite MSC API Automation | Previous: 10 Test Data, DB Refresh and Security

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.
- Keep each diagram in one full-width monospace block, character for character; never redraw it.
- Build only this part. Leave the page ready for the next part; do not add the Source and ownership band.

CONTENT:

# 11 Extend the Automation
Purpose: New-endpoint playbook and prompt library: discovery, TestNG implementation, encryption/data, suite wiring, Bruno/qTest/Jira traceability, verification, review, and documentation.

## 1. The new-endpoint workflow
Render this diagram as a full-width monospace block, exactly as written:

  [ intake ]     contract, auth, branding, data, safety, suites
        v
  [ discovery ]  reference class, POM, suite XML, fixtures,
                 Bruno request, qTest case
        v
  [ implement ]  POJO -> base-class auth -> request -> L1-L4
        v
  [ wire ]       group -> every branding block -> suite XML
                 -> Maven profile -> report listener
        v
  [ verify ]     compile -> targeted -> one branding
                 -> all brandings -> impacted regression
        v
  [ trace ]      Bruno request -> qTest case -> Jira link
                 -> coverage register
        v
  [ review ]     merge request: Summary, Related, Test plan, Risks
        v
  [ done ]       wired, evidenced, registers updated

Skipping the wire step is the most common failure: the code compiles and passes locally but never runs in any suite, so it is not delivered coverage.

Publish under "Unite MSC API Automation", then continue with Part B.
