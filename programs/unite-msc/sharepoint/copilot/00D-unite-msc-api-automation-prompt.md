PART D of 4. Edit the existing SharePoint page "Unite MSC API Automation" on API Testing Documentation Hub.

Append below existing content. Match its hero palette, table, section, callout, code, and checklist styling. Do not duplicate the hero, breadcrumb, or existing sections.

Finish with the gray Source and ownership band below.

Final band: owner QA Automation; GitLab api-test-automation is executable source of truth; credentials, tokens, certificates, host properties, environment files, DB connection strings, and raw PII stay out of SharePoint.

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

APPEND EXACTLY:

## Authoritative project links
Render these as a prominent Quick Links web part using labeled tiles.

| Resource | Purpose | URL |
|---|---|---|
| API Test Automation repository | Canonical automation repository | https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation |
| Mobile automation folder | Mobile 1, Mobile 2, Enrollment, and reporting code | https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/mobile?ref_type=heads |
| Unite MSC Bruno collection | Manual API exploration and testing collection | https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/bruno/Mobile/mobile-msc/Unite-MSC-Bruno_collection?ref_type=heads |
| qTest Test Design | Manual Unite MSC test cases and traceability | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212334&object=0&tab=testdesign |
| Unite MSC Epic QA-796 | Jira delivery scope and related stories | https://ascensuscollegesavings.atlassian.net/browse/QA-796 |

Informational callout: the manual test cases are in qTest Test Design, not Confluence. SharePoint provides navigation and operating guidance. qTest is the manual-test system of record. Jira is the delivery system of record. GitLab is the executable system of record.

## Source-of-truth and security
Informational callout: SharePoint explains how to use and support the automation. GitLab remains the source of truth for Java, suite XML, Maven profiles, Bruno, Postman, SQL, and pipeline configuration.

Repository: https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation
Mobile code: https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/mobile?ref_type=heads
Published documentation: this parent page and its eleven child pages on the API Testing Documentation Hub.

Prohibition callout: never paste passwords, JWT, SSN, certificates, host properties, environment JSON, database connection strings, or raw PII onto this page or any child page.

Republish the page when finished.
