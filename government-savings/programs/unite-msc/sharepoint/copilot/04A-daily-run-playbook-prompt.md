PART A of 3. Create a polished SharePoint Site Page titled "04 Daily Run Playbook".

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

Quick links row for this page: Parent: Unite MSC API Automation | Previous: 03 Access, Setup and Environments | Next: 05 Mobile 1 Automation

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.
- Keep each diagram in one full-width monospace block, character for character; never redraw it.
- Build only this part. Leave the page ready for the next part; do not add the Source and ownership band.

CONTENT:

# 04 Daily Run Playbook
Purpose: Repeatable daily workflow: choose the safe suite, verify data/environment, run the correct profile, inspect the portal, classify failures, and preserve evidence.

## 1. The daily loop
Render this diagram as a full-width monospace block, exactly as written:

              what do you need today?
                        |
   +---------+----------+-----------+-------------+
   |         |          |           |             |
 is the    broad      proof in   mutating or   debugging
 service   module     selected     strict      one class
 healthy?  proof      environment  checks          |
   |         |          |           |              |
Enrollment regression integration  smoke     gitignored
  smoke    (Stage1)    (QC4)     (check owned localhost
                                  state first)    XML
   +---------+----------+-----------+-------------+
                        |
                        v
   mvn -f mobile/<module>/pom.xml test
       "-P<suite>,<environment LAST>"
                        |
                        v
   <module>/target/mobile-ms-report/index.html
                        |
                 earliest failure
                        |
   +--------+-----------+----------+-----------+
   |        |           |          |           |
 green  environment   data    automation    product
record   no code    restore    fix class   bug lifecycle
         change     fixtures   or wiring    + evidence

Work top to bottom every day. Pick the suite first, gate the run second, then read the report before changing a single line of test code.

Publish under "Unite MSC API Automation", then continue with Part B.
