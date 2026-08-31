# Mobile Microservices API Automation — Architecture Decisions

| ID | Decision | Reason |
|----|----------|--------|
| ADR-011 | Keep Enrollment skeleton but defer encrypted request migration | Payload encryption contract needs dev confirmation |
| ADR-012 | Use Mobile 2 Dashboard as first real vertical slice | Lowest-risk path to prove auth and execution |
| ADR-013 | Implement non-IDP auth before IDP token exchange | Reduce troubleshooting complexity |
| ADR-014 | Do not create shared mobile auth utility until both flows are proven | Avoid premature abstraction |
| ADR-015 | Use selective DB validation | Avoid brittle and slow over-validation |
| ADR-016 | Keep Mobile 1 and Mobile 2 skeletons minimal | Prevent empty framework clutter |
| ADR-017 | Implement an isolated reusable Mobile MS authentication client before Dashboard migration | Both token flows are confirmed manually in Postman and will be reused by multiple Mobile MSC modules |
| ADR-018 | Return immutable authentication sessions instead of storing tokens globally | Prevent parallel-test conflicts and reduce hidden state |
| ADR-019 | Keep credentials outside Git and log masked token diagnostics only | Protect secrets and keep the framework safe |
| ADR-020 | Simplify the token client to the minimum required classes for two authentication endpoints | Two POST calls do not need configuration wrappers, nine POJOs, or a separate HTTP client file |
| ADR-021 | Prefer JsonPath extraction for small auth responses; add DTOs only when they improve clarity | HAL responses expose three token fields; JsonPath is sufficient |
| ADR-022 | Add a minimal standalone HTML report inside the auth-client module | QA-friendly pass/fail view without CI or shared-module overhead |
| ADR-023 | Extract reporting into shared support only after a second consumer exists | Avoid premature `mobile-ms-test-support` abstraction |
| ADR-024 | Use Nick's `jsonapi-auth` (`MobileServerClient`) as the shared mobile authentication source of truth | INFI-8078 merged to `main`; Mobile 1 already delegates here |
| ADR-025 | ~~Keep `mobile-ms-auth-client`~~ **Superseded (0.9):** auth verification lives in `unite-mobile2` smoke only; standalone module removed | Eliminates duplicate maintenance; `jsonapi-auth` is sole token implementation |
| ADR-026 | Do not duplicate shared token logic inside Mobile 2 | `unite-mobile2` calls `MobileServerClient`; wrapper client mirrors Mobile 1 for downstream APIs |
| ADR-027 | Extract Extent reporting into `mobile-ms-reporting` for reuse across Mobile MSC modules | Auth client + Mobile 2 are first consumers |
| ADR-028 | Keep reporting inside Mobile Microservices until a broader framework promotion is reviewed | Do not move into `jsonapi-core` or `jsonapi-auth` yet |

## Module Scope (Release 0.8)

| Module | Status | Notes |
|--------|--------|-------|
| `mobile-ms-reporting` | **New** | Reusable Extent + static portal (`index.html`) |
| `unite-mobile2` | Auth verification + bootstrap | `Mobile2SharedAuthSmokeTest` (2 tests); no Dashboard yet |
| `unite-mobile1` | Reference | Nick's `MobileHttpRestApiClient` pattern on `main` |
| `universal/jsonapi-auth` | Shared library | `MobileServerClient` — do not fork |

## Module Scope (Release 0.7)

| Module | Status | Notes |
|--------|--------|-------|
| `mobile-ms-auth-client` | **Simplified** | 5 core classes + 2 reporting classes; ExtentReports Spark HTML; JsonPath extraction |

## Module Scope (Release 0.6)

| Module | Status | Notes |
|--------|--------|-------|
| `mobile-ms-auth-client` | **Implemented** | NON_IDP + IDP exchange, TestNG suite, `mobile-ms-auth-smoke` profile |
| `unite-mobile1` | Skeleton | Consumes auth client (planned) |
| `unite-mobile2` | Skeleton | Consumes auth client (planned) |
| `unite-enrollment` | Pilot | Consumes auth client when QC4 routing unblocked |

## Module Scope (Release 0.5)

| Module | Status | Bootstrap only | Notes |
|--------|--------|----------------|-------|
| `unite-enrollment` | Existing pilot | No — smoke/regression scaffolds present | API blocked on QC4 routing |
| `unite-mobile1` | Skeleton | Yes | No endpoint, auth, or encryption code |
| `unite-mobile2` | Skeleton | Yes | Dashboard slice planned after auth confirmation |
