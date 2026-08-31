# Enrollment API — Automation Coverage Status

**Generated:** 2026-08-28  
**Source of truth:** `Enrollment End Points.xlsx` (tab: API Endpoints - Enrollment)  
**Repo:** `api-test-automation/mobile/enrollment`  
**Matrix Excel:** [Enrollment-Automation-Coverage-Matrix.xlsx](./Enrollment-Automation-Coverage-Matrix.xlsx)

---

## Summary

| Metric | Count |
|--------|-------|
| Total endpoints in catalog | **25** |
| **Java automated (Done)** | **19** (76%) |
| Core E2E wizard + submit | **14/15** (93%) |
| Not started (in scope) | **1** |
| Deferred (out of scope) | **5** |

**Blocking gap:** `review-confirm-entered` — Postman passes; **no Java test class yet** → no automated account creation.

---

## Legend

| Automation Status | Meaning |
|-------------------|---------|
| **Done** | TestNG class exists in `mobile/enrollment` |
| **Not Started** | In scope for current sprint; no Java class |
| **Deferred** | Out of scope — subsequent/partner/OAuth; next sprint research |

| Program Scope | Meaning |
|---------------|---------|
| In Scope | Required for MSC E2E happy path |
| In Scope (optional) | In Postman flow; can skip (mobile login, AIP, allocation funds GET) |
| Out of Scope (deferred) | Not targeting this sprint |

| Legacy / Migration | Meaning |
|--------------------|---------|
| Migrated from legacy | Was in old Cucumber/Postman collection (marked Done) |
| New in MSC | Added in new TestNG framework; not in legacy collection |
| Legacy existed — MSC ahead | Old collection still "In Progress" but Java is Done |

---

## Done — Java automated (19 endpoints)

| # | Endpoint | Test Class | Suites | Legacy note |
|---|----------|------------|--------|-------------|
| 1 | `/enrollmentapi/health/liveness` | `EnrollmentPingRequestTest` | smoke | Not in legacy Cucumber; added in MSC TestNG smoke |
| 2 | `/enrollmentapi/v1/ping` | `EnrollmentPingRequestTest` | smoke | Migrated from legacy; old collection marked Done |
| 3 | `/enrollmentapi/v1/certificate` | `EnrollmentCertificateRequestTest` | smoke | New in MSC automation (encryption setup) |
| 4 | `/enrollmentapi/v1/usstates` | `EnrollmentUsStatesRequestTest` | smoke | New in MSC automation |
| 5 | `/enrollmentapi/v1/country` | `EnrollmentCountryRequestTest` | smoke | New in MSC automation |
| 6 | `/enrollmentapi/v1/plans` | `EnrollmentPlansRequestTest` | smoke | Migrated from legacy; old collection marked Done |
| 7 | `/enrollmentapi/v1/plans/{planId}` | `EnrollmentPlansRequestTest` | smoke | Migrated from legacy; old collection marked Done |
| 8 | `/enrollmentapi/v1/content?branding={planId}&language=en` | `EnrollmentContentRequestTest` | regression, integration | New in MSC automation (not in legacy collection) |
| 9 | `/mobile1api/v1/mobilemembersession` | `MobileMemberSessionRequestTest` | smoke; regression (okdirect only) | New — cross-API (Mobile1); optional Postman step |
| 10 | `/enrollmentapi/v1/enrollments/enrollmentstarted` | `EnrollmentStartedRequestTest` | regression, integration | New in MSC automation; web account-owner UI only |
| 11 | `/enrollmentapi/v1/enrollments/prospects` | `ProspectRequestTest` | regression, integration | Migrated from legacy; old collection marked Done |
| 12 | `/enrollmentapi/v1/enrollments/enrollment/owner-entered` | `OwnerEnteredTests` | regression, integration | Migrated from legacy; old collection marked Done |
| 13 | `/enrollmentapi/v1/enrollments/enrollment/owner-address-` | `OwnerAddressEnteredRequestTest` | regression, integration | New in MSC automation (not listed in old collectio |
| 14 | `/enrollmentapi/v1/enrollments/enrollment/beneficiary-en` | `BeneficiaryEnteredTests` | regression, integration | Migrated from legacy; old collection marked Done |
| 15 | `/enrollmentapi/v1/verify/routingnumber` | `VerifyBankRoutingNumberRequestTest` | regression, integration | MSC automation done; old collection still marked I |
| 16 | `/enrollmentapi/v1/enrollments/enrollment/bank-entered` | `BankEnteredRequestTests` | regression, integration | Migrated from legacy; old collection marked Done |
| 17 | `/enrollmentapi/v1/enrollments/enrollment/recurring-cont` | `RecurringContributionEnteredRequestTest` | regression, integration | New in MSC automation; optional skip in Postman |
| 18 | `/enrollmentapi/v1/enrollmentallocationfunds/get` | `AllocationFundRequestTest` | regression, integration | New in MSC automation; alternative to SQL fund loo |
| 19 | `/enrollmentapi/v1/enrollments/enrollment/allocations-en` | `AllocationsEnteredRequestTests` | regression, integration | MSC automation done; old collection marked In Prog |

---

## Not started — in scope

| # | Endpoint | Remaining work |
|---|----------|----------------|
| 20 | `/enrollmentapi/v1/enrollments/enrollment/review-confirm-entered` | CODE GAP — blocks account creation; QA-1604 / QA-1810 |

---

## Deferred — out of scope (next sprint / research)

| # | Endpoint | Postman | Reason |
|---|----------|---------|--------|
| 21 | `/enrollmentapi/v1/subsequentenrollment/banks` | Not Working - 401 | QA-1792 — subsequent enrollment research |
| 22 | `/enrollmentapi/v1/enrollments/subsequentenrollment` | Not Working - 401 | QA-1791 — subsequent enrollment research |
| 23 | `/enrollmentapi/v1/enrollments/submit` | Not Working - 401 | QA-1808 — partner integration research |
| 24 | `/enrollmentapi/v1/upromiseaccount` | Authorization Failed | QA-1807 |
| 25 | `/enrollmentapi/v1/oauth/token` | Not Working - 401 | Not planned for MSC E2E |

---

## TestNG suite wiring

| Suite | What runs |
|-------|-----------|
| `enrollment-smoke-testng.xml` | Bootstrap GETs + optional mobile login |
| `enrollment-regression-testng.xml` | Full wizard (prospect → allocations); **no submit yet** |
| `enrollment-integration-testng.xml` | Same as regression on QC4 |

**Note:** No single suite runs prospect → **submit** end-to-end until `ReviewConfirmEnteredRequestTest` is added.

---

## New in MSC vs migrated from legacy

### Migrated from legacy (old collection marked Done)

- `/enrollmentapi/v1/ping` → `EnrollmentPingRequestTest`
- `/enrollmentapi/v1/plans` → `EnrollmentPlansRequestTest`
- `/enrollmentapi/v1/plans/{planId}` → `EnrollmentPlansRequestTest`
- `/enrollmentapi/v1/enrollments/prospects` → `ProspectRequestTest`
- `/enrollmentapi/v1/enrollments/enrollment/owner-entered` → `OwnerEnteredTests`
- `/enrollmentapi/v1/enrollments/enrollment/beneficiary-entered` → `BeneficiaryEnteredTests`
- `/enrollmentapi/v1/enrollments/enrollment/bank-entered` → `BankEnteredRequestTests`

### New in MSC automation (not in legacy collection)

- `/enrollmentapi/health/liveness` → `EnrollmentPingRequestTest`
- `/enrollmentapi/v1/certificate` → `EnrollmentCertificateRequestTest`
- `/enrollmentapi/v1/usstates` → `EnrollmentUsStatesRequestTest`
- `/enrollmentapi/v1/country` → `EnrollmentCountryRequestTest`
- `/enrollmentapi/v1/content?branding={planId}&language=en&name=enrollment` → `EnrollmentContentRequestTest`
- `/mobile1api/v1/mobilemembersession` → `MobileMemberSessionRequestTest`
- `/enrollmentapi/v1/enrollments/enrollmentstarted` → `EnrollmentStartedRequestTest`
- `/enrollmentapi/v1/enrollments/enrollment/owner-address-entered` → `OwnerAddressEnteredRequestTest`
- `/enrollmentapi/v1/enrollments/enrollment/recurring-contribution-entered` → `RecurringContributionEnteredRequestTest`
- `/enrollmentapi/v1/enrollmentallocationfunds/get` → `AllocationFundRequestTest`

---

## Regenerate

```powershell
cd programs/unite-msc/api-test-automation/postman/EnrollmentE2E/tools
python generate_enrollment_coverage_matrix.py
```
