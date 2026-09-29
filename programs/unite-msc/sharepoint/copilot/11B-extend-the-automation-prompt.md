PART B of 4. Edit the existing SharePoint page "11 Extend the Automation" on API Testing Documentation Hub.

Append below existing content. Match its hero palette, table, section, callout, code, and checklist styling. Do not duplicate the hero, breadcrumb, or existing sections.

Leave the page open for the next part.

Final band: owner QA Automation; GitLab api-test-automation is executable source of truth; credentials, tokens, certificates, host properties, environment files, DB connection strings, and raw PII stay out of SharePoint.

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

APPEND EXACTLY:

## 2. Intake before coding
Capture in the Jira story:

| Field | Required answer |
|---|---|
| Module | Mobile 1, Mobile 2, or Enrollment |
| Contract | method, path, headers, parameters, request/response shape |
| Auth | public, mobile JWT, IDP, prospect JWT, or member JWT |
| Branding | okdirect, newyork, nmdirect differences |
| Data | Oracle query, generated fixture, or prior-step context |
| Safety | read-only, creates owned data, mutates/deletes |
| Suites | regression, integration, smoke, localhost |
| Assertions | L1-L4 expected behavior |

Sources: canonical code https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/mobile?ref_type=heads, Bruno https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/bruno/Mobile/mobile-msc/Unite-MSC-Bruno_collection?ref_type=heads, qTest modules (Unite-MSC / MSC-Enrollment / MSC-Mobile1 / MSC-Mobile2), and the delivering story under https://ascensuscollegesavings.atlassian.net/browse/QA-796. Do not code from a screenshot or memory.

qTest:
| Module | qTest Test Design |
|---|---|
| Unite-MSC (parent) | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212334&object=0&tab=testdesign |
| MSC-Enrollment | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212335&object=0&tab=testdesign |
| MSC-Mobile1 | https://ascensus.qtestnet.com/p/118829/portal/project#id=69212337&object=0&tab=testdesign |
| MSC-Mobile2 | https://ascensus.qtestnet.com/p/118829/portal/project#id=69233940&object=0&tab=testdesign |

## 3. Choose the module pattern
| Endpoint type | Extend/reuse |
|---|---|
| Mobile 1 auth/profile/session/device | MobileBaseRequestTest + nearest mobile1 class |
| Mobile 2 account experience | Existing Mobile 2 class; reuse Mobile 1 auth/account context |
| Enrollment wizard POST | EnrollmentBaseTest + ProspectSessionContext + encryption helpers |
| Enrollment subsequent POST | Existing-member context + encrypted payload |
| HAL list GET | Existing GenericEmbeddedPOJO pattern; avoid one-off wrappers |

Follow the nearest working endpoint in the same module. Do not change shared framework APIs or unrelated POJOs merely to make one endpoint compile.

## 4. Implement the TestNG case
1. Add/reuse one request/response POJO per file following Lombok/Jackson conventions.
2. Put endpoint path and fixture name in the test class.
3. Use framework loaders/placeholders, not hardcoded IDs or personal data.
4. Configure auth through the module base class.
5. Build the request with the framework Rest Assured client.
6. Assert L1 status, L2 contract, L3 typed/schema where useful, and L4 business outcome.
7. Keep assertions lean and diagnostic; do not dump full bodies.
8. For mutation/delete, prove the record is automation-owned and leave deterministic state.

Republish the page when finished.
