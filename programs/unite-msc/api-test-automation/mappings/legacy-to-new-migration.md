# Legacy-to-New Migration Comparison

**Cleanup commit:** `78f372e` — removed `mobile-microservices/`; canonical root is `mobile/`.  
**Reference commit for old tree:** `bda1af5` (last Dashboard vertical slice before cleanup).

## Summary

| Dimension | Old (`mobile-microservices`) | New (`mobile/`) |
|-----------|------------------------------|-----------------|
| Reactor parent | `mobile-microservices/pom.xml` | `mobile/pom.xml` |
| Reporting | `mobile-ms-reporting/` | `mobile/reporting/` |
| Mobile 1 | `unite-mobile1/` | `mobile/mobile1/` |
| Mobile 2 | `unite-mobile2/` | `mobile/mobile2/` |
| Enrollment pilot | `unite-enrollment/` | `mobile/enrollment/` |
| Auth smoke | `unite-mobile2` shared-auth (2 tests) | `mobile1` auth regression (1 test) |
| Dashboard tests | 8 regression + 1 integration gate | 1 lean test (integration + regression suites) |
| Dashboard negatives | 4 tests + profile | Not migrated |
| Base test pattern | `MobileDashboardClient` + assertions helpers | `MobileBaseRequestTest` + inline POJO asserts |

## Migration Coverage Matrix

| Old Item | Old Purpose | New Location / Status | Migrated? | Reason if not | Follow-up |
|----------|-------------|----------------------|-----------|---------------|-----------|
| `mobile-microservices/pom.xml` | Parent reactor | `mobile/pom.xml` | Yes | — | — |
| `mobile-ms-reporting/` | Extent + static portal | `mobile/reporting/` | Yes | Listener + portal generator ported | — |
| `unite-mobile1/` | Mobile 1 bootstrap + session | `mobile/mobile1/` | Yes | Lean auth regression only | NM Direct / IDP later |
| `unite-mobile2/` | Dashboard + auth smoke | `mobile/mobile2/` | Yes | Dashboard lean; auth moved to mobile1 | — |
| `unite-enrollment/` | Enrollment pilot | `mobile/enrollment/` | Yes | Separate scope | QC4 404 blocker (historical) |
| `Mobile2SharedAuthSmokeTest` | JWT auth verification (2 tests) | `Mobile1AuthenticationTest` (1 test) | Partial | Consolidated to Mobile 1 Hawaii session POST | IDP flows later |
| `Mobile1BootstrapTest` | Bootstrap scaffold | Removed | No | Not needed | — |
| `MobileMemberSessionRequestTest` | Extra session test | File exists; **not in suite** | No | Not needed for baseline | Wire only if product asks |
| `MobileDashboardTest` (8 `@Test`) | Full Dashboard regression | `MobileDashboardRequestTest` (1 test) | Partial | **Intentionally simplified** | Expand when SQL mapping available |
| `MobileDashboardClient` | Auth + GET wrapper | `MobileBaseRequestTest` + `client.invokeRestApi` | Partial | Simplified | — |
| `MobileDashboardAssertions` | Shared assertion helpers | Inline private methods in test | Partial | Simplified | Re-extract only if checks grow |
| `MobileApiReportTrace` | Rich report trace builder | Removed | No | **Intentionally simplified** | Safe metadata via listener later |
| `MobileDashboardNegativeTest` (4 tests) | 401/500 auth negatives | Not present | No | **Auth-owned; not Dashboard baseline** | Auth module / future MR |
| `mobile-ms-dashboard-negative` profile | Negative suite runner | Not in `mobile2/pom.xml` | No | Out of scope | Auth team |
| `mobile-ms-auth-smoke` profile | Auth smoke on mobile2 | `mobile1-auth-regression` on mobile1 | Yes | Auth ownership clarified | — |
| `Mobile2AuthReportCases` | Report registry for auth | Not wired in canonical suites | No | Mobile 1 suite has no HTML listener | Optional later |
| `MobileDashboardReportCases` | Report registry for Dashboard | Not registered | No | `@Test(description)` fallback works | Optional registration |
| Secondary fixture user `2` tests | Multi-fixture health | Not in lean test | No | **Intentionally simplified** | Add when second fixture required |
| Cucumber WAR enrollment tests | Legacy functional reference | Not copied | No | **Historical docs only** | Functional reference for Activities/Content/Banks |
| `local-reference/mobile-microservices/postman/` | Manual QC4 assets | Not in repo | No | Historical | `postman/mobile/` at repo root |
| `scripts/run-mobile-ms-local.ps1` | Local runner | Not verified on main | Needs clarification | Check if still exists at repo root | Update or remove in separate hygiene MR |
| SQL `plan.sql` for X-App-Version | Client version gate | `MobileBaseRequestTest` uses SQL | Yes | — | DB reconciliation still deferred |
| `nmdirect.json` fixture | NM Direct QC4 | Present on disk; not in suites | No | **Future NM Direct / IDP** | — |
| Project docs under old tree | Authoritative docs | `mobile/project-documents/` | Partial | Several files still say `mobile-microservices` | Updated in QA-987 docs pass |

## Old 8 Dashboard Regression Checks — Classification

See `11-DASHBOARD-COVERAGE-MATRIX.md` for per-check detail.

| # | Old test / check | New status |
|---|------------------|------------|
| 1 | Primary fixture GET returns owner summary + accounts | **Covered** (lean `getMobileDashboard`) |
| 2 | Secondary fixture authenticates + HTTP 200 | **Deferred** — single fixture `1` only |
| 3 | Beneficiary names on accounts | **Deferred** — not asserted in lean test |
| 4 | Structural account fields (prefix, ext, regType, etc.) | **Deferred** — only balance + non-empty accounts |
| 5 | `totalBalance` coherent with account balances | **Partial** — non-negative totals only |
| 6 | `planId` present | **Deferred** |
| 7 | `mobileUgifts` collection | **Deferred** |
| 8 | `displayInStackup` flag | **Deferred** |

## Future Work (explicitly not migrated)

| Theme | Owner / trigger |
|-------|-----------------|
| SQL-backed validation | Dev provides service SQL / source mapping |
| NM Direct / IDP | Separate auth initiative |
| Auth negatives | Auth module — not Dashboard baseline |
| Restore 8-test regression | Only after lean baseline stable + data strategy agreed |

## Historical References

Files that still mention `mobile-microservices` paths for **release archaeology**: `01-RELEASE-NOTES.md`, `03-LEGACY-DISCOVERY-SUMMARY.md`, `09-SHARED-AUTH-ALIGNMENT.md`, `99-CURSOR-STATUS-EXPORT.md`, `04-FIRST-ENDPOINT-READINESS.md`, `NEXT-PROMPT-AFTER-QC4-404-FIX.md`. Use this document and `00-CURRENT-STATUS.md` for current truth.
