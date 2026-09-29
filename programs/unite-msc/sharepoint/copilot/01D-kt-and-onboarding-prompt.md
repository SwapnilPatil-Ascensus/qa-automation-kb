PART D of 4. Edit the existing SharePoint page "01 KT and Onboarding" on API Testing Documentation Hub.

Append below existing content. Match its hero palette, table, section, callout, code, and checklist styling. Do not duplicate the hero, breadcrumb, or existing sections.

Finish with the gray Source and ownership band below.

Final band: owner QA Automation; GitLab api-test-automation is executable source of truth; credentials, tokens, certificates, host properties, environment files, DB connection strings, and raw PII stay out of SharePoint.

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

APPEND EXACTLY:

## 9. Branching, merge requests, and standards
| Standard | Rule |
|---|---|
| Base branch | main |
| Branch name | feature/QA-####-short-description, matching the Jira key |
| Merge request | Use the repo template: Summary, Related, Test plan, Risks |
| Review gate | Local or CI checks pass; new scenarios executed in a test environment; no unintended API or config changes |
| Never commit | target/, your host overlay, credentials, tokens, certificates, or PII |

Track work under Epic QA-796 and link the Jira key in both the branch name and the merge request.

## 10. Definition of done for onboarding
- [ ] JDK, Maven, Git, and IDE plugins installed and verified.
- [ ] Parent build mvn -f mobile/pom.xml clean install -DskipTests succeeds.
- [ ] Personal host overlay created and confirmed gitignored.
- [ ] One Enrollment smoke run completed against Stage1.
- [ ] One Mobile 1 and one Mobile 2 suite run completed.
- [ ] HTML report located and one failure classified as environment, data, automation, or product.
- [ ] Bruno collection opened and one request executed manually.
- [ ] Branch and merge request standards understood; Epic QA-796 reviewed.

## 11. First-day troubleshooting
| Symptom | Fix |
|---|---|
| Surefire reports Unresolved compilation problems | Delete that module's target/maven-compile and rerun |
| Tests hit the wrong environment | Move acceptance-stage1 or acceptance-qc4 to the END of -P |
| Lombok or POJO compile errors in the IDE | Install the Lombok plugin and enable annotation processing |
| No tests ran | Confirm the suite profile name and that the suite XML exists in testsuites/ |
| Local suite not found | Copy localhost-testng.xml.example to localhost-testng.xml first |

Do not use src/test/resources/user/*.json for login data; authentication users are resolved from SQL at runtime.

Republish the page when finished.
