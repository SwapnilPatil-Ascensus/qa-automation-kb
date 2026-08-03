# JIRA — SYN-443 Jenkins Perf Regression (Backlog)

**Purpose:** Context file for creating/updating the JIRA backlog story.  
**Epic:** [SYN-443](https://ascensuscollegesavings.atlassian.net/browse/SYN-443)  
**Status:** Backlog — not current sprint  
**Prerequisite:** Stage 1 perf GO (2026-07-31) — see `docs/08-performance-test-results-and-handover.md`

---

## JIRA fields

| Field | Value |
|-------|-------|
| **Issue type** | Story |
| **Summary** | `[SYN-443][Perf][Jenkins] Add barcode return-mail PUT API to performance regression pipeline (Stage 1)` |
| **Epic link** | SYN-443 |
| **Priority** | Medium |
| **Sprint** | Backlog |
| **Story points** | 5 (suggest at refinement) |
| **Component** | Performance / Jenkins |
| **Labels** | `syn-443`, `barcode`, `performance`, `jenkins`, `regression`, `stage1`, `blazemeter` |
| **Assignee** | TBD (Priti Choudhary / QA Automation) |
| **Reporter** | Swapnil Patil |

---

## Description (copy into JIRA)

### Context

SYN-443 (Returned Mail Barcode / Mailstop) performance testing was completed ad hoc in **BlazeMeter (Taurus/BZT)** and signed off **GO** for **Stage 1** on 2026-07-31. Three load scenarios passed at 30, 45, and 60 scans/min with 0% meaningful error rate and ~52–55 ms average response time.

Scripts, test data, and Postman collections exist in `qa-automation-kb/programs/barcode-syn-443/` but are **not integrated into Jenkins** for repeatable regression. This story adds the barcode perf suite to our **existing performance regression toolchain** (Jenkins → Taurus/JMeter → BlazeMeter), aligned with IDP and other Universal Platform perf jobs.

**This is a backlog item** — not required for initial production release. It enables on-demand and scheduled re-runs after deployments.

### User outcome

As QA Automation, I want the barcode return-mail **Stage 1** perf scenario runnable from **Jenkins**, so we can regression-test endpoint performance without manual BlazeMeter setup.

### API under test

| Item | Value |
|------|-------|
| Method | `PUT` |
| URL | `https://api.stage1.acs529.com/api/v1/plans/unite/returnmail/{barcodeId}` |
| Body | `{"scanResultCode":"RETURNED"}` |
| Auth | Client cert `kofaxapi.stage.acs529.com.pfx` (Jenkins credential — not in repo) |
| Test data | `programs/barcode-syn-443/artifacts/unite-returnmail-put-stage1.csv` (~200 barcode IDs) |

**Sign-off environment:** Stage 1 only. **QC4 is out of scope** (daily deploy removes auth-bypass JAR → unstable 404/503).

### Baseline reference (2026-07-31 GO run)

| Test ID | BlazeMeter test name | Load | VUs | Duration | Error rate | Avg RT | p90 |
|---------|----------------------|------|-----|----------|------------|--------|-----|
| TC03 | `unite_returnmail_put_stage1_tc03_30spm` | 30 scans/min | 10 | 11 min | 0.01% | 54 ms | 91 ms |
| TC04 | `unite_returnmail_put_stage1_tc04_45spm` | 45 scans/min | 15 | 11 min | 0% | 52 ms | 85 ms |
| TC05 | `unite_returnmail_put_stage1_tc05_60spm` | 60 scans/min | 20 | 11 min | 0% | 55 ms | 88 ms |

**BlazeMeter project:** https://a.blazemeter.com/app/#/accounts/406482/workspaces/516742/projects/2587606/tests

### Scope

**In scope**

- Commit Taurus/JMeter scripts to `performance-test-automation` repo (follow IDP job pattern)
- Create Jenkins job(s) under existing perf folder
- Wire Stage 1 PFX + passphrase via **Jenkins credentials** (no secrets in git)
- Parameterize `barcodeId` from CSV
- Publish BlazeMeter report link + archive JTL/logs on failure
- Update runbook in `qa-automation-kb/programs/barcode-syn-443/`
- **Regression tiers:**
  - **Smoke** — TC03 (30 scans/min) for frequent/scheduled runs
  - **Full** — TC03–TC05 on demand or post-deploy

**Out of scope**

- QC4 Jenkins job
- Production load testing
- Functional / UI / Kofax scanner testing
- Implementation in the sprint that delivered initial GO

### Technical approach

Follow existing perf pipeline pattern:

| Component | Reference |
|-----------|-----------|
| Taurus YAML | `performance/universal-platform/idp/jmeter/idp-login-remote.yaml` |
| BlazeMeter reporting | `reporting.module: blazemeter` in Taurus YAML |
| Jenkins agent | Existing BZT/perf agent with network to `api.stage1.acs529.com` |

**Suggested repo layout:**

```
performance-test-automation/
  performance/
    synergy/barcode-returnmail/          # confirm folder name with team
      jmeter/
        unite-returnmail-put-stage1.jmx
        unite-returnmail-put-stage1-smoke.yaml    # TC03
        unite-returnmail-put-stage1-full.yaml     # TC03–TC05
      data/
        unite-returnmail-put-stage1.csv
```

**Jenkins**

| Item | Detail |
|------|--------|
| Credential | Stage 1 PFX + passphrase (secret store) |
| Keystore | JMeter Keystore Configuration |
| Triggers | Manual; optional weekly cron; post-deploy `[TBD]` |
| Pass/fail gate | Error rate ≤ 1%; p90 ≤ 150 ms `[TBD with Rajib]` |

### Dependencies

| Dependency | Owner |
|------------|-------|
| Working BZT/JMX from GO testing | Priti Choudhary |
| Jenkins credential (PFX) | Swapnil / DevOps |
| Agent network to Stage 1 | DevOps |
| BlazeMeter project access | QA Automation |
| Stage 1 barcode data refresh | Suresh Mahto / DBA |

### References

| Resource | Location |
|----------|----------|
| Results & handover | `programs/barcode-syn-443/docs/08-performance-test-results-and-handover.md` |
| Postman / cert setup | `programs/barcode-syn-443/docs/07-stage1-postman-cert-setup.md` |
| Test data | `programs/barcode-syn-443/artifacts/unite-returnmail-put-stage1.csv` |
| Execution report | `programs/barcode-syn-443/artifacts/UNITE-RETURNMAIL-PERFORMANCE-TEST-EXECUTION-REPORT-v1.2.docx` |
| Perf CI overview | `qa-knowledge-base/10_IMPORTS_RAW/.../CICD/05-performance-testing-pipelines.md` |

---

## Acceptance criteria

### AC1 — Scripts in source control

- [ ] JMeter script (`.jmx`) committed to `performance-test-automation` under agreed folder path
- [ ] Taurus YAML(s) committed for smoke (TC03) and full suite (TC03–TC05)
- [ ] CSV test data committed or documented pull from KB artifacts
- [ ] No PFX, passphrase, or secrets in repository

### AC2 — Jenkins smoke job (TC03)

```gherkin
Scenario: Smoke perf regression passes in Stage 1
  Given Jenkins credential for Stage 1 PFX is configured
  And the smoke job uses TC03 load profile (30 scans/min, 10 VU, 11 min hold)
  When the Jenkins job is triggered manually
  Then the build completes with status SUCCESS
  And HTTP error rate is ≤ 1%
  And p90 response time is ≤ 150 ms
  And all responses are 2xx
```

### AC3 — Jenkins full suite job (TC03–TC05)

```gherkin
Scenario: Full perf suite runnable on demand
  Given the full-suite Jenkins job exists
  When triggered manually with TC03, TC04, and TC05 profiles
  Then each scenario completes with error rate ≤ 1%
  And p90 per scenario is within baseline + 50% buffer (TC03: 137 ms, TC04: 128 ms, TC05: 132 ms)
```

### AC4 — Reporting & artifacts

- [ ] BlazeMeter report URL published in Jenkins build output
- [ ] JTL / logs archived as Jenkins build artifacts on failure
- [ ] Job name and parameter documentation added to KB

### AC5 — Security & credentials

- [ ] Stage 1 client cert loaded exclusively from Jenkins credentials
- [ ] Credential rotation documented (who owns PFX renewal)

### AC6 — Handoff

- [ ] QA Automation team can run smoke job without author assistance
- [ ] Retest trigger documented: new deployment / cert change / endpoint code change

---

## Definition of Done

Story moves to **Done** only when **all** items below are satisfied.

### Delivery

| # | Criterion | Evidence |
|---|-----------|----------|
| D1 | All **acceptance criteria** (AC1–AC6) met | JIRA checklist complete |
| D2 | JMeter/Taurus scripts **merged** to `performance-test-automation` integration branch | PR link in comment |
| D3 | Jenkins **smoke job** runs green end-to-end on Stage 1 | Build URL in comment |
| D4 | Jenkins **full suite job** created (may be separate job) and verified at least once | Build URL in comment |
| D5 | **No secrets** in git; PFX/passphrase only in Jenkins credential store | PR review sign-off |

### Quality gates

| # | Criterion | Evidence |
|---|-----------|----------|
| D6 | Smoke run: error rate **≤ 1%**, p90 **≤ 150 ms**, all **2xx** | BlazeMeter screenshot or report link |
| D7 | No open **Sev1/Sev2** defects on story scope | JIRA query / comment |

### Documentation & handoff

| # | Criterion | Evidence |
|---|-----------|----------|
| D8 | Runbook updated: `programs/barcode-syn-443/docs/09-jenkins-regression-runbook.md` (job name, params, triggers, creds owner) | KB PR or commit link |
| D9 | `programs/barcode-syn-443/jira/README.md` updated with JIRA ticket number once created | Commit link |
| D10 | Team notified (email/Teams) with Jenkins job name and when to run post-deploy | Comment with date |

### Review

| # | Criterion | Evidence |
|---|-----------|----------|
| D11 | **Peer review** on perf repo PR | Approved PR |
| D12 | **Swapnil or Rajib** acknowledges job meets regression intent | JIRA comment |

### Waivers

| Waiver | Requires |
|--------|----------|
| Full suite job (D4) deferred to follow-up story | PO comment + smoke job (D3) still required |
| Cron schedule not enabled at launch | Document manual trigger; backlog item for scheduling |

---

## Sub-tasks (JIRA)

| # | Sub-task | Owner | Maps to |
|---|----------|-------|---------|
| 1 | Export and commit BZT/JMX from BlazeMeter project | Priti | AC1 |
| 2 | Create `synergy/barcode-returnmail` folder in perf repo | Priti | AC1 |
| 3 | Create Jenkins credential for Stage 1 PFX | Swapnil / DevOps | AC5 |
| 4 | Create Jenkins smoke job (TC03) | Priti / Chaitanya | AC2 |
| 5 | Create Jenkins full suite job (TC03–TC05) | Priti | AC3 |
| 6 | Write `docs/09-jenkins-regression-runbook.md` | Swapnil | D8 |
| 7 | Demo run + team handoff | Swapnil | D10, D12 |

---

## Notes for refinement

- Confirm Jenkins folder name with Chaitanya (Universal Platform perf vs new Synergy folder).
- Confirm pass/fail thresholds with Rajib before enabling as release gate.
- Post-deploy webhook is optional phase 2 — do not block story on it.

---

**Author:** Swapnil Patil  
**Created:** 2026-07-31  
**Last updated:** 2026-07-31
