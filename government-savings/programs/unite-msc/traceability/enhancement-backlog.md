# Unite MSC — enhancement / gap backlog (from QA-1942)

**Audience:** receiving automation team  
**As of:** September 15, 2026  
**Parent:** [QA-1942](https://ascensuscollegesavings.atlassian.net/browse/QA-1942)

These are **not** coding defects in the migrated happy path. They are the next-layer items after L1–L4 sign-off.

| ID | Item | Why it showed up | Suggested next story |
|----|------|------------------|----------------------|
| E-01 | Bruno collections | **Resolved:** Unite MSC Bruno collection now exists | Maintain Enrollment/Mobile1/Mobile2 requests; keep environment values out of SharePoint |
| E-02 | PATCH logout session | Postman “Not Run”; no TestNG | Optional smoke if product wants logout coverage |
| E-03 | POST banks `planId=upromise` | Extra Postman query variant | Only if Upromise bank add is in-scope |
| E-04 | Enrollment nmdirect in suite XML | **Resolved in current XML:** regression/integration include nmdirect | Validate actual environment/CI execution before claiming a green scheduled run |
| E-05 | Enrollment GitLab nightly | No Mobile/Enrollment nightly is verified in current `.gitlab-ci.yml` | Implement and verify a scheduled job; QA-1405 is design context only |
| E-06 | L5 SQL API–DB asserts | QA-1054; Rajib/Henry L1–L4 only | Use `mobile-2/sql-field-validation/` if leadership reopens |
| E-07 | Partner submit / Upromise / OAuth | Excel catalog deferred | QA-1808 / QA-1807 |
| E-08 | Negatives / contract dump | Lean assertions by design | Receiving-team enhancement |
| E-09 | Deduplicate `MobileStackupRequestTest` packages | Two Java packages | Cleanup MR |
| E-10 | qTest manual cases + Jira links | Traceability to test management | Modules created: Unite-MSC (`69212334`), MSC-Enrollment (`69212335`), MSC-Mobile1 (`69212337`), MSC-Mobile2 (`69233940`). Per-endpoint deep links still next-sprint. |
| E-11 | SharePoint publish of this pack | In progress under API Testing Documentation Hub | Complete pages, links, attachments, and independent validation |
| E-12 | IDP QC4 401 on automation JWT | Java exists; env still flakes | Env/DevOps, not missing class |

Do **not** treat ops health/OpenAPI or M2 harness `GET mobilemembers/{planId}/{username}` as enhancement of business APIs.
