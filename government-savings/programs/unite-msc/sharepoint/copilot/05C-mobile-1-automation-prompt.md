PART C of 3. Edit the existing SharePoint page "05 Mobile 1 Automation" on API Testing Documentation Hub.

Append below existing content. Match its hero palette, table, section, callout, code, and checklist styling. Do not duplicate the hero, breadcrumb, or existing sections.

Finish with the gray Source and ownership band below.

Final band: owner QA Automation; GitLab api-test-automation is executable source of truth; credentials, tokens, certificates, host properties, environment files, DB connection strings, and raw PII stay out of SharePoint.

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

APPEND EXACTLY:

## 5. Test data resolution
MobileBaseRequestTest loads mobile.sql before the suite:

1. Selects an active automation-owned member for the current branding.
2. Requires the approved MFA-skip condition.
3. Resolves account extension, member ID, minimum app version, and routing/fixture data from Oracle.
4. Configures mobile session auth or IDP auth based on plan metadata.
5. Probes several candidate users for IDP-enabled plans and caches a working user.

Do not hardcode a customer, password, account extension, app version, or src/test/resources/user JSON into a new test.

## 6. Run and read the result
Regression command:

mvn -f mobile/mobile1/pom.xml test "-Pmobile1-regression,acceptance-stage1" "-Dhost.properties=<COMPUTERNAME>.properties" "-Dmobile.ms.report.environment=Stage1"

Other suite profiles: mobile1-integration, mobile1-smoke, mobile1-localhost. Keep acceptance-stage1 or acceptance-qc4 LAST.

Open target/mobile-ms-report/index.html for the portal and target/surefire-reports/ for TestNG detail.

## 7. Evidence and downloads
| Artifact | Use |
|---|---|
| Mobile 1 API Automation Sign-Off (DOCX) | Formal scope and completion record |
| mobile1-endpoint-current-state.csv | Endpoint to class to suite mapping |
| mobile1-signoff-summary.md | Quick status |
| Coverage chart | Optional executive visual |
| GitLab mobile/mobile1 | Executable source of truth |
| Bruno 02 - Mobile1 | Manual request exploration |
| qTest MSC-Mobile1 | Manual test cases: https://ascensus.qtestnet.com/p/118829/portal/project#id=69212337&object=0&tab=testdesign |

## 8. Known boundaries and first checks
Caution callout:
- Canonical TestNG includes IDP token exchange that legacy Cucumber did not.
- A QC4 401 can be an environment/IDP automation-JWT issue, not a missing class.
- PATCH logout remains an enhancement; do not count it as delivered.
- L5 field-by-field SQL reconciliation was analyzed but is not the sign-off gate.

When a case fails, capture endpoint ID, Java class/method, suite, branding, environment, HTTP status, and sanitized report link—not only a screenshot.

Republish the page when finished.
