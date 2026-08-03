# Unite Enrollment Automation Migration — Stories

**Epic link:** MOB-AUTO-E2 — Unite Enrollment Automation Migration

---

## MOB-AUTO-201 — Discover legacy Unite Enrollment automation assets

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Priority** | Highest |
| **Labels** | `mobile-automation`, `unite-msc`, `cucumber`, `api-automation` |
| **Component** | unite-enrollment |
| **Estimate** | M — **5 points** |

### Business Value

Produces the authoritative inventory needed to estimate migration effort and avoid migrating obsolete scenarios.

### Description

Catalog all Unite Enrollment API automation artifacts in the source application repository (read-only): feature files, step definitions, configs, SQL, test data, runners, and last-known execution status.

### Scope

- Count and list feature files and scenarios
- List step definition classes and shared utilities
- Document config/property files and environment assumptions
- Note IDP/Universal Platform dependencies
- Update [05-unite-enrollment-migration-tracker.md](../05-unite-enrollment-migration-tracker.md)

### Acceptance Criteria

- [ ] Inventory table populated in migration tracker (counts or TBD with owner)
- [ ] Source repo path documented (was TBD)
- [ ] Last known execution status recorded per asset group
- [ ] Top 10 risks/blockers listed with owners

### Technical Notes

- Source repo: TBD under `ascensus-gs/products/unitemsc`
- Do not modify source repo
- Coordinate with Infinity team data for QA-796 if applicable

### Dependencies

- MOB-AUTO-105 (repo access)

### Definition of Done

Inventory reviewed by QA lead; linked from Confluence tracker page.

---

## MOB-AUTO-202 — Map Enrollment feature files to step definitions

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Priority** | High |
| **Labels** | `mobile-automation`, `unite-msc`, `cucumber` |
| **Component** | unite-enrollment |
| **Estimate** | M — **5 points** |

### Business Value

Enables traceability from business scenarios to implementation and identifies orphaned or duplicate steps.

### Description

Create a mapping matrix linking each enrollment feature/scenario to its step definitions, shared steps, and reuse opportunities.

### Scope

- Feature → step definition map
- Flag duplicate step logic
- Flag steps with app-repo dependencies (anti-pattern for migration)

### Acceptance Criteria

- [ ] Mapping matrix attached to tracker or linked doc
- [ ] 100% of inventoried scenarios mapped or marked N/A
- [ ] Orphan step definitions identified
- [ ] Consolidation candidates listed (≥1 or "none found")

### Technical Notes

- Output format: table in tracker or CSV attachment

### Dependencies

- MOB-AUTO-201

### Definition of Done

Matrix reviewed; consolidation list agreed with Dev lead.

---

## MOB-AUTO-203 — Map Enrollment endpoints, payloads, validations, SQL, and configs

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Priority** | High |
| **Labels** | `mobile-automation`, `unite-msc`, `rest-assured`, `api-automation` |
| **Component** | unite-enrollment |
| **Estimate** | L — **8 points** |

### Business Value

Surfaces hidden coupling to endpoints, DB, and environments before migration starts.

### Description

For each enrollment scenario selected for migration, document REST endpoints, request/response payloads, assertion types, SQL scripts, and config keys required for QC4/Stage1 execution.

### Scope

- Endpoint list with HTTP methods
- Payload sources (inline vs file)
- DB validation SQL
- Environment-specific config keys

### Acceptance Criteria

- [ ] Endpoint catalog covers all vertical-slice candidate scenarios
- [ ] Each endpoint has QC4 base URL/config reference (TBD filled or flagged)
- [ ] SQL scripts categorized: migrate / rewrite / exclude
- [ ] Config gap list created for IDP/UP issues

### Technical Notes

- Align property files with `jsonapi-lib/.../config/unite/` pattern
- Reference [03-target-framework-architecture.md](../03-target-framework-architecture.md)

### Dependencies

- MOB-AUTO-202

### Definition of Done

Endpoint catalog stored in tracker; config gaps have RAID entries if blocking.

---

## MOB-AUTO-204 — Apply migration decision matrix to Enrollment scenarios

| Field | Value |
|-------|-------|
| **Type** | Task |
| **Priority** | High |
| **Labels** | `mobile-automation`, `unite-msc` |
| **Component** | unite-enrollment |
| **Estimate** | M — **3 points** |

### Business Value

Prevents blind copy-paste and documents exclusions for leadership transparency.

### Description

Evaluate every inventoried enrollment scenario using the decision matrix: migrate, update, consolidate, parameterize, exclude, park for review.

### Scope

- Populate Decision and Status columns in tracker
- Require reason for every exclude/park

### Acceptance Criteria

- [ ] 100% of scenarios have a decision recorded
- [ ] Exclusions log has reason, date, approver for each exclude
- [ ] ≥3 scenarios marked migrate for vertical slice

### Dependencies

- MOB-AUTO-201, MOB-AUTO-203

### Definition of Done

QA lead sign-off on exclusion list.

---

## MOB-AUTO-205 — Implement unite-enrollment module scaffold in API Automation Framework

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Priority** | Highest |
| **Labels** | `mobile-automation`, `unite-msc`, `cucumber`, `api-automation` |
| **Component** | unite-enrollment |
| **Estimate** | M — **5 points** |

### Business Value

Creates the target location for all enrollment automation with correct structure and tags.

### Description

Create `mobile-automation/unite-enrollment/` with folders: features, step-definitions, pojos, test-data, sql, runners, config — wired to `jsonapi-parent` and shared libraries.

### Scope

- Folder structure per approved design
- POM/module entry (TBD parent POM path)
- Base tags documented
- Empty smoke feature compiles

### Acceptance Criteria

- [ ] Module exists in target repo (branch/PR TBD)
- [ ] `mvn test` compiles module (zero scenarios or 1 placeholder)
- [ ] Package naming follows framework convention
- [ ] README or inline doc lists module purpose and tags

### Technical Notes

- Reuse `jsonapi-core`, `jsonapi-lib`, `qa-resource:database-loader`
- Target repo URL: TBD

### Dependencies

- MOB-AUTO-102 (folder design approved)

### Definition of Done

PR merged; module linked from architecture page.

---

## MOB-AUTO-206 — Migrate Enrollment vertical slice (3–5 scenarios)

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Priority** | Highest |
| **Labels** | `mobile-automation`, `unite-msc`, `cucumber`, `rest-assured` |
| **Component** | unite-enrollment |
| **Estimate** | L — **8 points** |

### Business Value

Proves end-to-end migration pattern before bulk investment.

### Description

Migrate 3–5 high-value enrollment scenarios into the target module. Execute successfully against QC4.

### Scope

- Migrate selected scenarios (from MOB-AUTO-204)
- Update step definitions to framework patterns
- Local and QC4 execution proof

### Acceptance Criteria

- [ ] ≥3 scenarios pass on QC4
- [ ] No dependency on application repo classes
- [ ] Execution logs attached to tracker
- [ ] Known failures documented with RAID links

### Technical Notes

- Tag: `@mobile @uniteEnrollment` (+ `@smoke` if in smoke set)
- See example feature in [03-target-framework-architecture.md](../03-target-framework-architecture.md)

### Dependencies

- MOB-AUTO-205, MOB-AUTO-203, MOB-AUTO-105

### Definition of Done

Vertical slice demo completed; M3 milestone marked in tracker.

---

## MOB-AUTO-207 — Externalize heavy Enrollment test data from feature files

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Priority** | High |
| **Labels** | `mobile-automation`, `unite-msc`, `api-automation` |
| **Component** | unite-enrollment |
| **Estimate** | M — **5 points** |

### Business Value

Improves maintainability and enables QC4/Stage1 switching without editing features.

### Description

Move inline JSON and large payloads from enrollment feature files into `test-data/` with logical names. Wire environment-specific values through config.

### Scope

- All vertical-slice scenarios externalized
- Naming convention documented
- Setup/cleanup assumptions documented

### Acceptance Criteria

- [ ] No payload >20 lines remains inline in vertical-slice features
- [ ] `test-data/` files use logical names (e.g. `validEnrollmentRequest.json`)
- [ ] QC4 and Stage1 can load data via config without feature edits
- [ ] Data setup/cleanup doc updated in runbook (or stub)

### Dependencies

- MOB-AUTO-206

### Definition of Done

Code review approved; data strategy section updated in architecture doc.

---

## MOB-AUTO-208 — Build Unite Enrollment smoke suite

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Priority** | High |
| **Labels** | `mobile-automation`, `unite-msc`, `cucumber`, `regression` |
| **Component** | unite-enrollment |
| **Estimate** | M — **5 points** |

### Business Value

Delivers fast CI feedback for critical enrollment paths.

### Description

Tag critical enrollment scenarios with `@smoke`. Validate Maven tag filter runs only smoke subset.

### Scope

- Identify critical paths (with product/QA lead)
- Apply `@smoke` tags
- Document expected runtime

### Acceptance Criteria

- [ ] ≥3 scenarios tagged `@smoke`
- [ ] Maven command documented and executed successfully (QC4)
- [ ] Smoke runtime documented (target: minutes — TBD actual)
- [ ] Non-smoke scenarios excluded when running smoke filter

### Technical Notes

```bash
# EXAMPLE — validate in MOB-AUTO-501
mvn test -pl mobile-automation/unite-enrollment -Denv=qc4 \
  -Dcucumber.filter.tags="@mobile and @uniteEnrollment and @smoke"
```

### Dependencies

- MOB-AUTO-206

### Definition of Done

M4 Smoke Suite Green in tracker.

---

## MOB-AUTO-209 — Build Unite Enrollment regression suite

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Priority** | High |
| **Labels** | `mobile-automation`, `unite-msc`, `cucumber`, `regression` |
| **Component** | unite-enrollment |
| **Estimate** | L — **8 points** |

### Business Value

Provides full migrated coverage for release confidence.

### Description

Migrate remaining scenarios marked **migrate** or **update** in the decision matrix. Tag with `@regression`. Document all exclusions.

### Scope

- Bulk migration of approved scenarios
- Regression tag application
- Exclusions log complete

### Acceptance Criteria

- [ ] All "migrate/update" scenarios implemented or moved to exclusions with approval
- [ ] `@regression` suite runs on QC4 with pass rate documented
- [ ] Exclusions log 100% complete in tracker
- [ ] Coverage summary: migrated vs excluded counts published

### Dependencies

- MOB-AUTO-208, MOB-AUTO-204

### Definition of Done

M5 Regression Suite Green in tracker.

---

## MOB-AUTO-210 — Stabilize Enrollment automation in QC4 and Stage1

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Priority** | High |
| **Labels** | `mobile-automation`, `unite-msc`, `regression` |
| **Component** | unite-enrollment |
| **Estimate** | M — **5 points** |

### Business Value

Ensures suites are reliable across environments, not just locally.

### Description

Fix environment-specific failures for enrollment smoke and regression in QC4 and Stage1. Document Stage1 data prerequisites.

### Scope

- QC4 stabilization (flake fixes, data fixes)
- Stage1 property alignment
- Stage1 smoke execution proof

### Acceptance Criteria

- [ ] Smoke passes 3 consecutive QC4 runs (or documented env issue)
- [ ] Smoke passes at least once on Stage1
- [ ] Stage1 data gaps documented in RAID if any
- [ ] Flaky tests quarantined with `@debug` or exclusion — not silent failure

### Dependencies

- MOB-AUTO-209, MOB-AUTO-503 (Stage1 pipeline optional parallel)

### Definition of Done

Stabilization notes in tracker; enrollment module ready for pipeline hard-gate (if policy agreed).
