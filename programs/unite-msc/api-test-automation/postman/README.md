# Postman — Mobile MSC

Collections in **automation repo**:

| Collection | Path |
|------------|------|
| MSC Mobile app | `api-test-automation/postman/mobile/mobile-msc/MSC-Mobile-app.postman_collection.json` |
| IDP session | `api-test-automation/postman/mobile/Mobile Endpoints (w- IDP Session).postman_collection.json` |

Environments: `api-test-automation/postman/environments/` (QC4, Stage 1, Stage 5).

Usage: `api-test-automation/postman/mobile/README.md`

## Enrollment E2E

| Asset | Path |
|-------|------|
| Dinesh mapping (source) | [EnrollmentE2E/Enrollment End Points.xlsx](./EnrollmentE2E/Enrollment%20End%20Points.xlsx) |
| Postman collection | [EnrollmentE2E/Enrollment -E2E.postman_collection.json](./EnrollmentE2E/Enrollment%20-E2E.postman_collection.json) |
| **Automation coverage matrix** | [EnrollmentE2E/Enrollment-Automation-Coverage-Matrix.xlsx](./EnrollmentE2E/Enrollment-Automation-Coverage-Matrix.xlsx) |
| Coverage status (markdown) | [EnrollmentE2E/Enrollment-Automation-Coverage-Status.md](./EnrollmentE2E/Enrollment-Automation-Coverage-Status.md) |

Regenerate matrix: `EnrollmentE2E/tools/generate_enrollment_coverage_matrix.py`

Legacy KB: `programs/unite-msc/msc-enrollment/postman/`

When adding automation, update the endpoint CSV in [mappings/](../mappings/).

**Sep 2026:** Coverage status regenerated after review-confirm + subsequent classes landed. Unified Postman (M1+M2+Enrollment) and Bruno conversion are upcoming stories — not in repo yet. See `mappings/legacy-new-postman-excel-mapping.md`.
