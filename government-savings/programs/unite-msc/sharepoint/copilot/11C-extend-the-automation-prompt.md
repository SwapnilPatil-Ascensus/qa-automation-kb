PART C of 4. Edit the existing SharePoint page "11 Extend the Automation" on API Testing Documentation Hub.

Append below existing content. Match its hero palette, table, section, callout, code, and checklist styling. Do not duplicate the hero, breadcrumb, or existing sections.

Leave the page open for the next part.

Final band: owner QA Automation; GitLab api-test-automation is executable source of truth; credentials, tokens, certificates, host properties, environment files, DB connection strings, and raw PII stay out of SharePoint.

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

APPEND EXACTLY:

## 5. Enrollment-specific rules
- Extend EnrollmentBaseTest, not BaseRequestTest directly.
- Load fixture -> apply branding/session data -> encrypt once.
- Mark encrypted API fields with @MobileEncrypt.
- Steps after prospect use ProspectSessionContext JWT.
- Insert the class in business order after its prerequisite.
- Add it to every intended branding block in regression, integration, and localhost XML.
- Do not create a new suite XML for one wizard step.
- Rerun the full chain; a dependent middle step is not standalone proof.

## 6. Wire execution correctly
| Check | Required |
|---|---|
| Test group | Matches suite include: regression, integration, or functional |
| Suite XML | Class added to every intended branding block |
| Maven profile | Existing POM profile points to that XML |
| Local XML | Example updated when local coverage is intended |
| Reporting | MobileMsHtmlReportListener remains registered |
| Environment | acceptance-stage1 / acceptance-qc4 stays last in -P |

A Java test not wired into the intended XML is coded but not delivered coverage.

## 7. Manual and management traceability
1. Add/update the request under the correct Bruno module folder.
2. Use variables/environment files; strip credentials and personal data.
3. Create/update the qTest manual case in the matching module folder with preconditions, steps, and expected result.
4. Link qTest and automation evidence to the delivering Jira story.
5. Add endpoint ID/class/method/profile/plants to the coverage register; copy plants from the XML branding blocks you changed, not an older CSV value.
6. Update sign-off/traceability if scope or exclusions changed.

Bruno: https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/bruno/Mobile/mobile-msc/Unite-MSC-Bruno_collection?ref_type=heads
Epic: https://ascensuscollegesavings.atlassian.net/browse/QA-796

qTest modules:
| Module | qTest Test Design |
|---|---|
| Unite-MSC (parent) | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212334&object=0&tab=testdesign |
| MSC-Enrollment | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212335&object=0&tab=testdesign |
| MSC-Mobile1 | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212337&object=0&tab=testdesign |
| MSC-Mobile2 | https://ascensus.qtestnet.com/p/118829/portal/project#id=69233940&object=0&tab=testdesign |

Republish the page when finished.
