# Backlog — Stories (Jira-ready)

**Legend:** `QA-S-*` = proposed Story key (replace with your project). Every Story links to an Epic from [epics.md](epics.md).  
**Note:** No `jira-export.csv` was available; deduplicate after import.

---

## Automation V3 — Stability & pipeline (Dinesh)

### QA-S-V3-001 — Stabilize IDP login — eliminate flaky failures in nightly V3 regression

**Epic:** QA-E-V3-STAB  
**Primary owner:** Dinesh

**Description**  
Identify root causes of intermittent IDP login failures in the Prime V3 / Unite IDP suite on Stage 1. Apply fixes (waits, data, environment assumptions, selectors, session handling) so the IDP login path is reliable in scheduled runs.

**Business context**  
IDP is the gate for most V3 scenarios; flakes hide real defects and burn offshore time. Stabilizing login restores trust in the nightly signal.

**Acceptance criteria**

```gherkin
Scenario: IDP login suite consecutive stability
  Given the IDP login regression suite is executed on Stage 1
  When the suite is run 5 consecutive times on the integration branch with no code changes
  Then each run completes with the same set of scenarios passed (no intermittent failures)

Scenario: Flake documentation
  Given a previously flaky scenario was fixed
  When the Story is closed
  Then a comment documents root cause category (data, timing, env, application defect) and the fix approach
```

**Subtasks**

- [Dev] Reproduce flake locally or from CI artifacts; capture HTML/screenshot/logs per failure mode.  
- [Dev] Implement code/test changes (framework or scenario level); open MR.  
- [Dev] Peer review on MR.  
- [QA] Run 5x consecutive validation on Stage 1; attach or link job URLs.  
- [QA] Update suite XML / tags if scenarios split for isolation.  
- [Either] Document known application defects separately if fix is not in automation scope.

**Definition of Done**

- [ ] AC satisfied; evidence linked in Jira.  
- [ ] Merged to integration branch; pipeline green.  
- [ ] No Sev1/Sev2 open on scope.  
- [ ] Nightly job includes updated suite.  
- [ ] Short comment on root-cause category for each major flake addressed.

---

### QA-S-V3-002 — Stabilize Universal Enrollment scenarios in V3 nightly

**Epic:** QA-E-V3-STAB  
**Primary owner:** Dinesh

**Description**  
Reduce failures and flakes in Universal Enrollment flows (Stage 1) by fixing test data, steps, and synchronization. Align scenarios with current UE UI and API behavior.

**Business context**  
UE is core V3 delivery; unstable suites delay release confidence and mask regressions.

**Acceptance criteria**

```gherkin
Scenario: UE regression green
  Given the Universal Enrollment suite configured for Stage 1
  When executed as part of the standard nightly V3 job
  Then all in-scope UE scenarios pass unless blocked by a linked open defect

Scenario: Data and environment assumptions documented
  Given the suite uses shared test data
  When a failure occurs due to data collision
  Then resolution is either isolated data strategy or documented constraint in Story comment
```

**Subtasks**

- [Dev] Triage failing UE methods; categorize (app vs test).  
- [Dev] Fix scenarios/POM/data; MR + review.  
- [QA] Full UE suite run on Stage 1; link report.  
- [QA] Verify CSR/UE handoffs if applicable.  
- [Either] Link blocking bugs with labels `blocks-automation`.

**Definition of Done**

- [ ] Nightly UE portion green or only known-blocked items with Jira links.  
- [ ] Code merged; CI green.  
- [ ] Documentation or comment for data ownership.

---

### QA-S-V3-003 — Attach V3 regression to approved CI/CD pipeline

**Epic:** QA-E-V3-PLAT  
**Primary owner:** Dinesh

**Description**  
Wire the agreed V3 regression entry point (Maven/TestNG) into the approved pipeline (GitLab or GitHub Actions per program decision), with artifacts (HTML report) retained.

**Business context**  
Pipeline execution enables scheduling, auditability, and offshore self-service without local-only runs.

**Acceptance criteria**

```gherkin
Scenario: Pipeline executes V3 suite
  Given the pipeline job is triggered manually or on schedule
  When the job runs on the integration branch
  Then the V3 regression stage completes and publishes TestNG/HTML artifacts

Scenario: Failure visibility
  Given a test failure occurs in the pipeline
  When the job completes
  Then the failure is visible in the job log and report link is attached to the build
```

**Subtasks**

- [Dev] Add/update pipeline YAML or Jenkinsfile per platform standard.  
- [Dev] Configure secrets/credentials via approved store.  
- [Dev] Peer review with platform/DevOps contact.  
- [QA] Smoke validation run from pipeline (not local only).  
- [Either] Update Confluence/CICD doc with job name and link.

**Definition of Done**

- [ ] Pipeline job name documented; link in Story.  
- [ ] At least one successful scheduled or manual run recorded.  
- [ ] Reports retained per retention policy.

---

### QA-S-V3-004 — V3 contribution flow automation (post-IDP)

**Epic:** QA-E-V3-TXN  
**Primary owner:** Dinesh

**Description**  
Automate member or CSR contribution flows in V3 after IDP authentication, covering screens and validations that differ from V2 legacy login paths.

**Business context**  
Contributions are high-volume; V3 path must be regression-protected before legacy retirement.

**Acceptance criteria**

```gherkin
Scenario: Happy path contribution
  Given a valid IDP-authenticated user for an in-scope plan
  When the user completes a contribution per approved test data
  Then the transaction completes and backend/DB assertions pass per SME rules

Scenario: Negative validation
  Given invalid contribution input
  When the user submits
  Then the UI shows expected validation and no partial commit occurs
```

**Subtasks**

- [Dev] Confirm plan list with SME; document in Story.  
- [Dev] Implement scenarios + step defs/POM updates.  
- [Dev] Peer review.  
- [QA] Execute on Stage 1; attach report.  
- [QA] Add to nightly suite XML if not already included.

**Definition of Done**

- [ ] Scenarios in nightly or scheduled suite.  
- [ ] Merged; green CI.  
- [ ] SME sign-off comment or linked approval.

---

### QA-S-V3-005 — V3 withdrawal flow automation (post-IDP)

**Epic:** QA-E-V3-TXN  
**Primary owner:** Dinesh

**Description**  
Automate withdrawal/distribution flow in V3 post-IDP for agreed plan(s), including CSR or member path per SME.

**Business context**  
Withdrawals are regulated and customer-impacting; automation reduces manual regression cost.

**Acceptance criteria**

```gherkin
Scenario: Withdrawal happy path
  Given prerequisites (account state, balances) per test data sheet
  When withdrawal is submitted through the automated flow
  Then expected confirmation and ledger/DB state match assertions

Scenario: Decline / hold path (if in scope)
  Given a condition that blocks withdrawal
  When the user attempts withdrawal
  Then the application displays the expected block message
```

**Subtasks**

- [Dev] Align test data with SME; secure storage.  
- [Dev] Implement automation; MR + review.  
- [QA] Stage 1 validation + report.  
- [QA] Register in suite XML.

**Definition of Done**

- [ ] In nightly or agreed schedule.  
- [ ] Merged; no open Sev1/2.  
- [ ] Linked test data reference (path redacted in Jira if secret).

---

### QA-S-V3-006 — V3 transfer flow automation (post-IDP)

**Epic:** QA-E-V3-TXN  
**Primary owner:** Dinesh

**Description**  
Automate transfer scenarios in V3 where UI or APIs differ from V2; include CSR/member variants per SME.

**Business context**  
Transfers span plans and compliance rules; gaps allow regressions at cutover.

**Acceptance criteria**

```gherkin
Scenario: Transfer completes
  Given source and destination accounts per test data
  When transfer is executed via automated flow
  Then balances and transaction records reflect success criteria

Scenario: Invalid transfer rejected
  Given disallowed transfer configuration
  When attempted
  Then user sees expected error and system state unchanged
```

**Subtasks**

- [Dev] SME workshop for rules; capture in comment.  
- [Dev] Implement + review.  
- [QA] Validate Stage 1; link report.  
- [QA] Suite integration.

**Definition of Done**

- [ ] Suite + CI as per team standard.  
- [ ] Documentation updated if new URLs or plans added.

---

### QA-S-V3-007 — V3 exchange flow automation (post-IDP)

**Epic:** QA-E-V3-TXN  
**Primary owner:** Dinesh

**Description**  
Automate exchange flows in V3 post-IDP (member/CSR as applicable) for in-scope plans.

**Business context**  
Exchanges interact with investment lineup; high regression value.

**Acceptance criteria**

```gherkin
Scenario: Exchange success
  Given eligible holdings per test data
  When exchange is performed
  Then fund allocations match expected post-conditions

Scenario: Plan-specific restriction
  Given a plan that blocks exchange type X
  When attempted
  Then UI/API returns expected restriction
```

**Subtasks**

- [Dev] Implement; MR + review.  
- [QA] Multi-plan sample if required by SME.  
- [QA] Nightly inclusion.

**Definition of Done**

- [ ] Merged; green.  
- [ ] Report linked; SME acknowledged plan list.

---

## Automation V2 — Transactions (Venkatesh)

### QA-S-V2-001 — CSR exchange scenarios — nightly stability

**Epic:** QA-E-V2-TXN  
**Primary owner:** Venkatesh

**Description**  
Ensure CSR-led exchange scenarios (custom/standard per suite) run reliably in V2 nightly across agreed plans; fix flakes and data issues.

**Business context**  
Exchange is a core transaction; regressions impact operations and members.

**Acceptance criteria**

```gherkin
Scenario: Nightly green
  Given the V2 nightly suite including CSR exchange
  When executed on Stage 1
  Then exchange scenarios pass for all in-scope plans in the suite

Scenario: Regression artifact
  Given a failure occurs
  When investigated
  Then failure is classified and linked bug created if application issue
```

**Subtasks**

- [Dev] Triage failures; fix tests/framework.  
- [Dev] MR + review.  
- [QA] Run full nightly slice; link report.  
- [QA] Update plan list in comment if changed.

**Definition of Done**

- [ ] Nightly stable 3 consecutive nights or documented blocker.  
- [ ] Merged; CI green.

---

### QA-S-V2-002 — CSR fund allocation scenarios — coverage and stability

**Epic:** QA-E-V2-TXN  
**Primary owner:** Venkatesh

**Description**  
Expand or stabilize CSR fund allocation and future allocation scenarios for V2; align with SME rules for DCA-eligible and non-DCA plans.

**Business context**  
Allocations drive compliance and statements; automation prevents silent UI regressions.

**Acceptance criteria**

```gherkin
Scenario: Allocation change persists
  Given CSR updates allocation per test data
  When saved
  Then persisted allocation matches expected percentages or units per assertion layer

Scenario: Negative allocation input
  Given invalid allocation totals
  When CSR saves
  Then validation prevents commit with expected messaging
```

**Subtasks**

- [Dev] Implement/extend scenarios.  
- [Dev] Review.  
- [QA] Stage 1 validation.  
- [QA] Nightly XML update.

**Definition of Done**

- [ ] In nightly.  
- [ ] Documentation for new test data.

---

### QA-S-V2-003 — Member transaction coverage expansion (multi-plan)

**Epic:** QA-E-V2-TXN  
**Primary owner:** Venkatesh

**Description**  
Add member-side transaction scenarios (where member actions allowed) across additional plans; positive and negative paths per SME.

**Business context**  
CSR-only coverage misses member-facing defects; expands confidence for self-service.

**Acceptance criteria**

```gherkin
Scenario: Member flow on new plan
  Given plan P is added to scope
  When member transaction scenario runs
  Then scenario passes on Stage 1 with approved data

Scenario: Negative member path
  Given disallowed member action for plan P
  When attempted
  Then expected error displayed
```

**Subtasks**

- [Dev] List plans with SME sign-off.  
- [Dev] Implement scenarios.  
- [QA] Validate; add to suite.

**Definition of Done**

- [ ] Merged; nightly updated.  
- [ ] Plan list in Story comment.

---

## Automation V2 — Profile & maintenance (Sunil)

### QA-S-V2-010 — Member profile update scenarios (email, phone, and related fields)

**Epic:** QA-E-V2-PROF  
**Primary owner:** Sunil

**Description**  
Automate legacy member profile updates (e.g., email, phone) where CSR profile already exists in nightly — close the member-side gap.

**Business context**  
Member self-service updates are high touch; gaps allow undetected regressions.

**Acceptance criteria**

```gherkin
Scenario: Member updates contact
  Given a member session with valid credentials
  When email or phone is updated per test data
  Then profile reflects new values and DB/assertions pass

Scenario: Invalid contact format
  Given invalid email or phone
  When submitted
  Then validation errors display and no DB change occurs
```

**Subtasks**

- [Dev] Implement member profile flows.  
- [Dev] Review.  
- [QA] Stage 1 run; link report.  
- [QA] Add to nightly.

**Definition of Done**

- [ ] Nightly includes scenarios.  
- [ ] Merged; green.

---

### QA-S-V2-011 — CSR Maintenance tabs — missing coverage

**Epic:** QA-E-V2-PROF  
**Primary owner:** Sunil

**Description**  
Identify CSR Maintenance tabs without automation; add scenarios for highest-risk tabs first per SME ranking.

**Business context**  
Operations rely on CSR maintenance; untested tabs risk production incidents.

**Acceptance criteria**

```gherkin
Scenario: Tab coverage recorded
  Given a Maintenance tab gap analysis is completed
  When documented in Story comment or linked doc
  Then each P1 tab has at least one automated scenario or explicit waiver

Scenario: P1 tab automated
  Given tab T is priority 1
  When automation runs on Stage 1
  Then scenario passes with assertions defined with SME
```

**Subtasks**

- [Dev] Gap analysis with SME; priority list.  
- [Dev] Implement P1 tabs.  
- [QA] Validate; iterate P2 as capacity allows.

**Definition of Done**

- [ ] P1 tabs covered or waived with PO approval.  
- [ ] Merged; report linked.

---

### QA-S-V2-012 — Negative scenarios across plans (V2 profile / maintenance)

**Epic:** QA-E-V2-PROF  
**Primary owner:** Sunil

**Description**  
Add negative and edge-case scenarios for profile/maintenance flows across multiple plans to expose validation and permission differences.

**Business context**  
Happy-path-only suites miss authorization and validation bugs.

**Acceptance criteria**

```gherkin
Scenario: Cross-plan negative matrix
  Given at least N plans in scope (N agreed with SME)
  When negative scenarios execute
  Then each plan shows expected error or restriction without server error

Scenario: No silent failures
  Given a scenario expects an error
  When executed
  Then the test asserts explicit message or code; not only absence of success
```

**Subtasks**

- [Dev] Build data matrix; implement.  
- [Dev] Review.  
- [QA] Execute matrix; attach summary table.

**Definition of Done**

- [ ] Matrix attached; merged.  
- [ ] Nightly runtime acceptable (no excessive duplication).

---

## Performance (Preeti)

### QA-S-PERF-001 — IDP login performance — Jenkins integration and schedule

**Epic:** QA-E-PERF-FLOW  
**Primary owner:** Preeti

**Description**  
Integrate IDP login end-to-end performance script into Jenkins (existing perf job family); enable scheduled execution and artifact retention.

**Business context**  
Login performance regressions impact all users; scheduling gives trend visibility.

**Acceptance criteria**

```gherkin
Scenario: Job runs in Jenkins
  Given the IDP login perf JMeter (or agreed tool) script
  When the Jenkins job runs
  Then the job completes with published report (JTL/HTML) linked

Scenario: Schedule active
  Given scheduling is enabled
  When the calendar trigger fires
  Then at least one successful scheduled run is recorded in the Story comment
```

**Subtasks**

- [Dev] Pipeline/job config with Nick/DevOps per runbook.  
- [Dev] Parameterize env and credentials.  
- [QA] Validate run; document schedule.  
- [Either] Link dashboard if exists.

**Definition of Done**

- [ ] Job link in Jira.  
- [ ] Schedule documented.  
- [ ] No secrets in repo.

---

### QA-S-PERF-002 — Forgot username performance flow in CI

**Epic:** QA-E-PERF-FLOW  
**Primary owner:** Preeti

**Description**  
Implement and wire forgot-username performance flow to CI with stable data and correlation rules.

**Business context**  
Auth-adjacent flows are sensitive to latency and caching issues.

**Acceptance criteria**

```gherkin
Scenario: Script runs in CI
  Given forgot-username perf script
  When executed in Jenkins job
  Then report generated and thresholds documented (even if baseline TBD)

Scenario: MFA dependency handled
  Given MFA blocks automation
  When blocked
  Then Story documents workaround or dependency ticket link
```

**Subtasks**

- [Dev] Script + parameterization.  
- [Dev] Integrate job.  
- [QA] Validate with Abhitosh/Nick as needed.

**Definition of Done**

- [ ] Job link; merged config.  
- [ ] Blockers documented if any.

---

### QA-S-PERF-003 — Forgot password performance flow in CI

**Epic:** QA-E-PERF-FLOW  
**Primary owner:** Preeti

**Description**  
Same as QA-S-PERF-002 for forgot-password path.

**Acceptance criteria**

```gherkin
Scenario: CI execution
  Given forgot-password perf script
  When Jenkins job runs
  Then report published and linked

Scenario: Stable environment
  Given Stage env instability
  When three consecutive runs vary beyond threshold
  Then infra ticket opened or note in Story
```

**Subtasks**

- [Dev] Script + job.  
- [QA] Validate; tune ramp-up.

**Definition of Done**

- [ ] Linked job + sample report.

---

### QA-S-PERF-004 — Profile password change performance flow

**Epic:** QA-E-PERF-FLOW  
**Primary owner:** Preeti

**Description**  
Automate member profile password change as performance scenario; integrate to CI when auth allows.

**Acceptance criteria**

```gherkin
Scenario: Flow executable
  Given password change path is accessible in Stage
  When perf script runs
  Then results captured and linked

Scenario: Blocked by MFA
  Given MFA dependency
  When unresolved
  Then explicit blocker linked; Story not closed as done without waiver
```

**Subtasks**

- [Dev] Implement script.  
- [QA] Coordinate MFA resolution.  
- [Either] Waiver from PO if out of scope.

**Definition of Done**

- [ ] Clear status: done OR blocked with waiver.

---

### QA-S-PERF-005 — qTest linkage for performance suites

**Epic:** QA-E-PERF-OPS  
**Primary owner:** Preeti

**Description**  
Map performance jobs/scenarios to qTest cycles and test cases for audit and traceability.

**Business context**  
Leadership and quality audits expect test evidence in qTest.

**Acceptance criteria**

```gherkin
Scenario: Traceability exists
  Given each active perf job
  When reviewed in qTest
  Then corresponding test case or cycle exists and is linked from Confluence or Story

Scenario: Ownership documented
  Given a new perf scenario is added
  When merged
  Then qTest artifact updated in same sprint
```

**Subtasks**

- [QA] qTest structure design with tooling owner.  
- [QA] Create/update cycles.  
- [Either] Document mapping table.

**Definition of Done**

- [ ] Link to qTest folder/cycle in Story.  
- [ ] Table maintained in team doc.

---

### QA-S-PERF-006 — Performance documentation pack (setup, process, test data)

**Epic:** QA-E-PERF-OPS  
**Primary owner:** Preeti

**Description**  
Publish Confluence/repo doc: how to run perf locally and in CI, data rules, secrets handling, troubleshooting.

**Business context**  
Offshore and partners need repeatable instructions.

**Acceptance criteria**

```gherkin
Scenario: Doc published
  Given the documentation page exists
  When a new engineer follows it
  Then they can run one standard script without asking for undocumented secrets

Scenario: Reviewed
  Given doc is draft
  When Tech Lead reviews
  Then approval comment on Story
```

**Subtasks**

- [Either] Author doc.  
- [Dev] Technical review.  
- [QA] Dry-run by second person; fix gaps.

**Definition of Done**

- [ ] Confluence URL in Jira.  
- [ ] Reviewer named.

---

### QA-S-PERF-007 — Performance regression suite baseline

**Epic:** QA-E-PERF-OPS  
**Primary owner:** Preeti

**Description**  
Define baseline metrics for agreed scenarios; store baseline file or dashboard snapshot; fail job on regression beyond threshold (when policy allows).

**Business context**  
Without baselines, performance tests are noise.

**Acceptance criteria**

```gherkin
Scenario: Baseline recorded
  Given stable window (e.g., 5 green runs)
  When baseline captured
  Then stored location documented in Story

Scenario: Regression rule (if enabled)
  Given a subsequent run exceeds threshold
  When job runs
  Then job fails or warns per policy
```

**Subtasks**

- [QA] Collect baseline runs.  
- [Dev] Implement threshold gate if required.  
- [Either] PO approves thresholds.

**Definition of Done**

- [ ] Baseline artifact path.  
- [ ] Policy documented.

---

### QA-S-PERF-008 — Performance process framework (roles, SLAs, intake)

**Epic:** QA-E-PERF-OPS  
**Primary owner:** Preeti

**Description**  
Lightweight operating model: who requests perf runs, lead time, how results are shared, when to block release.

**Business context**  
Prevents ad-hoc runs and unclear accountability.

**Acceptance criteria**

```gherkin
Scenario: RACI published
  Given one-page process doc
  When published
  Then roles for requester, executor, approver are explicit

Scenario: Intake path
  Given a new perf need
  When submitted
  Then it uses Jira template linked from doc
```

**Subtasks**

- [Either] Draft with lead.  
- [PO] Approve.  
- [Either] Link from governance KB.

**Definition of Done**

- [ ] Published link.  
- [ ] PO sign-off comment.

---

## Platform / Infrastructure (Lead)

### QA-S-PLAT-001 — API automation pipeline — harden GitHub Actions / GitLab job

**Epic:** QA-E-PLAT-INF  
**Primary owner:** Delivery lead

**Description**  
Stabilize API test pipeline (workflow, secrets, artifacts); align with Dong/platform on long-term GitLab vs GitHub direction.

**Business context**  
API tests protect services without full UI; pipeline is prerequisite for shift-left.

**Acceptance criteria**

```gherkin
Scenario: Pipeline green
  Given integration branch
  When API pipeline runs
  Then tests execute and report published

Scenario: Documented
  Given a new contributor
  When reading linked doc
  Then they can trigger or interpret job
```

**Subtasks**

- [Dev] Workflow YAML + secrets.  
- [Dev] Review with DevOps.  
- [QA] Smoke API run from pipeline only.

**Definition of Done**

- [ ] Job URL in Story.  
- [ ] Doc updated.

---

### QA-S-PLAT-002 — Stage 5 / CAT smoke suite in pipeline

**Epic:** QA-E-PLAT-INF  
**Primary owner:** Delivery lead

**Description**  
Run V2 CSR + V3 IDP/UE smoke against CAT/Stage 5 from pipeline with pass/fail gate for agreed use cases.

**Business context**  
Partner env validation before broader regression.

**Acceptance criteria**

```gherkin
Scenario: Smoke executes
  Given CAT/Stage5 credentials and DB
  When pipeline job runs
  Then smoke suite completes with report

Scenario: Scope documented
  Given smoke is subset
  When documented
  Then in-scope tests listed in comment or doc
```

**Subtasks**

- [Dev] Job + env config.  
- [QA] Validate smoke set with team.  
- [Either] Infra ticket for access if blocked.

**Definition of Done**

- [ ] Runnable job; link saved.  
- [ ] Blockers documented.

---

### QA-S-PLAT-003 — Environment-based smoke pipeline matrix

**Epic:** QA-E-PLAT-INF  
**Primary owner:** Delivery lead

**Description**  
Define which smoke runs on which Stage (1/2/4/5); matrix in Confluence; optional parameterized pipeline.

**Business context**  
Reduces wrong-env failures and confusion for offshore.

**Acceptance criteria**

```gherkin
Scenario: Matrix published
  Given matrix table env × suite
  When published
  Then each cell has owner job or explicit N/A

Scenario: Drift controlled
  Given a new env
  When added
  Then matrix updated same sprint
```

**Subtasks**

- [Either] Author matrix.  
- [Dev] Parameterize jobs if needed.  
- [PO] Approve scope.

**Definition of Done**

- [ ] Confluence link.

---

### QA-S-PLAT-004 — API ↔ UI traceability matrix

**Epic:** QA-E-PLAT-INF  
**Primary owner:** Delivery lead

**Description**  
Map critical UI flows to API endpoints and existing automated API tests (or gaps).

**Business context**  
Enables targeted regression when API changes.

**Acceptance criteria**

```gherkin
Scenario: Matrix covers P0 flows
  Given list of P0 UI journeys
  When matrix complete
  Then each has API mapping or explicit gap Story

Scenario: Gap Stories created
  Given a gap
  When identified
  Then child Story exists under this Epic or V3 txn Epic
```

**Subtasks**

- [Either] Facilitate workshop.  
- [Dev] Fill technical columns.  
- [QA] Validate with test inventory.

**Definition of Done**

- [ ] Link to sheet/Confluence.  
- [ ] Gap Stories linked.

---

### QA-S-PLAT-005 — Performance pipeline scheduling and ownership

**Epic:** QA-E-PLAT-INF  
**Primary owner:** Delivery lead

**Description**  
Assign owner for perf job health; schedules; alert channel on failure.

**Business context**  
Unowned jobs decay.

**Acceptance criteria**

```gherkin
Scenario: Owner named
  Given each perf job
  When documented
  Then primary and backup owner listed

Scenario: Alerting
  Given job failure
  When occurs
  Then notification reaches Teams channel or email per runbook
```

**Subtasks**

- [Either] Runbook update.  
- [Dev] Add notifications if missing.

**Definition of Done**

- [ ] Runbook link.

---

### QA-S-PLAT-006 — Delivery dashboard (Jira)

**Epic:** QA-E-PLAT-INF  
**Primary owner:** Delivery lead

**Description**  
Create or refresh Jira dashboard: throughput, blocked, sprint goal progress, perf job links (see governance `dashboards.md`).

**Business context**  
Single pane for leadership and team.

**Acceptance criteria**

```gherkin
Scenario: Dashboard accessible
  Given stakeholder opens URL
  When loaded
  Then filters match team project and are documented

Scenario: Maintained
  Given workflow change
  When occurs
  Then dashboard updated within 1 business day
```

**Subtasks**

- [Either] Build gadgets.  
- [SM] Validate filters.  
- [PO] Approve layout.

**Definition of Done**

- [ ] URL in Story + README.

---

### QA-S-PLAT-007 — Entity V3 pipeline — sync investigation and job health

**Epic:** QA-E-PLAT-INF  
**Primary owner:** Delivery lead

**Description**  
Resolve or document Entity V3 pipeline drift (Unite/Entity jobs out of sync); restore reliable trigger, branch, or artifact path per platform team.

**Business context**  
Broken Entity jobs hide regressions and waste offshore triage time.

**Acceptance criteria**

```gherkin
Scenario: Root cause recorded
  Given investigation completes
  When documented
  Then Jira comment states cause category (config, branch, credentials, infra)

Scenario: Job runnable or waiver
  Given fix or explicit waiver from PO
  When closed
  Then either green job link exists or waiver references leadership approval
```

**Subtasks**

- [Dev] Pair with Dong/platform on pipeline config.  
- [Dev] Implement fix or temporary workaround.  
- [QA] Smoke run post-fix.  
- [Either] Escalate if blocked >5 days.

**Definition of Done**

- [ ] Comment with outcome; link or waiver.  
- [ ] Merged config if applicable.

---

## Governance & delivery (Lead)

### QA-S-GOV-001 — Requirement intake — templates live + team walkthrough

**Epic:** QA-E-GOV-DEL  
**Primary owner:** Delivery lead

**Description**  
Operationalize `docs/jira-governance/01-requirement-intake/` in Jira (fields, optional request type); 30-min walkthrough for team.

**Business context**  
Reduces orphan requests and unclear AC.

**Acceptance criteria**

```gherkin
Scenario: Template usable
  Given requester creates intake item
  When using template
  Then required fields are visible and validated

Scenario: Training done
  Given walkthrough scheduled
  When completed
  Then attendance noted in Story comment
```

**Subtasks**

- [Either] Configure Jira with admin.  
- [Either] Record session or slides.  
- [PO] Attend and approve.

**Definition of Done**

- [ ] Link to recording/slides.  
- [ ] Jira config documented.

---

### QA-S-GOV-002 — Cross-team dependency ritual

**Epic:** QA-E-GOV-DEL  
**Primary owner:** Delivery lead

**Description**  
Weekly 30m: review `dependency-external` labeled items; owners and dates; escalate per escalation doc.

**Business context**  
Automation blocked on env, API, other teams.

**Acceptance criteria**

```gherkin
Scenario: Ritual occurs
  Given weekly slot
  When held
  Then notes posted to Confluence or Jira dashboard comment

Scenario: Aging dependencies flagged
  Given item blocked >5 days
  When reviewed
  Then escalation comment added
```

**Subtasks**

- [Either] Facilitate series.  
- [SM] Track actions.

**Definition of Done**

- [ ] Recurring invite exists.  
- [ ] First 4 weeks of notes linked.

---

### QA-S-GOV-003 — Regression documentation master refresh

**Epic:** QA-E-GOV-DEL  
**Primary owner:** Delivery lead

**Description**  
Align AM regression docs (V2/V3 modules) with actual suite XML and nightly jobs; fix broken links.

**Business context**  
Offshore and leadership rely on docs for scope truth.

**Acceptance criteria**

```gherkin
Scenario: Modules match suites
  Given module doc list
  When compared to suite XML
  Then discrepancies fixed or waiver documented

Scenario: Review sign-off
  Given Tech Lead review
  When approved
  Then comment on Story
```

**Subtasks**

- [Either] Audit with Venkatesh/Dinesh.  
- [Dev] Update markdown in KB.  
- [Either] Publish to Confluence.

**Definition of Done**

- [ ] PR merged to KB.  
- [ ] Confluence sync if applicable.

---

### QA-S-GOV-004 — Quarterly backlog health review with PO

**Epic:** QA-E-GOV-DEL  
**Primary owner:** Delivery lead

**Description**  
Run [backlog-health-rules.md](../02-backlog-management/backlog-health-rules.md) filters; close/merge stale items; confirm Ready queue depth.

**Business context**  
Prevents sprint planning thrash and hidden WIP.

**Acceptance criteria**

```gherkin
Scenario: Review completed
  Given quarter boundary
  When session runs
  Then notes list top stale items resolved

Scenario: Metrics recorded
  Given JQL filters
  When run
  Then counts pasted to Story or Confluence
```

**Subtasks**

- [SM] Run JQL; invite PO.  
- [PO] Decide merge/close.  
- [Either] Update filters if workflow changed.

**Definition of Done**

- [ ] Link to notes.  
- [ ] Stale backlog count reduced or explained.

---

## Summary

| Metric | Value |
|--------|-------|
| **Epics** | 9 (see [epics.md](epics.md)) |
| **Stories in this file** | 32 |
| **Jira export used** | None — dedupe required after import |

See [gaps-analysis.md](gaps-analysis.md) for stakeholder questions.

**Version:** 1.0
