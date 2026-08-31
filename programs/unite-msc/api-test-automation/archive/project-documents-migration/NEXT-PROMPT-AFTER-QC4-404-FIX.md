> **Historical prompt** — references `mobile-microservices/unite-enrollment`. Enrollment remains in `mobile/enrollment/` (separate scope).

# Next Prompt — After QC4 Enrollment 404 Is Fixed

Use only after manual Postman confirmation that **`GET /enrollmentapi/v1/plans`** (or dev-approved URL) returns **200** on QC4.

```text
Implement exactly ONE QC4 API smoke test for mobile-microservices/unite-enrollment.

Confirmed inputs (fill before run):
- ENROLLMENT_BASE_URL=<developer-confirmed-base-url>
- AUTH_MODE=<mobile-jwt | server-oauth>
- JWT_ACQUISITION=<e.g. mobilemembersession then bearer>
- PLANS_GET_PATH=/enrollmentapi/v1/plans
- BRANDING_PARAMETER=hawaii
- X_APP_VERSION=<if required>

Rules:
- Do not modify jsonapi-core, jsonapi-parent, jsonapi-lib, jsonapi-auth, universal/, astro/, or pipelines.
- No dependency upgrades.
- Packages: enrollment.plans (test), enrollment.client (only if needed), enrollment.core.pojo.
- JSON under src/test/resources/json/enrollment/ only if needed.
- No secrets in Git.

Tasks:
1. Add GetEnrollmentPlansSmokeTest (GET plans, assert 200, minimal body assert).
2. Register in smoke-testng.xml and regression-testng.xml; bootstrap-testng.xml unchanged.
3. Run test-compile, bootstrap script, smoke script, accountweb test-compile.
4. Add validation note under project-documents/ (e.g. 04-FIRST-API-SMOKE-EVIDENCE.md).
5. Stop after one API test. Do not commit unless asked.
```
