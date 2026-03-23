# Release Gate Suites (Prime V2)

Purpose: Release-gate regression run before promoting code. Covers a subset of critical flows.

## Suites

| Suite XML | Suite Name | Env | Tests | Coverage |
|-----------|------------|-----|-------|----------|
| stage1-frontoffice.xml | Stage1 Regression (Front Office) - Release | Stage 1 | 8 | IAD/MID/NVU Enrollment, NYA/MTB Contribution, ILB Enrollment |
| stage2-frontoffice.xml | Stage2 Regression (Front Office) - Release | Stage 2 | 8 | Same as Stage 1 release |
| unitefeedwts11.xml (release) | Unitefeedwts11 Regression (Backoffice) - Release | — | 9 | Mellon ACH Credit/Returns/Check/ECC/EPay/Positive Pay/Price, Vanguard Price |

**XML location:** `suites/v2/release/`
