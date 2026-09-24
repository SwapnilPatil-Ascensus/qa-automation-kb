# Unite MSC — enhancement / gap backlog (from QA-1942)

**Audience:** receiving automation team  
**As of:** September 15, 2026  
**Parent:** [QA-1942](https://ascensuscollegesavings.atlassian.net/browse/QA-1942)

These are **not** coding defects in the migrated happy path. They are the next-layer items after L1–L4 sign-off.

| ID | Item | Why it showed up | Suggested next story |
|----|------|------------------|----------------------|
| E-01 | Bruno collections | AC asked for Bruno map; repo has no `.bru` | Convert Postman (secrets stripped) |
| E-02 | PATCH logout session | Postman “Not Run”; no TestNG | Optional smoke if product wants logout coverage |
| E-03 | POST banks `planId=upromise` | Extra Postman query variant | Only if Upromise bank add is in-scope |
| E-04 | Enrollment nmdirect on CI XML | Localhost example only | After IDP/QC4 nmdirect is stable |
| E-05 | Enrollment GitLab nightly | Mobile 2 has nightly; Enrollment does not | Copy QA-1405 pattern |
| E-06 | L5 SQL API–DB asserts | QA-1054; Rajib/Henry L1–L4 only | Use `mobile-2/sql-field-validation/` if leadership reopens |
| E-07 | Partner submit / Upromise / OAuth | Excel catalog deferred | QA-1808 / QA-1807 |
| E-08 | Negatives / contract dump | Lean assertions by design | Receiving-team enhancement |
| E-09 | Deduplicate `MobileStackupRequestTest` packages | Two Java packages | Cleanup MR |
| E-10 | qTest manual cases + Jira links | Traceability to test management | Next sprint story already drafted |
| E-11 | SharePoint publish of this pack | Docs live in Git today | Ride Enrollment SharePoint story |
| E-12 | IDP QC4 401 on automation JWT | Java exists; env still flakes | Env/DevOps, not missing class |

Do **not** treat ops health/OpenAPI or M2 harness `GET mobilemembers/{planId}/{username}` as enhancement of business APIs.
