# Upcoming sprint stories

How to paste: Summary = Title line. Description = everything from Description through Definition of Done.
Parent epic for API/perf: QA-796. Labels: Upcoming, Hygin

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
