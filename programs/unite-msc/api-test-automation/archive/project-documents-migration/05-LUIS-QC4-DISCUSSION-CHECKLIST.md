# Luis Discussion Checklist — QC4 Enrollment Routing

Use this checklist in a working session with Luis / developers **before** implementing `GetPlansRequestTest`.

## Routing and URL

- [ ] What is the correct QC4 **base URL** for Enrollment APIs?
- [ ] Should automation use the **BFF host** (`mobile-authentication-uri` / Postman `mobileMsc.host.url`) or the **direct Enrollment microservice** (legacy `ENROLLMENT_SERVICE_URL`)?
- [ ] Does **GET `/enrollmentapi/v1/plans`** return **200** in QC4 on that host?
- [ ] What **config property key** should the pilot use (e.g. `enrollment-service-uri`)? (Value documented outside Git.)
- [ ] Are there **gateway or path-prefix** rules (e.g. extra context path on BFF)?

## Authentication

- [ ] Is **Mobile1 `mobilemembersession` JWT** sufficient for enrollment GET plans?
- [ ] Is an **IDP token exchange** required before enrollment calls?
- [ ] Which Postman folder/request sequence is authoritative (Member Session vs PKCE flow)?
- [ ] Should automation reuse **server OAuth** (`ServerHttpRestApiClient`) for any enrollment read APIs?

## Headers and contract

- [ ] Which headers are **mandatory** (e.g. `Authorization`, `X-App-Version`, branding)?
- [ ] Is **`X-App-Version`** required for **list** GET, or only for GET by plan id?
- [ ] Expected **response format** still HAL `_embedded.item`?
- [ ] Any **query parameters** required on list GET for QC4?

## Data and accounts

- [ ] Can GET plans run against **existing QC4 data** without SQL delete/create Plans backgrounds?
- [ ] Which **safe QC4 test account** should be used later for write flows (bank-entered, etc.)?

## Manual Postman Validation Result

Record results after manual execution (no secret values in this table).

| Check | Result | Notes |
|-------|--------|-------|
| Base URL confirmed | Pending | BFF vs direct |
| Auth confirmed | Pending | JWT source and request sequence |
| Required headers confirmed | Pending | Include X-App-Version if applicable |
| GET Plans returns 200 | Pending | `GET /enrollmentapi/v1/plans` |
| Response body validated | Pending | Structure / sample plan ids only |

## Outcomes

When all blocking rows are **Pass**:

1. Update `00-CURRENT-STATUS.md` blocker section.
2. Execute `NEXT-PROMPT-AFTER-QC4-404-FIX.md`.
3. Unblock `TODO-AUTO-01` in `02-TODO-TRACKER.md`.
