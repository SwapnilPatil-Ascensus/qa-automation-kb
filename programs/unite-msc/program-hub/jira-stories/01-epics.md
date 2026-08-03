# Mobile Microservices Automation — Epics

JIRA-ready epic definitions for the UniteMSC API automation migration program. Link all child stories to the appropriate epic below.

**Program context:** [Program hub README](../README.md) | **RAID:** [09-raid-log.md](../09-raid-log.md)

---

## Epic 1: Mobile Microservices Automation Discovery and Planning

| Field | Value |
|-------|-------|
| **Epic key (suggested)** | MOB-AUTO-E1 |
| **Type** | Epic |
| **Priority** | Highest |
| **Labels** | `mobile-automation`, `unite-msc`, `api-automation` |
| **Component** | QA Automation / Mobile MSC |

### Business Value

Establishes a fact-based migration plan before code movement. Reduces rework by inventorying legacy assets, aligning with the API Automation Framework, and resolving open architecture decisions.

### Description

Discover and document existing UniteMSC API automation in application repositories. Analyze the target API Automation Framework. Design the `mobile-automation/` module structure, migration rules, and decision matrix. Resolve pilot sequencing and architecture track (Cucumber migration vs Path B proposal).

### Scope

- Target framework analysis
- Folder/package design for `unite-enrollment`, `unite-mobile1`, `unite-mobile2`
- Migration decision matrix and rules
- Repo access and source-to-target mapping approach
- RAID decisions DEC-1 (pilot order) and DEC-2 (architecture track)

### Out of Scope

- Bulk scenario migration (Epics 2–4)
- CI pipeline implementation (Epic 5)

### Acceptance Criteria (Epic)

- [ ] Target framework structure documented with reuse patterns identified
- [ ] Approved `mobile-automation/` folder design committed to Confluence/program hub
- [ ] Migration decision matrix published and agreed by QA + Dev lead
- [ ] DEC-1 and DEC-2 recorded in RAID with decision owners and dates
- [ ] UniteMSC source repo map documented (paths TBD filled or flagged)

### Definition of Done (Epic)

All Epic 1 stories complete; discovery outputs linked from [05-unite-enrollment-migration-tracker.md](../05-unite-enrollment-migration-tracker.md); no open blocking spikes.

### Estimate

**T-shirt:** L | **Story points (rollup):** 21–34

---

## Epic 2: Unite Enrollment Automation Migration

| Field | Value |
|-------|-------|
| **Epic key (suggested)** | MOB-AUTO-E2 |
| **Type** | Epic |
| **Priority** | Highest |
| **Labels** | `mobile-automation`, `unite-msc`, `cucumber`, `rest-assured` |
| **Component** | unite-enrollment |

### Business Value

Unite Enrollment is the **pilot module**. Successful migration proves the pattern for Mobile 1 and Mobile 2 and delivers the first trustworthy centralized regression signal.

### Description

Inventory, evaluate, and migrate useful Unite Enrollment API automation from application repos into `mobile-automation/unite-enrollment/` in the API Automation Framework. Deliver vertical slice, smoke suite, and regression suite with documented exclusions.

### Scope

- Full legacy inventory for enrollment
- 3–5 scenario vertical slice
- Test data externalization
- `@smoke` and `@regression` tagged suites
- QC4 and Stage1 execution proof

### Dependencies

- Epic 1 complete (design + decisions)
- Read access to UniteMSC enrollment service repo (TBD path)

### Acceptance Criteria (Epic)

- [ ] Enrollment inventory complete in migration tracker
- [ ] ≥3 scenarios pass in target framework on QC4 (vertical slice)
- [ ] Smoke suite executable via Maven with `@uniteEnrollment` and `@smoke`
- [ ] Regression suite runs with exclusions documented
- [ ] Stage1 execution proof for smoke (or agreed subset)

### Definition of Done (Epic)

Enrollment tracker shows M4 (smoke) and M5 (regression) milestones met; exclusions approved; handoff notes in runbook.

### Estimate

**T-shirt:** L–XL | **Story points (rollup):** 34–55 | **Calendar:** 3–5 weeks (1 QA)

---

## Epic 3: Unite Mobile 1 Automation Migration

| Field | Value |
|-------|-------|
| **Epic key (suggested)** | MOB-AUTO-E3 |
| **Type** | Epic |
| **Priority** | High |
| **Labels** | `mobile-automation`, `unite-msc`, `cucumber`, `rest-assured` |
| **Component** | unite-mobile1 |

### Business Value

Extends proven migration pattern to Mobile 1, including **encryption-handling** scenarios required for MSC API coverage.

### Description

Repeat the enrollment migration pattern for `unite-mobile1`: inventory, vertical slice, data externalization, smoke/regression suites, stabilization in QC4/Stage1.

### Dependencies

- Epic 2 complete (or parallel only if DEC-1 changes pilot order)
- Encryption utilities/patterns from framework or prior module

### Acceptance Criteria (Epic)

- [ ] Mobile 1 inventory and decision matrix applied per scenario
- [ ] Vertical slice green on QC4
- [ ] Smoke and regression suites tagged and executable
- [ ] Encryption-related scenarios documented and passing or excluded with reason

### Definition of Done (Epic)

Mobile 1 tracker milestones M3–M5 complete; pipeline can run `@uniteMobile1` suites.

### Estimate

**T-shirt:** M–L | **Story points (rollup):** 21–34 | **Calendar:** 2–4 weeks

---

## Epic 4: Unite Mobile 2 Automation Migration

| Field | Value |
|-------|-------|
| **Epic key (suggested)** | MOB-AUTO-E4 |
| **Type** | Epic |
| **Priority** | High |
| **Labels** | `mobile-automation`, `unite-msc`, `cucumber`, `rest-assured` |
| **Component** | unite-mobile2 |

### Business Value

Covers the IdP-aware BFF with the broadest cross-service exposure. Completes the three-module API automation migration scope.

### Description

Migrate `unite-mobile2` automation using the established pattern. Address auth, dashboard, and account-related flows. Map coverage to OpenAPI (`mobile2.yaml` — TBD).

### Dependencies

- Epic 2 pattern proven (order may change per DEC-1)
- IDP/QC4 config stable or documented workarounds

### Acceptance Criteria (Epic)

- [ ] Mobile 2 inventory complete; coverage mapped to critical endpoints
- [ ] Vertical slice green on QC4
- [ ] Smoke and regression suites executable
- [ ] Cross-service dependencies documented in tracker

### Definition of Done (Epic)

Mobile 2 tracker complete; program-level three-module regression runnable.

### Estimate

**T-shirt:** M–L | **Story points (rollup):** 21–34 | **Calendar:** 2–4 weeks

---

## Epic 5: Regression Suite and Pipeline Integration

| Field | Value |
|-------|-------|
| **Epic key (suggested)** | MOB-AUTO-E5 |
| **Type** | Epic |
| **Priority** | High |
| **Labels** | `mobile-automation`, `unite-msc`, `api-automation`, `regression` |
| **Component** | CI/CD / Pipeline |

### Business Value

Makes migrated automation a **CI gate** for GitHub/GitLab pipelines — the primary driver for the UniteMSC migration program.

### Description

Validate Maven commands, integrate module/env/tag-based CI jobs for QC4 (PR gate) and Stage1 (post-deploy), configure reporting/artifacts, and define operational policies (env-health, quarantine).

### Dependencies

- At least pilot module smoke suite (Epic 2)
- DevOps runner access and secrets (TBD)

### Acceptance Criteria (Epic)

- [ ] Documented, validated Maven commands per module/env/tag
- [ ] QC4 pipeline runs smoke on PR for pilot module
- [ ] Stage1 verification step defined and tested
- [ ] Reports published as CI artifacts
- [ ] Env-health / quarantine approach documented

### Definition of Done (Epic)

M6 Pipeline Green milestone met; merge policy agreed with DevOps.

### Estimate

**T-shirt:** L | **Story points (rollup):** 21–34

---

## Epic 6: Documentation, Reporting, and Handoff

| Field | Value |
|-------|-------|
| **Epic key (suggested)** | MOB-AUTO-E6 |
| **Type** | Epic |
| **Priority** | Medium |
| **Labels** | `mobile-automation`, `unite-msc` |
| **Component** | Documentation |

### Business Value

Ensures leadership visibility, operational continuity, and knowledge transfer beyond a single QA resource.

### Description

Publish Confluence hub, maintain RAID and weekly status, deliver runbook/troubleshooting guide, and complete program sign-off against success criteria.

### Dependencies

- Epics 1–5 in progress or complete

### Acceptance Criteria (Epic)

- [ ] Confluence hub published per README copy order
- [ ] Runbook covers local run, CI re-run, common failures
- [ ] Weekly status template in use for ≥2 weeks
- [ ] Sign-off checklist from program overview reviewed and signed

### Definition of Done (Epic)

M7 Handoff Complete; program status summary updated to green or accepted risk.

### Estimate

**T-shirt:** M | **Story points (rollup):** 13–21

---

## Epic Link Summary

| Epic | Suggested key | Child story files |
|------|---------------|-------------------|
| Discovery and Planning | MOB-AUTO-E1 | [05-cross-cutting](./05-cross-cutting-framework-and-pipeline-stories.md) |
| Unite Enrollment | MOB-AUTO-E2 | [02-unite-enrollment](./02-unite-enrollment-stories.md) |
| Unite Mobile 1 | MOB-AUTO-E3 | [03-unite-mobile1](./03-unite-mobile1-stories.md) |
| Unite Mobile 2 | MOB-AUTO-E4 | [04-unite-mobile2](./04-unite-mobile2-stories.md) |
| Pipeline Integration | MOB-AUTO-E5 | [05-cross-cutting](./05-cross-cutting-framework-and-pipeline-stories.md) |
| Documentation and Handoff | MOB-AUTO-E6 | [05-cross-cutting](./05-cross-cutting-framework-and-pipeline-stories.md) |
