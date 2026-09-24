# Enrollment — reporting, triage, evidence

**QA-893 / QA-2042**

## What to look at after a run

| Artifact | Where | Use |
|----------|--------|-----|
| Surefire | `mobile/enrollment/target/surefire-reports/` | Pass/fail XML |
| HTML / Extent | `target/mobile-ms-report/` if listener is on the suite | Human triage |
| GitLab job | Enrollment nightly — **not wired** | Future sustainment |

## Dashboards

There is no separate Enrollment Power BI. Use TestNG HTML + GitLab job when it exists. Leadership coverage numbers live in this KB (`Enrollment-Automation-Coverage-Status.md`), not in Jenkins.

## Failure triage

1. Environment vs script vs product (same as `automation-bug-lifecycle/`).
2. Attach HTML snippet **with secrets stripped**.
3. Product defect: Prompt H / Jira. Do not file a bug for missing nmdirect CI or deferred partner APIs.

## Evidence retention

| Keep | Do not keep |
|------|-------------|
| Date, plant, suite name, pass counts | Raw JWT, passwords, SSN, full Authorization |
| Sanitized surefire summary | Host `.properties` files |
| Link to GitLab job | Screenshots of tokens |

Reports are gitignored. Copy a **redacted** summary into `evidence/regression-runs/` if leadership needs a dated folder.

## Nightly ownership

Until an ACM is named, AMSQUAD continues to own interpretation of red jobs. Enrollment nightly is a follow-up story, not a sign-off blocker for happy-path coding.
