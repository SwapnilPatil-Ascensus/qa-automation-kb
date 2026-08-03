# [UNITE-MSC][ENVP][CICD] Coordinate DevOps integration of Mobile 1/2 API suites into environment pipeline workflow

**Epic:** QA-600 (link QA-796) · **Assignee:** Swapnil Patil · **Story points:** 5

---

## Description

**ENVP (Environment Pipeline)** per Epic **QA-600** and Aha **ACS-5289** requires packaged, runnable automation suites wired to CI with clear UI vs API labeling. Unite MSC Mobile 2 master regression targets **GitLab nightly** in `api-test-automation` (QA-1405 pattern). Mobile 1 suites are expanding. **DevOps implements** pipeline YAML and schedules; **this story** is QA coordination — requirements, job design review, validation runs, and runbook documentation.

**Purpose:** Get Mobile 1 and Mobile 2 API regression integrated into the ENVP/GitLab workflow so deployments can use MSC automation as a confidence gate.

**In scope:**
- DevOps partnership to add/adjust GitLab CI jobs in `api-test-automation` repo
- Mobile 2 job: `scheduled_mobile2_master_regression` — QC4 phase 1, Stage 1 phase 2 (Maven profiles `mobile-ms-master-regression`, `acceptance-qc4`, `acceptance-stage1`)
- Mobile 1 job slot documented when master suite is ready (`mobile1` POM install pattern)
- Validate Maven commands, `devopsProperties`, `gitlab.properties`, secure files — no secrets in KB
- Surefire JUnit ingest, HTML report publishing, failure triage path documented
- ENVP workflow mapping — nightly vs post-deploy trigger, pass/fail gate, triage owner
- KB runbook update; align API vs UI taxonomy with UEPIPE ENVP stories

**Out of scope:**
- Authoring all pipeline YAML (DevOps)
- Universal Enrollment UI ENVP suite (UEPIPE-01)
- Sonar/Fortify/unit gates
- Modifying `prime-test-automation` Selenium nightly

**Reference:** `programs/unite-msc/leadership/2026-07-17-leadership-update/jira-story-mobile2-nightly-gitlab.md`, `programs/unite-msc/api-validation/JIRA-story-mobile2-qc4-pipeline-dashboard.md`

---

## Acceptance Criteria

- [ ] DevOps sub-task or linked ticket created with agreed job name, schedule, and Maven command for Mobile 2 master regression
- [ ] Phase 1 (QC4) job runs green at least once; JUnit and HTML report artifacts published in GitLab
- [ ] Phase 2 (Stage 1) approach documented — second Maven leg or separate schedule
- [ ] Mobile 1 pipeline slot documented (job stub or follow-on story linked)
- [ ] ENVP mapping doc completed: trigger (nightly vs post-deploy), pass/fail gate, triage owner
- [ ] KB runbook updated with pipeline URL, rerun criteria, and troubleshooting — no secrets committed
- [ ] Sample green build URL posted in QA-600 or QA-796 Jira comment
- [ ] Retry/flake policy referenced (UEPIPE-03 or team standard)

---

## Definition of Done

- All acceptance criteria met with GitLab pipeline URL and KB runbook path in Jira
- QA Automation can trigger Mobile 2 regression from GitLab without DevOps hand-holding for routine runs
- ENVP stakeholders can see where MSC API jobs fit in the deployment workflow
- Story closed with pipeline evidence attached or linked
