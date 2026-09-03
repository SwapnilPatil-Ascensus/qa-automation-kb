# Upcoming sprint stories

How to paste: Summary = Title line. Description = everything from Description through Definition of Done.
Parent epic for API/perf: QA-796. Labels: Upcoming, Hygin

# Performance testing

---

Title
[PERF TESTING][UNITE-MSC Setup] Mobile 1 non-IDP session performance baseline

Description
Preeti is next on Mobile 1 after Mobile 2. Do not performance-test every Mobile 1 endpoint. P0 is authentication: POST /mobile1api/v1/mobilemembersession. Reuse the existing non-IDP fragment inside unite-msc-non-idp-login.jmx. Produce an M1-labeled baseline and SLOs (throughput, error rate, p95).

Acceptance Criteria
Script or YAML choice clearly named Mobile 1 non-IDP session (not only buried inside M2 dashboard journey).
QC4 or agreed env baseline captured (numbers on ticket, no secrets).
Scope statement: other M1 endpoints deferred.

Definition of Done
Script committed in performance-test-automation.
Baseline attached.
Linked to QA-796.

---

Title
[PERF TESTING][Unite-MSC-LOGIN-BZT] Mobile 1 IDP login to mobilememberidptoken load baseline

Description
P0 for Mobile 1 IDP: existing unite-msc-idp-login.jmx / msc-idp-login.jmx already drive IDP PKCE plus POST /mobile1api/v1/mobilememberidptoken. Label and analyze this as Mobile 1 auth, not only as a Mobile 2 dashboard setup. Run on BlazeMeter or Jenkins remote YAML.

Acceptance Criteria
IDP Mobile 1 auth journey executed under load.
Results analyzed (pass/fail vs agreed SLO).
No expansion into biometric, devices, push, password, CSR, close-account.

Definition of Done
BlazeMeter/Jenkins result linked.
Notes in perf tracker.

---

Title
[PERF TESTING][Unite-MSC-CICD] Add Mobile 1 auth YAML choices to AGSUP_UNITE_MSC_ENDURANCE

Description
Jenkins job AGSUP_UNITE_MSC_ENDURANCE exists for Unite MSC (QA-1229, QA-1305) with non-IDP and IDP login YAMLs aimed at dashboard. Add explicit Mobile 1 auth choices so Preeti can run M1 without changing job structure. Do not recreate those Done tickets.

Acceptance Criteria
Job parameter lists Mobile 1 non-IDP and Mobile 1 IDP (or clearly documented equivalent existing YAMLs).
One successful parameterized run for each M1 choice.
Runbook updated with job URL http://jenkinsqant1:8080/view/Performance/job/AGSUP_UNITE_MSC_ENDURANCE/

Definition of Done
Job config change documented.
Sample build linked.

---

Title
[PERF TESTING][UNITE-MSC Setup] Enrollment end-to-end submission performance (not subsequent sprawl)

Description
Enrollment perf should be one E2E happy path to submit, not every microservice and not subsequent enroll as P0. Reuse performance/universal-platform/universal-enrollment/jmeter/up-enrollment-submission.jmx. Capture QC4/agreed-env baseline. Subsequent and isolated aws-account/validation scripts stay deferred.

Acceptance Criteria
E2E submission journey runs under load.
Endpoints in scope documented from ue_flow.txt (cms, metadata, plans, login, snapshot/validation loop, allocation funds, accounts submit).
Baseline numbers on ticket.
Subsequent enroll explicitly out of scope.

Definition of Done
Script/YAML identified and any MSC naming/docs updated.
Baseline attached.

---

Title
[PERF TESTING][Unite-MSC-BZT] Analyze Enrollment E2E on BlazeMeter

Description
Run the Enrollment submission JMeter/Taurus remote YAML on BlazeMeter, analyze errors and p95, and record whether it is ready to schedule nightly.

Acceptance Criteria
BlazeMeter (or Jenkins remote) report linked.
Pass/fail vs SLO.
List of blocking script vs env issues.

Definition of Done
Analysis markdown in kb or ticket.
Go/no-go for nightly job.

---

Title
[PERF TESTING][Unite-MSC-CICD] Jenkins job and nightly for Enrollment E2E (mirror Mobile 2)

Description
Mobile 2 endurance job is on-demand, not nightly. Enrollment needs the same pattern as Mobile 2: a Jenkins parameterized job plus a timer once the E2E script is stable. QA-454 is historical UP enrollment Jenkins. This story is MSC Enrollment E2E parity, not a duplicate of Mobile 2 login jobs.

Acceptance Criteria
Jenkins job can run up-enrollment-submission remote YAML.
Nightly schedule documented (or explicitly delayed if E2E not stable, with date).
Load servers / Docker Taurus notes match existing MSC job.

Definition of Done
Job URL on ticket.
One scheduled or manual production-like run evidenced.

---

Title
[PERF TESTING][Unite-MSC-CICD] Schedule AGSUP_UNITE_MSC_ENDURANCE nightly for Mobile 2 login

Description
AGSUP_UNITE_MSC_ENDURANCE is manual. IDP UP has weekday nightlies. Add a timer for Unite MSC Mobile 2 non-IDP login (and IDP login if stable) so MSC has a nightly perf signal. After Mobile 1 and Enrollment scripts are ready, add them to the same schedule in follow-on (do not wait to schedule M2).

Acceptance Criteria
Timer configured (document days/time).
At least one overnight run completed.
Failure notification path documented (email/Slack/Teams as team uses).

Definition of Done
Schedule screenshot or Jenkins config note on ticket.
Linked from perf tracker.

---

Title
[PERF TESTING][UNITE-MSC Docs] Unite MSC performance documentation hub

Description
Huge documentation gap. Tracker in api-validation is stale vs live script names. programs/Performance Testing has IDP login but no Unite MSC Mobile/Enrollment program folder. Create runbooks: how to run local YAML, remote Jenkins, what is in scope (M1 auth, M2 login+dashboard, Enrollment E2E), SLOs, and what is out of scope.

Acceptance Criteria
Tracker updated to real filenames (unite-msc-non-idp-login.jmx, unite-msc-idp-login.jmx, up-enrollment-submission.jmx, module jmx files not scheduled).
Preeti-ready Mobile 1 auth runbook.
Enrollment E2E runbook.
Nightly vs on-demand job list.

Definition of Done
Docs in qa-automation-kb programs/Performance Testing or unite-msc perf tracker.
Old tracker marked superseded.

---

Title
[PERF TESTING][UNITE-MSC Docs] CI/CD stories for adding Mobile 1 and Enrollment to nightly after scripts exist

Description
Same nightly pattern will be repeated when Mobile 1 auth and Enrollment E2E are ready: add YAML to Jenkins choice list and to the timer. This story is the checklist and implementation for those two additions so they are not forgotten after Preeti finishes scripts.

Acceptance Criteria
Checklist: script merged, YAML remote, Jenkins choice, one manual run, then timer.
Mobile 1 auth added to nightly when M1 baseline story is Done.
Enrollment E2E added to nightly when Enrollment E2E is stable.
core-getEndpoints and banks/ugift/contribution module jmx stay optional/not default nightly.

Definition of Done
Jenkins schedule includes the agreed journeys.
Docs list what is nightly vs on-demand.
Do not recreate QA-1802 contribution jmx as part of P0 nightly.

---
