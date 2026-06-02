# 02 — Current State Assessment

## Executive Summary

UniteMSC API automation today lives **inside application development repositories**, is **inconsistently executed**, and is **not production-ready as a regression signal**. Treat existing assets as a **baseline reference** for migration—not as trusted coverage. Mobile UI automation is stale, lightly maintained, and on a **separate track** (BrowserStack/Node); this page focuses on **API/microservices** state.

---

## Repository Pattern

| Element | Typical location | Notes |
|---------|------------------|-------|
| Application code | `src/main` in service repos | UniteMSC services under GitLab: `ascensus-gs/products/unitemsc` (TBD: exact repo paths per service) |
| API test artifacts | `src/test` — features, step definitions, configs | Co-located with app code; weak QA ownership |
| Execution profile | `mvn install -P debug` (Cucumber + Cucable, Failsafe) | Per-service integration suites |
| Test data | `*Datastore.sql` snapshots in service repos | Locally seeded Postgres; not representative of shared QC4/Stage DB |

## Existing Assets (API automation)

| Asset type | Description | Migration relevance |
|------------|-------------|---------------------|
| Cucumber feature files | BDD scenarios near application code | Primary migration source |
| Step definitions | Rest Assured–based steps | Map to target framework packages |
| Config / properties | Environment-specific settings | Must align with QC4, Stage1, Stage2, Stage5 patterns |
| SQL / DB validation | Embedded or referenced SQL | Externalize; validate against shared DB strategy |
| Test data | Often heavy payloads inside features | Externalize to JSON/test-data files |
| Runners / profiles | Maven profiles, tags | Map to centralized tag and suite strategy |

## Problems Identified

| Problem | Impact |
|---------|--------|
| **Mixed ownership** | Tests maintained like unit/integration tests by dev teams; QA cannot reliably own regression |
| **Stale / not running E2E** | IdP and Universal Platform integrations were never completed; suites stopped being a reliable signal |
| **Environment blind spot** | Local seed data always matched code under test; **cross-team DB drift** on shared QC4/Stage not caught until QA/Staging |
| **Heavy feature files** | Hard to read, parameterize, and reuse across environments |
| **Hidden dependencies** | Possible coupling to application classes or repo-specific utilities |
| **Pipeline gap** | Legacy pipelines abandoned or broken; GitHub migration needs a working integration gate |
| **Limited QA bandwidth** | Discussion notes: one QA (Nick) heavily associated with mobile automation knowledge |

## Mobile UI Automation (separate — context only)

| Area | Current condition |
|------|-------------------|
| Stack | Node.js, npm, WebDriver-based automation |
| Execution | BrowserStack Local required for internal service routing |
| Maintenance | Many cases stale; only some flows (e.g., login, withdrawal) recently validated |
| Pipeline | Former pipeline not maintained; App Center deprecation contributed to failure |
| Priority | **Not current program focus** — documented under Mobile UI Automation placeholder |

## Integration Test Design Context (engineering proposal)

A separate design proposal (`mobile-msc-integration-test-design.md`) describes **Path B**: centralized `unite-msc/` module in `qa-automation/api-test-automation/`, TestNG-based tests, versioned zip via Nexus, PR gate against **real QC4 DB**, pilot on **`unite-mobile2`**. This differs from the **Cucumber migration** track in technology and pilot ordering.

| Aspect | Cucumber migration (this program) | Path B integration framework (proposal) |
|--------|-----------------------------------|----------------------------------------|
| Target | API Automation Framework + Cucumber | `unite-msc/` + TestNG + Nexus zip |
| Pilot (documented) | Unite Enrollment | unite-mobile2 |
| Existing Cucumber in app repos | Migrate useful scenarios | Deprecate at cutover (XOR) |

**Action:** Leadership should confirm whether tracks merge, run in parallel, or one supersedes the other. Until decided, both are noted in RAID.

## Current State Conclusion

| Statement | Detail |
|-----------|--------|
| Baseline only | Do not declare current automation as regression-ready |
| Migration required | Centralize, validate, tag, and pipeline-enable |
| Discovery first | Full inventory before bulk migration |
| Environment proof | Every migrated scenario needs execution proof in QC4/Stage |

## Inventory Checklist (TBD per module)

| Item | Unite Enrollment | Unite Mobile 1 | Unite Mobile 2 |
|------|------------------|----------------|----------------|
| Feature file count | TBD | TBD | TBD |
| Step definition classes | TBD | TBD | TBD |
| Active endpoints covered | TBD | TBD | TBD |
| Config files | TBD | TBD | TBD |
| SQL scripts | TBD | TBD | TBD |
| Last known green run | TBD | TBD | TBD |
| Known blockers (IDP, UP, encryption) | TBD | TBD | TBD |

## Related Pages

| Page | Purpose |
|------|---------|
| [03-target-framework-architecture.md](./03-target-framework-architecture.md) | Target structure and standards |
| [04-migration-strategy.md](./04-migration-strategy.md) | How to move from current to target |
| [05-unite-enrollment-migration-tracker.md](./05-unite-enrollment-migration-tracker.md) | Enrollment inventory and status |
