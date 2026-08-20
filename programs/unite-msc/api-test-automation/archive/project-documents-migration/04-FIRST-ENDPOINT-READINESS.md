> **Historical readiness** — enrollment-focused. Dashboard baseline is validated under `mobile/mobile2/` per `00-CURRENT-STATUS.md`.

# Unite Enrollment — First Endpoint Readiness

## Selected Endpoint

**GET `/enrollmentapi/v1/plans`**

## Why This Endpoint Was Selected

- Read-only; no encrypted enrollment event body.
- Primary legacy scenario: `GET Plans for mobile enrollment` in `planselection.feature`.
- Lowest-risk Wave 1 item in `03-LEGACY-DISCOVERY-SUMMARY.md`.
- Pilot QC4 blocker is routing (404 on BFF); confirming this GET returns **200** unblocks `TODO-AUTO-01`.
- Plan-by-id GET is a follow-on (`/plans/{id}`) after list GET is stable.

## Legacy Source Assets

| Asset | Path | Purpose |
|-------|------|---------|
| Feature | `src/test/resources/features/planselection.feature` | Scenarios `@getPlansSelectionEnrollment`, `@getPlanSelectionEnrollment`, `@getplanSelectionEnrollmentAppVersion` |
| Step definitions | `src/test/java/enrollment/PlanSelectionStepdefs.java` | HTTP GET, status assert, HAL parse, metadata asserts |
| Domain model | `src/main/java/com/cs529/enrollment/domain/EnrollmentPlan.java` | Response field model (application coupling — do not import in centralized pilot) |
| Resource (app) | `src/main/java/com/cs529/enrollment/resource/PlanSelectionResource.java` | Service route reference (read-only context) |
| Shared HTTP helper | `com.cs529.library.resource.HttpSupport` | `jwtCollaboratorTestRequest` for list GET |
| Properties | `com.cs529.library.resource.Properties.ENROLLMENT_SERVICE_URL` | JVM base URL (not BFF by default) |
| JSON helper | `com.cs529.library.resource.JsonUtil` | `_embedded.item` → `EnrollmentPlan[]` |
| World state | `enrollment/EnrollmentWorld.java` | Stores plans between When/Then steps |

## URL Construction

| Component | Legacy Source | Postman Source (local-reference / prior audit) | Confirmed? | Notes |
|-----------|---------------|-----------------------------------------------|------------|--------|
| Base URL | `System.getProperty(Properties.ENROLLMENT_SERVICE_URL)` | `{{mobileMsc.host.url}}` (maps to unpacked `mobile-authentication-uri` in unite `qc4.properties`) | **No** | Legacy uses **direct enrollment service** JVM property; Postman MSC uses **BFF host** — root cause of QC4 404 investigation |
| Path prefix | `enrollmentEndPoint = ENROLLMENT_SERVICE_URL + "/enrollmentapi/v1/"` | Same path segment under host variable | **Partial** | Path shape agreed; host is not |
| List resource | `GET enrollmentEndPoint + "plans"` → `/enrollmentapi/v1/plans` | Expected relative path `/enrollmentapi/v1/plans` on MSC host (verify in local Postman when folder restored) | **No** | Must return 200 on developer-confirmed host |
| Query parameters | None on list GET | None observed for list (verify in Postman) | **Partial** | Legacy list call has no query map |
| Path parameters | N/A for list | N/A | Yes | By-id uses `/plans/{id}` (out of scope for first smoke) |
| Framework property (today) | N/A in legacy centralized model | `mobile-authentication-uri` only in `jsonapi-lib` unite `qc4.properties` | **No** | **No `enrollment-service-uri`** (or equivalent) in framework config yet (`TODO-QC4-01`, `T-006`) |

## Authentication

| Question | Legacy Finding | Postman Finding | Developer Confirmation Needed |
|----------|----------------|-----------------|------------------------------|
| Auth mode for list GET | `HttpSupport.jwtCollaboratorTestRequest(scenario)` before GET | MSC flow: Mobile1 **Member Session** → bearer `{{mobileMsc.jwt}}` (per pilot audit) | Is collaborator JWT equivalent to Postman mobile session JWT for enrollment? |
| Server OAuth | Not used for list GET in legacy | Universal auth collections exist under tracked `postman/` (separate flow) | Confirm enrollment does **not** require IDP PKCE for read-only plans |
| IDP exchange | Not in `PlanSelectionStepdefs` list GET | Tracked `postman/mobile/` documents IDP ↔ mobile token exchange | Required for GET plans on QC4? (`TODO-QC4-02`) |
| Certificate / mTLS | Via shared `HttpSupport` / RestAssured setup | Not documented in readiness pass | Match environment TLS expectations |

## Required Headers

| Header | Required? | Source | Notes |
|--------|-------------|--------|-------|
| `Authorization: Bearer <jwt>` | **Yes** (legacy list GET) | `jwtCollaboratorTestRequest` | Token acquisition TBD in centralized framework (`TODO-QC4-02`) |
| `X-App-Version` | **No** for list GET in legacy | Plan-by-id uses `1.5.0`; wrong version scenario expects **426** | Confirm with Luis whether BFF/list requires app version (`TODO-QC4-02`) |
| `Content-Type` | N/A (GET, no body) | — | — |
| Custom gateway headers | Unknown | Postman / BFF SME | Any API gateway or branding headers? |

## Request Details

| Item | Value or Finding |
|------|------------------|
| HTTP method | GET |
| Relative path | `/enrollmentapi/v1/plans` |
| Request body | None |
| Legacy scenario name | `GET Plans for mobile enrollment` |
| Tags | `@integration @planselection @getPlansSelectionEnrollment` |

## Expected Response

| Validation | Expected Behavior | Source |
|------------|-------------------|--------|
| Status code | **200** | `PlanSelectionStepdefs` `@When("GET Plans for mobile enrollment")` |
| Body shape | HAL-style collection; items under `_embedded.item` | `JsonUtil.getObject(response, JsonUtil.EMBEDDED_ITEM, EnrollmentPlan[].class)` |
| Field asserts (legacy) | Full datatable match on id, deprecatedId, description, mobileEnabled, colors, CSR phone, search terms, contrib mins, etc. | `planselection.feature` Then step + `BeanAssert.assertEqualList` |
| Plan metadata | Separate `@And` asserts `planMetadata` keys per traunch | Same feature |
| Wrong app version | **426** for GET by id with bad `x-app-version` | Separate scenario — not first smoke |

**Pilot smoke scope (proposed):** assert **200** + non-empty body + minimal structural check (e.g. `_embedded` or array present). **Defer** full datatable parity and DB-seeded plan rows until data strategy agreed.

## POJO Strategy

| POJO | Reuse Existing? | Create Endpoint-Specific? | Notes |
|------|-----------------|---------------------------|-------|
| `com.cs529.enrollment.domain.EnrollmentPlan` | **No** | — | Application domain; violates lightweight decoupling |
| `BootstrapSamplePOJO` | N/A | — | Bootstrap only |
| `EnrollmentPlanPOJO` (proposed) | — | **Yes** (minimal fields) | Under `enrollment.core.pojo` or `enrollment.plans.pojo` — id, deprecatedId, description, productName, mobileEnabled, primaryColor, secondaryColor only for smoke |
| HAL wrapper | — | Optional later | Only if `assertThat` needs typed `_embedded` |

## Schema Validation

- Legacy: **no** JSON Schema files; Cucumber datatables + `BeanAssert`.
- Centralized pilot: **defer** JSON Schema until official schema artifact and SME approval (`T-015`).

## SQL Validation

| Item | Legacy | Pilot recommendation |
|------|--------|----------------------|
| Background | `Given I delete Plans`, `And I create Plans`, `And I create Traunch Metadata` with large fixtures | **Defer** for first smoke — requires DB/Cassandra strategy |
| Assertions | Indirect — data seeded then compared to GET response | QC4 may use **existing environment data**; confirm with Luis |
| Centralized SQL | `sql/enrollment/README.md` placeholder | Add scripts only when write/read tests need DB |

## Shared JSON API Libraries to Reuse

| Capability | Existing Class or Path | Reuse Decision |
|------------|------------------------|----------------|
| Test base | `core.test.BaseRequestTest` | **Reuse** — same as `MobileMicroservicesBootstrapTest`, `GetAccountRequestTest` |
| HTTP client (Universal OAuth) | `core.auth.util.ServerHttpRestApiClient` | **Reuse pattern** only if SME confirms server OAuth; **not** legacy list auth |
| HTTP abstraction | `core.restassured.HttpRestApiClient` | **Extend** — new enrollment client only if needed (`enrollment.client`, `T-019`) |
| Response wrapper | `core.restassured.HttpRestApiClientResponse` | **Reuse** — `invokeRestApi`, `convertToPOJO` |
| REST constants | `constants.common.GeneralConstants.RestType`, `HTTP_STATUS_CODES` | **Reuse** |
| Assertions | `assertThat`, `assertEquals`, `assertNotNull` (TestNG static) | **Reuse** per workspace rules |
| JSON load | `loadJsonFile`, `loadJson` on `BaseRequestTest` | **Reuse** if fixture JSON added |
| Environment | `setupEnvironmentBeforeAll`, `getProperty`, `getProject()` → `unite` | **Reuse**; add property key after `TODO-QC4-01` |
| TestNG listener | `core.listener.JsonApiResourceManager` | **Reuse** (already in suite XML) |
| Auth module | `jsonapi-auth` / `AuthServerClient` | **Available**; mobile JWT adapter **not built** (MSC-001 backlog) |
| Config unpack | `jsonapi-lib` classifier `resources-unite` → `qc4.properties` | **Reuse** for hosts; **do not commit** unpacked files |

## Proposed Target Package

Lightweight structure (documentation only — **no Java created in this pass**):

```text
src/test/java/enrollment/plans/
├── GetPlansRequestTest.java    # proposed name; see NEXT-PROMPT alias GetEnrollmentPlansSmokeTest
└── pojo/                       # only if required — prefer enrollment.core.pojo
```

Optional (only if justified after QC4 auth decision):

```text
src/test/java/enrollment/client/
└── EnrollmentHttpRestApiClient.java   # extends HttpRestApiClient; sets base URI from property
```

## TestNG Suite Changes

| Suite | Change |
|-------|--------|
| `bootstrap-testng.xml` | **No change** — keep bootstrap-only |
| `smoke-testng.xml` | Add class `enrollment.plans.GetPlansRequestTest`; replace or supplement bootstrap-only group with smoke/API group per Nick pattern |
| `regression-testng.xml` | Same GET Plans class when smoke stable |

Maven profiles (unchanged): `-Pacceptance-qc4,mobile-ms-smoke` with `-Denvironment.properties=qc4.properties`.

## Luis / Developer Questions

1. QC4 **enrollment base URL**: BFF (`mobile-authentication-uri`) vs direct enrollment microservice URL?
2. Property key for automation config (e.g. `enrollment-service-uri`) and sample non-secret documentation?
3. Does **GET `/enrollmentapi/v1/plans`** return **200** on the confirmed host?
4. Auth: **mobilemembersession JWT** only, or IDP PKCE + exchange first?
5. Mandatory headers for enrollment GET (especially **`X-App-Version`**)?
6. Does QC4 need **SQL seeding** or is existing plan data sufficient for read-only GET?
7. Safe QC4 test account for later write flows (not needed for GET plans smoke).

See also: `05-LUIS-QC4-DISCUSSION-CHECKLIST.md`.

## Implementation Stop Conditions

- **Do not** add Java test classes until manual Postman GET plans returns **200** on developer-confirmed URL.
- **Do not** guess BFF vs direct host or weaken status assertions.
- **Do not** commit secrets, raw Postman JSON, or unpacked `config/*.properties`.
- **Do not** import `com.cs529.enrollment.domain.*` or copy Cucumber stepdefs wholesale.
- **Do not** modify `jsonapi-*`, `universal/`, pipelines, or tracked `postman/environments/*`.
- **Stop** if auth requires shared-core mobile JWT adapter — record backlog item and escalate before coding.

## Exact Next Step After QC4 Returns 200

1. Complete manual validation rows in `05-LUIS-QC4-DISCUSSION-CHECKLIST.md`.
2. Run implementation instructions in `NEXT-PROMPT-AFTER-QC4-404-FIX.md` (one smoke test only).
3. Record evidence in a future `04-FIRST-API-SMOKE-EVIDENCE.md` (not created until implementation pass).

---

*Local Postman note:* `local-reference/mobile-microservices/postman/` was **not present on disk** during this readiness pass (restore from secure store for manual QC4 validation). Findings above combine legacy source inspection with prior pilot Postman audit documented in `03-LEGACY-DISCOVERY-SUMMARY.md`.*
