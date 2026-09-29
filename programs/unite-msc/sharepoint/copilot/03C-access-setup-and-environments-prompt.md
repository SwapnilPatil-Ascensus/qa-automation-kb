PART C of 3. Edit the existing SharePoint page "03 Access, Setup and Environments" on API Testing Documentation Hub.

Append below existing content. Match its hero palette, table, section, callout, code, and checklist styling. Do not duplicate the hero, breadcrumb, or existing sections.

Finish with the gray Source and ownership band below.

Final band: owner QA Automation; GitLab api-test-automation is executable source of truth; credentials, tokens, certificates, host properties, environment files, DB connection strings, and raw PII stay out of SharePoint.

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

APPEND EXACTLY:

## 6. Manual-tool environments
| Tool | Setup |
|---|---|
| Bruno | Open Unite-MSC-Bruno_collection; choose Enrollment, Mobile1, or Mobile2 folder |
| Bruno Stage1 environments | Env-Enrollment-Stage1.yml, Env-Mobile1-Stage1.yml, Env-Mobile2-Stage1.yml; treat populated values as sensitive |
| Postman | Use approved Mobile collection for IDP/mobile token exploration |
| qTest | Open the matching module folder under Test Design |

Bruno: https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/bruno/Mobile/mobile-msc/Unite-MSC-Bruno_collection?ref_type=heads

qTest modules:
| Module | qTest Test Design |
|---|---|
| Unite-MSC (parent) | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212334&object=0&tab=testdesign |
| MSC-Enrollment | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212335&object=0&tab=testdesign |
| MSC-Mobile1 | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212337&object=0&tab=testdesign |
| MSC-Mobile2 | https://ascensus.qtestnet.com/p/118829/portal/project#id=69233940&object=0&tab=testdesign |

Use request folders to explore contracts. Do not paste Bruno/Postman environment contents into SharePoint, Jira, or Teams. Prefer a local stripped environment for demonstrations; treat committed Stage1 environment YAML as sensitive operational material.

## 7. Setup verification
- [ ] Maven parent build succeeds.
- [ ] java -version and mvn -version meet repo requirements.
- [ ] Personal host overlay is outside git status.
- [ ] acceptance-stage1 / acceptance-qc4 is last in the Maven profile list.
- [ ] Enrollment smoke reaches the intended environment.
- [ ] target/mobile-ms-report/index.html opens.
- [ ] Bruno collection and correct Stage1 environment open.
- [ ] No token, password, SSN, or private endpoint is pasted into a ticket or SharePoint.

Republish the page when finished.
