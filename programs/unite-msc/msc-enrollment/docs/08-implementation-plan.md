# Implementation Plan

Phased plan to move from Postman manual testing to automated TestNG in `api-test-automation/mobile/enrollment`.

---

## Phase 0 — Postman E2E (current)

**Goal:** One person can complete enrollment on Stage1 using Postman.

| Task | Owner | Status |
|------|-------|--------|
| Restructure `msc-enrollment` folder | QA | Done |
| Document all endpoints & workflow | QA | Done |
| Plain payload templates per step | QA | Done |
| Stage1 Postman collection (13 steps) | QA | Done |
| EncryptHelper CLI workflow documented | QA | Done |
| Run happy path on Stage1, capture evidence | Dinesh / QA | Pending |
| Verify account in DB post-submit | QA | Pending |

**Exit criteria:** ENR-001 passes manually on Stage1 with encrypted payloads.

---

## Phase 1 — Test data utility & config

**Goal:** Reproducible unique data generation.

| Task | Location | Details |
|------|----------|---------|
| Add `enrollment-uri` property | `stage1.properties`, `qc4.properties` | `https://unite-bff-cloud.stage1.unite529.com` |
| Create `EnrollmentTestDataBuilder` | `mobile/enrollment/src/main/java/` | Username, email, SSN, usernameHash |
| Add `enrollment.sql` | `src/test/resources/sql/` | Post-submit account lookup by username |
| Add `allocation-fund-lookup.sql` | `src/test/resources/sql/` | Pre-run: active `FUND_ID` for branding (`TU_TRAUNCH` + `TU_TRAUNCH_FUND`) — see [11-allocation-fund-sql.md](11-allocation-fund-sql.md) |
| `EnrollmentTestDataBuilder.getFundId(branding)` | Java utility | Calls allocation SQL; sets fund for steps 12 & 13 |
| Port `get.mobile.min.version` | Already in `mobile.sql` | For x-app-version header |

**Exit criteria:** Builder generates valid unique data; SQL finds created account; **SQL resolves active `fundId` for plan branding**.

---

## Phase 2 — HTTP client & POJOs

**Goal:** Encrypted API calls from Java.

| Task | Details |
|------|---------|
| `EnrollmentBaseRequestTest` | Extends `BaseRequestTest`; calls `configureMobileEncryption(enrollmentUri, ENROLLMENT)` |
| `EnrollmentHttpRestApiClient` | Prospect JWT header, JSON array bodies, relaxed SSL |
| POJOs | `ProspectEnrollmentPOJO`, `OwnerPOJO`, `BeneficiaryPOJO`, `BankPOJO`, `AllocationPOJO` extending `BaseMobilePOJO` |
| JSON fixtures | `src/test/resources/json/enrollment/` per step |

**Pattern to follow:** `mobile1/MobileBaseRequestTest.java`

**Exit criteria:** Java can call GET plans + POST prospects with encryption.

---

## Phase 3 — First automated test (smoke)

**Goal:** ENR-001 in TestNG.

| Test | Steps | Assertions |
|------|-------|------------|
| `EnrollmentSmokeGetTest` | ping, plans, plan-by-id | HTTP 200 |
| `EnrollmentHappyPathTest` | prospects + review-confirm (shortcut) | 200, empty errors, JWT, account SQL |

TestNG suite: `testsuites/smoke-testng.xml`

**Exit criteria:** `mvn test -Pacceptance-stage1` green for smoke suite.

---

## Phase 4 — Full wizard & negatives

| Test | Coverage |
|------|----------|
| `EnrollmentFullWizardTest` | All 13 steps |
| `EnrollmentDuplicateUsernameTest` | ENR-003 |
| `EnrollmentInvalidRoutingTest` | ENR-004 |

Add to `regression-testng.xml`.

---

## Phase 5 — CI & multi-plan

| Task | Details |
|------|---------|
| Jenkins job for Stage1 enrollment smoke | Nightly |
| Add `okdirect` plan variant | Plan-specific host |
| QC4 enablement | After Stage1 stable 2+ weeks |

---

## Effort estimate

| Phase | Effort | Dependency |
|-------|--------|------------|
| 0 Postman | 2–3 days | EncryptHelper access |
| 1 Test data | 1–2 days | Phase 0 |
| 2 Client/POJOs | 3–5 days | jsonapi-encryption familiarity |
| 3 Smoke test | 2–3 days | Phase 2 |
| 4 Full regression | 3–5 days | Phase 3 |
| 5 CI/multi-plan | 2–3 days | Phase 4 |

**Total:** ~3–4 weeks for one engineer.

---

## Risks & mitigations

| Risk | Mitigation |
|------|------------|
| Encryption complexity | Use `EncryptHelper` / `BaseMobilePOJO` — avoid custom crypto |
| QC4 instability | Stage1-first per team decision |
| SSN collisions | Builder with date+random; optional DB pre-check |
| Host confusion (wtn vs cloud) | Separate `enrollment-uri` config property |
| Event chaining complexity | Shortcut path: prospect + review-confirm only |

---

## Definition of done (automation)

- [ ] Smoke suite passes on Stage1 nightly
- [ ] Creates `QAAUTOTEST_ENR_*` account findable by mobile1 SQL
- [ ] No SQL assertions during wizard (only post-submit)
- [ ] Encrypted payloads via framework (not Postman scripts)
- [ ] README in `mobile/enrollment` documents how to run
