# Sprint Kickoff — Unite MSC API Framework Stories (By Assignee)

**Purpose:** Pull-ready stories to start **this sprint** — create `mobile-automation/` in the API Automation Framework, run discovery in parallel, and **stand up Postman with Dev** on each module track.

**Program reference:** [03-target-framework-architecture.md](../03-target-framework-architecture.md) | [01-program-overview-and-plan-of-action.md](../01-program-overview-and-plan-of-action.md)

**Epic links (existing):**

| Epic | Key | Use for |
|------|-----|---------|
| Discovery and Planning | MOB-AUTO-E1 | Framework scaffold, repo access, design |
| Unite Enrollment Migration | MOB-AUTO-E2 | Enrollment discovery + scaffold |
| Unite Mobile 2 Migration | MOB-AUTO-E4 | Mobile 2 discovery + scaffold (parallel track) |

**Labels (all stories):** `mobile-automation`, `unite-msc`, `api-automation`, `sprint-kickoff`

**Bulk import:** [08-sprint-kickoff-import.csv](./08-sprint-kickoff-import.csv)

---

## Sprint goal

| Goal | Done when |
|------|-----------|
| **Framework exists in API Automation Framework repo** | `mobile-automation/` parent + at least one module compiles via Maven |
| **Postman working with Dev on QC4** | Each assignee has a validated Postman environment + collection for their module |
| **Discovery started** | Tracker inventory rows populated for assigned module |
| **Team unblocked** | Repo access confirmed; target repo URL/branch documented |

---

## Recommended sprint board (3 parallel tracks)

| Order | Assignee | Framework story | Postman + Dev story | Discovery story |
|-------|----------|-----------------|----------------------|-------------------|
| 1 | **You (QA Lead)** | MOB-AUTO-S26-001 | MOB-AUTO-S26-002 | MOB-AUTO-S26-003 |
| 2 | **Venkatesh** | MOB-AUTO-S26-004 | MOB-AUTO-S26-005 | MOB-AUTO-S26-006 |
| 3 | **Dinesh** | MOB-AUTO-S26-007 | MOB-AUTO-S26-008 | MOB-AUTO-S26-009 |

**Suggested story points (sprint total ~34):** Lead 13 · Venkatesh 11 · Dinesh 10 — adjust at refinement.

**Dependencies:** MOB-AUTO-S26-001 must merge before S26-004 and S26-007 scaffolds. Postman stories can start Day 1 with Dev (parallel to framework).

---

## Track 1 — You (QA Lead)

---

### MOB-AUTO-S26-001 — Create mobile-automation parent module in API Automation Framework

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Assignee** | QA Lead (you) |
| **Priority** | Highest |
| **Story Points** | 8 |
| **Epic** | MOB-AUTO-E1 |
| **Component** | Framework |
| **Labels** | `mobile-automation`, `unite-msc`, `api-automation`, `cucumber`, `sprint-kickoff` |
| **Maps to** | MOB-AUTO-101, MOB-AUTO-102 (partial), MOB-AUTO-105 |

### Context

Unite MSC API automation must live under `mobile-automation/` in the API Automation Framework, reusing `json-api`, `jsonapi-parent`, and shared config patterns per [03-target-framework-architecture.md](../03-target-framework-architecture.md).

### Description

Create the **parent** `mobile-automation/` module structure in the API Automation Framework repo:

```
api-automation/
├── json-api/                    # existing
├── universal/                   # existing
└── mobile-automation/           # NEW
    ├── pom.xml                  # child of jsonapi-parent
    ├── README.md
    ├── unite-enrollment/        # submodule placeholder
    ├── unite-mobile1/           # submodule placeholder
    └── unite-mobile2/           # submodule placeholder
```

Wire Maven parent, shared dependencies (`jsonapi-core`, `jsonapi-lib`, `jsonapi-encryption`, `qa-resource:database-loader`), Cucumber + Rest Assured versions aligned with framework, and document tag standards (`@mobile`, `@uniteEnrollment`, `@uniteMobile1`, `@uniteMobile2`, `@smoke`, `@regression`).

### Scope

**In:** Parent POM, folder layout, README, empty compiles for three child module stubs, branch/PR to API Framework repo  
**Out:** Scenario migration, CI pipeline, Postman (separate stories)

### Acceptance Criteria

- [ ] Target API Automation Framework **repo URL and branch** documented in tracker / RAID (replace TBD)
- [ ] `mobile-automation/pom.xml` inherits `jsonapi-parent`; `mvn clean compile` succeeds from repo root
- [ ] Three child module folders exist with minimal POM + package structure per architecture doc
- [ ] README lists module purpose, tag conventions, and link to program hub Confluence/markdown
- [ ] Reuse matrix (reuse / extend / new) attached — maps to MOB-AUTO-101 output
- [ ] PR reviewed by Dev lead; no secrets in committed property files

### Dependencies

- [ ] API Automation Framework repo access for QA Lead
- [ ] Dev lead confirms parent path (`mobile-automation/` alongside `json-api/`)

### Definition of Done

PR merged; architecture page reference updated; Venkatesh/Dinesh can branch from main for module stories.

---

### MOB-AUTO-S26-002 — Collaborate with Dev: Postman workspace for Unite Enrollment (QC4)

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Assignee** | QA Lead (you) |
| **Priority** | Highest |
| **Story Points** | 3 |
| **Epic** | MOB-AUTO-E2 |
| **Component** | unite-enrollment |
| **Labels** | `mobile-automation`, `unite-msc`, `postman`, `sprint-kickoff` |

### Context

Postman is the fastest way to validate endpoints, auth, and payloads **with Dev** before Cucumber migration. Enrollment is the **program pilot module**.

### Description

Partner with Unite Enrollment **Dev team** to stand up a shared Postman workspace:

1. Import or build collection from OpenAPI/Swagger (or Dev-provided export)
2. Configure **QC4 environment** (base URLs, auth tokens, IDP headers — via Postman secrets, not repo)
3. Validate **≥3 critical enrollment endpoints** manually (create/read/update or agreed happy paths)
4. Document which requests map to vertical-slice Cucumber candidates

### Scope

**In:** Postman collection + QC4 environment, Dev pairing sessions, endpoint parity checklist  
**Out:** Automated Cucumber tests (Venkatesh track); production Postman deployment

### Acceptance Criteria

- [ ] Shared Postman workspace/collection link documented (team access — not in git)
- [ ] QC4 environment variables defined with Dev (base URL, auth, required headers)
- [ ] **≥3 enrollment API calls** return expected status codes with Dev present (screenshot or export attached to Jira)
- [ ] Auth/IDP blockers logged in RAID if any endpoint fails
- [ ] Checklist maps Postman requests → legacy Cucumber scenario names (for migration)
- [ ] Dev contact and session date recorded in enrollment tracker

### Dependencies

- [ ] Dev availability (Enrollment service team)
- [ ] QC4 access for QA Lead
- [ ] MOB-AUTO-105 or equivalent repo/access unblocked

### Definition of Done

Postman collection usable by Venkatesh for step-definition work; no credentials in repo.

---

### MOB-AUTO-S26-003 — Confirm UniteMSC repo access and close DEC-1 pilot order for sprint

| Field | Value |
|-------|-------|
| **Type** | Task |
| **Assignee** | QA Lead (you) |
| **Priority** | Highest |
| **Story Points** | 2 |
| **Epic** | MOB-AUTO-E1 |
| **Component** | Governance |
| **Labels** | `mobile-automation`, `unite-msc`, `sprint-kickoff` |
| **Maps to** | MOB-AUTO-104, MOB-AUTO-105 |

### Description

Unblock the team for sprint execution:

1. Verify **read access** to `ascensus-gs/products/unitemsc` for you, Venkatesh, and Dinesh
2. Document repo map: service → test artifact path
3. Facilitate **DEC-1** decision: Enrollment-first (program brief) vs Mobile 2-first (Nick/Brian estimate) — record in [09-raid-log.md](../09-raid-log.md)
4. Confirm whether DEC-2 (Cucumber vs Path B TestNG) is **Cucumber migration** for this sprint

### Acceptance Criteria

- [ ] All three assignees can clone/read UniteMSC test folders
- [ ] Repo map table in technical reference or tracker
- [ ] DEC-1 recorded with date, owner, and sprint impact note
- [ ] DEC-2 recorded or explicitly deferred with Cucumber as sprint default
- [ ] Action items A1–A4 in [action-items.md](../action-items.md) updated

### Definition of Done

RAID updated; sprint plan aligned with DEC-1 outcome.

---

## Track 2 — Venkatesh

---

### MOB-AUTO-S26-004 — Implement unite-enrollment module scaffold and base Cucumber runner

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Assignee** | Venkatesh |
| **Priority** | Highest |
| **Story Points** | 5 |
| **Epic** | MOB-AUTO-E2 |
| **Component** | unite-enrollment |
| **Labels** | `mobile-automation`, `unite-msc`, `cucumber`, `rest-assured`, `sprint-kickoff` |
| **Maps to** | MOB-AUTO-205 |

### Description

After MOB-AUTO-S26-001 merges, implement **`mobile-automation/unite-enrollment/`** with full structure:

```
unite-enrollment/
├── features/
├── step-definitions/
├── pojos/
├── test-data/
├── sql/
├── runners/
└── config/
```

Deliver:

- Module POM wired to parent
- Base Cucumber runner with QC4 profile hook (`-Denv=qc4`)
- **Placeholder smoke feature** (`@mobile @uniteEnrollment @smoke`) that compiles
- Base step-definition class using framework REST helpers from `jsonapi-core` / `jsonapi-lib`
- Sample externalized JSON in `test-data/` (minimal valid payload)

### Acceptance Criteria

- [ ] `mvn test -pl mobile-automation/unite-enrollment` compiles (0–1 passing placeholder scenario)
- [ ] Package naming follows existing API framework convention
- [ ] Tags documented in module README
- [ ] No dependency on UniteMSC application repo classes
- [ ] PR reviewed by QA Lead + Dev lead

### Dependencies

- MOB-AUTO-S26-001 merged

### Definition of Done

PR merged; ready for vertical-slice scenario migration next sprint.

---

### MOB-AUTO-S26-005 — Collaborate with Dev: Postman validation for Enrollment vertical-slice candidates

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Assignee** | Venkatesh |
| **Priority** | High |
| **Story Points** | 3 |
| **Epic** | MOB-AUTO-E2 |
| **Component** | unite-enrollment |
| **Labels** | `mobile-automation`, `unite-msc`, `postman`, `sprint-kickoff` |

### Description

Using the Postman workspace from MOB-AUTO-S26-002 (or building on it with Dev):

1. Identify **3–5 vertical-slice candidate** enrollment flows with Dev
2. Execute each flow in Postman on QC4; capture request/response examples
3. Export sanitized examples to `test-data/` reference (no secrets — redact tokens)
4. Document assertion points for Cucumber migration (status, key JSON fields, optional DB check)

### Acceptance Criteria

- [ ] **≥3 vertical-slice candidates** agreed with Dev and listed in enrollment tracker
- [ ] Each candidate has a working Postman request on QC4 (Dev sign-off)
- [ ] Sanitized request/response samples stored under `test-data/` or linked doc (no credentials)
- [ ] Blockers (IDP, data, encryption) logged in RAID with owner
- [ ] Mapping table: Postman request name → planned Cucumber scenario name

### Dependencies

- MOB-AUTO-S26-002 in progress or complete (shared Postman workspace)
- Dev pairing time scheduled

### Definition of Done

Venkatesh can start MOB-AUTO-206 (vertical slice migration) next sprint without re-discovery.

---

### MOB-AUTO-S26-006 — Discover and inventory legacy Unite Enrollment automation assets

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Assignee** | Venkatesh |
| **Priority** | High |
| **Story Points** | 3 |
| **Epic** | MOB-AUTO-E2 |
| **Component** | unite-enrollment |
| **Labels** | `mobile-automation`, `unite-msc`, `cucumber`, `sprint-kickoff` |
| **Maps to** | MOB-AUTO-201 (partial — inventory only this sprint) |

### Description

Read-only inventory of Unite Enrollment test assets in UniteMSC source repo:

- Feature file and scenario counts
- Step definition classes
- Config/property files
- SQL scripts and test data locations
- Last-known execution status

Populate [05-unite-enrollment-migration-tracker.md](../05-unite-enrollment-migration-tracker.md) inventory section.

### Acceptance Criteria

- [ ] Inventory table populated (counts or TBD with owner)
- [ ] Source repo path documented per service
- [ ] Top 5 risks/blockers listed
- [ ] Feature → step mapping started (≥50% scenarios mapped or all if ≤20 scenarios)
- [ ] No modifications to source application repo

### Dependencies

- MOB-AUTO-S26-003 (repo access)

### Definition of Done

QA Lead reviews inventory; feeds MOB-AUTO-204 decision matrix next sprint.

---

## Track 3 — Dinesh

---

### MOB-AUTO-S26-007 — Implement unite-mobile2 module scaffold in API Automation Framework

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Assignee** | Dinesh |
| **Priority** | High |
| **Story Points** | 5 |
| **Epic** | MOB-AUTO-E4 |
| **Component** | unite-mobile2 |
| **Labels** | `mobile-automation`, `unite-msc`, `cucumber`, `rest-assured`, `sprint-kickoff` |
| **Maps to** | Mobile 2 scaffold (parallel to MOB-AUTO-205) |

### Description

After MOB-AUTO-S26-001 merges, implement **`mobile-automation/unite-mobile2/`** using the **same structure** as enrollment (features, steps, pojos, test-data, sql, runners, config).

Deliver:

- Module POM + compile proof
- Placeholder feature tagged `@mobile @uniteMobile2 @smoke`
- Base step-definition skeleton for BFF/auth patterns (empty steps OK)
- Notes on IDP/auth config dependencies from `jsonapi-lib/.../config/unite/`

**Rationale:** Mobile 2 is the alternate pilot per Nick/Brian estimates and Path B proposal. Parallel scaffold de-risks sequencing if DEC-1 chooses Mobile 2 first.

### Acceptance Criteria

- [ ] `mvn test -pl mobile-automation/unite-mobile2` compiles
- [ ] Structure mirrors enrollment module (documented in README)
- [ ] Tags `@mobile @uniteMobile2` documented
- [ ] IDP/auth config gaps listed (TBD items in RAID if needed)
- [ ] PR reviewed by QA Lead

### Dependencies

- MOB-AUTO-S26-001 merged

### Definition of Done

PR merged; Mobile 2 track ready for discovery → vertical slice.

---

### MOB-AUTO-S26-008 — Collaborate with Dev: Postman setup for Unite Mobile 2 BFF/auth (QC4)

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Assignee** | Dinesh |
| **Priority** | High |
| **Story Points** | 3 |
| **Epic** | MOB-AUTO-E4 |
| **Component** | unite-mobile2 |
| **Labels** | `mobile-automation`, `unite-msc`, `postman`, `sprint-kickoff` |

### Description

Partner with **Unite Mobile 2 / BFF Dev team** to stand up Postman for QC4:

1. Import OpenAPI (`mobile2.yaml` — path TBD with Dev) or Dev export
2. Configure QC4 environment (auth, IDP token flow, base URLs)
3. Validate **≥3 critical paths**: e.g. auth/login, dashboard, account summary (exact endpoints agreed with Dev)
4. Document cross-service dependencies (which downstream calls BFF triggers)

### Acceptance Criteria

- [ ] Postman collection for Mobile 2 exists in shared workspace (team access)
- [ ] QC4 environment works for auth flow with Dev assistance
- [ ] **≥3 BFF endpoints** return expected responses on QC4 (evidence in Jira)
- [ ] Auth/IDP failures documented in RAID with workaround or owner
- [ ] Critical-path endpoint list added to [07-unite-mobile2-migration-tracker.md](../07-unite-mobile2-migration-tracker.md)
- [ ] No credentials committed to git

### Dependencies

- Dev availability (Mobile 2 team)
- QC4 access for Dinesh
- MOB-AUTO-S26-003 repo access

### Definition of Done

Dinesh can map Postman flows to Cucumber scenarios; unblocks Mobile 2 vertical slice.

---

### MOB-AUTO-S26-009 — Discover and inventory legacy Unite Mobile 2 automation assets

| Field | Value |
|-------|-------|
| **Type** | Story |
| **Assignee** | Dinesh |
| **Priority** | High |
| **Story Points** | 2 |
| **Epic** | MOB-AUTO-E4 |
| **Component** | unite-mobile2 |
| **Labels** | `mobile-automation`, `unite-msc`, `cucumber`, `sprint-kickoff` |
| **Maps to** | MOB-AUTO-401 (partial — inventory this sprint) |

### Description

Read-only inventory of Unite Mobile 2 test assets:

- Cucumber features + `*IT.java` integration tests (if present)
- Step definitions and auth helpers
- Config files and OpenAPI references
- Cross-service dependency notes

Populate [07-unite-mobile2-migration-tracker.md](../07-unite-mobile2-migration-tracker.md).

### Acceptance Criteria

- [ ] Inventory table populated for Mobile 2
- [ ] OpenAPI/spec path documented (or flagged TBD)
- [ ] Cross-service dependencies listed (auth, enrollment, account, etc.)
- [ ] Top 5 migration risks recorded
- [ ] Comparison note: overlap with Postman critical paths from S26-008

### Dependencies

- MOB-AUTO-S26-003 (repo access)

### Definition of Done

QA Lead reviews; feeds sprint planning for Mobile 2 vertical slice.

---

## Sprint checklist (pull into Jira)

### Before sprint start

- [ ] Create/link epics MOB-AUTO-E1, E2, E4 (or map to QA-796 parent if applicable)
- [ ] Import stories from [08-sprint-kickoff-import.csv](./08-sprint-kickoff-import.csv)
- [ ] Assign MOB-AUTO-S26-001 to QA Lead — **Day 1 priority**
- [ ] Schedule Dev pairing sessions for S26-002, S26-005, S26-008 (same week)
- [ ] Confirm API Framework repo URL in RAID (action A3)

### During sprint

- [ ] Daily: Postman + framework progress in standup
- [ ] Mid-sprint: Venkatesh/Dinesh blocked until S26-001 merges — use time for discovery + Postman with Dev
- [ ] End of sprint: at least one module `mvn test` compiles; three Postman tracks validated

### Next sprint candidates (not in this pull)

| Story ID | Summary |
|----------|---------|
| MOB-AUTO-206 | Migrate Enrollment vertical slice (Venkatesh) |
| MOB-AUTO-405 | Migrate Mobile 2 vertical slice (Dinesh) |
| MOB-AUTO-501 | Validate Maven commands |
| MOB-AUTO-502 | QC4 smoke pipeline |

---

## Quick copy — Jira summary lines

```text
[MSC Framework] Create mobile-automation parent module in API Automation Framework
[MSC Postman] Collaborate with Dev — Postman QC4 setup for Unite Enrollment
[MSC Governance] Confirm UniteMSC repo access and close DEC-1 for sprint
[MSC Enrollment] Implement unite-enrollment scaffold and base Cucumber runner
[MSC Postman] Collaborate with Dev — Postman validation for Enrollment slice candidates
[MSC Enrollment] Discover and inventory legacy Enrollment automation assets
[MSC Mobile2] Implement unite-mobile2 module scaffold in API Automation Framework
[MSC Postman] Collaborate with Dev — Postman QC4 setup for Mobile 2 BFF/auth
[MSC Mobile2] Discover and inventory legacy Mobile 2 automation assets
```

---

## Related existing stories (do not duplicate in Jira)

| New sprint ID | Existing program ID |
|---------------|---------------------|
| S26-001 | 101, 102, 105 |
| S26-002, S26-005 | (new — Postman track) |
| S26-003 | 104, 105 |
| S26-004 | 205 |
| S26-006 | 201 |
| S26-007 | Mobile 2 scaffold (part of 401 series) |
| S26-009 | 401 |

Use **either** sprint IDs **or** existing MOB-AUTO-2xx IDs in Jira — not both for the same work.
