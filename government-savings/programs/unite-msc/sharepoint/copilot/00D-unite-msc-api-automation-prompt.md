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

## Validation and sign-off bar
| Layer | Meaning | Sign-off |
|---|---|---|
| L1 | HTTP status and transport | Required |
| L2 | Contract and response shape | Required |
| L3 | Schema and typed payload | Required where supported |
| L4 | Business assertions | Required |
| L5 | API-to-database field reconciliation | Optional enhancement; not the completion gate |

Leadership directed that L5 SQL field reconciliation is not the completion gate. Do not claim L5 is implemented.

## Authoritative project links
Render these as a prominent Quick Links web part using labeled tiles.

| Resource | Purpose | URL |
|---|---|---|
| API Test Automation repository | Canonical automation repository | https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation |
| Mobile automation folder | Mobile 1, Mobile 2, Enrollment, and reporting code | https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/mobile?ref_type=heads |
| Unite MSC Bruno collection | Manual API exploration and testing collection | https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/bruno/Mobile/mobile-msc/Unite-MSC-Bruno_collection?ref_type=heads |
| Unite MSC Epic QA-796 | Jira delivery scope and related stories | https://ascensuscollegesavings.atlassian.net/browse/QA-796 |

### Manual test cases (qTest Test Design)
| Module | qTest Test Design |
|---|---|
| Unite-MSC (parent) | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212334&object=0&tab=testdesign |
| MSC-Enrollment | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212335&object=0&tab=testdesign |
| MSC-Mobile1 | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212337&object=0&tab=testdesign |
| MSC-Mobile2 | https://ascensus.qtestnet.com/p/118829/portal/project#id=69233940&object=0&tab=testdesign |

Informational callout: the manual test cases live in these four qTest modules, not Confluence. SharePoint provides navigation and operating guidance. qTest is the manual-test system of record. Jira is the delivery system of record. GitLab is the executable system of record.

## Source-of-truth and security
Informational callout: SharePoint explains how to use and support the automation. GitLab remains the source of truth for Java, suite XML, Maven profiles, Bruno, Postman, SQL, and pipeline configuration.

Repository: https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation
Mobile code: https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/mobile?ref_type=heads
Published documentation: this parent page and its eleven child pages on the API Testing Documentation Hub.

Prohibition callout: never paste passwords, JWT, SSN, certificates, host properties, environment JSON, database connection strings, or raw PII onto this page or any child page.

Republish the page when finished.
