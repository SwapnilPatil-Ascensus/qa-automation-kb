# Adding a New REST API Endpoint

See [Endpoint migration playbook](01-endpoint-migration-playbook.md) for the full workflow.

## Checklist

1. Audit — coverage matrix before code
2. POJOs — one per file, extend `BasePOJO`
3. Test class — extend `MobileBaseRequestTest` (mobile1/mobile2) or `EnrollmentBaseTest` (enrollment)
4. Suite XML + Maven profile (mobile1/mobile2 only — enrollment uses **one** suite; append classes)
5. JSON/SQL fixtures if needed
6. QC4 / Stage1 run — document in module README
7. Update mapping CSV in [mappings/](../../mappings/)

## Enrollment (`mobile/enrollment`)

- **Master guide:** `api-test-automation/mobile/enrollment/ENROLLMENT-AUTOMATION-GUIDE.md` (KB copy: [msc-enrollment/docs/12-automation-team-guide.md](../../msc-enrollment/docs/12-automation-team-guide.md))
- Extend `EnrollmentBaseTest`; one `*RequestTest` per wizard step
- Append test class to `enrollment-regression-testng.xml`, `enrollment-integration-testng.xml`, and localhost example — **do not** add new suite XML files
- Step 1 sets `ProspectSessionContext`; steps 2+ use Bearer JWT
- Postman plain payloads: [msc-enrollment/postman/payloads/plain/](../../msc-enrollment/postman/payloads/plain/)

## Cursor

Use [guardrails](02-cursor-guardrails.md) and [MR review](03-cursor-validation-and-mr-review.md). For enrollment, rule `enrollment-wizard.mdc` in `api-test-automation`.
