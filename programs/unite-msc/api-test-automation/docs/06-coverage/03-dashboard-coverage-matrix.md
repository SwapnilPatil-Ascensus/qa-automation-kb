# Dashboard Coverage Matrix

**Current test:** `mobile2.dashboard.MobileDashboardRequestTest#getMobileDashboard`  
**Fixture:** user id `1`, branding `hawaii`, `idpEnabled: false`  
**Endpoint:** `GET /mobile2api/v1/mobiledashboard`

## Current Coverage (lean baseline)

| Check | Asserted? | Notes |
|-------|-----------|-------|
| HTTP 200 | Yes | |
| HAL `_embedded.item` present | Yes | |
| `ownerFirstName` non-blank | Yes | Contract |
| `ownerLastName` non-blank | Yes | Business |
| `totalBalance` present, ≥ 0 | Yes | Coherence — not sum-of-accounts |
| `asOfDate` non-blank | Yes | Contract |
| `mobileAccounts` non-empty | Yes | |
| First account `acctBalance` ≥ 0 | Yes | Minimal account sanity |
| SQL / DB cross-check | No | TODO in test — **future scope** |
| POJO full compare (`assertThat`) | No | Field-level asserts only |

## Intentionally Deferred (old 8-test regression)

| Old scenario | Why deferred | Dependency |
|--------------|--------------|------------|
| Secondary fixture (`user id 2`) | Lean baseline uses primary only | Fixture approval / multi-user need |
| Beneficiary names on accounts | Legacy `assertBeneficiaryNamesOnHawaiiAccounts` | API + fixture data |
| Structural fields per account | prefix, ext, regType, traunchId, acctState, etc. | Product sign-off on required fields |
| `totalBalance` sum coherence | Exact arithmetic vs accounts | May need SQL-backed expected values |
| `planId` present | Legacy assertion | Confirm still required in API contract |
| `mobileUgifts` array + nested validity | Legacy ugift checks | API availability on Hawaii QC4 |
| `displayInStackup` flag | Legacy stackup intent | Product confirmation |

## Out of Scope (not Dashboard baseline)

| Scenario | Classification |
|----------|----------------|
| Invalid username/password → 401 | Auth-owned negative |
| Dashboard GET without Authorization → 401 | Auth-owned negative |
| Malformed bearer → 500 | Auth-owned negative |
| NM Direct Dashboard | Future NM Direct / IDP |
| IDP / PKCE login path | Future NM Direct / IDP |

## SQL-Backed Next Checks (future)

When dev provides SQL / source mapping:

| Candidate check | Data needed |
|-----------------|-------------|
| Account balance vs DB | Query + account keys from fixture |
| Owner name vs DB | Member / account join |
| `totalBalance` vs sum of accounts | Aggregation rule from service team |
| Beneficiary names vs DB | Beneficiary table mapping |
| `asOfDate` freshness | Pricing / valuation timestamp source |

## Suite Inventory

| Suite XML | Profile | Tests | Class |
|-----------|---------|-------|-------|
| `dashboard-integration-testng.xml` | `mobile-ms-integration` | 1 | `MobileDashboardRequestTest` |
| `dashboard-regression-testng.xml` | `mobile-ms-dashboard-regression` | 1 | `MobileDashboardRequestTest` |

Same test method runs in both suites; suite name drives report category and portal subtitle.
