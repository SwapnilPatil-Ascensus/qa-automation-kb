# Upcoming sprint stories

How to paste: Summary = Title line. Description = everything from Description through Definition of Done.
Parent epic for API/perf: QA-796. Labels: Upcoming, Hygin

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
