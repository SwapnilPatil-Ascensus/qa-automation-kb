PART C of 4. Edit the existing SharePoint page "02 Architecture and Ownership" on API Testing Documentation Hub.

Append below existing content. Match its hero palette, table, section, callout, code, and checklist styling. Do not duplicate the hero, breadcrumb, or existing sections.

Leave the page open for the next part.

Final band: owner QA Automation; GitLab api-test-automation is executable source of truth; credentials, tokens, certificates, host properties, environment files, DB connection strings, and raw PII stay out of SharePoint.

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

APPEND EXACTLY:

## 3. Repository and module map
Mobile root: https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/mobile?ref_type=heads

| Area | GitLab path | Purpose |
|---|---|---|
| Root parent | pom.xml | Builds jsonapi, universal, astro, mobile |
| Mobile parent | mobile/pom.xml | Builds reporting, enrollment, mobile1, mobile2 |
| Shared framework | jsonapi/jsonapi-core | BaseRequestTest, resource loading, SQL, Rest Assured |
| Mobile 1 | mobile/mobile1 | Authentication/session and member-profile capabilities |
| Mobile 2 | mobile/mobile2 | Account experience; reuses Mobile 1 auth base |
| Enrollment | mobile/enrollment | Encrypted wizard + subsequent enrollment |
| Reporting | mobile/reporting | Static portal + Extent detail + sanitization |
| Manual API testing | https://gitlab.com/ascensus-gs/products/depot/qa-automation/api-test-automation/-/tree/main/bruno/Mobile/mobile-msc/Unite-MSC-Bruno_collection?ref_type=heads | Unite MSC Bruno collection |

## 4. Module inheritance and shared behavior
| Module | Base and shared behavior |
|---|---|
| Mobile 1 | MobileBaseRequestTest extends BaseRequestTest; loads mobile.sql, selects an Oracle-backed automation user, resolves minimum app version, configures mobile/IDP auth |
| Mobile 2 | Reuses Mobile 1 authentication and account context rather than duplicating login endpoints |
| Enrollment | EnrollmentBaseTest owns encryption, prospect/member session context, JSON fixtures, and ordered wizard state |

TestNG passes branding as okdirect, newyork, or nmdirect. SQL and JSON placeholders are resolved for that branding. IDP-enabled plans probe for a login-capable automation user; the framework can fall back to mobile-session auth where designed.

## 5. Related automation estates
| Estate | Technology | Relationship |
|---|---|---|
| Canonical API automation | Maven, TestNG, Rest Assured | Extend for Unite MSC API endpoints |
| Legacy Unite API/mobile reference | Cucumber features and older endpoint flows | Traceability/reference only; do not extend |
| V2 Unite UI automation | Ant, Selenium, Cucumber | UI regression; not API source of truth |
| V3 Unite / Universal Enrollment UI | Maven, Selenium/Cucumber | UI journey coverage; complements API tests |
| Performance automation | JMeter/Taurus performance suites | Load/performance concern; separate from functional L1-L4 |

Do not confuse UI page objects or performance scripts with canonical API coverage. Cross-reference them only when a business journey or pipeline needs layered proof.

Republish the page when finished.
