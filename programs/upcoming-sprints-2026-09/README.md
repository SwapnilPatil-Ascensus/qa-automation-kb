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

## Current Unite MSC docs in this repo

`programs/unite-msc/` now has four folders only: `leadership/`, `mobile-1/`, `mobile-2/`, `enrollment/`.

Enrollment coverage: `programs/unite-msc/enrollment/coverage/` (status MD, matrix XLSX, endpoint CSV).
Mobile sign-off: `programs/unite-msc/mobile-1/signoff/`, `programs/unite-msc/mobile-2/signoff/`.
