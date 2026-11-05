PART C of 3. Edit the existing SharePoint page "06 Mobile 2 Automation" on API Testing Documentation Hub.

Append below existing content. Match its hero palette, table, section, callout, code, and checklist styling. Do not duplicate the hero, breadcrumb, or existing sections.

Finish with the gray Source and ownership band below.

Final band: owner QA Automation; GitLab api-test-automation is executable source of truth; credentials, tokens, certificates, host properties, environment files, DB connection strings, and raw PII stay out of SharePoint.

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

APPEND EXACTLY:

## 5. Run and read the result
Regression command:

mvn -f mobile/mobile2/pom.xml test "-Pmobile2-regression,acceptance-stage1" "-Dhost.properties=<COMPUTERNAME>.properties" "-Dmobile.ms.report.environment=Stage1"

Other profiles: mobile2-integration, mobile2-smoke, mobile2-localhost. Keep the environment profile last. If Mobile 2 compilation is stale, delete mobile/mobile2/target/maven-compile; delete Mobile 1's compiled output too if the inherited auth class is stale.

Report: mobile/mobile2/target/mobile-ms-report/index.html.

## 6. Evidence and downloads
| Artifact | Use |
|---|---|
| Mobile 2 API Automation Sign-Off (DOCX) | Formal scope and completion record |
| mobile2-endpoint-current-state.csv | Endpoint to class to suite mapping |
| unite-msc-endpoint-summary.csv | Compact evidence register |
| Coverage chart | Optional executive visual |
| GitLab mobile/mobile2 | Executable source of truth |
| Bruno 03 - Mobile2 | Manual request exploration |
| qTest MSC-Mobile2 | Manual test cases: https://ascensus.qtestnet.com/p/118829/portal/project#id=69233940&object=0&tab=testdesign |

## 7. Known boundaries and enhancements
Caution callout:
- Destructive bank/contribution cases stay separated from broad regression.
- Dynamic fixtures can fail after an Oracle refresh even when the API is healthy.
- POST mobilebanks?planId=upromise is optional enhancement scope, not part of the 24 signed-off business operations.
- Two MobileStackupRequestTest package locations are a cleanup candidate; do not duplicate a third.

Use current GitLab POM/XML as executable truth. Capture row ID, class/method, branding, suite, environment, status, and sanitized report during triage.

Republish the page when finished.
