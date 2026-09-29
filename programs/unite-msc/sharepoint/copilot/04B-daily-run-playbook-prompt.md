PART B of 3. Edit the existing SharePoint page "04 Daily Run Playbook" on API Testing Documentation Hub.

Append below existing content. Match its hero palette, table, section, callout, code, and checklist styling. Do not duplicate the hero, breadcrumb, or existing sections.

Leave the page open for the next part.

Final band: owner QA Automation; GitLab api-test-automation is executable source of truth; credentials, tokens, certificates, host properties, environment files, DB connection strings, and raw PII stay out of SharePoint.

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

APPEND EXACTLY:

## 2. Choose the suite
| Goal | Suite |
|---|---|
| Service/bootstrap health | Enrollment smoke |
| Broad read/non-destructive module coverage | regression |
| Integration proof in selected environment | integration |
| Mutating/destructive or strict checks | smoke |
| One class/branding while developing | gitignored localhost XML |

Mobile 1/2 smoke includes mutations; Enrollment smoke is health/reference GETs. Read the module page before treating every smoke suite as harmless.

## 3. Pre-run gate
1. Pull main and inspect the relevant module README/POM/XML.
2. Confirm module, suite, branding set, and Stage1 or QC4.
3. Confirm your personal host overlay exists and is not in git status.
4. Ask whether an Oracle refresh or service deployment occurred.
5. Confirm automation-owned auth/data prerequisites.
6. Put acceptance-stage1 or acceptance-qc4 LAST in -P.
7. For destructive smoke, inspect current owned state before running.

## 4. Run commands by module
Render as a preformatted code block. Replace <COMPUTERNAME> with your own host overlay.

# Enrollment
mvn -f mobile/enrollment/pom.xml test "-Pmobile-ms-enrollment-smoke,acceptance-stage1" "-Dhost.properties=<COMPUTERNAME>.properties" "-Dmobile.ms.report.environment=Stage1"
mvn -f mobile/enrollment/pom.xml test "-Pmobile-ms-enrollment-regression,acceptance-stage1" "-Dhost.properties=<COMPUTERNAME>.properties" "-Dmobile.ms.report.environment=Stage1"
mvn -f mobile/enrollment/pom.xml test "-Pmobile-ms-enrollment-integration,acceptance-qc4" "-Dhost.properties=<COMPUTERNAME>.properties" "-Dmobile.ms.report.environment=QC4"

# Mobile 1
mvn -f mobile/mobile1/pom.xml test "-Pmobile1-regression,acceptance-stage1" "-Dhost.properties=<COMPUTERNAME>.properties" "-Dmobile.ms.report.environment=Stage1"
mvn -f mobile/mobile1/pom.xml test "-Pmobile1-integration,acceptance-qc4" "-Dhost.properties=<COMPUTERNAME>.properties" "-Dmobile.ms.report.environment=QC4"
mvn -f mobile/mobile1/pom.xml test "-Pmobile1-smoke,acceptance-stage1" "-Dhost.properties=<COMPUTERNAME>.properties" "-Dmobile.ms.report.environment=Stage1"

# Mobile 2
mvn -f mobile/mobile2/pom.xml test "-Pmobile2-regression,acceptance-stage1" "-Dhost.properties=<COMPUTERNAME>.properties" "-Dmobile.ms.report.environment=Stage1"
mvn -f mobile/mobile2/pom.xml test "-Pmobile2-integration,acceptance-qc4" "-Dhost.properties=<COMPUTERNAME>.properties" "-Dmobile.ms.report.environment=QC4"
mvn -f mobile/mobile2/pom.xml test "-Pmobile2-smoke,acceptance-stage1" "-Dhost.properties=<COMPUTERNAME>.properties" "-Dmobile.ms.report.environment=Stage1"

The environment profile must stay LAST in -P. M1/M2 smoke and Enrollment suite profiles default to QC4 unless an acceptance overlay overrides them.

Republish the page when finished.
