# Unite Mobile 2 Automation Migration — Stories

**Epic link:** MOB-AUTO-E4 — Unite Mobile 2 Automation Migration

**Note:** Nick/Brian estimates sequence Mobile 2 **first** for pipeline/setup. If DEC-1 adopts that order, execute this epic before Epic 2/3. Path B proposal also pilots on `unite-mobile2` — align with DEC-2.

---

## MOB-AUTO-401 — Discover legacy Unite Mobile 2 automation assets

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Priority** | High |
| **Labels** | `mobile-automation`, `unite-msc`, `cucumber`, `api-automation` |
| **Component** | unite-mobile2 |
| **Estimate** | M — **5 points** |

### Business Value

Mobile 2 is the BFF with highest cross-service and schema-drift exposure; inventory drives realistic estimates.

### Description

Inventory Cucumber/feature assets, `*IT.java` integration tests (if present), configs, and OpenAPI coverage baseline for `unite-mobile2`.

### Acceptance Criteria

- [ ] Inventory in [07-unite-mobile2-migration-tracker.md](../07-unite-mobile2-migration-tracker.md) complete
- [ ] Cucumber `*IT.java` suites listed with run status (running / broken / unknown)
- [ ] OpenAPI spec location documented (`mobile2.yaml` — TBD)
- [ ] Cross-service dependencies listed (auth, account, dashboard)

### Dependencies

- MOB-AUTO-105

### Definition of Done

Inventory reviewed; Path B overlap noted in RAID if applicable.

---

## MOB-AUTO-402 — Map Mobile 2 features, endpoints, and critical-path coverage

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Priority** | High |
| **Labels** | `mobile-automation`, `unite-msc`, `rest-assured`, `api-automation` |
| **Component** | unite-mobile2 |
| **Estimate** | L — **8 points** |

### Business Value

Aligns test migration with UX-critical endpoints and GitHub cutover smoke requirements.

### Description

Map scenarios to endpoints; define critical-path set (health, login, dashboard golden path per integration design). Apply decision matrix.

### Acceptance Criteria

- [ ] Endpoint catalog mapped to OpenAPI (or gap list)
- [ ] Critical-path scenario list agreed (smoke vs v1 scope)
- [ ] Decision matrix 100% applied
- [ ] IdP integration requirements documented

### Dependencies

- MOB-AUTO-401

### Definition of Done

Critical-path list signed off by QA + Dev lead.

---

## MOB-AUTO-403 — Implement unite-mobile2 module scaffold

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Priority** | High |
| **Labels** | `mobile-automation`, `unite-msc`, `cucumber` |
| **Component** | unite-mobile2 |
| **Estimate** | S — **3 points** |

### Business Value

Target location for Mobile 2 automation and pipeline smoke gate.

### Description

Create `mobile-automation/unite-mobile2/` module using established pattern.

### Acceptance Criteria

- [ ] Module compiles; base config for QC4/Stage1
- [ ] Tags `@mobile @uniteMobile2` documented
- [ ] If Path B: document relationship to `unite-msc/jsonapi-mobile2` (TBD)

### Dependencies

- MOB-AUTO-205 or MOB-AUTO-303 (scaffold template)

### Definition of Done

PR merged.

---

## MOB-AUTO-404 — Migrate Mobile 2 vertical slice (smoke-critical paths)

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Priority** | Highest |
| **Labels** | `mobile-automation`, `unite-msc`, `cucumber`, `rest-assured` |
| **Component** | unite-mobile2 |
| **Estimate** | L — **8 points** |

### Business Value

Delivers minimum viable gate for GitHub migration (health, login, dashboard).

### Description

Migrate 3–5 scenarios covering health endpoints, login, and dashboard golden path. Execute on QC4 against real shared DB pattern.

### Acceptance Criteria

- [ ] Health, login, dashboard scenarios pass on QC4
- [ ] Tests use unique test data keys (no global table counts)
- [ ] DB assertions use framework JDBC utilities
- [ ] Failures triaged: test vs env vs schema drift

### Technical Notes

- Align with smoke definition in `mobile-msc-integration-test-design.md` if Path B adopted
- Concurrency: unique keys per run

### Dependencies

- MOB-AUTO-403, MOB-AUTO-402

### Definition of Done

M3 vertical slice green; demo to DevOps for pipeline story.

---

## MOB-AUTO-405 — Integrate Mobile 2 smoke with DevOps pipeline (pilot)

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Priority** | Highest |
| **Labels** | `mobile-automation`, `unite-msc`, `regression`, `api-automation` |
| **Component** | unite-mobile2 |
| **Estimate** | L — **8 points** |

### Business Value

Unblocks GitHub PR gate for Mobile 2 service repo (Nick estimate: 1 sprint for smoke + pipeline).

### Description

Wire Mobile 2 smoke suite into CI on PR against QC4. Coordinate with DevOps for runner, secrets, and service deploy model (TBD).

### Acceptance Criteria

- [ ] PR pipeline runs `@uniteMobile2 @smoke` on QC4
- [ ] Pipeline publishes pass/fail to PR check
- [ ] Secrets not in property files
- [ ] Runbook section for re-triggering pipeline

### Dependencies

- MOB-AUTO-404, MOB-AUTO-502

### Definition of Done

At least one successful PR pipeline run recorded.

---

## MOB-AUTO-406 — Build Mobile 2 full regression suite and Stage1 stabilization

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Priority** | High |
| **Labels** | `mobile-automation`, `unite-msc`, `cucumber`, `regression` |
| **Component** | unite-mobile2 |
| **Estimate** | XL — **13 points** |

### Business Value

Closes coverage gap between smoke-only cutover and full critical-path (v1) coverage.

### Description

Migrate remaining approved scenarios to `@regression`. Stabilize QC4 and Stage1. Document exclusions. Target critical-path coverage per OpenAPI policy (reviewer-enforced).

### Acceptance Criteria

- [ ] Regression suite runs on QC4
- [ ] Stage1 smoke/regression per release policy (TBD)
- [ ] Coverage delta vs OpenAPI documented
- [ ] Exclusions log complete
- [ ] M5 milestone in Mobile 2 tracker

### Dependencies

- MOB-AUTO-405, MOB-AUTO-503

### Definition of Done

Mobile 2 module migration complete for program scope.
