# Code Coverage & Test Metrics — Mobile 1, Mobile 2, Enrollment

**As of:** 2026-09-02

## Summary

| Module | Endpoint ops / business endpoints | @Test methods | Sign-off |
|--------|-----------------------------------|---------------|----------|
| Mobile 1 | 26 operations | ~26 | COMPLETE (Word pack exists) |
| Mobile 2 | 24/25 business (96.0%) | ~26 | COMPLETE (Word pack exists) |
| Enrollment | 25 automated / 28 catalog (3 partner deferred) | 25 | **NOT STARTED** — coverage MD/XLSX refreshed Sep 2 |

## QC4 execution snapshot (Jul 2026)

See `evidence/regression-runs/qc4-module-suites-results.csv`:
- Mobile 2: 20/22 module profiles PASS
- Contribution integration/regression: 5 failures (investigate)

## Deliverables

| Artifact | Path |
|----------|------|
| Combined endpoint register | `mappings/endpoint-signoff-register.csv` |
| Enrollment endpoint register | `mappings/enrollment-endpoint-current-state.csv` |
| Mobile 1 sign-off DOCX | `docs/06-coverage/signoff/Mobile-1-API-Automation-Sign-Off.docx` |
| Mobile 2 sign-off DOCX | `docs/06-coverage/signoff/Mobile-2-API-Automation-Sign-Off.docx` |
| Enrollment coverage status | `postman/EnrollmentE2E/Enrollment-Automation-Coverage-Status.md` |

## Definition

- **Endpoint coverage** = canonical TestNG test exists for HTTP method + path
- **JaCoCo** = Java line coverage on framework code (separate CI gate program in government-savings-assessment)
