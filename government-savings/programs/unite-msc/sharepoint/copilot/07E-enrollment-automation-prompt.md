PART E of 5. Edit the existing SharePoint page "07 Enrollment Automation" on API Testing Documentation Hub.

Append below existing content. Match its hero palette, table, section, callout, code, and checklist styling. Do not duplicate the hero, breadcrumb, or existing sections.

Finish with the gray Source and ownership band below.

Final band: owner QA Automation; GitLab api-test-automation is executable source of truth; credentials, tokens, certificates, host properties, environment files, DB connection strings, and raw PII stay out of SharePoint.

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

APPEND EXACTLY:

## 7. Run and report
Smoke:
mvn -f mobile/enrollment/pom.xml test "-Pmobile-ms-enrollment-smoke,acceptance-stage1" "-Dhost.properties=<COMPUTERNAME>.properties" "-Dmobile.ms.report.environment=Stage1"

Full regression:
mvn -f mobile/enrollment/pom.xml test "-Pmobile-ms-enrollment-regression,acceptance-stage1" "-Dhost.properties=<COMPUTERNAME>.properties" "-Dmobile.ms.report.environment=Stage1"

Report: mobile/enrollment/target/mobile-ms-report/index.html.

Start with smoke after a refresh. Do not run the full wizard until certificate, metadata, plan, fund, routing, and authentication prerequisites are healthy.

## 8. Evidence, handoff, and boundaries
| Artifact | Use |
|---|---|
| Enrollment API Automation Sign-Off | Scope, exclusions, acceptance |
| Enrollment coverage matrix/workbook | 28-row catalog and 25 automated rows |
| enrollment-endpoint-current-state.csv | Endpoint/class/suite/plant register |
| Architecture and Execution guides | Setup, run, troubleshoot |
| DB Refresh Checklist | Restore data after refresh |
| AI Scenario Guide | Extend the ordered wizard |
| Bruno 01 - Enrollment | Manual endpoint exploration |
| qTest MSC-Enrollment | Manual test cases: https://ascensus.qtestnet.com/p/118829/portal/project#id=69212335&object=0&tab=testdesign |

Caution callout: QC4 instability, IDP/reverse-proxy behavior, plan metadata, or refreshed data can block proof without indicating an automation defect. Enrollment nightly remains separate delivery scope until a verified job exists.

## 9. Current-vs-historical source rule
Current executable truth is mobile/enrollment/pom.xml and the current TestNG XML, which contain okdirect, newyork, and nmdirect blocks. Prefer mobile/enrollment/README.md for current commands.

If an older Architecture, Sign-Off, coverage file, or enhancement backlog says Enrollment has only two regression plants, NM Direct is localhost-only, Bruno is missing, or a nightly is live, treat that statement as historical until the attachment is refreshed. Do not claim a GitLab nightly without a verified CI job.

Republish the page when finished.
