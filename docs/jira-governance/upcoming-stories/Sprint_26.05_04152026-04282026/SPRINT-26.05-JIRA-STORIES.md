# Sprint 26.05 — Jira Story Markdown (drafts)

**Sprint window:** 15 Apr 2026 – 28 Apr 2026  
**Reporter:** Swapnil Patil  
**Epic links:** Map each Story to your Jira Epic (e.g. `QA-E-V2-*`, `QA-E-V3-*`, `QA-E-PLAT-INF`, `QA-E-PERF-FLOW`) — **Needs Validation** if not confirmed.

**Evidence index:** See [README.md](README.md).

---

## A) Venkatesh Mallela

### S2605-01 — Story

**Summary:** `[V2][CSR][Exchange] Filter accounts for Exchange — custom + annual criteria`

**Issue type:** Story  
**Assignee:** Venkatesh Mallela

**Description**

- **As a** QA automation engineer  
- **I want** automation that selects **only eligible accounts** for CSR **Exchange** (custom and annual paths) per business rules  
- **So that** exchange scenarios do not pull ineligible accounts and nightly regression stays reliable

**Scope**

- **Portal:** CSR only.  
- **Stack:** V2 (legacy / Ant / Jenkins per program).  
- **In:** Account-selection / filtering logic aligned to **Custom Exchange** and **Annual Exchange** CSR flows; reuse or extend patterns described in KB `jira-export.csv` (e.g. CSR custom exchange locators in `csr_element_locators.txt` / `common_element_locators.txt`, `unite-automation.jar`, tags `@regression` / `@dailyrun`). Reference exchange-related Jira narratives: **QA-531**, **QA-533** (custom/annual CSR/member context).  
- **Out:** Member portal (see **S2605-02**).

**Acceptance Criteria (GWT)**

```gherkin
Scenario: Custom exchange account filter
  Given CSR exchange automation runs with test data marked for custom exchange eligibility
  When accounts are resolved for a custom exchange scenario
  Then only accounts meeting agreed custom-exchange rules are selected (ineligible excluded or asserted as blocked)

Scenario: Annual exchange account filter
  Given CSR exchange automation runs with test data for annual exchange
  When accounts are resolved for an annual exchange scenario
  Then only accounts meeting agreed annual-exchange rules are selected

Scenario: Regression safety
  Given existing CSR exchange scenarios in regression
  When this Story is merged
  Then previously passing tagged scenarios still pass unless a linked defect changes expected behavior
```

**Definition of Done**

- [ ] Merged to integration branch; V2 job green for in-scope tags.  
- [ ] SME/QA Lead comment with rule summary or link to testcase CSV row names used.  
- [ ] Evidence: report link or Jenkins job URL.

**Dependencies / Risks**

- Depends on SME rules for eligibility matrix.  
- **Risk:** Data drift between plans — document which traunch/plans are in scope.

**Labels:** `automation`, `v2`, `csr`, `exchange`, `jenkins`, `regression`, `qa-board-view`

**Component/Area:** `v2`, `csr`, `exchange`, `jenkins`

**Test coverage expectations**

- **Suite location / tags:** **Needs Validation** in `prime-test-automation` repo for exact feature file and TestNG suite name; KB cites `@regression`, `@dailyrun` on related exchange work.  
- **Pipeline:** Jenkins (and/or GitLab if dual) — **Needs Validation** for job name.  
- **Stability:** No new intermittent failures beyond agreed flake budget.

---

### S2605-02 — Story

**Summary:** `[V2][Member][Exchange] Filter accounts for Exchange — custom + annual criteria`

**Issue type:** Story  
**Assignee:** Venkatesh Mallela

**Description**

- **As a** QA automation engineer  
- **I want** the same **account filtering** concept as **S2605-01** applied to **member portal** exchange flows  
- **So that** member custom and annual exchange automation uses eligible accounts only

**Scope**

- **Portal:** Member only (not CSR).  
- **Stack:** V2.  
- **In:** Filtering for **Custom** and **Annual** member exchange; KB references member exchange stories/subtasks (**QA-530**, **QA-534**, **QA-535**, **QA-536**, `AnnualExchange.feature` mentioned in `jira-export.csv`).  
- **Out:** CSR exchange (S2605-01).

**Acceptance Criteria (GWT)**

```gherkin
Scenario: Member custom exchange eligible account
  Given member portal exchange automation with custom exchange test data
  When account resolution runs
  Then only eligible accounts proceed per SME rules

Scenario: Member annual exchange eligible account
  Given member portal annual exchange test data
  When account resolution runs
  Then only eligible accounts proceed per SME rules
```

**Definition of Done**

- [ ] Merged; member exchange subset green on Stage 1.  
- [ ] Tags documented (`@regression` / `@dailyrun` per program).  
- [ ] Report evidence attached.

**Dependencies / Risks**

- **Depends on:** S2605-01 patterns where logic can be shared.  
- **Risk:** Member vs CSR rule differences — SME sign-off.

**Labels:** `automation`, `v2`, `member`, `exchange`, `jenkins`, `regression`, `qa-board-view`

**Component/Area:** `v2`, `member`, `exchange`, `jenkins`

**Test coverage expectations**

- **Suite / paths:** **Needs Validation** — confirm feature paths in `prime-test-automation` (not stored in this KB repo).

---

### S2605-03 — Spike

**Summary:** `[V2][Spike] Ugift — CSR + member coverage, data, gaps, story breakdown`

**Issue type:** Spike  
**Assignee:** Venkatesh Mallela

**Description**

- **As a** QA lead  
- **I want** a short research pass on **Ugift** flows and automation  
- **So that** follow-on Stories **S2605-04** / **S2605-05** are scoped to real gaps

**Scope**

- **Portal:** CSR and member. **Stack:** V2.  
- **Ugift repo paths / feature names:** **Needs Validation** — no `ugift` string in `docs/jira-governance` search; inventory must be done in **prime-test-automation** (or owning repo) and pasted into findings.

**Research questions**

1. Where are Ugift scenarios (if any) in V2 automation?  
2. What data setup / secrets / env flags are required?  
3. What is already covered vs missing for smoke vs regression?  
4. Which flows are P1 for CSR vs member?

**Deliverables**

- Findings doc (Confluence or Story comment) with links to paths/commits.  
- Recommended story breakdown + list of test cases to automate with proposed tags (`@smoke` / `@regression` — **Needs Validation** against team convention).

**Definition of Done**

- [ ] Deliverables linked from Spike.  
- [ ] Explicit “no automation found” OR list of files/suites.

**Dependencies / Risks**

- **Risk:** No Ugift code in expected repo — escalate product owner.

**Labels:** `automation`, `v2`, `csr`, `member`, `ugift`, `spike`, `qa-board-view`

**Component/Area:** `v2`, `csr`, `member`, `ugift`

---

### S2605-04 — Story

**Summary:** `[V2][CSR][Ugift] Automate key Ugift CSR flows (post-spike)`

**Issue type:** Story  
**Assignee:** Venkatesh Mallela

**Description**

- **As a** regression owner  
- **I want** automated **Ugift CSR** flows identified in **S2605-03**  
- **So that** CSR Ugift paths are protected in nightly regression

**Scope:** V2, CSR only. **Out:** Member (S2605-05).

**Acceptance Criteria (GWT)**

```gherkin
Scenario: Spike-linked flow passes
  Given spike S2605-03 lists flow F as P1 CSR Ugift
  When automation for F runs on Stage 1
  Then F completes with agreed assertions

Scenario: Tagging
  Given merged tests for F
  Then scenarios carry agreed smoke/regression tags per spike table
```

**Definition of Done**

- [ ] Merged; stable run evidence.  
- [ ] Nightly or agreed suite updated — **Needs Validation** suite file name in automation repo.

**Dependencies / Risks**

- **Blocked by** S2605-03.

**Labels:** `automation`, `v2`, `csr`, `ugift`, `jenkins`, `regression`, `qa-board-view`

**Component/Area:** `v2`, `csr`, `ugift`, `jenkins`

---

### S2605-05 — Story

**Summary:** `[V2][Member][Ugift] Automate key Ugift member flows (post-spike)`

**Issue type:** Story  
**Assignee:** Venkatesh Mallela

**Description**

- **As a** regression owner  
- **I want** automated **Ugift member** flows from **S2605-03**  
- **So that** member Ugift is regression-protected

**Scope:** V2, member only.

**Acceptance Criteria (GWT)** — mirror **S2605-04** with member context.

**Definition of Done** — same pattern; **Depends on** S2605-03.

**Labels:** `automation`, `v2`, `member`, `ugift`, `jenkins`, `regression`, `qa-board-view`

**Component/Area:** `v2`, `member`, `ugift`, `jenkins`

---

## B) Sunil Godiyal

### S2605-06 — Spike

**Summary:** `[V2][CSR][Spike] CSR Maintenance Screen — regression gap analysis + matrix`

**Issue type:** Spike  
**Assignee:** Sunil Godiyal

**Description**

- **As a** QA automation engineer  
- **I want** an inventory of **CSR Maintenance** UI tabs vs automated coverage  
- **So that** missing tabs become sized Stories (**S2605-07** family)

**Scope**

- **Portal:** CSR only. **Stack:** V2.  
- Align to backlog intent **QA-S-V2-011** in `docs/jira-governance/backlog/stories.md`.

**Research questions**

1. Which automated tests exist today for CSR maintenance (feature files, suites)?  
2. Which Maintenance **tabs/sections** exist in the app (SME walkthrough)?  
3. Coverage matrix: tab → scenario → tag → suite/job.  
4. Do existing tests still pass / stable on Stage 1?  
5. Multi-plan: are analyzed items included in regression suites?

**Deliverables**

- Coverage matrix + list of missing tabs + **proposed Story titles** per gap row.  
- Links to evidence: e.g. KB `jira-export.csv` references **PersonalInformation.feature**, **Profile Maintenance**, `stage1-csr-acct-maintenance` report paths (use current internal report base URL).

**Acceptance Criteria (GWT)**

```gherkin
Scenario: Matrix complete
  Given CSR Maintenance is enumerated by tab
  When the spike is closed
  Then each tab is marked Covered Partial Covered or Gap with file references or N/A

Scenario: Stability sample
  Given existing maintenance automation exists
  When a sample regression run executes on Stage 1
  Then pass or fail is recorded with job or report link
```

**Definition of Done**

- [ ] Findings attached; PO/QA Lead acknowledgment comment optional.  
- [ ] List of Jira Story candidates for gaps (titles only).

**Dependencies / Risks**

- **Risk:** Tab naming mismatch app vs automation — use screenshots in doc.

**Labels:** `automation`, `v2`, `csr`, `spike`, `regression`, `qa-board-view`

**Component/Area:** `v2`, `csr`, `jenkins`

---

### S2605-07 — Story family (post-spike)

**Do not bulk-file before S2605-06.** For each **missing** tab row from the spike matrix, create one Story by cloning [SUNIL-TAB-STORY-TEMPLATE.md](SUNIL-TAB-STORY-TEMPLATE.md) and replacing `<TAB_NAME>`.

**Placeholder examples (Needs Validation — not confirmed gaps):**  
`CSR Maintenance – <TAB_NAME> regression coverage` × N rows from spike.

**KB-only feature names (for inventory, not proof of gap):** `PersonalInformation.feature`, `Profile Maintenance` (from `jira-export.csv`).

---

## C) Swapnil Patil

### S2605-08 — Story

**Summary:** `[V2] Stage 5 smoke suite — composition, tags, pass criteria`

**Issue type:** Story  
**Assignee:** Swapnil Patil

**Description**

- **As a** platform QA owner  
- **I want** a **defined Stage 5 smoke** suite for **V2**  
- **So that** CAT/Stage 5 validation is repeatable before deeper regression

**Scope**

- **Stack:** V2. **Portal:** KB backlog **QA-S-PLAT-002** says “V2 CSR + V3 IDP/UE smoke” for CAT/Stage 5 — **for this Story restrict documented scope to V2 portion** unless leadership extends (split V3 to **S2605-10**).

**Acceptance Criteria (GWT)**

```gherkin
Scenario: Suite composition documented
  Given Stage 5 smoke is defined
  When documented in Story or linked Confluence
  Then in-scope modules flows tags and minimum pass rules are listed

Scenario: Runnable
  Given Stage 5 credentials and config
  When the smoke command job is executed
  Then the suite completes with published report artifact
```

**Definition of Done**

- [ ] Document merged to KB or Confluence; link in Jira.  
- [ ] **Needs Validation:** exact Ant/Jenkins target name from automation repo.

**Dependencies / Risks**

- **Depends on** Stage 5 access (see `docs/jira-governance/backlog/gaps-analysis.md` — Stage 5 / CAT hostnames & credentials).

**Labels:** `automation`, `v2`, `pipeline`, `jenkins`, `smoke`, `qa-board-view`

**Component/Area:** `v2`, `pipeline`, `jenkins`

---

### S2605-09 — Story

**Summary:** `[V2] Integrate Stage 5 smoke into pipeline — schedule + on-demand + docs`

**Issue type:** Story  
**Assignee:** Swapnil Patil

**Description**

- **As a** release stakeholder  
- **I want** Stage 5 smoke **wired to CI** with **schedule + manual** trigger  
- **So that** results are visible without local-only runs

**Scope:** V2 pipeline (Jenkins per historical work in `jira-export.csv`; GitLab **Needs Validation**).

**Acceptance Criteria (GWT)**

```gherkin
Scenario: On demand
  Given a pipeline operator
  When they trigger the Stage 5 smoke job
  Then the job runs and publishes artifacts

Scenario: Scheduled
  Given the agreed cron or GitLab schedule
  When the schedule fires
  Then the job runs with retained artifacts

Scenario: Triage
  Given a failure
  When triage occurs
  Then assignee follows team failure template (link in Story comment)
```

**Definition of Done**

- [ ] Job link in Jira; at least one successful scheduled or manual run.  
- [ ] Docs updated (see **S2605-12**).

**Dependencies / Risks**

- **Depends on** S2605-08 suite definition.

**Labels:** `automation`, `v2`, `pipeline`, `jenkins`, `gitlab`, `smoke`, `qa-board-view`

**Component/Area:** `v2`, `pipeline`, `jenkins`, `gitlab`

---

### S2605-10 — Story

**Summary:** `[V3] Smoke suite — framework patterns, tags, minimal stable set`

**Issue type:** Story  
**Assignee:** Swapnil Patil

**Description**

- **As a** V3 regression owner  
- **I want** a **Maven/TestNG-aligned smoke** set in the V3 framework  
- **So that** fast signal precedes full nightly

**Scope:** V3 only (Maven; modules such as `unite/*` — **Needs Validation** exact module list in `prime-test-automation`).

**Evidence:** Tag examples `@regression`, `@dailyrun` in KB; `stage1-contributions.xml` and `stage1-universal-enroll-integration.xml` show suite composition patterns in this repo.

**Acceptance Criteria (GWT)**

```gherkin
Scenario: Smoke list exists
  Given V3 smoke scenarios are chosen
  When documented
  Then each scenario has module path tag and owner

Scenario: Local or CI run
  Given integration branch
  When smoke profile runs
  Then completion with report under target surefire reports path pattern (Needs Validation exact profile name)
```

**Definition of Done**

- [ ] Merged suite or tag filter; evidence run.  
- [ ] Linked to **S2605-11** for pipeline.

**Labels:** `automation`, `v3`, `pipeline`, `gitlab`, `smoke`, `idp`, `qa-board-view`

**Component/Area:** `v3`, `pipeline`, `gitlab`, `idp`

---

### S2605-11 — Story

**Summary:** `[V3] Integrate V3 smoke into pipeline + schedule (ENVP / CI gating — validate)`

**Issue type:** Story  
**Assignee:** Swapnil Patil

**Description**

- **As a** pipeline consumer  
- **I want** V3 smoke in **CI** with schedule  
- **So that** offshore and leads see consistent results

**Scope:** V3, `pipeline`, `gitlab` (GitLab referenced in `stories.md` QA-S-V3-003 and MEMCONTRIB drafts). **ENVP / gating:** `docs/jira-governance/upcoming-stories/Env-Pipeline_project/` (QA-600, ACS-5289, `stage1-ue-integration-test`) — **Needs Validation** whether smoke uses same gate mechanism.

**Acceptance Criteria (GWT)**

```gherkin
Scenario: Pipeline publishes artifacts
  Given V3 smoke job exists
  When job completes
  Then TestNG or Cucumber report link is available

Scenario: Schedule
  Given agreed schedule
  When triggered
  Then job appears in history with stable naming
```

**Definition of Done**

- [ ] Job documented; **Needs Validation** for “CI switch” wording confirmed with DevOps.

**Labels:** `automation`, `v3`, `pipeline`, `gitlab`, `github-actions`, `smoke`, `qa-board-view`

**Component/Area:** `v3`, `pipeline`, `gitlab`, `github-actions`

---

### S2605-12 — Story

**Summary:** `[Docs] Confluence — V2/V3 smoke, suites, schedules, how to run, ownership`

**Issue type:** Story  
**Assignee:** Swapnil Patil

**Description**

- **As a** engineer joining the program  
- **I want** one **Confluence** page (or section) describing new suites and pipelines  
- **So that** execution and ownership are obvious

**Scope:** Documentation only; link **S2605-08**–**11** outcomes.

**Evidence:** Confluence base references in `jira-export.csv` (`pageId=315559619`).

**Acceptance Criteria (GWT)**

```gherkin
Scenario: Page exists
  Given work from S2605-08 through 11
  When published
  Then page lists suite job schedule tags how to run owner escalation

Scenario: Linked from Jira
  Given Stories 08 to 11 exist
  When this Story closes
  Then each linked Story has URL in comment or field
```

**Definition of Done**

- [ ] Confluence URL in Jira; peer review by QA Lead.

**Labels:** `automation`, `v2`, `v3`, `pipeline`, `documentation`, `qa-board-view`

**Component/Area:** `v2`, `v3`, `pipeline`

---

## D) Dinesh Kumar

### S2605-13 — Story

**Summary:** `[V3][Member] Withdrawal flow automation (post-IDP)`

**Issue type:** Story  
**Assignee:** Dinesh Kumar

**Description**

- **As a** member regression owner  
- **I want** **withdrawal** automated in **V3 member** path post-IDP  
- **So that** regulated flows are covered in nightly

**Scope:** V3, **member** portal. Align to **QA-S-V3-005** in `docs/jira-governance/backlog/stories.md`. KB export references **`stage1-withdrawals`** as a module name in regression commentary.

**Acceptance Criteria (GWT)** — use withdrawal happy/decline scenarios from **QA-S-V3-005** in `stories.md` (copy Gherkin from backlog).

**Definition of Done**

- [ ] Merged; in nightly or agreed `stage1-*` suite — **Needs Validation** exact XML name.  
- [ ] Report link.

**Labels:** `automation`, `v3`, `member`, `withdrawal`, `idp`, `gitlab`, `regression`, `qa-board-view`

**Component/Area:** `v3`, `member`, `withdrawal`, `idp`, `pipeline`, `gitlab`

---

### S2605-14 — Story

**Summary:** `[V3][Member] Remaining transactions — transfers, exchanges (confirm gaps first)`

**Issue type:** Story  
**Assignee:** Dinesh Kumar

**Description**

- **As a** regression owner  
- **I want** **transfer** and **exchange** (and other key member transactions) covered in V3 where missing  
- **So that** parity with business risk

**Scope:** V3 member. **QA-S-V3-006**, **QA-S-V3-007** in `stories.md` provide AC templates.

**Acceptance Criteria (GWT)**

```gherkin
Scenario: Gap confirmation
  Given prime-test-automation V3 member transaction inventory
  When compared to SME priority list
  Then this Story lists only flows confirmed missing

Scenario: Implemented flow passes
  Given a missing flow F is implemented
  When nightly runs
  Then F passes on Stage 1 with assertions
```

**Definition of Done**

- [ ] Comment lists **before/after** coverage; SME sign-off.

**Dependencies / Risks**

- **Needs Validation:** must diff against existing tests in repo before coding.

**Labels:** `automation`, `v3`, `member`, `exchange`, `withdrawal`, `idp`, `gitlab`, `qa-board-view`

**Component/Area:** `v3`, `member`, `exchange`, `idp`, `pipeline`, `gitlab`

---

### S2605-15 — Story

**Summary:** `[V3] Port IDP login coverage from Universal Enrollment module into Unite V3`

**Issue type:** Story  
**Assignee:** Dinesh Kumar

**Description**

- **As a** V3 owner  
- **I want** **IDP login** cases that live with **Universal Enrollment** today centralized for **Unite V3**  
- **So that** tagging and pipeline integration match V3 conventions

**Scope:** V3. **Evidence:** `jira-export.csv` references **IDPLogin.feature**, **UniversalEnrollment** suites, labels `IDP_LoginAutomation`; `UEPIPE-02` references `unite/unite-universal-enrollment` and `UniversalEnrollmentPositive.feature`. **Target module path for “Unite V3”:** **Needs Validation** in automation repo.

**Acceptance Criteria (GWT)**

```gherkin
Scenario: Parity
  Given a baseline list of IDP scenarios in Universal Enrollment
  When port completes
  Then equivalent scenarios exist under Unite V3 module with same business intent

Scenario: Pipeline
  Given V3 nightly job
  When it runs
  Then IDP scenarios execute from the new location without duplicate maintenance burden (deprecate old entry per team agreement)
```

**Definition of Done**

- [ ] MR merged; deprecation note for old location if applicable.  
- [ ] Nightly green or only linked defects.

**Labels:** `automation`, `v3`, `idp`, `enrollment`, `gitlab`, `regression`, `qa-board-view`

**Component/Area:** `v3`, `idp`, `enrollment`, `pipeline`, `gitlab`

---

### S2605-16 — Story

**Summary:** `[V3][Pipeline] Environment pipeline project — align automation gates`

**Issue type:** Story  
**Assignee:** Dinesh Kumar

**Description**

- **As a** ENVP stakeholder  
- **I want** pipeline project updates so **environment pipeline** needs are met  
- **So that** promotion gates run the right suites

**Scope:** V3 / platform. **Evidence:** `docs/jira-governance/upcoming-stories/Env-Pipeline_project/README.md` (QA-600, ACS-5289, `stage1-ue-integration-test`). `jira-export.csv` triage text references **`scheduled_regression_job`** (confirm current name in live pipeline YAML — **Needs Validation**).

**Acceptance Criteria (GWT)**

```gherkin
Scenario: Documented change
  Given a pipeline change is required
  When merged
  Then Story comment links to MR and describes trigger artifacts

Scenario: Validation run
  Given post-merge pipeline
  When executed
  Then job completes with visible report
```

**Definition of Done**

- [ ] DevOps/QA sign-off comment.

**Labels:** `automation`, `v3`, `pipeline`, `gitlab`, `qa-board-view`

**Component/Area:** `v3`, `pipeline`, `gitlab`

---

### S2605-17 — Story

**Summary:** `[V3][NTP] Baseline automation suite + nightly regression entry`

**Issue type:** Story  
**Assignee:** Dinesh Kumar

**Description**

- **As a** QA owner  
- **I want** an **NTP (NT Management Platform)** automation baseline in V3  
- **So that** nightly regression includes NTP

**Scope:** V3. **Evidence in KB:** **None** for NTP paths — **Needs Validation** entire technical approach (module name, URLs, feature ownership).

**Acceptance Criteria (GWT)**

```gherkin
Scenario: Baseline exists
  Given NTP scope agreed with SME
  When baseline tests are added
  Then at least one happy path per agreed surface runs on Stage 1

Scenario: Nightly
  Given nightly regression configuration
  When nightly runs
  Then NTP suite is invoked and reported
```

**Definition of Done**

- [ ] SME-approved scope comment; job link.

**Labels:** `automation`, `v3`, `gitlab`, `regression`, `qa-board-view`

**Component/Area:** `v3`, `pipeline`, `gitlab`

---

## E) Priti Choudhary

### S2605-18 — Story

**Summary:** `[Perf] Forgot Username + Forgot Password flows in performance framework`

**Issue type:** Story  
**Assignee:** Priti Choudhary

**Description**

- **As a** performance engineer  
- **I want** **Forgot Username** and **Forgot Password** in the perf framework (JMeter per backlog **QA-S-PERF-002/003** family in `stories.md`)  
- **So that** auth-adjacent load is measured

**Scope:** `perf`, `jenkins` (QA-S-PERF-001 references Jenkins schedule). **Needs Validation:** exact `.jmx` repo path in performance repo.

**Acceptance Criteria (GWT)**

```gherkin
Scenario: Scripts run
  Given perf environment credentials
  When forgot username and forgot password scripts execute
  Then both complete with success criteria documented in Story

Scenario: Data and auth boundaries
  Given test users are defined
  When runs execute
  Then no PII leakage in logs and rate limits respected
```

**Definition of Done**

- [ ] Jenkins (or CI) job link; baseline metrics attached.

**Labels:** `perf`, `jenkins`, `member`, `idp`, `qa-board-view`

**Component/Area:** `perf`, `jenkins`, `member`, `idp`

---

### S2605-19 — Story

**Summary:** `[Perf] Nightly regression perf package (prod-like) — IDP + forgot + change password`

**Issue type:** Story  
**Assignee:** Priti Choudhary

**Description**

- **As a** performance owner  
- **I want** a **nightly perf package** with **IDP login**, **forgot username**, **forgot password**, **change password**  
- **So that** regressions in auth performance are visible daily

**Evidence:** **QA-S-PERF-001**, **QA-S-PERF-004** themes in `stories.md`; **QA-461** “Universal financial withdrawals Perf … Jenkins … Nightly” pattern in `jira-export.csv` as precedent for Jenkins+nightly packaging.

**Acceptance Criteria (GWT)**

```gherkin
Scenario: Nightly runs
  Given Jenkins schedule configured
  When nightly executes
  Then all four flows run and results stored

Scenario: Thresholds
  Given baseline metrics
  When results exceed thresholds
  Then alert or ticket rules per team process are followed (Needs Validation)
```

**Definition of Done**

- [ ] Schedule screenshot or job config link; threshold doc.

**Labels:** `perf`, `jenkins`, `idp`, `member`, `qa-board-view`

**Component/Area:** `perf`, `jenkins`, `idp`, `member`

---

### S2605-20 — Story

**Summary:** `[Perf] Change password (member profile) — dynamic header handler + reliable validation`

**Issue type:** Story  
**Assignee:** Priti Choudhary

**Description**

- **As a** performance engineer  
- **I want** a **dynamic header handler** for change-password flows blocked by rotating header keys  
- **So that** JMeter (or agreed tool) can run reliably

**Evidence:** `jira-export.csv` includes narrative on **change password from profile security settings** (authenticated user, MFA context) — use as business context; **script location Needs Validation**.

**Acceptance Criteria (GWT)**

```gherkin
Scenario: Handler works
  Given dynamic header keys rotate per environment rules
  When the handler script runs
  Then requests succeed for change password flow across N consecutive runs

Scenario: Validation
  Given successful run
  When results reviewed
  Then assertions match agreed HTTP codes and response time limits
```

**Definition of Done**

- [ ] Script in repo; peer review; Jenkins evidence.

**Labels:** `perf`, `jenkins`, `member`, `idp`, `qa-board-view`

**Component/Area:** `perf`, `jenkins`, `member`, `idp`

---

### S2605-21 — Story

**Summary:** `[Perf] Enrollment flow performance — UI and/or API (approach TBD from repo)`

**Issue type:** Story  
**Assignee:** Priti Choudhary

**Description**

- **As a** performance stakeholder  
- **I want** **enrollment** covered by perf tests  
- **So that** load-sensitive enrollment paths are baselined

**Scope:** **Needs Validation** — choose UI vs API vs both after reviewing existing perf assets in performance repo (not in KB file listing).

**Acceptance Criteria (GWT)**

```gherkin
Scenario: Approach chosen
  Given repo inventory
  When Story is refined
  Then description states UI API or both with rationale

Scenario: Baseline run
  Given chosen approach
  When executed in perf env
  Then results attached with thresholds
```

**Definition of Done**

- [ ] Inventory note in Jira; first baseline run linked.

**Labels:** `perf`, `jenkins`, `enrollment`, `v3`, `qa-board-view`

**Component/Area:** `perf`, `jenkins`, `enrollment`

---

*End of SPRINT-26.05 Jira Story Markdown.*
