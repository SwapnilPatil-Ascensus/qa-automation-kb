# Suggested Jira Stories — Coverage Intelligence Program

**As of:** 2026-07-21  
**Epic suggestion:** GS Coverage Intelligence & Quality Gates  
**Format:** Ready to paste into Jira

---

## Story 1: Coverage Register MVP

**Title:** GS Coverage Register MVP — versioned CSV/JSON with metric A–E separation

**Business value:** Leadership receives trustworthy, dated, platform-specific coverage metrics without a single misleading GS-wide percentage.

**Description:**  
Extend existing Python utilities (`government-savings-automation-assessment/tools/`, `coverage-intelligence-assessment/tools/`) to produce a weekly versioned coverage register. Each row includes numerator, denominator, formula, as-of date, source, confidence, owner, freshness status, and verification label. Import approved rows into `verified-metrics-register.csv`. Generate leadership summary MD from register only.

**Acceptance criteria:**
- [ ] Register schema documented with required fields
- [ ] Weekly automated run produces timestamped CSV/JSON
- [ ] No blended A–E metrics in output
- [ ] Leadership summary generated from register import
- [ ] Manual override path documented for SME-reviewed rows

**Dependencies:** Metric definitions A–E approved; repo scanner available  
**Risks:** Manual edits bypass automation — mitigate with git-versioned register  
**Evidence:** `verified-metrics-register.csv`, `live_validation_build.py`  
**Owner recommendation:** QA Automation Lead

---

## Story 2: qTest Read-Only Integration

**Title:** qTest read-only collector for test inventory and execution history

**Business value:** Replaces stale PDF exports with current test inventory for metric B and execution metric C.

**Description:**  
Implement scheduled Python collector using qTest REST API v3. Extract cases, automation flags, regression designation, requirement links, and last execution per case. Output `qtest-snapshot.json` and normalized CSV. Read-only — no writes to qTest.

**Acceptance criteria:**
- [ ] `QTEST_BASE_URL`, `QTEST_API_TOKEN`, `QTEST_PROJECT_ID` configured securely
- [ ] Weekly snapshot with case count and last-run timestamps
- [ ] Stale data flagged when last run >30 days
- [ ] Collector logs errors without failing silently

**Dependencies:** IT provisions qTest API token  
**Risks:** Rate limits; incomplete custom fields  
**Evidence:** `qtest-readiness-assessment.md`, export 2026-06-29  
**Owner recommendation:** QA Automation Engineer

---

## Story 3: Jira Scope Integration

**Title:** Jira read-only collector for approved scope and acceptance criteria

**Business value:** Establishes authoritative business denominator for coverage reconciliation.

**Description:**  
Collect scoped epics/stories for Government Savings programs. Extract acceptance criteria count, linked qTest keys where present, and service/endpoint identifiers from labels or custom fields. Output `jira-scope-snapshot.json`.

**Acceptance criteria:**
- [ ] Jira API credentials configured
- [ ] Filtered JQL for GS scope agreed with Product
- [ ] Weekly snapshot with story count and AC count
- [ ] Link quality report (`jira-qtest-link-quality.csv`) refreshed

**Dependencies:** Jira API access; approved scope JQL  
**Risks:** Jira hygiene varies by team  
**Evidence:** `jira-scope-assessment.md`  
**Owner recommendation:** QA Automation + BA

---

## Story 4: GitLab Live Pipeline Collector

**Title:** GitLab pipeline collector for execution and gate evidence

**Business value:** Provides live metric D (CI integration) and E (gate behavior) without manual YAML review.

**Description:**  
Using GitLab REST API or `glab`, collect last pipeline status per known job: `scheduled_regression_job`, `scheduled_metadataweb_stage1`, UniteMSC service pipelines. Map to repository inventory. Output `execution-snapshot.json`.

**Acceptance criteria:**
- [ ] Valid GitLab PAT with read_api scope
- [ ] Last run status, duration, and artifact presence captured
- [ ] Scheduled vs MR pipelines distinguished
- [ ] Failures marked; YAML presence not counted as execution

**Dependencies:** CI-003 GitLab PAT  
**Risks:** Token expiry; external template jobs not visible in repo YAML  
**Evidence:** `pipeline-job-inventory.csv`, glab HTTP 401  
**Owner recommendation:** QA Automation Engineer

---

## Story 5: GitHub Actions Collector

**Title:** GitHub Actions collector for Mobile 2 deployment validation evidence

**Business value:** Closes gap on GHA workflow not present in `api-test-automation` clone.

**Description:**  
Install `gh` CLI and configure token. Collect workflow runs for Mobile 2 Nexus/Dashboard pipeline. Output `gha-execution-snapshot.json` with pass/fail and artifact links.

**Acceptance criteria:**
- [ ] Workflow repository identified and cloned
- [ ] Last 30 days of runs captured
- [ ] Distinguished from GitLab scheduled regression
- [ ] Documented as deployment validation (metric E subset)

**Dependencies:** GitHub token; workflow repo URL  
**Risks:** Repo access permissions  
**Evidence:** `17-MOBILE2-NEXUS-GITHUB-ACTIONS-PIPELINE.md`, E-011  
**Owner recommendation:** QA Automation Engineer

---

## Story 6: Jenkins Collector

**Title:** Jenkins collector for V2 UI and performance execution evidence

**Business value:** Captures legacy V2 and performance jobs not visible in GitLab YAML.

**Description:**  
Collect job status for `AGSUP_IDP_REGRESSION_SUITE`, `AGSUP_UNITE_MSC_ENDURANCE`, inferred V2 UI regression, and TB refresh jobs. Output `jenkins-execution-snapshot.json`.

**Acceptance criteria:**
- [ ] Jenkins API URL and token configured
- [ ] Job list matches KB inventory
- [ ] Last run and result captured per job
- [ ] TB refresh jobs marked as environment prep not regression gate

**Dependencies:** Jenkins API access  
**Risks:** Job names differ by environment  
**Evidence:** `ci-gate-assessment.md`, perf tracker  
**Owner recommendation:** QA Automation + DevOps

---

## Story 7: JaCoCo Coverage-Delta Pilot

**Title:** JaCoCo coverage-delta comparison pilot on unite-mobile2

**Business value:** Enables evidence-based answer to "can we block MR on coverage decrease?"

**Description:**  
Implement `compare_jacoco.py` to diff MR JaCoCo XML against `main` baseline. Report overall regression and changed-code coverage. Phase 1: informational MR comment only.

**Acceptance criteria:**
- [ ] Script reads two jacoco.xml files and git diff scope
- [ ] Outputs pass/fail with numeric delta
- [ ] Sample MR demonstrates report
- [ ] Documented as metric A gate pilot — not business automation

**Dependencies:** CI-008 pipeline artifact  
**Risks:** Baseline artifact missing on first run  
**Evidence:** `unite-mobile2/pom.xml` 90% threshold, implementation plan  
**Owner recommendation:** QA Automation Engineer

---

## Story 8: Branch Protection Required Check

**Title:** Add coverage-delta as required protected-branch status check (pilot)

**Business value:** Enforces coverage regression policy without replacing existing approvals.

**Description:**  
After Phase 1 tuning, configure GitLab protected `main` on `unite-mobile2` to require `coverage-delta-check` job. Retain existing Snyk, pipeline, and senior Code Review rules.

**Acceptance criteria:**
- [ ] Job appears in MR status checks
- [ ] Merge blocked when check fails (Phase 3)
- [ ] Existing controls unchanged
- [ ] Documented in repository matrix

**Dependencies:** Story 7; DevOps pipeline template  
**Risks:** False positives block delivery — require Phase 1–2 first  
**Evidence:** `code-coverage-gate-decision-brief.md`  
**Owner recommendation:** DevOps Engineer

---

## Story 9: Controlled Bypass Process

**Title:** Coverage gate exception process with auditable bypass group

**Business value:** Leadership can trust gates have a governed escape hatch for exceptional cases.

**Description:**  
Define named senior exception group (subset of Code Review). Require waiver ID, reason, risk owner, expiration (max 30 days). Publish monthly `coverage-exception-register.csv`. Configure GitLab approval rule for bypass.

**Acceptance criteria:**
- [ ] Exception group named and membership approved
- [ ] Waiver template fields mandatory
- [ ] Monthly register published to leadership
- [ ] Distinct from general MR approval bypass

**Dependencies:** Leadership approval  
**Risks:** Bypass becomes routine — monitor exception count  
**Evidence:** `ci-gate-strategy.md` section 7  
**Owner recommendation:** QA Governance + DevOps

---

## Story 10: qTest/Test-Code Identifier Standard

**Title:** Stable automation_id standard linking qTest, Jira, and test code

**Business value:** Enables automated reconciliation across ALM and repositories.

**Description:**  
Publish standard: `automation_id`, `qtest_case_id`, `jira_key`, `endpoint_key`. Pilot on Mobile 2 tests in `api-test-automation`. Add MR template reminder for new tests.

**Acceptance criteria:**
- [ ] Standard published in KB standards folder
- [ ] ≥10 Mobile 2 tests carry all four identifiers
- [ ] Reconciliation prototype matches ≥10 rows
- [ ] No qTest writes required

**Dependencies:** Team agreement  
**Risks:** Adoption lag on legacy tests  
**Evidence:** `identifier-mapping-candidates.csv`  
**Owner recommendation:** QA Automation Lead

---

## Story 11: Freshness SLA

**Title:** Coverage metric freshness SLA and governance cadence

**Business value:** Prevents stale execution evidence from being presented as current.

**Description:**  
Define SLA: execution metrics ≤7 days; inventory ≤30 days; qTest/Jira snapshots weekly. Label register rows Stale when exceeded. Assign owners per domain.

**Acceptance criteria:**
- [ ] SLA published in `data-freshness-and-ownership.md`
- [ ] Register auto-flags stale rows
- [ ] Leadership report shows as-of dates on every metric
- [ ] Owners named per platform (M1, M2, V2, V3)

**Dependencies:** Register MVP  
**Risks:** Teams cannot meet SLA without CI schedules — prioritize QA-1405  
**Evidence:** M-M2-EXEC Stale status  
**Owner recommendation:** QA Governance Lead

---

## Story 12: Leadership Reporting Automation

**Title:** Automated leadership summary from coverage register

**Business value:** Reduces manual synthesis and ensures consistent metric separation in executive comms.

**Description:**  
Extend `generate_gs_assessment_deliverables.py` to produce weekly leadership MD/PDF from register only. Include exception report and trend section. Never output blended GS-wide %.

**Acceptance criteria:**
- [ ] One-command generation from register
- [ ] All metrics include as-of date and status label
- [ ] PDF ≤3 pages for executive summary
- [ ] Contradiction section when data-conflicts exist

**Dependencies:** Register MVP; collectors  
**Risks:** Over-automation hides context — keep notes field  
**Evidence:** `leadership-summary.md`, deliverables generator  
**Owner recommendation:** QA Automation Lead

---

## Story 13: Mobile 2 API GitLab Nightly (QA-1405)

**Title:** QA-1405 — Schedule Mobile 2 master regression on GitLab Stage 1

**Business value:** Closes metric D/E gap for highest-visibility MSC API automation.

**Description:**  
Add `scheduled_mobile2_stage1` job to `api-test-automation/.gitlab-ci.yml` running `master-regression-testng.xml` with secure files. Configure GitLab pipeline schedule.

**Acceptance criteria:**
- [ ] Job in `.gitlab-ci.yml` on `main`
- [ ] Pipeline schedule configured and green
- [ ] JUnit artifacts archived
- [ ] M-M2-CI updated to 100% in register

**Dependencies:** DevOps secure files; QA-1405  
**Risks:** Environment instability — not a merge gate  
**Evidence:** E-009 YAML absence  
**Owner recommendation:** DevOps + QA Automation

---

*Link stories to epic GS Coverage Intelligence. Prioritize 1, 4, 7, 8, 9, 11, 13 for Michael Blake follow-up.*
