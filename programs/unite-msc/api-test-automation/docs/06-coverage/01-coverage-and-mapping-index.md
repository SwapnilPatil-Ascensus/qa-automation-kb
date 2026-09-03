# Coverage and Mapping Index

## Endpoint CSVs (this folder)

| File | Scope |
|------|-------|
| [endpoint-signoff-register.csv](../../mappings/endpoint-signoff-register.csv) | **Combined M1+M2 sign-off register** |
| [mobile1-endpoint-current-state.csv](../../mappings/mobile1-endpoint-current-state.csv) | Mobile 1 — 26 operations (Aug 2026) |
| [mobile2-endpoint-current-state.csv](../../mappings/mobile2-endpoint-current-state.csv) | Mobile 2 — 25 endpoints (Aug 2026) |
| [unite-msc-endpoint-summary.csv](../../mappings/unite-msc-endpoint-summary.csv) | Leadership rollup |
| [enrollment-endpoint-current-state.csv](../../mappings/enrollment-endpoint-current-state.csv) | Enrollment — wizard + subsequent (Sep 2026) |

## Sign-off handover (DOCX)

| File | Scope |
|------|-------|
| [Mobile-1-API-Automation-Sign-Off.docx](./signoff/Mobile-1-API-Automation-Sign-Off.docx) | Formal Word — Mobile 1 |
| [Mobile-2-API-Automation-Sign-Off.docx](./signoff/Mobile-2-API-Automation-Sign-Off.docx) | Formal Word — Mobile 2 |
| [05-code-coverage-metrics.md](./05-code-coverage-metrics.md) | Test & endpoint metrics |

Leadership copies: `programs/government-savings-assessment/01-inventory/` — keep in sync.

## Enrollment coverage (updated 2026-09-02)

- [Enrollment-Automation-Coverage-Status.md](../../postman/EnrollmentE2E/Enrollment-Automation-Coverage-Status.md) — **25/28 catalog rows Done**; remaining 3 are partner/OAuth deferred
- [Enrollment-Automation-Coverage-Matrix.xlsx](../../postman/EnrollmentE2E/Enrollment-Automation-Coverage-Matrix.xlsx)
- [05-unite-enrollment-migration-tracker.md](../../../program-hub/05-unite-enrollment-migration-tracker.md)
- Enrollment **sign-off Word pack is not created yet** (Mobile 1/2 packs exist)

## Migration docs

- [legacy-to-new-migration.md](../../mappings/legacy-to-new-migration.md)
- [legacy-new-postman-excel-mapping.md](../../mappings/legacy-new-postman-excel-mapping.md)
- [Mobile2 verification runbook](02-mobile2-verification-runbook.md)
- [Dashboard coverage matrix](03-dashboard-coverage-matrix.md)

## Postman

`api-test-automation/postman/mobile/` — see [postman/README.md](../../postman/README.md)

## Code coverage / leadership

`programs/government-savings-assessment/` — coverage matrices, JaCoCo gate plans, coverage intelligence.

## Program trackers

`programs/unite-msc/program-hub/05-unite-enrollment-migration-tracker.md`  
`programs/unite-msc/program-hub/06-unite-mobile1-migration-tracker.md`  
`programs/unite-msc/program-hub/07-unite-mobile2-migration-tracker.md`
