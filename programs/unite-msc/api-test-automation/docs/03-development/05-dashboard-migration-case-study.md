# Dashboard Migration Case Study

Reference implementation for Mobile 2 endpoint migration. Canonical root: `mobile/`. Cleanup commit: `78f372e`.

## Objective

Establish the first **lean, repeatable** Mobile 2 API baseline under canonical `mobile/`:

- Prove Hawaii non-IDP auth works via Mobile 1
- Automate one happy-path Dashboard GET with POJO mapping
- Wire integration + regression suites and HTML reporting
- Defer SQL, NM Direct/IDP, and expanded regression until data/auth strategy is ready

## Starting Point

| Item | State before migration |
|------|------------------------|
| Active tree | `mobile-microservices/` (pilot reactor) |
| Dashboard tests | 8 regression checks + helpers (`MobileDashboardClient`, `MobileDashboardAssertions`) |
| Auth | Split across `unite-mobile1` / `unite-mobile2` smoke |
| Reporting | `mobile-ms-reporting` under old tree |
| Enrollment | Pilot scaffold; QC4 404 blocker |
| Legacy functional tests | Cucumber WAR (read-only reference) |

## Discovery Process

### Postman / endpoint validation

| Step | Action |
|------|--------|
| 1 | Review MSC Postman collection (`postman/mobile/`) — request paths, headers, auth chain |
| 2 | Confirm Hawaii QC4 host (Unite BFF) and `GET /mobile2api/v1/mobiledashboard` returns 200 with valid session |
| 3 | Capture **structure** of HAL `_embedded.item` — not exact balances for automation |
| 4 | Record `idpEnabled: false` for Hawaii fixture — non-IDP login path |
| 5 | Do **not** paste tokens, passwords, or account numbers into docs or reports |

### Legacy repo review

| Step | Action |
|------|--------|
| 1 | Read old `mobile-microservices/unite-mobile2` Dashboard tests (git history: `bda1af5`) |
| 2 | List each `@Test` and assertion helper — build coverage matrix (`10-LEGACY-TO-NEW-MIGRATION.md`) |
| 3 | Treat Cucumber enrollment/Dashboard features as **functional reference only** |
| 4 | Classify each check: migrate now / simplify / defer / auth-owned |

## Why Enrollment Was Deferred

| Factor | Detail |
|--------|--------|
| QC4 blocker | `enrollmentapi` routes returned **404** via BFF — URL/routing unclear |
| Scope | Enrollment is a separate product vertical (`mobile/enrollment/`) |
| Risk | Guessing endpoints or weakening assertions is not acceptable |
| Decision | Finish auth + one Mobile 2 GET slice first; enrollment waits for dev-confirmed base URL |

See historical `04-FIRST-ENDPOINT-READINESS.md` (enrollment-focused).

## Why Dashboard Was Selected First

| Reason | Detail |
|--------|--------|
| Auth dependency | Dashboard requires authenticated GET — validates end-to-end auth + API |
| Readiness | Endpoint path known; Hawaii fixture stable (`user id 1`) |
| Low write risk | GET-only; no mutation side effects |
| High visibility | Core mobile landing data — good pilot for reporting and POJO pattern |
| Legacy coverage | Old repo already had Dashboard tests to compare against |

## Old vs New Structure

| Area | Old (`mobile-microservices`) | New (`mobile/`) |
|------|------------------------------|-----------------|
| Parent | `mobile-microservices/pom.xml` | `mobile/pom.xml` |
| Mobile 1 | `unite-mobile1/` | `mobile/mobile1/` |
| Mobile 2 | `unite-mobile2/` | `mobile/mobile2/` |
| Reporting | `mobile-ms-reporting/` | `mobile/reporting/` |
| Dashboard test | `MobileDashboardTest` (8 tests) | `MobileDashboardRequestTest` (1 test) |
| Auth helpers | `MobileDashboardClient` | `MobileBaseRequestTest` + `setTestUser` |
| Assertions | `MobileDashboardAssertions` | Private methods in test class |
| Auth negatives | `MobileDashboardNegativeTest` | Not ported — auth-owned |

## Auth Decision

| Rule | Implementation |
|------|----------------|
| Mobile 1 owns auth | `Mobile1AuthenticationTest` — Hawaii member session POST |
| Mobile 2 reuses auth | `MobileDashboardRequestTest extends MobileBaseRequestTest` |
| Setup group | `@BeforeMethod(groups = {"setup"})` on `MobileBaseRequestTest` |
| Hawaii first | `hawaii.json`, `idpEnabled: false`, `setTestUser("1")` |
| NM Direct / IDP | `nmdirect.json` exists; **not in suites** — future scope |
| Auth negatives | Stay in auth module — not Dashboard baseline |

## Dashboard Implementation Summary

| Principle | What we did |
|-----------|-------------|
| Lean TestNG | One `@Test` — `getMobileDashboard` |
| POJO conversion | `MobileDashboardEmbeddedPOJO`, `MobileDashboardItemPOJO`, `MobileAccountSummaryPOJO` |
| Minimal business checks | Owner names, `totalBalance` ≥ 0, `asOfDate`, non-empty accounts, first balance ≥ 0 |
| No assertion helper class | Inline `assertContractFields` / `assertBusinessFields` |
| No auth negatives | 401/500 invalid-auth tests not in Dashboard suite |
| No SQL yet | TODO comment — DB reconciliation deferred |
| No redundant client | `client.invokeRestApi` via shared `MobileHttpRestApiClient` |

## Suite Summary

| Suite | Profile | Class | Tests | Report listener |
|-------|---------|-------|-------|-----------------|
| Mobile 1 Auth Regression | `acceptance-qc4`, `mobile1-auth-regression` | `Mobile1AuthenticationTest` | 1 | No |
| Mobile 2 Dashboard Integration | `mobile-ms-integration` | `MobileDashboardRequestTest` | 1 | Yes |
| Mobile 2 Dashboard Regression | `mobile-ms-dashboard-regression` | `MobileDashboardRequestTest` | 1 | Yes |

Same Dashboard test runs in both Mobile 2 suites; suite name drives report category/subtitle.

## Reporting Summary

| Item | Detail |
|------|--------|
| Path | `mobile/mobile2/target/mobile-ms-report/index.html` |
| Branding | `Mobile MSC` / **API Automation** |
| Suite-aware titles | Integration vs regression subtitles differ |
| Test title | From `@Test(description=...)` |
| Secrets / PII | No raw tokens, passwords, Authorization headers, or account numbers (verified) |
| Gap | Safe auth metadata (fixture id, branding, token fingerprint) — follow-up MR |

See `08-HTML-REPORTING-GUIDE.md`.

## Legacy-to-New Coverage Summary

| Category | Examples |
|----------|----------|
| **Migrated** | Reporting module, canonical reactor, auth regression, Dashboard GET, suite profiles |
| **Intentionally simplified** | 8 tests → 1; removed client/assertion/trace helpers |
| **Deferred** | Secondary fixture, ugifts, planId, displayInStackup, beneficiary/structural fields, balance sum coherence |
| **Auth-owned** | Dashboard negative tests (401/500) |
| **Future** | SQL/DB checks, NM Direct/IDP |

Full matrix: `10-LEGACY-TO-NEW-MIGRATION.md`, `11-DASHBOARD-COVERAGE-MATRIX.md`.

## Validation Commands

```powershell
# Mobile 1 auth — expect 1 pass
mvn -f mobile/mobile1/pom.xml clean test "-Pacceptance-qc4,mobile1-auth-regression" "-Denvironment.properties=qc4.properties"

# Mobile 2 integration — expect 1 pass
mvn -f mobile/mobile2/pom.xml clean test "-Pmobile-ms-integration" "-Denvironment.properties=qc4.properties"

# Mobile 2 regression — expect 1 pass
mvn -f mobile/mobile2/pom.xml clean test "-Pmobile-ms-dashboard-regression" "-Denvironment.properties=qc4.properties"

# Parent build
mvn -f mobile/pom.xml test-compile
mvn -f mobile/pom.xml clean install -DskipTests
```

**Note:** Transient QC4 `Connection reset` may occur; HTTP client retries. Re-run once before treating as outage.

## Known Gaps

| Gap | Owner / trigger |
|-----|-----------------|
| SQL validation | Dev SQL / source mapping |
| DB reconciliation | Same + fixture account keys |
| NM Direct / IDP | Auth initiative |
| Additional Dashboard regression (7 deferred checks) | Product + data strategy |
| Report auth metadata | Small reporting MR |

## Lessons Learned

| Lesson | Detail |
|--------|--------|
| Audit before code | Migration matrix prevented blind port of 8 tests |
| One happy path first | Faster CI signal; easier SDET review |
| Auth in one module | Mobile 1 owns session; Mobile 2 stays thin |
| Helpers have a cost | Old assertion/client classes obscured intent |
| Docs are part of delivery | `project-documents/` enables next modules without re-discovery |
| Environment flakiness ≠ code defect | Log connection resets; retry before changing tests |

## What to Repeat for Next Modules

1. Audit legacy + Postman → coverage matrix
2. One lean `*RequestTest` extending `MobileBaseRequestTest`
3. POJOs per response fragment; meaningful asserts only
4. Integration suite + profile; regression when justified
5. HTML report validation — no secrets
6. Update `project-documents/` and module README
7. Defer SQL and auth negatives until explicitly in scope

**Playbook:** `14-MOBILE-ENDPOINT-MIGRATION-PLAYBOOK.md`  
**Guardrails:** `15-CURSOR-MIGRATION-GUARDRAILS.md`
