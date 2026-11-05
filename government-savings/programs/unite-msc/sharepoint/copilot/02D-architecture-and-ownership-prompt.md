PART D of 4. Edit the existing SharePoint page "02 Architecture and Ownership" on API Testing Documentation Hub.

Append below existing content. Match its hero palette, table, section, callout, code, and checklist styling. Do not duplicate the hero, breadcrumb, or existing sections.

Finish with the gray Source and ownership band below.

Final band: owner QA Automation; GitLab api-test-automation is executable source of truth; credentials, tokens, certificates, host properties, environment files, DB connection strings, and raw PII stay out of SharePoint.

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

APPEND EXACTLY:

## 6. Configuration layers
| Layer | Example | Responsibility |
|---|---|---|
| Suite profile | mobile1-regression | Selects TestNG XML and groups |
| Environment profile | acceptance-stage1 / acceptance-qc4 | Overrides environment.properties; must be last in -P |
| Environment file | stage1.properties / qc4.properties | Service routes and non-secret environment behavior |
| Host overlay | <COMPUTERNAME>.properties | Personal Oracle URL/user/password; local and gitignored |
| Suite XML | testsuites/*-testng.xml | Branding blocks, class order, listeners |

The suite XML is executable truth for what runs. A Java class not wired into the intended XML does not count as executed coverage.

## 7. Validation boundary
| Layer | Meaning | Sign-off |
|---|---|---|
| L1 | HTTP status and transport | Required |
| L2 | Contract and response shape | Required |
| L3 | Schema and typed payload | Required where supported |
| L4 | Business assertions | Required |
| L5 | API-to-database field reconciliation | Analysis/future enhancement; not the completion gate |

Oracle is actively used for test-data selection, minimum mobile version, routing/fund/contribution fixtures, and Enrollment post-account verification. That is different from universal field-by-field API-to-DB reconciliation, which leadership did not require for sign-off.

## 8. Reporting architecture
MobileMsHtmlReportListener is registered in suite XML. It creates:

- target/mobile-ms-report/index.html — leadership-friendly portal.
- target/mobile-ms-report/extent/detail.html — Extent test detail.
- pages for test details, categories, logs, history, and about.
- data/summary.json and data/history.json.
- target/surefire-reports/ — TestNG/JUnit execution detail.

SensitiveDataSanitizer redacts bearer tokens, JWT-like values, passwords, client secrets, and signing keys from report text. Sanitization is a defense, not permission to log secrets.

## 9. Ownership and source-of-truth
| Area | Owner / source |
|---|---|
| Java, POM, TestNG XML, SQL, reporting | GitLab api-test-automation; QA Automation |
| Manual API requests | Unite MSC Bruno collection |
| Manual test cases | qTest: Unite-MSC, MSC-Enrollment, MSC-Mobile1, MSC-Mobile2 |
| Delivery scope and stories | Jira Epic QA-796 |
| Runner, schedule, secure files, hard gates | DevOps + QA Automation |
| Service behavior and unknown DB mappings | Product/development SME |
| Day-to-day run, triage, data upkeep | Receiving automation team after handoff |

Caution callout: named approvers remain required wherever sign-off documents still contain [NEED_INPUT].

Republish the page when finished.
