Create a modern, visually polished SharePoint Site Page titled "01 KT and Onboarding".

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

Quick links row for this page: Parent: Unite MSC API Automation | Previous: Unite MSC API Automation | Next: 02 Architecture and Ownership

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

PAGE CONTENT — build the page from exactly this material:

# 01 KT and Onboarding
Purpose: A receiving engineer can find the code, run one safe suite, locate a report, and know where to ask for help.

## First-week path
| Day | Task | Evidence |
|---|---|---|
| 1 | Confirm GitLab, Jira, VPN, Java 17, Maven 3.9+, and approved DB access | Access checklist complete |
| 2 | Clone api-test-automation; build the mobile parent with tests skipped | Successful Maven build |
| 3 | Run one smoke profile using a local gitignored host overlay | HTML/Surefire report |
| 4 | Trace one endpoint from CSV to Java class to suite XML to report | Review notes |
| 5 | Shadow failure triage and DB-refresh preparation | KT sign-off |

## What to read, in order
1. 02 Architecture and Ownership
2. 03 Access, Setup and Environments
3. 04 Daily Run Playbook
4. The applicable module page: 05, 06, or 07
5. 09 Reporting and Troubleshooting
6. 10 Test Data, DB Refresh and Security
7. Review the Unite MSC Epic: https://ascensuscollegesavings.atlassian.net/browse/QA-796
8. Review manual cases in qTest Test Design: https://ascensus.qtestnet.com/p/118829/portal/project#id=69212334&object=0&tab=testdesign
9. Open the manual API collection in Bruno: https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/bruno/Mobile/mobile-msc/Unite-MSC-Bruno_collection?ref_type=heads

## KT demonstration
The engineer must demonstrate each of these live:
- Find a test class from an endpoint ID in the coverage register.
- Show which XML suite and Maven profile execute it.
- Run a non-destructive smoke or targeted test.
- Find the generated report and classify one sample failure.
- Explain what changes after a Stage1 or QC4 database refresh.
- Explain the L1-L4 validation boundary and why L5 SQL is not the completion gate.

## Completion checklist
- [ ] Engineer can run without copying another person's host file.
- [ ] Engineer knows credentials, JWT, SSN, and environment JSON never go in SharePoint or Git.
- [ ] Engineer can distinguish environment, data, automation, and product failures.
- [ ] Engineer knows Mobile 1, Mobile 2, and Enrollment ownership boundaries.
- [ ] KT reviewer records open questions and owners rather than inventing answers.

After generating, verify the page title, the breadcrumb, the quick links, and the Source and ownership band, then publish under "Unite MSC API Automation".
