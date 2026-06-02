# Cross-Cutting — Framework, Pipeline, and Documentation Stories

Stories spanning discovery, framework design, pipeline, and handoff. Grouped by epic link.

---

## Epic 1: Discovery and Planning (MOB-AUTO-E1)

---

### MOB-AUTO-101 — Spike: Analyze target API Automation Framework structure

| Field | Value |
|-------|-------|
| **Type** | Spike |
| **Priority** | Highest |
| **Labels** | `mobile-automation`, `api-automation` |
| **Component** | Framework |
| **Estimate** | M — **5 points** |
| **Epic** | MOB-AUTO-E1 |

### Business Value

Ensures migration reuses existing patterns instead of reinventing utilities.

### Description

Review `json-api`, `universal/`, `jsonapi-parent`, property loading, reporting, and DB loader patterns. Document what Mobile MSC modules must reuse vs extend.

### Acceptance Criteria

- [ ] Reuse matrix published (reuse / extend / new)
- [ ] Gaps listed with recommended owners
- [ ] Target repo URL and branch strategy documented (TBD → filled or escalated)
- [ ] Spike time-box: 3 days

### Definition of Done

Output linked from [11-technical-reference](../11-technical-reference-and-cursor-execution-notes.md).

---

### MOB-AUTO-102 — Design mobile-automation folder and package structure

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Priority** | Highest |
| **Labels** | `mobile-automation`, `api-automation`, `cucumber` |
| **Component** | Framework |
| **Estimate** | M — **5 points** |
| **Epic** | MOB-AUTO-E1 |

### Business Value

Prevents inconsistent structure across three service modules.

### Description

Produce approved design for `mobile-automation/unite-enrollment|mobile1|mobile2` per [03-target-framework-architecture.md](../03-target-framework-architecture.md). Include tagging and test-data standards.

### Acceptance Criteria

- [ ] Design reviewed and approved by QA + Dev lead
- [ ] Confluence/architecture page updated
- [ ] Package naming convention documented
- [ ] POJO and config conventions referenced from framework

### Dependencies

- MOB-AUTO-101

### Definition of Done

M2 Target Design Complete milestone.

---

### MOB-AUTO-103 — Document migration decision matrix and migration rules

| Field | Value |
|-------|-------|
| **Type** | Task |
| **Priority** | High |
| **Labels** | `mobile-automation`, `unite-msc` |
| **Component** | Framework |
| **Estimate** | S — **2 points** |
| **Epic** | MOB-AUTO-E1 |

### Business Value

Shared rules for all three module migrations.

### Description

Publish decision matrix (migrate/update/consolidate/parameterize/exclude/park) and migration rules in program hub. Train team on usage.

### Acceptance Criteria

- [ ] [04-migration-strategy.md](../04-migration-strategy.md) reviewed and current
- [ ] Team walkthrough completed (notes attached)
- [ ] Tracker columns match matrix vocabulary

### Definition of Done

Linked from all three module trackers.

---

### MOB-AUTO-104 — Spike: Resolve pilot order and architecture track (DEC-1, DEC-2)

| Field | Value |
|-------|-------|
| **Type** | Spike |
| **Priority** | Highest |
| **Labels** | `mobile-automation`, `unite-msc` |
| **Component** | Governance |
| **Estimate** | S — **3 points** |
| **Epic** | MOB-AUTO-E1 |

### Business Value

Unblocks sprint planning and prevents duplicate work across Cucumber vs Path B tracks.

### Description

Facilitate decision on: (1) pilot module order — Enrollment first vs Mobile 2 first; (2) Cucumber migration vs Path B TestNG `unite-msc/` vs hybrid. Update RAID.

### Acceptance Criteria

- [ ] DEC-1 and DEC-2 closed in [09-raid-log.md](../09-raid-log.md)
- [ ] Decision communicated to team with impact on epic sequencing
- [ ] Action items updated

### Dependencies

- Leadership + Architecture availability

### Definition of Done

RAID decisions table has dates and owners.

---

### MOB-AUTO-105 — Obtain UniteMSC source repo access and document repo map

| Field | Value |
|-------|-------|
| **Type** | Task |
| **Priority** | Highest |
| **Labels** | `mobile-automation`, `unite-msc` |
| **Component** | Discovery |
| **Estimate** | XS — **1 point** |
| **Epic** | MOB-AUTO-E1 |

### Business Value

Unblocks all discovery stories.

### Description

Secure read access to `ascensus-gs/products/unitemsc` and document service paths for enrollment, mobile1, mobile2 test artifacts.

### Acceptance Criteria

- [ ] All QA team members who need access have it
- [ ] Repo map table: service → path → test artifact location
- [ ] Recorded in technical reference page

### Definition of Done

Access verified by attempting clone/read of test folders.

---

### MOB-AUTO-106 — Spike: Evaluate Playwright/Karate only if framework blocker proven

| Field | Value |
|-------|-------|
| **Type** | Spike |
| **Priority** | Lowest |
| **Labels** | `mobile-automation`, `api-automation` |
| **Component** | Framework |
| **Estimate** | S — **2 points** |
| **Epic** | MOB-AUTO-E1 |

### Business Value

Documents deliberate technology choice; avoids ad-hoc framework churn.

### Description

**Only execute if** a concrete blocker is raised against Java/Cucumber/Rest Assured. Otherwise mark cancelled with "no blocker" note.

### Acceptance Criteria

- [ ] Spike outcome: proceed with current stack OR documented blocker with leadership approval for alternative
- [ ] No alternative framework introduced without approval

### Definition of Done

RAID updated; spike closed or cancelled.

---

## Epic 5: Pipeline Integration (MOB-AUTO-E5)

---

### MOB-AUTO-501 — Validate and document Maven execution commands per module

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Priority** | High |
| **Labels** | `mobile-automation`, `api-automation`, `cucumber`, `regression` |
| **Component** | Pipeline |
| **Estimate** | M — **5 points** |
| **Epic** | MOB-AUTO-E5 |

### Business Value

Replaces placeholder commands with validated runbook entries.

### Description

Validate Maven commands for smoke/regression per module and environment. Update [08-regression-suite-and-pipeline-strategy.md](../08-regression-suite-and-pipeline-strategy.md).

### Acceptance Criteria

- [ ] Commands validated for enrollment (pilot) — QC4 smoke + regression
- [ ] Commands marked VALIDATED vs EXAMPLE in docs
- [ ] Local run instructions in runbook
- [ ] Tag expressions tested for correct scenario subset

### Dependencies

- MOB-AUTO-208 minimum

### Definition of Done

Runbook Maven section complete.

---

### MOB-AUTO-502 — Integrate QC4 smoke pipeline for pilot module

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Priority** | Highest |
| **Labels** | `mobile-automation`, `unite-msc`, `regression`, `api-automation` |
| **Component** | Pipeline |
| **Estimate** | L — **8 points** |
| **Epic** | MOB-AUTO-E5 |

### Business Value

Turns automation into a merge gate for GitHub/GitLab migration.

### Description

Implement CI job: PR trigger → QC4 → run pilot module smoke → publish results. TBD: GitHub Actions vs GitLab; self-hosted runner labels.

### Acceptance Criteria

- [ ] Pipeline runs on PR commit to pilot service branch
- [ ] Uses validated Maven smoke command
- [ ] Credentials from secrets manager only
- [ ] PR check shows pass/fail
- [ ] Merge policy documented (hard block vs advisory — per DEC)

### Dependencies

- MOB-AUTO-208 or MOB-AUTO-405 (smoke suite); DevOps

### Definition of Done

M6 partial — QC4 smoke green for pilot.

---

### MOB-AUTO-503 — Integrate Stage1 post-deploy verification pipeline

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Priority** | High |
| **Labels** | `mobile-automation`, `unite-msc`, `regression` |
| **Component** | Pipeline |
| **Estimate** | M — **5 points** |
| **Epic** | MOB-AUTO-E5 |

### Business Value

Catches environment-specific failures after deploy.

### Description

Add Stage1 step to release pipeline using same tags or expanded regression per policy.

### Acceptance Criteria

- [ ] Stage1 job runs after deploy with `stage1.properties`
- [ ] Failure halts promotion per release team policy (documented)
- [ ] At least one successful Stage1 run recorded

### Dependencies

- MOB-AUTO-502, MOB-AUTO-210 or equivalent stabilization

### Definition of Done

Stage1 documented in pipeline strategy page.

---

### MOB-AUTO-504 — Configure CI reporting and artifact publishing

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Priority** | Medium |
| **Labels** | `mobile-automation`, `api-automation`, `regression` |
| **Component** | Pipeline |
| **Estimate** | M — **5 points** |
| **Epic** | MOB-AUTO-E5 |

### Business Value

Speeds triage and leadership visibility of failures.

### Description

Publish HTML/XML reports as pipeline artifacts; add PR summary comment if supported (TBD tooling).

### Acceptance Criteria

- [ ] Reports retained ≥30 days in CI (or per org policy)
- [ ] Failed scenario name visible in PR check or comment
- [ ] Reporting approach documented (Allure vs existing — TBD)

### Dependencies

- MOB-AUTO-502

### Definition of Done

Sample report link attached to runbook.

---

### MOB-AUTO-505 — Define env-health probe and test quarantine policy

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Priority** | High |
| **Labels** | `mobile-automation`, `unite-msc`, `regression` |
| **Component** | Pipeline |
| **Estimate** | M — **5 points** |
| **Epic** | MOB-AUTO-E5 |

### Business Value

Prevents hard-block gate from blocking teams during QC4 outages.

### Description

Design and implement env-health pre-check, limited retry policy, and quarantine process for flaky tests.

### Acceptance Criteria

- [ ] Env-health probe runs before suite; fails fast with clear message if QC4 unhealthy
- [ ] Quarantine process documented (who approves, max duration)
- [ ] Slack alert channel identified for env-wide failures (TBD)
- [ ] Policy linked from pipeline strategy page

### Dependencies

- MOB-AUTO-502

### Definition of Done

Policy reviewed by DevOps + QA lead.

---

## Epic 6: Documentation and Handoff (MOB-AUTO-E6)

---

### MOB-AUTO-601 — Publish Confluence Mobile Automation Program Hub

| Field | Value |
|-------|-------|
| **Type** | Task |
| **Priority** | Medium |
| **Labels** | `mobile-automation`, `unite-msc` |
| **Component** | Documentation |
| **Estimate** | S — **2 points** |
| **Epic** | MOB-AUTO-E6 |

### Business Value

Single source of truth for leadership and team.

### Description

Copy `docs/mobile-automation-program-hub/` pages to Confluence per [README.md](../README.md) order. Fix internal links.

### Acceptance Criteria

- [ ] All 11 pages + status summary + action items published
- [ ] Mobile UI Automation placeholder page created
- [ ] RAID and trackers accessible to stakeholders

### Definition of Done

Confluence URL shared with team.

---

### MOB-AUTO-602 — Create automation runbook and troubleshooting guide

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Priority** | Medium |
| **Labels** | `mobile-automation`, `api-automation`, `cucumber` |
| **Component** | Documentation |
| **Estimate** | M — **5 points** |
| **Epic** | MOB-AUTO-E6 |

### Business Value

Reduces bus factor and speeds onboarding beyond Nick.

### Description

Runbook: local setup, Maven commands, env switching, common failures (IDP, data, DB drift), pipeline re-run, quarantine.

### Acceptance Criteria

- [ ] Runbook covers all three modules
- [ ] Troubleshooting section with ≥5 common failure patterns
- [ ] Linked from Confluence technical reference page

### Dependencies

- MOB-AUTO-501, MOB-AUTO-210

### Definition of Done

Runbook reviewed by second QA team member.

---

### MOB-AUTO-603 — Create weekly leadership status template and first two reports

| Field | Value |
|-------|-------|
| **Type** | Task |
| **Priority** | Medium |
| **Labels** | `mobile-automation`, `unite-msc` |
| **Component** | Documentation |
| **Estimate** | S — **2 points** |
| **Epic** | MOB-AUTO-E6 |

### Business Value

Consistent leadership communication.

### Description

Use [10-weekly-status-and-leadership-updates.md](../10-weekly-status-and-leadership-updates.md) template; publish first two weekly updates.

### Acceptance Criteria

- [ ] Template in active use in Confluence
- [ ] Two weekly entries with status, blockers, metrics
- [ ] RAID updates referenced each week

### Definition of Done

Leadership acknowledges receipt of updates.

---

### MOB-AUTO-604 — Program sign-off and handoff review

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Priority** | Medium |
| **Labels** | `mobile-automation`, `unite-msc`, `regression` |
| **Component** | Documentation |
| **Estimate** | M — **3 points** |
| **Epic** | MOB-AUTO-E6 |

### Business Value

Formal closure against program success criteria.

### Description

Review sign-off checklist from program overview with QA lead and leadership. Document accepted gaps and backlog.

### Acceptance Criteria

- [ ] Sign-off checklist completed or exceptions documented
- [ ] [status-summary.md](../status-summary.md) updated to final status
- [ ] Remaining backlog items converted to JIRA if needed
- [ ] M7 Handoff Complete milestone marked

### Dependencies

- Epics 2–5 substantially complete

### Definition of Done

Sign-off meeting notes attached to Confluence.
