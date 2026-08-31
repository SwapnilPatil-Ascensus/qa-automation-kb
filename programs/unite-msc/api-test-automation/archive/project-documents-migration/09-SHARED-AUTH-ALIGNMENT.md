> **Historical document** — paths reference removed `mobile-microservices/`. Current auth baseline: `mobile/mobile1/` + `07-LOCAL-SETUP-AND-RUN-GUIDE.md`.

# Nick Shared Authentication Alignment

## Shared Auth Entry Point

| Item | Detail |
|------|--------|
| Module | `universal/jsonapi-auth` |
| Primary class | `core.auth.mobile.MobileServerClient` |
| HTTP helper | `core.auth.mobile.util.MobileHttpRestApiClient` |
| NON_IDP entry | `getMobileToken()` |
| IDP entry | `getAccessToken()` (session login + `/idptokenexchange`) |
| Reverse IDP flow | `getMobileToken(String accessToken)` via `/mobilememberidptoken` |

Endpoints (constants in `MobileServerClient`):

- `POST /mobile1api/v1/mobilemembersession`
- `POST /mobile1api/v1/idptokenexchange`
- `POST /mobile1api/v1/mobilememberidptoken`

## Mobile 1 Usage Pattern

`unite-mobile1` wraps shared auth in `mobile1.util.MobileHttpRestApiClient`:

1. `setupBeforeEach` reads `mobile-authentication-uri`, optional PKCE (`authentication-uri`, `web-client-id`) when `users.idpEnabled` is true.
2. `setTestUser(userId)` loads credentials from `src/test/resources/user/<env>/<branding>.json`.
3. `configure(branding, username, password)` delegates to `MobileServerClient.configure(...)`.
4. `setDefaultHeaders` lazily obtains a bearer token:
   - **NON_IDP:** `mobileClient.getMobileToken().getJwtToken()`
   - **PKCE + IDP:** `authClient.getAccessTokenByCode()` then `mobileClient.getMobileToken(accessToken)`

Downstream API calls reuse the same `HttpRestApiClient` with `Authorization: Bearer <token>` and `X-App-Version` from DB (`plan.sql`).

## NON_IDP Flow

```text
MobileLoginPOJO(planId, username, password)
  → POST /mobile1api/v1/mobilemembersession
  → MobileSessionPOJO.jwtToken
  → Bearer JWT on downstream requests
```

Nick's payload uses `planId`, `username`, `password` only (no `rememberMe` / `deviceUuid`).

## IDP Flow

```text
getMobileToken()  // establishes session JWT on internal client
  → POST /mobile1api/v1/idptokenexchange (re-login payload)
  → AuthAccessTokenPOJO(accessToken, signingKey)
```

Mobile 1 PKCE path is separate: `AuthServerClient` obtains an OAuth access token first, then exchanges to mobile JWT via `/mobilememberidptoken`.

## Credential and Environment Configuration

| Source | Mobile 1 | Mobile 2 smoke (auth verification) |
|--------|----------|-----------------------------------|
| Plan ID | TestNG `branding` parameter | TestNG `branding` |
| Username / password | `user/<env>/<branding>.json` | `user/qc4/hawaii.json` (same schema as Mobile 1) |
| Base URL | `mobile-authentication-uri` in `qc4.properties` | Same |
| IDP OAuth | `authentication-uri`, `web-client-id` when `idpEnabled` | Not used in shared-auth smoke |
| Relaxed SSL | `setRelaxedSSL(true)` in tests | `MobileServerClient.configure(true)` after `configure(uri,...)` |

## Token Lifecycle

| Consumer | Lifecycle |
|----------|-----------|
| Mobile 1 `MobileHttpRestApiClient` | Token cached in client instance field until new client / configure |
| Nick `MobileServerClient` | Session JWT stored on internal `MobileHttpRestApiClient` after login |
| Mobile 2 smoke | One configured `MobileServerClient` per class; each test calls shared entry point |

## Mobile 2 Reuse Decision

- **Use** `core.auth.mobile.MobileServerClient` as the shared source of truth.
- **Add** `mobile2.util.MobileHttpRestApiClient` mirroring Mobile 1 for future Dashboard API tests.
- **Do not** duplicate token HTTP logic inside `unite-mobile2`.
- **Smoke proof:** `Mobile2SharedAuthSmokeTest` calls `getMobileToken()` and `getAccessToken()` directly.

## Auth Verification Decision (Release 0.9)

| Role | Decision |
|------|----------|
| `mobile-ms-auth-client` | **Removed** — redundant after Mobile 2 shared-auth smoke |
| Verification location | `unite-mobile2` — `Mobile2SharedAuthSmokeTest` (2 tests) |
| Implementation | Direct `MobileServerClient.getMobileToken()` / `getAccessToken()` — no duplicate token logic |
| Reporting | `mobile-ms-reporting` via TestNG listener |

## Open Questions

1. Should `MobileLoginPOJO` gain `rememberMe` / `deviceUuid` for parity with Postman MSC collection?
2. Should Mobile 2 Dashboard use NON_IDP JWT or IDP access token on QC4?

## Comparison Table

| Area | Nick Shared Implementation | Mobile 2 Decision |
|------|---------------------------|-------------------|
| Source module | `universal/jsonapi-auth` | Consume `jsonapi-auth` only |
| Entry class | `MobileServerClient` | `MobileServerClient` for smoke; wrapper client for APIs |
| NON_IDP | `getMobileToken()` | `getMobileToken()` |
| IDP exchange | `getAccessToken()` | `getAccessToken()` |
| JWT extraction | POJO `MobileSessionPOJO` | POJO via shared client |
| Access token | `AuthAccessTokenPOJO` | `AuthAccessTokenPOJO` |
| Signing key | On session / token POJO | Presence flag only in reports |
| Credentials | `configure(uri, branding, user, pass)` | User JSON file (Mobile 1 convention) |
| App version | `3.9.0` in shared HTTP client | Shared client default |
| Reporting | None in jsonapi-auth | `mobile-ms-reporting` portal |
| Dashboard APIs | N/A | Deferred |

## Mobile 1 vs Mobile 2 Comparison

| Area | Mobile 1 | Mobile 2 | Aligned? | Difference needed? |
|------|----------|----------|----------|-------------------|
| Shared auth entry | `MobileServerClient` via `mobile1.util.MobileHttpRestApiClient` | `MobileServerClient` direct in smoke; same wrapper for future APIs | Yes | Smoke calls shared entry points directly — no token duplication |
| NON_IDP | `getMobileToken()` in `setDefaultHeaders` | `getMobileToken()` in smoke test | Yes | — |
| IDP access token | PKCE path when `idpEnabled`; else same NON_IDP | `getAccessToken()` in smoke test | Yes | Smoke proves Nick's IDP exchange path |
| HTTP helper | `mobile1.util.MobileHttpRestApiClient` | **None** — removed duplicate wrapper | Yes | Future Dashboard: add wrapper in Mobile 2 only when needed, or mirror Mobile 1 pattern locally |
| Default headers | Lazy token in `setDefaultHeaders` + DB `X-App-Version` | Not used in auth smoke | Yes | Auth smoke uses `MobileServerClient` directly |
| Environment props | Unpacked `qc4.properties` via framework | Same | Yes | — |
| Branding / planId | TestNG `branding` parameter | Same | Yes | — |
| User JSON | `user/qc4/hawaii.json`, `nmdirect.json` | `user/qc4/hawaii.json` | Yes | Mobile 2 uses QC4 hawaii only for smoke |
| Bootstrap suite | `bootstrap-testng.xml` | **Removed** — auth smoke only | Yes | Mobile 2 past skeleton phase |
| Maven profile | `mobile-ms-bootstrap` | `mobile-ms-auth-smoke` / `acceptance-qc4` → auth smoke | Yes | No bootstrap profile |
| Reporting | Not wired yet | `mobile-ms-reporting` listener | Partial | Mobile 1 can adopt same listener when API tests land |
| Masked diagnostics | Framework logging | `SensitiveDataSanitizer` + report metadata | Yes | — |

## JSON Test-User Comparison

| File | Environment | Schema match | QA-only account | Token stored? | Secret risk | Decision |
|------|-------------|--------------|-----------------|---------------|-------------|----------|
| `unite-mobile1/.../user/qc4/hawaii.json` | QC4 | Reference | Yes (synthetic automation) | No | Low — test credentials only | Keep |
| `unite-mobile2/.../user/qc4/hawaii.json` | QC4 | Identical structure to Mobile 1 | Yes | No | Low — same pattern as Mobile 1 | Keep |

Fields: `idpEnabled`, `users[].id`, `username`, `password`, `data.account` only. No JWT, access token, signing key, or client secret fields.

## Cleanup Summary

| Module | Before (tracked) | After (tracked) | Removed | Reason |
|--------|------------------|-----------------|---------|--------|
| `mobile-ms-auth-client` | 13 | 0 | 13 (module removed) | Redundant — verification moved to Mobile 2 |
| `mobile-ms-reporting` | 10 | 10 | 0 | Single reporting source |
| `unite-mobile2` | 12 | 7 | 5 | Removed duplicate client wrapper + bootstrap scaffolding |

**Tracked files removed:**

- `mobilems/auth/reporting/*` (5 Java classes) — duplicate of `mobilems/reporting/*`
- `src/test/resources/reporting/portal/assets/*` (3 files) — duplicate of reporting module assets

**Local generated clutter removed (not tracked, gitignored):**

- `assembly/`, `docs/`, `logs/`, `samples/`, `lombok.config`
- `src/main/resources/security/`, `src/main/resources/sql/`, `src/test/resources/config/`
- Obsolete untracked POJOs and JSON fixtures (already absent or removed by `mvn clean`)

## Final Lightweight Tree

```text
mobile-microservices/
├── mobile-ms-reporting/       # reusable Extent + static portal (6 Java + assets)
├── unite-mobile1/             # Nick shared-auth wrapper + bootstrap
├── unite-mobile2/             # shared-auth verification only (7 tracked files)
└── unite-enrollment/          # enrollment pilot skeleton
```

## Client Layer Comparison (Nick review)

| Class | Module | Purpose | Unique logic? | Duplicate? | Referenced by | Decision |
|-------|--------|---------|---------------|------------|---------------|----------|
| `MobileServerClient` | `jsonapi-auth` | Shared auth entry (`getMobileToken`, `getAccessToken`) | Yes — Nick's implementation | No | Mobile 1 wrapper, Mobile 2 smoke | **Keep** — source of truth |
| `core.auth.mobile.util.MobileHttpRestApiClient` | `jsonapi-auth` | Low-level login/exchange HTTP for `MobileServerClient` | Yes | No | `MobileServerClient` only | **Keep** |
| `mobile1.util.MobileHttpRestApiClient` | `unite-mobile1` | Lazy bearer + PKCE + `X-App-Version` for API tests | Yes — endpoint test harness | No | `MobileBaseRequestTest` | **Keep** in Mobile 1 |
| `mobile2.util.MobileHttpRestApiClient` | ~~unite-mobile2~~ | Copy of Mobile 1 wrapper | No | **Yes** | Nothing after smoke refactor | **Removed** |

**Dependency direction:** `unite-mobile1` → `jsonapi-auth`, `unite-mobile2` → `jsonapi-auth`. **No** `unite-mobile2` → `unite-mobile1` dependency. Mobile 1 is a test module, not a shared library.

**Version management:** `jsonapi-core` and `jsonapi-auth` versions cascade from `jsonapi/jsonapi-parent` `dependencyManagement`. `jsonapi-mobile-ms-reporting` and `extentreports` are managed in `mobile-microservices/pom.xml` (`${project.version}` / `${extentreports.version}`) — consuming modules declare dependencies without explicit versions.

## Bootstrap Cleanup

| File | Removed? | Reason |
|------|----------|--------|
| `testsuites/bootstrap-testng.xml` | Yes | Skeleton phase complete |
| `Mobile2BootstrapTest.java` | Yes | Replaced by auth smoke |
| `BootstrapSamplePOJO.java` | Yes | Bootstrap-only |
| `bootstrap-sample.json` | Yes | Bootstrap-only |
| `mobile-ms-bootstrap` Maven profile | Yes | No bootstrap suite |
| `acceptance-stage1` profile | Yes | Pointed at removed bootstrap suite |
| `acceptance-qc4` profile | Retained | Now runs `auth-smoke-testng.xml` |

## Reporting Promotion Readiness

| Class | Responsibility | Referenced by | Required? | Mobile-specific hardcoding? | Portable later? |
|-------|----------------|---------------|-----------|----------------------------|-----------------|
| `MobileMsHtmlReportListener` | Extent + portal lifecycle | unite-mobile2 TestNG | Yes | Module/env via system properties | Yes |
| `SensitiveDataSanitizer` | Mask tokens/secrets in HTML | Listener, tests | Yes | None | Yes |
| `MobileMsReportCaseRegistry` | Optional business metadata | Mobile 2 report cases | Yes | None — register per module | Yes |
| `MobileMsReportPortalGenerator` | Static HTML pages | Listener `onFinish` | Yes | About text mentions auth flows (cosmetic) | Yes — minor text tweak |
| `MobileMsReportRunSummary` | Run aggregates | Listener, generator | Yes | Defaults only | Yes |
| `MobileMsReportTestResult` | Sanitized test row | Listener, generator | Yes | None | Yes |

**Promotion answer:** Yes — `mobile-ms-reporting` can move into broader `jsonapi` reporting support later with a **small additive move**:

- Package rename: `mobilems.reporting` → e.g. `core.reporting.mobile` (TBD)
- Maven: `jsonapi-mobile-ms-reporting` → `jsonapi-reporting-support` (TBD)
- Consumers: update dependency + import paths only; listener registration unchanged
- **Not a rewrite** — portal assets, JSON history manifest, and sanitization stay as-is
- **Deferred:** GitLab Pages, nightly archive jobs, jsonapi-core promotion review (ADR-028)

## Exact Maven Commands

| Purpose | Command |
|---------|---------|
| Reporting install (direct child runs) | `mvn -f mobile-microservices/mobile-ms-reporting/pom.xml clean install -DskipTests` |
| Parent reactor | `mvn -f mobile-microservices/pom.xml clean install -DskipTests` |
| Mobile 2 shared-auth smoke | `mvn -f mobile-microservices/unite-mobile2/pom.xml clean test "-Pacceptance-qc4,mobile-ms-auth-smoke" "-Denvironment.properties=qc4.properties" "-Dmobile.auth.diagnostics=true"` |
| Mobile 1 bootstrap | `mvn -f mobile-microservices/unite-mobile1/pom.xml clean test "-Pacceptance-qc4,mobile-ms-bootstrap" "-Denvironment.properties=qc4.properties"` |

## Local Report Paths

| Module | Path |
|--------|------|
| Mobile 2 shared-auth | `mobile-microservices/unite-mobile2/target/mobile-ms-report/index.html` |

Open directly in a browser — no local server required.
