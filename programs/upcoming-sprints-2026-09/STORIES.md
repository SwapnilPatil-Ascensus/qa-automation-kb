# Upcoming sprint stories — copy paste for Jira

Parent: QA-796 for API and Unite MSC perf. V2/V3 can sit under daily regression / platform support. Labels: Upcoming, Hygin

How to paste: Summary = Title line. Description = everything from Description through Definition of Done.

Do not recreate: QA-1595 through QA-1604, QA-1751-1753, QA-1769, QA-1775-1792, QA-1807, QA-1808, QA-1853-1855, QA-1405, QA-1229, QA-1305, QA-1275, QA-1526, QA-1820, QA-1802.

---

# API / Unite MSC

---

Title
[UNITE-MSC][Enrollment] Sign-off package and coverage metrics for Enrollment API automation

Description
Mobile 1 and Mobile 2 already have Word sign-off packs. Enrollment coding is now complete for the happy-path wizard including review-confirm and for subsequent enrollment on okdirect and newyork. Produce the Enrollment sign-off package in the same quality: coverage metrics, suite list, plant matrix, exclusions, and execution evidence. Update qa-automation-kb mappings so they stay the source of truth.

Acceptance Criteria
Enrollment Word sign-off exists next to Mobile 1 and Mobile 2 packs.
Markdown summary matches live TestNG classes in api-test-automation/mobile/enrollment.
Coverage metrics include endpoint count, @Test count, plants, and deferred partner APIs.
Exclusions documented: submit, Upromise, OAuth, negatives.
Evidence folder or CI links attached for okdirect and newyork regression.

Definition of Done
Sign-off files committed in qa-automation-kb under docs/06-coverage/signoff.
QA lead reviewed the pack.
Ticket linked to QA-796.

---

Title
[UNITE-MSC][Enrollment][CICD] GitLab nightly regression for Enrollment API (OK Direct and New York)

Description
Mobile 2 has a GitLab nightly (QA-1405). Enrollment regression XML already runs okdirect and newyork but is not wired as a scheduled job in the local api-test-automation gitlab-ci. Add a nightly (and document the include) so Enrollment is a pipeline suite, not only a local Maven profile.

Acceptance Criteria
Scheduled GitLab job runs mobile-ms-enrollment-regression (or equivalent) on Stage1 for okdirect and newyork.
Job publishes HTML report the same way Mobile 2 nightly does.
Failure does not silently skip remaining classes.
Runbook updated with job name, schedule, and how to replay locally.

Definition of Done
Pipeline green at least once on Stage1.
Job URL and sample report linked on the ticket.
Docs updated in qa-automation-kb pipeline folder.

---

Title
[UNITE-MSC][Enrollment] Add NM Direct to Enrollment regression and integration suites

Description
Target plants are New York, NM Direct, and OK Direct. Enrollment CI suites cover okdirect and newyork only. nmdirect exists on localhost-testng.xml.example. Add nmdirect to regression and integration XML, fixtures, and evidence. Fix localhost example so it matches the CI class list (content, recurring, subsequent bank-entered, subsequent beneficiary, subsequent recurring).

Acceptance Criteria
nmdirect is a third plan block in enrollment-regression-testng.xml and enrollment-integration-testng.xml.
Localhost example class list matches regression.
At least one QC4 or Stage1 evidence run for nmdirect happy path.
Known nmdirect failures documented rather than hidden.

Definition of Done
XML merged.
Evidence attached.
Coverage CSV plant column updated.

---

Title
[UNITE-MSC][CICD] Pipeline suite readiness across OK Direct, New York, and NM Direct

Description
Walk Mobile 1, Mobile 2, and Enrollment suites against the three target plants. Record what already runs, what is missing, and close only the gaps that are in scope. Today New York is enrollment-only. Mobile 1/2 are okdirect + nmdirect. Enrollment CI is okdirect + newyork. Produce a plant x module matrix and wire missing suites that the team agrees to keep.

Acceptance Criteria
Published matrix: module x plant x suite (smoke, integration, regression, nightly).
Each in-scope cell either green with evidence or explicitly out of scope with reason.
Missing in-scope suites added to TestNG XML and pipeline includes.
MobileMemberSessionRequestTest group mismatch on Enrollment is fixed or documented.

Definition of Done
Matrix checked into qa-automation-kb mappings.
Pipeline jobs listed with URLs.
Receiving team can run each in-scope suite from the runbook.

---

Title
[UNITE-MSC][Enhancement] Negative and extra functional cases catalog for handover (Enrollment plus leftover Mobile 1/2)

Description
Happy-path coding is done. Negatives were largely deferred (Enrollment has none; Dashboard negatives were not migrated). Catalog recommended negatives and extra functional cases for the receiving team. Do not implement every case in this story. Hand them a prioritized list they can pull.

Acceptance Criteria
Enrollment negatives listed (invalid routing, alloc not 100, bad password, missing T&C, duplicate prospect, expired JWT, etc.) with suggested priority.
Mobile 2 dashboard/auth negatives called out as not migrated from legacy.
Mobile 1 items that are comments-only / OOS called out.
Each item tagged P1/P2/P3 and whether it belongs in regression or functional.

Definition of Done
Catalog markdown in qa-automation-kb.
Receiving team walkthrough done or notes attached.
No requirement to automate all items in this ticket.

---

Title
[UNITE-MSC][Postman] Consolidate Mobile 1, Mobile 2, and Enrollment into one Postman collection

Description
Collections exist separately (API repo mobile folder, KB Mobile1, Mobile2, EnrollmentE2E). Create one workspace collection covering all three modules with shared environments (QC4, Stage1) and folders per module. Align requests to the Excel sheets and Java classes. Update Excel where subsequent Enrollment POSTs are missing from the catalog.

Acceptance Criteria
Single Postman collection with folders Mobile1, Mobile2, Enrollment (wizard + subsequent).
Shared env files for QC4 and Stage1 without secrets committed.
Collection README: how to get token, branding (okdirect, newyork, nmdirect), and encryption notes.
Excel catalog updated for subsequent beneficiary, bank-entered, recurring.
Happy-path Enrollment E2E runnable from the unified collection.

Definition of Done
JSON committed in api-test-automation/postman and copied or linked in qa-automation-kb.
No credentials in git.

---

Title
[UNITE-MSC][Bruno] Convert the unified Unite MSC Postman collection to Bruno

Description
Team is moving from Postman to Bruno. After the unified Postman collection exists, convert it to a Bruno collection with the same folder structure and environments.

Acceptance Criteria
Bruno collection opens locally and runs Enrollment happy path plus Mobile 1 auth smoke plus one Mobile 2 GET (dashboard).
Env files for QC4 and Stage1.
Short README: install Bruno, import, select env, run folder.
Parity note: any Postman-only scripts that did not convert.

Definition of Done
Bruno files committed (no secrets).
Demo or recording attached or notes for the receiving team.

---

Title
[UNITE-MSC][Docs] Keep legacy / new repo / Postman / Excel mapping current

Description
A first mapping document was added at programs/unite-msc/api-test-automation/mappings/legacy-new-postman-excel-mapping.md. Complete any missing Excel rows, confirm Postman request names, and get receiving-team sign-off that the mapping is the handoff artifact.

Acceptance Criteria
Every Java test class maps to Excel row and Postman request (or listed as Java-only).
Every Excel row maps to Java status Done/Deferred.
Legacy vs new improvement notes reviewed with the team.
Receiving team accepts the mapping as complete.

Definition of Done
Mapping file updated if Excel/Postman changed.
Linked from coverage index.
Ticket closed only after review comment from QA lead.

---

Title
[UNITE-MSC][Docs] Technical setup and onboarding for Unite MSC API automation

Description
Handoff needs one onboarding path: clone api-test-automation, host properties, QC4 vs Stage1, Maven profiles for mobile1/mobile2/enrollment, encryption/AES, report output, and where docs live in qa-automation-kb. Existing READMEs in mobile modules are the base. Produce a single onboarding guide the receiving team can follow without Slack archaeology.

Acceptance Criteria
New engineer can run enrollment smoke and one Mobile 2 module suite from the guide.
Secrets/PII rules stated (no credentials in git).
Links to module READMEs, wizard guide, coverage index.
Troubleshooting: common 401, X-App-Version, branding, DB overlay.

Definition of Done
Guide in qa-automation-kb (api-test-automation/docs/01-onboarding or handoff folder).
Walkthrough completed once with a team member or recorded notes.

---

Title
[UNITE-MSC][Docs] Cursor / AI playbook for adding a new MSC API scenario

Description
When a new endpoint or scenario arrives, the receiving team should use Cursor (or similar) against the existing Enrollment wizard pattern and Mobile 1/2 request-test pattern. Write a playbook: which files to copy, how to add a TestNG class to existing suite XML (do not create new XML), fixtures, groups, and how to update coverage CSV/Excel.

Acceptance Criteria
Playbook covers Enrollment step add (ENROLLMENT-WIZARD-GUIDE.md) and a Mobile 2 new GET.
Checklist: test class, suite XML, fixture, coverage CSV, Postman/Bruno request.
Example prompt the engineer can paste into Cursor.
Warning: do not invent payloads; use Postman/Excel.

Definition of Done
Playbook committed.
Linked from onboarding guide.

---

Title
[UNITE-MSC][Docs] Reporting and dashboarding for Unite MSC API runs

Description
HTML listener/reporting exists under mobile/reporting. Document how reports are produced locally, what the nightly publishes, where to find history, and what a leadership dashboard should show (pass/fail by module and plant). Include the known gap if Nexus/GitHub consumer docs are separate.

Acceptance Criteria
Runbook: local report path, CI artifact location, retention.
Recommended dashboard widgets: module, plant, suite, trend.
If no dashboard tool is live, document the interim (HTML zip + this markdown) and the enhancement to wire a real dashboard.

Definition of Done
Guide committed under docs/02-daily-usage or docs/03-development as appropriate.
Sample report screenshot or link attached (no PII).

---

Title
[UNITE-MSC][Docs] Handoff documentation pack for Unite MSC API (receiving team)

Description
Package onboarding, coverage, mapping, sign-off, pipeline, AI playbook, reporting, and enhancement backlog into one handoff index. This is the close-out documentation story after the individual docs exist.

Acceptance Criteria
Single index page listing every handoff artifact with owner and last updated date.
Open gaps listed: nmdirect CI, negatives, partner APIs, New York on Mobile 1/2 if still out of scope.
Receiving team named and ack captured on the ticket.

Definition of Done
Index in qa-automation-kb.
QA-796 comment with the index link.

---

# V2 UI automation

---

Title
[V2][Daily-Regression] Hygiene pass on Stage1 daily after IDP plan migration

Description
V2 Jenkins daily still owns ~14 XMLs and ~182 test blocks. Several tickets already removed IDP-migrated legacy/NextGen cases (QA-1275, QA-1526, QA-1820). This story is the leftover hygiene: confirm daily XMLs only contain suites we still intend to run, remove or archive dead references, and publish a current V2 daily inventory. Do not recreate those earlier tickets.

Acceptance Criteria
Inventory of bin/regression/daily XML files with test counts and intent (keep / retire / migrate to V3).
stage1-web-login.xml empty shell is either restored with real tests or removed from the Jenkins job so docs do not imply login still runs.
No duplicate work of QA-1820. Link those tickets.

Definition of Done
Inventory markdown in qa-automation-kb.
Jenkins job list matches the inventory.
Dead suites not left silently in daily.

---

Title
[V2][Enrollment] Inventory leftover enrollment and member features not in daily

Description
V2 has ~179 enrollment-path features vs a small set referenced from daily XML. Catalog what is in daily vs repo-only (including CSR enrollment, prefill, ABLE, NextGen, plan folders). This inventory feeds V3 migration stories. No mass port in this ticket.

Acceptance Criteria
Table: feature / area / in daily Y/N / recommend migrate to V3 / keep V2 / retire.
CSR enrollment daily list captured (MID, advisors, subsequent, prefill).
Member-related daily vs leftover (profile, contrib, withdraw, transfer, ugift).

Definition of Done
Inventory committed.
Used as input for V3 CSR and member stories.

---

Title
[V2][Docs] Document current Jenkins daily vs what has moved to V3 GitLab

Description
V2 still runs STAGE1-Daily-Unite-Prime-Regression (Jenkins). V3 runs GitLab scheduled_regression_job (UE then Unite master). Write a single page so the team does not assume V2 web login or V3 CSR enrollment exists.

Acceptance Criteria
Page lists V2 daily XMLs, V3 master children, and UP rollovers (not scheduled).
States clearly: CSR enrollment is V2 only today. V2 web-login daily is empty. OK Direct enrollment is V2 only.
Job names and how to read last run.

Definition of Done
Doc in qa-knowledge-base or upcoming-sprints folder.
Linked from automation-bug-lifecycle / regression docs if those point at old job lists.

---

Title
[V2][Daily-Regression] Stabilize remaining V2 daily suites still owned this sprint

Description
While enrollment/login/registration/member migrate to V3, V2 daily still runs CSR account maintenance, contributions, withdrawals, transfers, investments, ugift, LA Able, Empower, Sardine. Triage and stabilize failures on the suites we are not retiring this sprint so Jenkins signal stays usable.

Acceptance Criteria
Failing tests on keep-suites classified (env, data, script, product).
Flakes quarantined or fixed per triage rules.
Keep-suites listed as green or with known defects in Jira.

Definition of Done
Latest Jenkins daily result summarized on the ticket.
No silent skips of entire keep-suites.

---

# V3 UI automation

---

Title
[V3][Universal-Enrollment] Stabilize Stage1 Universal Enrollment daily

Description
V3 GitLab scheduled job runs Universal Enrollment master (24 blocks) then Unite master. Enrollment must be stable before expanding. Fix or quarantine known flaky first-step / login-reg failures. Do not add new features until the current XML is a trustworthy gate.

Acceptance Criteria
stage1-ue-regression-master (universal-enrollment-stage1.xml) has a documented green run or a listed defect per remaining fail.
Flakes have owner and quarantine tag if not fixed.
Runbook: Maven profile stage1-ue-regression-test.

Definition of Done
CI scheduled job UE portion explained on the ticket with log URL.
Stabilization notes in qa-automation-kb v3 enrollment module doc if it exists.

---

Title
[V3][Universal-Enrollment] Wire leftover @dailyrun features into daily XML

Description
These features already have @dailyrun but are not in universal-enrollment-stage1.xml: UniversalEnrollmentJAO, UniversalEnrollmentMatchingGrantMultipleBeneficiaries, UniversalEnrollmentPagspSubBene. Add them to daily after stabilize, or drop the tag if they are not ready.

Acceptance Criteria
Each leftover feature is either in the daily XML with a plan parameter or explicitly excluded with reason.
CI run includes them or exclusion is in the inventory.
No feature left with @dailyrun but missing from XML without a comment.

Definition of Done
XML merged.
Evidence of pass or ticketed fail.

---

Title
[V3][CSR-Enrollment] Migrate CSR enrollment vertical slice from V2 to V3

Description
Legacy plans moved to IDP and Universal platform. CSR enrollment still runs only on V2 daily (MID, advisors, subsequent) plus V2 universal-platform CSR suites. V3 has zero CSR enrollment features. Port a vertical slice: CSR positive enroll + subsequent for an agreed plan (recommend NYD or MID equivalent on UE/IDP). Add stage1-csr-enrollment.xml and include it in Unite or UE master as decided.

Acceptance Criteria
New V3 feature(s) for CSR enroll happy path and subsequent.
Suite XML in bin/regression/daily and referenced from a master used by GitLab schedule.
Data/plan confirmed with SME (IDP/Universal).
V2 counterpart listed as keep-until-green or retire-after-parity.

Definition of Done
Scheduled or at least master-wired run evidence.
Mapped in V2 leftover inventory.

---

Title
[V3][Web-Registration] Add WebRegistrationNegative to Stage1 daily

Description
V3 Unite daily already runs first-time and re-reg (MDD/NYD/NMD). WebRegistrationNegative.feature is tagged @dailyrun but not in stage1-web-registration.xml. Wire it. Expand plants only if the negative scenarios already support them.

Acceptance Criteria
WebRegistrationNegative is in stage1-web-registration.xml and therefore in stage1-unite-regression-master.
CI evidence for the negative scenarios.
V2 daily remaining RID-only negative is noted as legacy leftover.

Definition of Done
XML merged.
Failures triaged.

---

Title
[V3][IDP-Login] Harden web login daily and confirm V2 login is retired

Description
V3 daily IDP login covers NMD, NYD, NJD, MDD, OHD, PAG, NDD. V2 stage1-web-login.xml is empty. Confirm IDP login daily is the login source of truth. Add only high-value recovery/edge cases already in features but not selected by daily tags. Do not rebuild legacy non-IDP login.

Acceptance Criteria
Documented plan list for daily vs smoke (smoke has a larger plan set).
V2 empty web-login daily is retired from Jenkins or clearly unused.
Any extra login scenarios added have evidence.

Definition of Done
Login runbook updated.
Ticket links the V2 hygiene ticket.

---

Title
[V3][Member] Move member-related coverage from V2 to V3 (personal info, contrib, withdraw)

Description
V3 Unite daily already has thinner member/CSR personal info, contributions, and withdrawals vs V2. Identify the V2 member scenarios still required now that plans are on IDP/Universal and add the missing ones to V3 daily. Do not copy the entire V2 CSR maintenance matrix.

Acceptance Criteria
Gap list: V2 member/CSR maint vs V3 daily.
P1 scenarios added to existing V3 XMLs or a new focused XML included in master.
P2 left as enhancement list.
Evidence on at least NYD and one other IDP plan.

Definition of Done
Master suite updated.
Gap list checked in.

---

Title
[V3][CSR-Enrollment] Follow-on: advisor, ABLE, and prefill CSR enrollments

Description
After the CSR vertical slice is green, port the next V2 daily CSR enrollment set: advisor plans (NYA/COA/RIA/NMA/AKA as still valid on Universal/IDP) and prefill (Wealthfront/PAD/NVU/Vanguard) only if those products still enroll that way. ABLE CSR vs member enroll called out explicitly.

Acceptance Criteria
Decision table: each V2 CSR enroll block migrate / retire.
Migrated items have V3 features and daily wiring.
Retired items have SME reason.

Definition of Done
Decision table committed.
Migrated tests evidenced.

---

Title
[V3][Enrollment] OK Direct enrollment disposition (keep V2, port to UE, or retire)

Description
OK Direct (okd) still appears on V2 enrollment daily and smoke and not on V3 UE daily. Decide with product/QA: migrate to Universal Enrollment, keep a thin V2 suite, or retire. Implement the decision.

Acceptance Criteria
Written decision with plan code okd.
If migrate: at least one UE scenario on OK Direct in daily or a dated follow-up.
If retire: removed from V2 daily with comment and inventory update.

Definition of Done
Decision on ticket.
Suites match the decision.

---

Title
[V3][Regression] Add missing high-value areas to V3 master (selective, not full V2 copy)

Description
V3 Unite daily does not include transfers, investments, ugift, empower, sardine, full CSR profile matrix. V3 universal-platform rollovers exist but are not on the GitLab schedule. After enrollment/login/registration/member P1, add only P1 leftovers the team still needs as quality gates.

Acceptance Criteria
P1 list agreed (suggested start: CSR enroll suite once built, WebReg negatives, optional UP rollovers schedule).
Each add is in a master used by GitLab scheduled_regression_job or a documented separate schedule.
P2 remains enhancement.

Definition of Done
.gitLab-ci or master XML updated.
Coverage note in kb.

---

Title
[V3][Docs] V2 to V3 runbook for Unite and Universal Enrollment

Description
There is no dedicated in-repo UI V2 to V3 migration README. Write one page: repos, bin/regression/daily folders, tags @regression @dailyrun, Maven profiles, GitLab vs Jenkins, plan codes (nyd, nmd, okd), and what moved.

Acceptance Criteria
Engineer can find how to run V3 UE daily and Unite master locally.
Plan code table including NY, NM Direct, OK Direct.
Links to leftover inventory and CSR migration stories.

Definition of Done
Doc in qa-automation-kb.
Linked from upcoming-sprints README.

---

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
