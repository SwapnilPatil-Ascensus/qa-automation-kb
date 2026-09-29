PART C of 4. Edit the existing SharePoint page "01 KT and Onboarding" on API Testing Documentation Hub.

Append below existing content. Match its hero palette, table, section, callout, code, and checklist styling. Do not duplicate the hero, breadcrumb, or existing sections.

Leave the page open for the next part.

Final band: owner QA Automation; GitLab api-test-automation is executable source of truth; credentials, tokens, certificates, host properties, environment files, DB connection strings, and raw PII stay out of SharePoint.

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

APPEND EXACTLY:

## 6. Run your first suite
Start with the Enrollment smoke suite; it is the least destructive. Replace <COMPUTERNAME> with your own overlay name.

mvn -f mobile/enrollment/pom.xml test "-Pmobile-ms-enrollment-smoke,acceptance-stage1" "-Dhost.properties=<COMPUTERNAME>.properties" "-Dmobile.ms.report.environment=Stage1"

mvn -f mobile/mobile1/pom.xml test "-Pmobile1-regression,acceptance-stage1" "-Dhost.properties=<COMPUTERNAME>.properties" "-Dmobile.ms.report.environment=Stage1"

mvn -f mobile/mobile2/pom.xml test "-Pmobile2-regression,acceptance-stage1" "-Dhost.properties=<COMPUTERNAME>.properties" "-Dmobile.ms.report.environment=Stage1"

For ad-hoc local work, copy the example suite first, then use the localhost profile:

copy mobile\mobile1\testsuites\localhost-testng.xml.example mobile\mobile1\testsuites\localhost-testng.xml
mvn -f mobile/mobile1/pom.xml test "-Pmobile1-localhost,acceptance-stage1" "-Dhost.properties=<COMPUTERNAME>.properties"

Swap acceptance-stage1 for acceptance-qc4 to target QC4.

## 7. Find your report
| Output | Path |
|---|---|
| HTML report | <module>/target/mobile-ms-report/index.html |
| TestNG and Surefire output | <module>/target/surefire-reports/ |

Open it directly, for example: start mobile\enrollment\target\mobile-ms-report\index.html

Plans run as a TestNG branding parameter: okdirect, newyork, nmdirect.

## 8. Manual API testing: Bruno and Postman
Use these to explore an endpoint before writing or debugging a TestNG case.

| Tool | Location | Contents |
|---|---|---|
| Bruno | bruno/Mobile/mobile-msc/Unite-MSC-Bruno_collection | Folders 01 - Enrollment, 02 - Mobile1, 03 - Mobile2 |
| Bruno environments | Same collection, environments/ | Env-Enrollment-Stage1.yml, Env-Mobile1-Stage1.yml, Env-Mobile2-Stage1.yml |
| Postman | postman/mobile | Mobile Endpoints (w/ IDP Session) for PKCE, member session, and token exchange |

Bruno collection: https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/bruno/Mobile/mobile-msc/Unite-MSC-Bruno_collection?ref_type=heads

Manual test cases (qTest):
| Module | qTest Test Design |
|---|---|
| Unite-MSC (parent) | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212334&object=0&tab=testdesign |
| MSC-Enrollment | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212335&object=0&tab=testdesign |
| MSC-Mobile1 | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212337&object=0&tab=testdesign |
| MSC-Mobile2 | https://ascensus.qtestnet.com/p/118829/portal/project#id=69233940&object=0&tab=testdesign |

Prohibition callout: treat populated Bruno/Postman environment files as sensitive operational material. Do not paste their values into SharePoint, Jira, Teams, or prompts; use a stripped local demo environment.

Republish the page when finished.
