PART A of 2. Create a polished SharePoint Site Page titled "11 Extend the Automation".

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
- Build only this part. Leave the page ready for the next part; do not add the Source and ownership band.

CONTENT:

# 11 Extend the Automation
Purpose: How to add a scenario safely, including AI-assisted authoring and the definition of done.

## Add a scenario from an existing pattern
1. Identify the endpoint row and nearest canonical TestNG class in https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/mobile?ref_type=heads
2. Confirm method, path, and plant behavior with approved source evidence.
3. Review the matching manual request in https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/bruno/Mobile/mobile-msc/Unite-MSC-Bruno_collection?ref_type=heads
4. Review or create the manual case in https://ascensus.qtestnet.com/p/118829/portal/project#id=69212334&object=0&tab=testdesign
5. Link the manual and automated coverage to the delivering story under https://ascensuscollegesavings.atlassian.net/browse/QA-796
6. Reuse the module base test and framework helpers.
7. Use encrypted POST handling for Enrollment.
8. Add lean L1-L4 assertions; do not dump full PII responses.
9. Wire the class into every intended XML and Maven profile.
10. Update the module coverage register.
11. Run targeted, module, and applicable master suites.
12. Attach sanitized evidence and obtain review.

Publish under "Unite MSC API Automation", then continue with Part B.
