# Upcoming two-sprint backlog (Sep 2026)

Parent epic for API work: QA-796 Unite MSC Test Automation  
Suggested Jira labels: Upcoming, Hygin, unite-msc  
Do not recreate existing coding tickets listed at the bottom of STORIES.md

## Copy-paste stories

One file with all categories:

- STORIES.md

Same content split by area:

- 01-api-msc-stories.md
- 02-v2-stories.md
- 03-v3-stories.md
- 04-performance-stories.md

Each story has Title, Description, Acceptance Criteria, Definition of Done. Paste Title into Jira Summary. Paste the rest into Description (Jira Cloud markdown).

## What was verified in local repos (Sep 2 2026)

API (api-test-automation/mobile): Mobile 1 and Mobile 2 coding complete. Enrollment wizard including review-confirm plus subsequent enrollment coded for OK Direct and New York. NM Direct enrollment is localhost only. No Bruno. No unified Postman. No enrollment nightly in local gitlab-ci.

V2 (unite-test-automation/unite bin/regression/daily): ~182 daily blocks. Enrollment and CSR enrollment still live here. stage1-web-login.xml is empty.

V3 Unite + Universal Enrollment: GitLab scheduled UE (24) then Unite master (36). No CSR enrollment. Several @dailyrun features not in XML.

Performance: Mobile 2 JMeter + AGSUP_UNITE_MSC_ENDURANCE exists but not nightly timer. Mobile 1 is auth-only inside those scripts. Enrollment E2E jmx exists (up-enrollment-submission.jmx). Docs are thin.

## Documents updated in this repo (this pass)

programs/unite-msc/program-hub/05-unite-enrollment-migration-tracker.md — rewritten to current coding status  
programs/unite-msc/program-hub/status-summary.md — leadership one-pager  
programs/unite-msc/program-hub/README.md — link to this folder  
programs/unite-msc/api-test-automation/postman/EnrollmentE2E/tools/generate_enrollment_coverage_matrix.py — subsequent + review-confirm marked Done  
programs/unite-msc/api-test-automation/postman/EnrollmentE2E/Enrollment-Automation-Coverage-Status.md — regenerated  
programs/unite-msc/api-test-automation/postman/EnrollmentE2E/Enrollment-Automation-Coverage-Matrix.xlsx — regenerated (25 Done / 28 catalog)  
programs/unite-msc/api-test-automation/postman/README.md — Sep note  
programs/unite-msc/api-test-automation/mappings/README.md — new files  
programs/unite-msc/api-test-automation/mappings/enrollment-endpoint-current-state.csv — new  
programs/unite-msc/api-test-automation/mappings/legacy-new-postman-excel-mapping.md — new  
programs/unite-msc/api-test-automation/docs/06-coverage/01-coverage-and-mapping-index.md  
programs/unite-msc/api-test-automation/docs/06-coverage/05-code-coverage-metrics.md  
programs/unite-msc/api-test-automation/docs/06-coverage/signoff/README.md  
programs/unite-msc/api-test-automation/docs/06-coverage/signoff/enrollment-signoff-summary.md — new draft
