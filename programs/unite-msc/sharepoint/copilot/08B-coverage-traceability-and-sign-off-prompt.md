PART B of 3. Edit the existing SharePoint page "08 Coverage, Traceability and Sign-off" on API Testing Documentation Hub.

Append below existing content. Match its hero palette, table, section, callout, code, and checklist styling. Do not duplicate the hero, breadcrumb, or existing sections.

Leave the page open for the next part.

Final band: owner QA Automation; GitLab api-test-automation is executable source of truth; credentials, tokens, certificates, host properties, environment files, DB connection strings, and raw PII stay out of SharePoint.

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

APPEND EXACTLY:

## 4. Coverage sources
| Source | System of record |
|---|---|
| Mobile 1 | mobile1-endpoint-current-state.csv |
| Mobile 2 | mobile2-endpoint-current-state.csv |
| Enrollment | enrollment-endpoint-current-state.csv and the coverage workbook |
| Legacy to canonical | legacy-to-canonical-traceability.csv |
| Automated implementation | https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/mobile?ref_type=heads |
| Manual API collection | https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/bruno/Mobile/mobile-msc/Unite-MSC-Bruno_collection?ref_type=heads |
| Delivery scope and stories | https://ascensuscollegesavings.atlassian.net/browse/QA-796 |

Manual test cases (qTest):
| Module | qTest Test Design |
|---|---|
| Unite-MSC (parent) | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212334&object=0&tab=testdesign |
| MSC-Enrollment | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212335&object=0&tab=testdesign |
| MSC-Mobile1 | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212337&object=0&tab=testdesign |
| MSC-Mobile2 | https://ascensus.qtestnet.com/p/118829/portal/project#id=69233940&object=0&tab=testdesign |

## 5. Trace one endpoint end to end
1. Pick the endpoint ID in the module register.
2. Confirm method/path, feature area, migration status, validation layers, and branding.
3. Open the canonical Java class/method in https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/mobile?ref_type=heads
4. Confirm its suite XML, Maven profile, groups, and every intended branding block.
5. Confirm the manual Bruno request where one exists: https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/bruno/Mobile/mobile-msc/Unite-MSC-Bruno_collection?ref_type=heads
6. Confirm or create the qTest manual case in the matching module folder (Unite-MSC, MSC-Enrollment, MSC-Mobile1, or MSC-Mobile2).
7. Link the case and automation evidence to the delivering Jira story under https://ascensuscollegesavings.atlassian.net/browse/QA-796
8. Open the formal sign-off pack for exclusions/approvals.
9. Attach a sanitized report or job artifact; never use code presence as run evidence.

qTest modules:
| Module | qTest Test Design |
|---|---|
| Unite-MSC (parent) | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212334&object=0&tab=testdesign |
| MSC-Enrollment | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212335&object=0&tab=testdesign |
| MSC-Mobile1 | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212337&object=0&tab=testdesign |
| MSC-Mobile2 | https://ascensus.qtestnet.com/p/118829/portal/project#id=69233940&object=0&tab=testdesign |

Republish the page when finished.
