Create a modern, visually polished SharePoint Site Page titled "10 Test Data, DB Refresh and Security".

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

Quick links row for this page: Parent: Unite MSC API Automation | Previous: 09 Reporting and Troubleshooting | Next: 11 Extend the Automation

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

PAGE CONTENT — build the page from exactly this material:

# 10 Test Data, DB Refresh and Security
Purpose: How to keep automation data valid, what to do after a refresh, and what must never reach SharePoint.

## Test-data principles
- Use automation-owned users and accounts, for example approved QAAUTOTEST patterns.
- Generate unique data where the flow supports it.
- Do not mutate arbitrary records returned by broad random SQL.
- Record plant and environment with evidence.

## After a database refresh
1. Confirm environment restoration is complete.
2. Restore or recreate approved automation accounts.
3. Confirm MFA and IDP prerequisites for the selected plants.
4. Confirm plan metadata, app version, routing, and fund fixtures.
5. Validate VPN, Frogger, and database connectivity.
6. Run the smallest smoke suite.
7. Run targeted module regression only after smoke is green.
8. Record remaining environment gaps in RAID or Jira.

## SQL boundary
Enrollment SQL in Git supports test-data setup and post-account verification. Mobile 1 and Mobile 2 field-level SQL analysis exists for future work. Leadership approved L1-L4 as the completion bar; do not claim L5 is implemented.

## Never upload to SharePoint
Prohibition callout:
- Postman environment JSON.
- Local host or property overlays.
- Passwords, tokens, certificates, private keys, SSN, or raw PII.
- Database connection strings.
- Raw SQL exports containing customer-like data.
- target/ reports that include unsanitized payloads.

SharePoint links to controlled Git paths and ticketing processes. It is not a secret store or an executable configuration source.

After generating, verify the page title, the breadcrumb, the quick links, and the Source and ownership band, then publish under "Unite MSC API Automation".
