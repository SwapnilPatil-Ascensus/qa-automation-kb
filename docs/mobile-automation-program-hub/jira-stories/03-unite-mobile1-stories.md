# Unite Mobile 1 Automation Migration — Stories

**Epic link:** MOB-AUTO-E3 — Unite Mobile 1 Automation Migration

**Prerequisite:** Enrollment migration pattern proven (Epic 2) unless DEC-1 changes pilot order.

---

## MOB-AUTO-301 — Discover legacy Unite Mobile 1 automation assets

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Priority** | High |
| **Labels** | `mobile-automation`, `unite-msc`, `cucumber`, `api-automation` |
| **Component** | unite-mobile1 |
| **Estimate** | M — **5 points** |

### Business Value

Baselines Mobile 1 coverage and highlights encryption-related complexity early.

### Description

Inventory all Mobile 1 API automation in the source repo: features, steps, configs, SQL, test data. Flag encryption-specific steps and dependencies.

### Acceptance Criteria

- [ ] Inventory table in [06-unite-mobile1-migration-tracker.md](../06-unite-mobile1-migration-tracker.md) populated
- [ ] Encryption-related assets explicitly tagged in inventory
- [ ] Source repo path documented (TBD → filled)
- [ ] Dependency on Mobile 2 setup documented if applicable (per Nick estimate)

### Dependencies

- MOB-AUTO-201 (pattern established); MOB-AUTO-105

### Definition of Done

Inventory reviewed by QA lead.

---

## MOB-AUTO-302 — Map Mobile 1 features, endpoints, payloads, SQL, and configs

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Priority** | High |
| **Labels** | `mobile-automation`, `unite-msc`, `rest-assured` |
| **Component** | unite-mobile1 |
| **Estimate** | M — **5 points** |

### Business Value

Single reference for migration and encryption refactor scope.

### Description

Produce feature→step map and endpoint catalog for Mobile 1, including encryption handling touchpoints.

### Acceptance Criteria

- [ ] Feature→step map complete
- [ ] Endpoint catalog with encryption flags
- [ ] Decision matrix applied (migrate/update/consolidate/parameterize/exclude/park)
- [ ] ≥2 vertical-slice candidates identified

### Dependencies

- MOB-AUTO-301

### Definition of Done

Mapping attached to Mobile 1 tracker.

---

## MOB-AUTO-303 — Implement unite-mobile1 module scaffold

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Priority** | High |
| **Labels** | `mobile-automation`, `unite-msc`, `cucumber` |
| **Component** | unite-mobile1 |
| **Estimate** | S — **3 points** |

### Business Value

Reuses enrollment scaffold pattern with minimal new structure.

### Description

Create `mobile-automation/unite-mobile1/` module mirroring enrollment structure; wire POM and base config.

### Acceptance Criteria

- [ ] Module compiles in target framework
- [ ] Tags `@mobile @uniteMobile1` documented
- [ ] Encryption utility reuse path documented (from enrollment or shared lib)

### Dependencies

- MOB-AUTO-205 (enrollment scaffold as template)

### Definition of Done

PR merged; linked from architecture page.

---

## MOB-AUTO-304 — Migrate Mobile 1 vertical slice with encryption handling

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Priority** | High |
| **Labels** | `mobile-automation`, `unite-msc`, `cucumber`, `rest-assured` |
| **Component** | unite-mobile1 |
| **Estimate** | L — **8 points** |

### Business Value

Validates the hardest Mobile 1 differentiator (encryption) in the target framework.

### Description

Migrate 3–5 Mobile 1 scenarios including at least one encryption flow. Prove QC4 execution.

### Acceptance Criteria

- [ ] ≥3 scenarios pass on QC4
- [ ] ≥1 encryption scenario passes or is excluded with approved reason
- [ ] No app-repo class dependencies
- [ ] Encryption approach documented for Mobile 2/Enrollment reuse

### Dependencies

- MOB-AUTO-303, MOB-AUTO-302

### Definition of Done

M3 vertical slice green in Mobile 1 tracker.

---

## MOB-AUTO-305 — Externalize Mobile 1 test data and build smoke suite

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Priority** | Medium |
| **Labels** | `mobile-automation`, `unite-msc`, `cucumber`, `regression` |
| **Component** | unite-mobile1 |
| **Estimate** | M — **5 points** |

### Business Value

Readable features and fast CI feedback for Mobile 1.

### Description

Externalize payloads for vertical-slice scenarios; tag critical paths `@smoke`; validate Maven smoke command on QC4.

### Acceptance Criteria

- [ ] Test data externalized for all smoke scenarios
- [ ] `@smoke` filter runs successfully on QC4
- [ ] Smoke runtime documented

### Dependencies

- MOB-AUTO-304

### Definition of Done

M4 smoke milestone in Mobile 1 tracker.

---

## MOB-AUTO-306 — Build Mobile 1 regression suite and stabilize QC4/Stage1

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Priority** | High |
| **Labels** | `mobile-automation`, `unite-msc`, `cucumber`, `regression` |
| **Component** | unite-mobile1 |
| **Estimate** | L — **8 points** |

### Business Value

Completes Mobile 1 module migration for program scope.

### Description

Migrate remaining approved scenarios; tag `@regression`; stabilize QC4 and Stage1; finalize exclusions log.

### Acceptance Criteria

- [ ] Regression suite runs on QC4 with documented pass rate
- [ ] Stage1 smoke passes at least once
- [ ] Exclusions log complete
- [ ] M5 and stabilization notes in tracker

### Dependencies

- MOB-AUTO-305, MOB-AUTO-503 (Stage1 pipeline)

### Definition of Done

Mobile 1 tracker milestones M4–M5 complete.
