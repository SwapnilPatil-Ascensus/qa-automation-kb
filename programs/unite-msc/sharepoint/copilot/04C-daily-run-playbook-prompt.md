PART C of 3. Edit the existing SharePoint page "04 Daily Run Playbook" on API Testing Documentation Hub.

Append below existing content. Match its hero palette, table, section, callout, code, and checklist styling. Do not duplicate the hero, breadcrumb, or existing sections.

Finish with the gray Source and ownership band below.

Final band: owner QA Automation; GitLab api-test-automation is executable source of truth; credentials, tokens, certificates, host properties, environment files, DB connection strings, and raw PII stay out of SharePoint.

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

APPEND EXACTLY:

## 5. Local targeted workflow
1. Copy testsuites/localhost-testng.xml.example to localhost-testng.xml.
2. Keep one intended branding block and the required setup/target classes.
3. Never edit shared regression XML merely to debug locally.
4. For Enrollment, preserve the ordered prerequisite chain through the failing step.
5. Run the module localhost profile with the environment profile last.
6. Restore or discard only your gitignored localhost file after diagnosis.

## 6. Read the result
1. Open <module>/target/mobile-ms-report/index.html.
2. Confirm suite/module/environment labels.
3. Review pass/fail/skip totals and earliest failure.
4. Open extent/detail.html for test detail.
5. Use target/surefire-reports only for compile/setup stack traces or JUnit XML.
6. In an ordered Enrollment chain, fix the first failure before treating later skips as defects.

## 7. Classify and act
| Result | Action |
|---|---|
| Green | Record command, environment, branding, commit, report artifact |
| Environment/service | Record timestamp/status/dependency; do not edit tests |
| Oracle/test data | Restore only approved automation fixtures |
| Automation | Reproduce targeted; fix class/XML/profile/reporting wiring |
| Product/contract | Follow automation bug lifecycle with sanitized evidence |
| Expected exclusion | Link sign-off/backlog; do not report as missing coverage |

## 8. Run record
Minimum evidence:
- module and profile command;
- environment and branding;
- commit SHA and run timestamp;
- passed/failed/skipped counts;
- first failure class/method and endpoint ID;
- sanitized portal/Surefire or GitLab artifact;
- classification and Jira link.

Code presence is not fresh execution evidence.

## 9. Run discipline
Prohibition callout:
- Do not silently remove classes from XML to make a run green.
- Quarantine only with a visible tag or exclusion and a linked follow-up.
- Do not commit target/.
- Do not loop-retry an environment-wide failure.
- Do not rerun destructive tests against unknown records.
- Do not attach raw request or response payloads containing PII or JWT.

Republish the page when finished.
