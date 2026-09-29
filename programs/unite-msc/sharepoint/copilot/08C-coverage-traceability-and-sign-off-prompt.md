PART C of 3. Edit the existing SharePoint page "08 Coverage, Traceability and Sign-off" on API Testing Documentation Hub.

Append below existing content. Match its hero palette, table, section, callout, code, and checklist styling. Do not duplicate the hero, breadcrumb, or existing sections.

Finish with the gray Source and ownership band below.

Final band: owner QA Automation; GitLab api-test-automation is executable source of truth; credentials, tokens, certificates, host properties, environment files, DB connection strings, and raw PII stay out of SharePoint.

RULES:
- Preserve every row, step, checklist item, and code block.
- Invent no metrics, commands, owners, URLs, approvals, status, or availability.
- Never add passwords, JWT, SSN, certificates, host properties, environment JSON, DB connection strings, or raw PII.
- Keep [NEED_INPUT]. Edit only this page; create no child pages.

APPEND EXACTLY:

## 6. Evidence package
| Evidence | Reviewer use |
|---|---|
| Three formal sign-off documents | Scope, metrics, exclusions, approval |
| Three endpoint current-state registers | Row-level class/method/suite/plant mapping |
| Enrollment coverage workbook/catalog | Original catalog vs delivered status |
| Legacy-to-canonical DOCX + CSV | 83-row comparison and improvements |
| Enhancement backlog | Deferred/non-defect next-layer scope |
| HTML portal + Surefire/GitLab artifacts | Actual execution result |

Approvals marked [NEED_INPUT] remain open until names/dates are supplied. Never manufacture an approval.

## 7. Explicit exclusions and next layer
Not missing business coverage:
- Mobile 2 acceptance harness GET mobilemembers/{planId}/{username}.
- Operations health/OpenAPI utilities outside the business API numerator.
- Enrollment partner submit, Upromise, and OAuth deferred under separate scope.

Enhancement backlog:
- PATCH logout session and optional Upromise bank variant.
- Broader negative/contract tests.
- qTest-to-Jira linkage completion.
- Verified Enrollment nightly job.
- Optional L5 SQL field reconciliation only if leadership reopens it.

The original traceability snapshot said no Bruno files existed. The current GitLab repository now contains the Unite MSC Bruno collection; use the current repo, not that historical gap statement.

## 8. Source freshness rule
For executable behavior and plants, current POM/TestNG XML wins. Some historical sign-off/coverage attachments predate three-plan XML and the Bruno collection. Until refreshed, do not use an older CSV plant column to dispute current okdirect/newyork/nmdirect XML.

Current .gitlab-ci.yml does not prove a Mobile 2 or Enrollment nightly. Describe nightly enablement as unverified/follow-up unless an actual current job and schedule are reviewed.

Republish the page when finished.
