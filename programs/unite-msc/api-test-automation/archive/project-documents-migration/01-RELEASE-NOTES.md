> **Historical document** — describes the pre-canonical `mobile-microservices/` era. Current truth: `00-CURRENT-STATUS.md`, `10-LEGACY-TO-NEW-MIGRATION.md`. Canonical root is `mobile/`.

# Mobile Microservices API Automation — Release Notes

## Release 0.8 — Shared Auth Alignment, Mobile 2 Auth Reuse, and Reusable Reporting

| Field | Value |
|-------|-------|
| Date | 2026-06-02 |
| Branch | `feature/QA-987-featureAuthTokenClient` |
| Scope | Rebase on `main` (INFI-8078 shared auth), Mobile 2 shared-auth smoke, `mobile-ms-reporting` extraction |
| Validation | jsonapi-auth compile, auth-client smoke, Mobile 1/2 compile + smoke, parent compile, accountweb compile |
| Known Limitations | Dashboard endpoint not implemented; auth-client retains dedicated JsonPath client for diagnostics |

**Included:**

- Rebase onto latest `main` preserving Nick's `MobileServerClient` in `universal/jsonapi-auth`
- `mobile-ms-reporting` module (`MobileMsHtmlReportListener`, `SensitiveDataSanitizer`, portal generator)
- Mobile 2 `Mobile2SharedAuthSmokeTest` via shared `MobileServerClient` (no duplicated token logic)
- `mobile2.util.MobileHttpRestApiClient` mirroring Mobile 1 for future API tests
- ADR-024 through ADR-028 and `09-NICK-SHARED-AUTH-ALIGNMENT.md`

---

## Release 0.1 — Framework Skeleton

| Field | Value |
|-------|-------|
| Date | 2026-06-02 |
| Branch | `feature/QA-987-CreateMobileMscFramework` |
| Commit | `2b7583d` |
| Scope | Module registration, unite-enrollment skeleton, TestNG suites, bootstrap test, local scripts, initial Docs tree |
| Validation | Bootstrap PASS |
| Known Limitations | No API tests; smoke/regression reference bootstrap only |

**Included:** module registration, Unite Enrollment skeleton, TestNG XML suites, bootstrap validation, local runner scripts, shared JSON API reuse, no pipeline changes.

---

## Release 0.2 — Lightweight Alignment

| Field | Value |
|-------|-------|
| Date | 2026-06-02 |
| Branch | `feature/QA-987-CreateMobileMscFramework` |
| Commit | `2b7583d` (same baseline; alignment before cleanup commit) |
| Scope | Package and resource path normalization |
| Validation | Bootstrap PASS after moves |
| Known Limitations | Temporary `core.test` package removed; no API tests |

**Included:** Nick-aligned endpoint-based structure, `enrollment.*` packages, POJO under `enrollment.core.pojo`, JSON under `json/enrollment/`, SQL placeholder, build validation, existing-module impact validation.

---

## Release 0.3 — Legacy Discovery and QC4 Investigation

| Field | Value |
|-------|-------|
| Date | 2026-06-02 |
| Branch | `feature/QA-987-CreateMobileMscFramework` |
| Commit | `c52eac3` (structure cleanup and project-documents) |
| Scope | Postman inventory, legacy scan, 404 analysis, Wave 1 proposal |
| Validation | Read-only / documentation only |
| Known Limitations | Implementation intentionally paused until QC4 404 resolved |

**Included:** Postman inventory, QC4 environment inspection, legacy repo scan, feature/scenario inventory, endpoint inventory, 404 analysis, Wave 1 proposal, **no real API migration**.

---

## Release 0.4 — Repository Hygiene and Postman Audit

| Field | Value |
|-------|-------|
| Date | 2026-06-02 |
| Branch | `feature/QA-987-CreateMobileMscFramework` |
| Commit | `cace799` (cleanup), `7a0a3e0` (status export) |
| Scope | Final worktree audit, ignore hardening, generated-folder cleanup, validation, check-in |
| Validation | `clean test-compile`, bootstrap suite, local runner, accountweb `test-compile` |
| Known Limitations | Real API migration intentionally deferred until QC4 GET plans returns 200 |

**Included:**

- Top-level `postman/` structure audited (tracked Nick framework assets unchanged)
- Local Postman references verified ignored under `local-reference/`
- Generated Maven unpack folders identified and module `.gitignore` added
- Confirmed temporary autopilot packs already removed; no raw Postman under `Docs/`
- No raw Postman assets committed; no enrollment `config/*.properties` staged
- Universal (`jsonapi-aws-accountweb`) impact check — no source changes
- Real API migration remains **intentionally paused** pending Luis/developer QC4 routing

---

## Release 0.5 — Mobile 1 and Mobile 2 Framework Skeletons

| Field | Value |
|-------|-------|
| Date | 2026-06-02 |
| Branch | `feature/QA-987-Mobile1Mobile2Framework` |
| Commit | See `99-CURSOR-STATUS-EXPORT.md` (Release 0.5 check-in) |
| Scope | Additive `unite-mobile1` and `unite-mobile2` lightweight modules |
| Validation | `clean test-compile` + bootstrap per module; parent compile; accountweb impact |
| Known Limitations | No endpoint, auth, encryption, or pipeline work |

**Included:**

- Two additive lightweight modules registered in `mobile-microservices/pom.xml`
- Non-network bootstrap TestNG suites (`mobile1.bootstrap`, `mobile2.bootstrap`)
- Module `.gitignore` aligned with `unite-enrollment`
- Architecture decisions ADR-011 through ADR-016 in `03-ARCHITECTURE-DECISIONS.md`
- **No** endpoint implementation, auth client, encryption utility, or pipeline changes

---

## Release 0.6 — Reusable Mobile Authentication Token Client

| Field | Value |
|-------|-------|
| Date | 2026-06-08 |
| Branch | `feature/QA-987-featureAuthTokenClient` |
| Scope | Isolated `mobile-ms-auth-client` module |
| Validation | `test-compile`, auth TestNG suite (QC4), parent compile, accountweb impact |
| Known Limitations | No Dashboard implementation; no Enrollment encryption; no pipeline changes |

**Included:**

- Isolated reusable client module (`mobile-ms-auth-client`)
- NON_IDP JWT flow (`POST /mobile1api/v1/mobilemembersession`)
- IDP token-exchange flow (`POST /mobile1api/v1/idptokenexchange`)
- Immutable `MobileAuthSession` model (no global token storage)
- Masked `TokenDiagnostics` (opt-in via `-Dmobile.auth.diagnostics=true`)
- TestNG suite `testsuites/auth-token-client-testng.xml`
- Maven profile `mobile-ms-auth-smoke` + `acceptance-qc4`
- Validation: mapping tests PASS; integration tests PASS against QC4 with local env credentials
- Architecture decisions ADR-017 through ADR-019

**Not included:** Dashboard API tests, legacy Dashboard migration, Enrollment encryption, pipeline changes, shared `jsonapi-*` library modifications.

---

## Release 0.7 — Auth Client Simplification and Minimal HTML Reporting

| Field | Value |
|-------|-------|
| Date | 2026-06-08 |
| Branch | `feature/QA-987-featureAuthTokenClient` |
| Scope | Aggressive simplification + standalone HTML report |
| Validation | `test-compile`, full auth suite (QC4), parent compile, accountweb impact |
| Known Limitations | HTML report is local-only; GitLab artifact publishing deferred |

**Included:**

- Removed `MobileAuthConfiguration`, `MobileMsHttpRestApiClient`, all auth POJOs, mapping fixtures/tests
- JsonPath token extraction; Gson map login body
- Relaxed SSL off by default; QC4/lower env only
- Single test class `MobileAuthTokenClientTest`
- ExtentReports Spark HTML at `target/mobile-ms-report/index.html`
- QA guides `07-LOCAL-SETUP-AND-RUN-GUIDE.md`, `08-HTML-REPORTING-GUIDE.md`
- ADR-020 through ADR-023

**Not included:** Dashboard tests, Enrollment encryption, pipeline changes, shared reporting module.
