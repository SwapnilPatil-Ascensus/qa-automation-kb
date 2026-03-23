# Smoke Test Suites – CAT / Stage 5 / Stage 2 (Prime V2)

Purpose: Quick-validation suites for partner testing environments (CAT/Stage 5) and Stage 2 before functional testing begins. Separate from main nightly regression.

## Suites

| Suite XML | Suite Name | Env | Active Tests | Notes |
|-----------|------------|-----|-------------|-------|
| stage5-enrollments.xml | Regression Test Suite - Enrollments | Stage 5 | 4 (most commented out) | MI Direct CSR, NYA Advisor CSR, COA/AKA Advisor CSR |
| stage5-contributions.xml | Regression Test Suite - Contributions | Stage 5 | 2 | NYD/NYA CSR Member Single Contribution |
| stage5-acct-overview.xml | Regression Test Suite - Account Balance Page | Stage 5 | 6 | NJ/NM/NY/RI Direct, AK Able, NY Advisor |
| stage5-web-login.xml | Regression Test Suite - Legacy Web Registration | Stage 5 | 4 | MID/RIB Login, Forgot Username, Forgot Password |
| stage5-web-registration.xml | Regression Test Suite - Legacy Web Registration | Stage 5 | 4 | CAD/COB Registration, First Time Account |
| stage5-csr-acct-maintenance.xml | Regression Test Suite - Account or Profile Maintenance | Stage 5 | 3 (most commented) | NY Able, NY Advisor Personal Info |
| stage2-fromtoffice-smoke.xml | Smoke Test in Stage 2 (Front Office) | Stage 2 | 27 | Balance, Profile, Enrollment, Contributions, Withdrawals, Registration, Login |
| localstage2smoke.xml | Smoke Test in Stage 2 (Front Office) | Stage 2 | 45+ | Broad coverage (all modules) |
| unitefeedwts11.xml (smoke) | Unitefeedwts11 Smoke Test | — | 3 | NextGen Enrollment Smoke MID, NYB Contribution, WID Contribution |
| feedprocs21.xml | Smoke Test in Stage 2 | Stage 2 | Same as localstage2smoke | Duplicate |

**Notes:** Stage 5 suites use CAT / Stage 5 DB. Many tests are commented out (reduced scope for smoke). Not in original Confluence documentation.

**XML location:** `suites/v2/smoke/`
