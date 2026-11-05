# Upcoming sprint stories

How to paste: Summary = Title line. Description = everything from Description through Definition of Done.
Parent epic for API/perf: QA-796. Labels: Upcoming, Hygin

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
