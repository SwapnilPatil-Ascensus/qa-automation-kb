PART B of 4. Edit the existing SharePoint page "01 KT and Onboarding" on API Testing Documentation Hub.

Append below existing content. Match its hero palette, table, section, callout, code, and checklist styling. Do not duplicate the hero, breadcrumb, or existing sections.

Leave the page open for the next part.

Final band: owner QA Automation; GitLab api-test-automation is executable source of truth; credentials, tokens, certificates, host properties, environment files, DB connection strings, and raw PII stay out of SharePoint.

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

APPEND EXACTLY:

## 3. Open it in your IDE
1. Import api-test-automation as an existing Maven project.
2. Install the Lombok plugin and enable annotation processing; the POJOs will not compile without it.
3. Install TestNG support so you can run a single class.
4. In VS Code or Cursor, open the repo folder, add the Java and Maven extensions, and run suites from the integrated terminal.
5. Maven compiles to target/maven-compile, deliberately separate from the IDE's own output, so IDE auto-build cannot overwrite Maven classes mid-run.

## 4. Create your host overlay (one time)
Each engineer needs a personal, gitignored host file. Never copy another engineer's file.

1. Build first. The config folder is empty in a fresh clone.
2. Open src/test/resources/config/ in the module you will run.
3. Copy config.properties to <COMPUTERNAME>.properties.
4. Fill in the three keys: UNITEDATABASEURL, UNITEUSERNAME, UNITEPASSWORD.
5. Pass it on every run with -Dhost.properties=<COMPUTERNAME>.properties

Why the folder looks empty before a build: config.properties and the environment files stage1, qc4, qc1, stage5, and cat are not committed in the module. Maven unpacks them from the shared jsonapi-lib resource artifact during generate-resources, and the module gitignore excludes every *.properties file in that folder. Do not try to commit them.

Name the file after your machine. The build derives the default host file from your COMPUTERNAME on Windows or HOSTNAME on Linux, which is why the convention exists; passing -Dhost.properties explicitly overrides that default.

Prohibition callout: the host overlay holds database credentials. It stays local. Never commit it, attach it, or paste its contents into SharePoint, Jira, or Teams.

## 5. Maven profiles you will actually use
| Module | Suite profiles | Suite XML folder |
|---|---|---|
| mobile1 | mobile1-regression, mobile1-integration, mobile1-smoke, mobile1-localhost | mobile/mobile1/testsuites/ |
| mobile2 | mobile2-regression, mobile2-integration, mobile2-smoke, mobile2-localhost | mobile/mobile2/testsuites/ |
| enrollment | mobile-ms-enrollment-regression, mobile-ms-enrollment-integration, mobile-ms-enrollment-smoke, mobile-ms-enrollment-localhost | mobile/enrollment/testsuites/ |
| Environment overlay | acceptance-stage1, acceptance-qc4 | Applies to all three modules |

Caution callout: list the environment profile LAST in -P. It overrides the environment.properties set by the suite profile. mobile1-smoke, mobile2-smoke, and Enrollment suite profiles default to qc4.properties; append acceptance-stage1 to run them against Stage1.

Republish the page when finished.
