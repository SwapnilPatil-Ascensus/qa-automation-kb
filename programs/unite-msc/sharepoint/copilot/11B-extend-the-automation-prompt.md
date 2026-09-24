PART B of 2. Edit the existing SharePoint page "11 Extend the Automation" on API Testing Documentation Hub.

Append below existing content. Match its hero palette, table, section, callout, code, and checklist styling. Do not duplicate the hero, breadcrumb, or existing sections.

Finish with the gray Source and ownership band below.

Final band: owner QA Automation; GitLab api-test-automation is executable source of truth; credentials, tokens, certificates, host properties, environment files, DB connection strings, and raw PII stay out of SharePoint.

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

APPEND EXACTLY:

## AI-assisted prompt pattern
Render as a preformatted code block:

Add a TestNG case for {METHOD} {PATH} in {MODULE}.
Follow {EXISTING_CLASS}; do not change shared framework APIs.
Do not log JWT, password, SSN, or full personal payloads.
Add lean status and key business assertions.
Wire only the approved plants and suite XMLs.
Update the endpoint coverage register.

Caution callout: human review is mandatory. AI must not invent endpoints, expected values, SQL mappings, plants, or credentials.

## Definition of done
- [ ] Code review complete and pipeline green.
- [ ] Test is wired to the intended suite, not merely present.
- [ ] Existing module and master suites show no unintended regression.
- [ ] Coverage and traceability register updated.
- [ ] Secrets scan clean.
- [ ] Operational documentation updated when commands, environments, or ownership change.

## Reference downloads
Use the page library for approved sign-off, coverage, and traceability attachments.

- Automated code and configuration: https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation
- Mobile implementation: https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/mobile?ref_type=heads
- Manual API testing in Bruno: https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/bruno/Mobile/mobile-msc/Unite-MSC-Bruno_collection?ref_type=heads
- Manual test cases in qTest Test Design: https://ascensus.qtestnet.com/p/118829/portal/project#id=69212334&object=0&tab=testdesign
- Unite MSC Jira Epic and related stories: https://ascensuscollegesavings.atlassian.net/browse/QA-796

Republish the page when finished.
