# JIRA Story 2 — [PERF TESTING][IDP-LOGIN-BZT] Jenkins setup and end-to-end BlazeMeter testing for post-login banner pages

---

## JIRA fields (copy/paste)

| Field | Value |
|-------|-------|
| **Issue Type** | Story |
| **Summary** | `[PERF TESTING][IDP-LOGIN-BZT] Jenkins setup and end-to-end BlazeMeter testing for post-login banner pages` |
| **Priority** | High |
| **Sprint** | Next sprint (starts Aug 5, 2026) |
| **Assignee** | Preeti Choudhary |
| **Reporter** | Swapnil Patil |
| **Components** | Performance Testing, IDP Login, Jenkins |
| **Labels** | performance-testing, idp-login, jmeter, jenkins, blazemeter, stage1, jia-banner |
| **Story Points** | 5 |
| **Epic Link** | IDP Login Post-Banner Performance Testing (Jia Server Investigation) |
| **Linked Issues** | Blocked by / follows Story 1 (script deploy & local validation) |

---

## Description

### Background

Story 1 delivers a working `idp-login-resources.jmx` with 6 post-login banner/dashboard `.cs` GET requests. This story covers **Jenkins deployment, BlazeMeter end-to-end execution on stage1, baseline reporting, and the stakeholder-requested load profile** — plus preparation for post-patch comparison when the platform team applies their fix.

Platform team (Arun, Mayank, Dhruv) needs performance data for:
- 5 distinct plans
- 50 parallel users
- Post-login banner pages (`customBannerMessage.cs` and related endpoints)
- Comparison before/after platform patch on stage1

### Business value

- Automated repeatable perf test for post-login banner lag on stage1
- Baseline metrics for platform team before patch deployment
- Evidence for go/no-go on patch effectiveness
- Shared BlazeMeter reports for Arun, Mayank, Dhruv, and leadership

### Scope — IN

- Sync deployed JMX from Story 1 to Jenkins agent (`loadtestwt2` / `agsup-endurance`)
- Validate existing Jenkins job `AGSUP_ENDURANCE_THROUGHPUT` runs successfully with updated script (15 BlazeMeter labels)
- Confirm BlazeMeter report shows new transaction steps (8-A-1 through 8-A-6)
- Coordinate with DevOps on GitLab → Jenkins agent sync process
- Evaluate/create Jenkins job configuration for stakeholder load profile (50 users, 5 plans, 5 min)
- Execute baseline run on stage1 with agreed parameters
- Capture and publish BlazeMeter report links
- Document results in KB (`BASELINE_RESULTS.md` update)
- Coordinate with Arun on final plan selection and load parameters
- Prepare rerun procedure for post-patch comparison (execute when patch is deployed — may be separate follow-up task)

### Scope — OUT

- JMeter script authoring (Story 1 — unless E2E reveals fixes needed)
- Platform patch development or deployment
- Production load testing
- BlazeMeter project/license changes
- Functional regression testing (separate `AGSUP_IDP_REGRESSION_SUITE`)

---

## Technical details

### Jenkins — existing job

| Field | Value |
|-------|-------|
| Job name | `AGSUP_ENDURANCE_THROUGHPUT` |
| URL | http://jenkinsqant1:8080/view/Performance/job/AGSUP_ENDURANCE_THROUGHPUT/ |
| View | Performance |
| Agent | `loadtestwt2` |
| Working dir | `/home/devops/agsup-endurance` |
| Upstream trigger | `AGSUP_IDP_REGRESSION_SUITE` (nightly) |
| Docker image | `blazemeter/taurus:withplugins:latest` |

### Default parameters (nightly endurance — Phase 1 E2E)

| Parameter | Value |
|-----------|-------|
| server | loadtestwt2 |
| yaml | `universal/idp/jmeter/idp-login-resources-remote.yaml` |
| environment | stage1 |
| encrypted | false |
| concurrency | 25 |
| duration | 1h |
| ramp | 5m |
| throughput | 600 |

### Stakeholder load profile (Phase 2 — confirm with Arun)

| Parameter | Target | Notes |
|-----------|--------|-------|
| Plans | 5 distinct | Suggested: nyd, nmd, njd, idd, mod |
| Total users | 50 parallel | ~10 per plan |
| Ramp | 5 minutes | |
| Duration | 5 minutes hold | **Confirm with Arun** |
| Throughput | 600/min | Tune if errors spike |
| Focus endpoints | `customBannerMessage.cs` + all 6 new pages | |

### Optional: dedicated Jenkins job

Consider creating `AGSUP_IDP_BANNER_PERF` (or one-off parameterized build) so nightly 25-user/1h endurance is not disrupted. Document decision in JIRA.

### BlazeMeter

| Field | Value |
|-------|-------|
| Project | AGS Automation Regression |
| Test name | IDP Test - Member Login (CS/API w/ Resources + Post-Login Pages) |
| Expected labels | 15 (9 original + 6 new banner/dashboard steps) |

### Docker command (reference)

```bash
docker run --rm --privileged \
  -e jmconcurrency=25 -e jmhold=1h -e jmramp=5m -e jmthroughput=600 -e jencryption=false \
  -v /home/devops/agsup-endurance:/bzt-configs \
  --env-file setup/stage1.properties \
  blazemeter/taurus:withplugins:latest \
  setup/base_taurus.yaml universal/idp/jmeter/idp-login-resources-remote.yaml
```

### Test data

- CSV: `idp-login-stage1.csv` (no change expected)
- For 5-plan / 50-user run: filter or subset CSV to selected plans (see `docs/reference/TEST_DATA.md`)

### Success metrics to capture

| Metric | Source |
|--------|--------|
| Avg / p90 / p95 / p99 response time per label | BlazeMeter |
| Error % per label (especially 8-A-1 through 8-A-6) | BlazeMeter |
| Total throughput (hits/s) | BlazeMeter |
| Comparison vs pre-change baseline (build #597) | `docs/reference/BASELINE_RESULTS.md` |

### Pre-change baseline (reference)

| Metric | Value (build #597) |
|--------|-------------------|
| Users | 25 |
| Avg RT | 331 ms |
| p90 | 944 ms |
| Error % | 0.44% |
| Step 8 Overview avg RT | 1,653 ms (3.83% errors) |

---

## Tasks / Subtasks

### Phase A — Jenkins deploy & smoke (Sprint start)

- [ ] **2.1** Confirm Story 1 JMX is merged in GitLab `performance-test-automation`
- [ ] **2.2** Coordinate with DevOps: sync `agsup-endurance` on `loadtestwt2` from GitLab
- [ ] **2.3** (Optional) Update `idp-login-resources-remote.yaml` BlazeMeter test name in repo + agent
- [ ] **2.4** Trigger manual Jenkins build: concurrency=1, duration=5m, environment=stage1
- [ ] **2.5** Verify BlazeMeter report shows **15 transaction labels** including 8-A-1 through 8-A-6
- [ ] **2.6** Fix any Jenkins/agent issues (path, CSV, auth folder, proxy)

### Phase B — Full E2E validation (existing profile)

- [ ] **2.7** Run `AGSUP_ENDURANCE_THROUGHPUT` with default params (25 users, 1h, 5m ramp, stage1)
- [ ] **2.8** Capture BlazeMeter master link; verify error % acceptable (≤ baseline + 0.5%)
- [ ] **2.9** Document per-label metrics for new banner steps in JIRA + update `BASELINE_RESULTS.md`
- [ ] **2.10** Share BlazeMeter link with Swapnil, Arun, Mayank, Dhruv on Teams

### Phase C — Stakeholder load test

- [ ] **2.11** Confirm with Arun: 5 plans, 50 users, duration, user split
- [ ] **2.12** Prepare CSV subset or Jenkins params for 5-plan run
- [ ] **2.13** Create dedicated Jenkins job OR one-off parameterized build (document choice)
- [ ] **2.14** Execute 50-user / 5-plan / 5m run on stage1
- [ ] **2.15** Capture BlazeMeter report; highlight `customBannerMessage.cs` and all 8-A-* steps
- [ ] **2.16** Present results to platform team; log as **pre-patch baseline**

### Phase D — Post-patch readiness

- [ ] **2.17** Document rerun procedure (same Jenkins params, same plans)
- [ ] **2.18** Add post-patch comparison template to KB or JIRA
- [ ] **2.19** Execute post-patch rerun when platform team deploys (may roll to follow-up story if patch not ready this sprint)

---

## Acceptance criteria

| # | Criterion | Verifiable by |
|---|-----------|---------------|
| AC1 | Updated JMX from Story 1 is deployed and running on Jenkins agent `loadtestwt2` | Jenkins console log shows correct script path |
| AC2 | Manual Jenkins smoke (1 user, 5m) completes with all **15 BlazeMeter labels** present | BlazeMeter report screenshot/link |
| AC3 | Full E2E run on stage1 (25 users, 1h, 5m ramp) completes; BlazeMeter link captured | BlazeMeter master URL in JIRA |
| AC4 | New banner/dashboard steps (8-A-1 through 8-A-6) appear in BlazeMeter with metrics (avg RT, p90, error %) | BlazeMeter transaction table |
| AC5 | Overall error rate ≤ **1%** on full E2E run OR failures documented as stage1 env issues with evidence | BlazeMeter summary |
| AC6 | Stakeholder load test executed per agreed params (50 users, 5 plans, 5m ramp — confirm duration with Arun) | BlazeMeter report |
| AC7 | Pre-patch baseline report shared with Arun, Mayank, Dhruv on Teams with BlazeMeter link | Teams message / JIRA comment |
| AC8 | `docs/reference/BASELINE_RESULTS.md` updated with new run metrics | Git commit / KB update |
| AC9 | Post-patch rerun procedure documented; ready to execute when platform patch is deployed | KB or JIRA doc link |
| AC10 | Jenkins job configuration documented (existing vs new job, parameters used) | JIRA / `JENKINS_AND_BLAZEMETER.md` update |

---

## Definition of Done (DoD)

- [ ] Story 1 completed and JMX available in GitLab (prerequisite)
- [ ] All acceptance criteria (AC1–AC10) met or explicitly deferred with stakeholder approval (e.g. post-patch rerun if patch not on stage1 this sprint)
- [ ] Jenkins agent synced with latest JMX; deploy process documented
- [ ] At least **two** successful BlazeMeter runs completed and linked in JIRA:
  - Run 1: Validation (25 users, 1h — or approved equivalent)
  - Run 2: Stakeholder profile (50 users, 5 plans)
- [ ] BlazeMeter reports show 15 transaction labels including all 6 new post-login pages
- [ ] Results shared with platform stakeholders (Arun, Mayank, Dhruv) on Teams
- [ ] KB updated: `BASELINE_RESULTS.md`, `OPEN_ITEMS.md` (closed/updated items), Jenkins docs if job created
- [ ] No unresolved **blocker** defects preventing repeatability of the Jenkins run
- [ ] Demo or walkthrough provided to Swapnil / QA lead (BlazeMeter dashboard + key metrics)
- [ ] Post-patch comparison procedure documented for follow-up execution

---

## Dependencies

| Dependency | Owner | Required by |
|------------|-------|-------------|
| Story 1 complete (working JMX in GitLab) | Preeti | Sprint start |
| DevOps: `agsup-endurance` sync process | DevOps | Phase A |
| Arun: confirm 5 plans + 50-user profile | Arun | Phase C |
| Mayank: Network tab / endpoint questions | Mayank | As needed |
| stage1 environment stable | Platform/Infra | All phases |
| Platform patch on stage1 (for post-patch rerun) | Platform team | Phase D — may slip |

## Risks

| Risk | Mitigation |
|------|------------|
| Jenkins agent not synced after GitLab push | DevOps coordination task 2.2 |
| 50-user run impacts stage1 | Schedule with platform team; off-peak window |
| Patch not ready this sprint | Document rerun procedure; defer AC9 execution |
| BlazeMeter error spike on banner steps | Compare with Story 1 local smoke; engage Mayank |

## Open items to resolve during sprint

See `docs/open-items/OPEN_ITEMS.md` — especially:
- Which 5 plans for 50-user run (Arun)
- Test duration: 5m total vs 5m ramp + hold (Arun)
- Separate Jenkins job vs reuse existing (Swapnil/DevOps)
- Post-patch pass/fail threshold (Arun/Platform)

---

## References

- Story 1: `docs/jira/STORY-1-IDP-BANNER-SCRIPT-DEPLOY.md`
- KB handoff: `PRITI_HANDOFF.md`
- Jenkins: http://jenkinsqant1:8080/view/Performance/job/AGSUP_ENDURANCE_THROUGHPUT/
- Pre-change baseline: `docs/reference/BASELINE_RESULTS.md` (build #597, master 82884601)
- Workflow: `docs/workflow/WORKFLOW.md`
- Environment setup: `docs/setup/ENVIRONMENT_SETUP.md`

---

## Suggested JIRA comment on completion

```
Story 2 complete.

Jenkins:
- Job: AGSUP_ENDURANCE_THROUGHPUT (or AGSUP_IDP_BANNER_PERF)
- Agent sync: <date/method>

BlazeMeter runs:
1. E2E validation (25u/1h): <master link>
2. Stakeholder run (50u/5 plans): <master link>

New steps 8-A-1..8-A-6 metrics: <summary p90/error%>
Shared with Arun/Mayank/Dhruv on Teams: <date>

Pre-patch baseline: captured
Post-patch rerun: documented, pending platform patch
```

---

## Follow-up story (if needed)

If platform patch lands after this sprint:

**Summary:** `[PERF TESTING][IDP-LOGIN-BZT] Post-patch comparison run on stage1`  
**Scope:** Re-run identical 50-user/5-plan profile; compare 8-A-* p90/error% vs Story 2 baseline; share delta with platform team.
