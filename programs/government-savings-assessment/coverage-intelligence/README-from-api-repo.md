# Coverage Intelligence Assessment

**Assessment date:** 2026-07-20  
**Single source of truth:** `../government-savings-automation-assessment/03-analysis/verified-metrics-register.csv`

This module does **not** maintain independent percentages. Import metrics from the verified register after each validation session.

## Current authoritative metrics (snapshot)

| Metric ID | Value | Status |
|-----------|-------|--------|
| GS-M2-IMPL | 24/24 (100% in-scope) | Verified current |
| GS-M2-MASTER | 41 master regression executions | Verified current |
| GS-M2-EXEC-QC4 | 20/22 module profiles pass | Pending refresh |
| GS-M1-IMPL | 6 endpoints (no denominator) | Verified implemented |
| GS-UNIV-META | Scheduled Stage1 job | Verified scheduled |

## Refresh procedure

1. Re-run repository inventory scanners  
2. Update `01-inventory/*-endpoint-current-state.csv`  
3. Ingest latest CI execution results  
4. Rebuild `verified-metrics-register.csv`  
5. Update leadership summary from register only  

## Integration gaps tracked

See `../government-savings-automation-assessment/03-analysis/coverage-calculation-notes.md` and `ci-gate-assessment.md`.
