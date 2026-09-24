Create a modern, visually polished SharePoint Site Page titled "04 Daily Run Playbook".

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

PAGE CONTENT — build the page from exactly this material:

# 04 Daily Run Playbook
Purpose: The day-to-day procedure for running a suite and handling the result.

## Before every run
1. Confirm the intended module, plant, environment, and suite.
2. Confirm VPN or Frogger connectivity and environment health.
3. Check whether a database refresh occurred.
4. Use automation-owned data; do not select arbitrary customer-like records.
5. Ensure the local host overlay is present and gitignored.

## Enrollment run examples
Render as a preformatted code block:

# Stage1 smoke
mvn -f mobile/enrollment/pom.xml test "-Pmobile-ms-enrollment-smoke,acceptance-stage1" "-Dhost.properties=<YOUR_HOST_FILE>"

# Stage1 regression: OK Direct and New York
mvn -f mobile/enrollment/pom.xml test "-Pmobile-ms-enrollment-regression,acceptance-stage1" "-Dhost.properties=<YOUR_HOST_FILE>"

# QC4 integration
mvn -f mobile/enrollment/pom.xml test "-Pmobile-ms-enrollment-integration,acceptance-qc4" "-Denvironment.properties=qc4.properties" "-Dhost.properties=<APPROVED_QC4_FILE>"

For Mobile 1 and Mobile 2, use the Maven profiles documented in their module POM and suite XML. Do not guess a profile from an old Confluence page.

## After every run
| Result | Action |
|---|---|
| Green | Save the run URL or report when evidence is required |
| Environment failure | Record endpoint, environment, timestamp, and dependency |
| Data failure | Refresh only automation-owned fixtures |
| Automation failure | Reproduce targeted; link class and suite |
| Product failure | Follow the automation bug lifecycle with sanitized evidence |

## Run discipline
Prohibition callout:
- Do not silently remove classes from XML to make a run green.
- Quarantine only with a visible tag or exclusion and a linked follow-up.
- Do not commit target/.
- Do not attach raw request or response payloads containing PII or JWT.

After generating, verify the page title, the breadcrumb, the quick links, and the Source and ownership band, then publish under "Unite MSC API Automation".
