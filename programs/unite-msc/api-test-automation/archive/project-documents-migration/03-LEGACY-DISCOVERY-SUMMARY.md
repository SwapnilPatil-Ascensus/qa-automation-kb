> **Historical discovery** — legacy Cucumber/Postman findings. Canonical migration status: `10-LEGACY-TO-NEW-MIGRATION.md`.

# Unite Enrollment Legacy Discovery Summary

## Legacy Repo

`C:\Workspace\GitLab\MobileAutomation\UniteMSC\unite-enrollment` (read-only)

- Maven WAR, Cucumber 5.6, REST Assured via `HttpSupport`
- Tests in `src/test/java/enrollment/*Stepdefs.java`
- Features in `src/test/resources/features/` (13 files)

## Inventory

| Item | Count |
|------|-------|
| Scenarios (approx.) | **85** |
| Feature files | **13** |
| Step-definition classes | **14** |
| Distinct enrollment route patterns | **~12+** |
| Postman MSC requests (centralized local ref) | **13** |

## Legacy Design

- Cucumber + JUnit 4 (not TestNG)
- `EnrollmentWorld` shared state across steps
- Domain POJOs from `com.cs529.enrollment.domain.*` (application coupling)
- In-process mocks under `com.cs529.enrollment.service.mock.*`
- Encrypted payloads via `BeanUtils.setEncryptedProperties` + AES key steps
- Heavy SQL/Cassandra backgrounds in features

## Endpoint Inventory (patterns)

| Method | Path pattern | Legacy consumer |
|--------|--------------|-----------------|
| GET | `/enrollmentapi/v1/plans` | PlanSelectionStepdefs |
| GET | `/enrollmentapi/v1/plans/{id}` | PlanSelectionStepdefs |
| GET | `/enrollmentapi/v1/content` | ContentServiceStepdefs |
| POST | `/enrollmentapi/v1/enrollments/enrollment/{eventType}` | Bank, Owner, Beneficiary, ... |
| POST | `/enrollmentapi/v1/enrollments/enrollment/review-confirm-entered` | EnrollmentsStepdefs |
| POST | `/enrollmentapi/v1/enrollments/subsequentenrollment/review-confirm-entered` | SubSequentEnrollmentStepdefs |
| POST | `/enrollmentapi/v1/enrollments/submit` | VanguardStepdefs |

Base URL: `System.getProperty(Properties.ENROLLMENT_SERVICE_URL)` — **not** Postman BFF host by default.

## Auth Findings

- `HttpSupport.jwtCollaboratorTestRequest` — plan GET
- `HttpSupport.jwtAcceptanceTestRequest` — content GET
- Postman MSC: `mobilemembersession` → `mobileMsc.jwt` bearer
- Centralized framework: server OAuth via `jsonapi-auth`; mobile JWT adapter **not built**

## JSON / POJO Findings

- HAL-style `_embedded.item` parsing via `JsonUtil`
- Large Cucumber tables → encrypted fields
- Postman enrollment body: JSON array of event objects (encrypted)
- Centralized pilot: `BootstrapSamplePOJO` only; future POJOs under `enrollment.core.pojo`

## SQL Findings

- Feature backgrounds: delete/create Plans, Members, Cassandra snapshots, etc.
- Wave 1 read APIs should avoid heavy DB setup
- Centralized: use `sql/enrollment/*.sql` when needed; shared SQL unpacked at build

## Local Postman Reference (Git-ignored)

- Local Postman assets exist under `local-reference/mobile-microservices/postman/` (MSC collection, QC4 auth environments).
- QC4 environment assets exist for manual routing and auth checks.
- Files remain **local-only** (`local-reference/` in root `.gitignore`); raw values are intentionally excluded from Git.

## QC4 Findings

- Postman `mobileMsc.host.url` aligns with `mobile-authentication-uri` in unpacked qc4.properties
- No enrollment URI in framework config
- Postman env contains secrets locally only (never committed)

## 404 Investigation

| Request | POST `.../bank-entered` on BFF host |
| Response | 404 |
| Likely mismatch | BFF routing vs legacy `ENROLLMENT_SERVICE_URL` |

## Proposed Wave 1

| Order | Scenario | Endpoint | Method | Reason |
|-------|----------|----------|--------|--------|
| 1 | GET Plans | `/enrollmentapi/v1/plans` | GET | Read-only and lowest risk |
| 2 | Terms / Content | `/enrollmentapi/v1/content` | GET | Read-only content validation |
| 3 | Metadata Calendar | `/metadataapi/v2/calendar` | GET | BFF auth verification |
| 4 | Plan by ID | `/enrollmentapi/v1/plans/{id}` | GET | Parameterized validation |
| 5 | Bank Entered | `/enrollmentapi/v1/enrollments/enrollment/bank-entered` | POST | Only after route and auth clarification |

## Deferred Items

- Full `enrollment.feature` happy path (Wave 3)
- Vanguard / Upromise feature files
- Cucumber parity / parallel reports
- Pipeline integration
- Shared-core changes (MSC-001–004)

## SME Questions

See `00-CURRENT-STATUS.md` — Luis / Developer Questions section.
