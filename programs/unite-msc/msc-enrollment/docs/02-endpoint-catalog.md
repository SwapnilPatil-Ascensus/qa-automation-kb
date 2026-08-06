# Endpoint Catalog — MSC Enrollment API

Base path: `/enrollmentapi/v1`

Common headers for all requests:

| Header | Required | Value |
|--------|----------|-------|
| `Content-Type` | Yes | `application/json` |
| `x-app-version` | Yes (Stage1+) | From env, e.g. `1.8.0` or `3.1.0` |
| `Authorization` | Wizard POSTs only | `Bearer {prospectJwt}` |

---

## 1. Health & infrastructure

| # | Method | Path | Auth | Encryption | Purpose |
|---|--------|------|------|------------|---------|
| — | GET | `/health/liveness` | None | No | Liveness probe |
| — | GET | `/health/readiness` | None | No | DB + config check |
| — | GET | `/health/readiness/all` | None | No | Readiness + Cassandra |
| — | DELETE | `/health/cache` | None | No | Clear caches |

*Not needed for E2E testing.*

---

## 2. Reference & bootstrap (GET — no encryption)

### 2.1 GET `/certificate`

| | |
|---|---|
| **Auth** | None |
| **Encryption** | No |
| **Purpose** | Returns RSA public key for encrypting AES session key |
| **Response** | `{ "_embedded": { "item": { "certificate": "<base64 DER>" } } }` |
| **Code** | `CertificateResource` (shared library) |
| **Notes** | Called automatically by `EncryptHelper` CLI; manual call optional for debugging |

### 2.2 GET `/ping`

| | |
|---|---|
| **Auth** | None |
| **Response** | `{ "status": "OK", "uri": "..." }` |
| **Validation** | HTTP 200 |

### 2.3 GET `/usstates`

| | |
|---|---|
| **Auth** | None |
| **Response** | `[{ "id": "MA", "name": "Massachusetts" }, ...]` |
| **Validation** | HTTP 200; array not empty |
| **Notes** | Optional for E2E; used by mobile UI for state dropdown |

### 2.4 GET `/plans`

| | |
|---|---|
| **Auth** | None |
| **Query** | `page` (optional) |
| **Response** | HAL list of mobile-enabled plans |
| **Validation** | HTTP 200; target plan present |
| **Downstream** | `metadataapi` |

### 2.5 GET `/plans/{planId}`

| | |
|---|---|
| **Auth** | None |
| **Header** | `x-app-version` ≥ 1.5.0 required |
| **Path param** | `planId` — branding slug, e.g. `hawaii`, `okdirect` |
| **Response** | Plan detail + funds; extract `fundId` for allocations |
| **Validation** | HTTP 200; capture first `fundId` |
| **Error** | HTTP 426 if `x-app-version` too old |

---

## 3. Create prospect (POST — encryption required on Stage1)

### POST `/enrollments/prospects`

| | |
|---|---|
| **Auth** | None |
| **Encryption** | **Yes** — all PII + `encAesKey` |
| **Body** | JSON **array** with one `Enrollment` object |

**Mandatory fields:**

```json
[{
  "planId": null,
  "usernameHash": "<Base64 SHA-512 of username>",
  "encAesKey": "<RSA-wrapped AES key>",
  "prospect": {
    "username": "<unique>",
    "password": "<encrypted>",
    "plan": "hawaii",
    "email": "<encrypted>",
    "challengeQuestion": "<encrypted>",
    "challengeResponse": "<encrypted>"
  },
  "owner": {
    "firstName": "<encrypted>",
    "lastName": "<encrypted>",
    "ssn": "<encrypted>",
    "dob": "<encrypted ISO date>",
    "changeId": "TEST_ID"
  }
}]
```

**Key rules:**
- `planId` on root = `null` at prospect step
- `prospect.plan` = plaintext branding slug (e.g. `hawaii`)
- `usernameHash` = Base64(SHA-512(username)) — computed, not AES encrypted

**Response (200):**

```json
[{
  "jwtToken": "<prospect JWT — save this>",
  "errors": [],
  "correlationId": "...",
  "eventId": "...",
  "seqNum": 1
}]
```

**What happens in code:**
1. Validates plan exists via metadata MS
2. Checks username availability via `accountapi/members/verify/prospects`
3. Fires `prospect-entered` event
4. Creates prospect session via `authenticationapi/prospectsession`
5. Saves Cassandra enrollment snapshot
6. Returns `ENROLL_PROSPECT` JWT

**Common errors:**

| Error | Cause |
|-------|-------|
| HTTP 500 | Plain body on Stage1, double encryption, empty body |
| `USERNAME_NOT_AVAILABLE` | Duplicate username/email |
| Decryption exception | Wrong cert/key for environment |

---

## 4. Wizard events — POST `/enrollments/enrollment/{event}`

All wizard POSTs require:
- **Bearer** `prospectJwt` from create-prospect
- **Encrypted** body with same `encAesKey` session
- JSON **array** format

### 4.1 `owner-entered`

| | |
|---|---|
| **Required** | No (re-validated at submit) |
| **Validates via** | `profileapi/owners/verify/ownerInfo` + `accountapi/rootaccounts/verify` |
| **Key fields** | `owner.firstName`, `lastName`, `ssn`, `dob`, `changeId` |
| **Response** | Updated event metadata; optional `x-enc-jwttoken` header |

### 4.2 `owner-address-entered`

| | |
|---|---|
| **Required** | No |
| **Validates via** | `profileapi/owners/verify/address` |
| **Key fields** | `mlAddline1`, `mlCity`, `mlZipcode`, `mlStatelabel`, `permAddline1`, `permCity`, `permZipcode`, `permStatelabel`, `phone`, `phoneType` |
| **Notes** | PO Box rules, state/zip validation |

### 4.3 `beneficiary-entered`

| | |
|---|---|
| **Required** | No |
| **Validates via** | `profileapi/beneficiaries/verify/beneficiaryInfo` + `accountapi/rootaccounts/beneficiaries/verify` |
| **Key fields** | `beneficiary.firstName`, `lastName`, `ssn`, `dob`, address fields, `isCtznOrResalien`, `countryCode` |
| **Notes** | Bene SSN must differ from owner SSN |

### 4.4 `bank-entered`

| | |
|---|---|
| **Required** | No (unless one-time funding) |
| **Validates via** | `bankapi/bankInstructions/verify?validateBank=Y` |
| **Key fields** | `bankName`, `routingNumber`, `accountNumber`, `confirmAccountNumber`, `accountType` (C/S), `isDomestic` |

### 4.5 `recurring-contribution-entered`

| | |
|---|---|
| **Required** | **Optional** — skip with `"skipped": true` |
| **Validates via** | `bankapi/bankInstructions/verify` (recurring) |
| **Key fields** | `amount`, `frequency`, `beginDate`, `debitDate` |
| **Notes** | `beginDate` ≥ 3 business days out |

### 4.6 `allocations-entered`

| | |
|---|---|
| **Required** | Yes at submit (empty → `REQUIRED_ALLOCATIONS`) |
| **Validates via** | `accountapi/allocations/verify` |
| **Key fields** | `enrollmentAllocations[].fundId`, `percentAlloc` (must sum to 100) |
| **Notes** | `fundId` — **API automation:** SQL lookup from `TU_TRAUNCH` + `TU_TRAUNCH_FUND` (see [11-allocation-fund-sql.md](11-allocation-fund-sql.md)). **Postman:** from GET `/plans/{id}` step 04 or manual SQL |

---

## 5. Helpers

### POST `/verify/routingnumber`

| | |
|---|---|
| **Auth** | Prospect JWT or acceptance test |
| **Encryption** | Yes (`routingNumber`, `encAesKey`) |
| **Body** | `[{ "routingNumber": "<encrypted>", "encAesKey": "..." }]` |
| **Response** | `[{ "bankName": "Chase", "errors": [] }]` |
| **Required** | **Optional** — bank-entered also validates routing |

### POST `/enrollmentallocationfunds/get`

| | |
|---|---|
| **Auth** | None |
| **Encryption** | Yes (`dob`, `planId`) |
| **Purpose** | Age-based fund portfolio suggestions |
| **Required** | Optional for fixed-fund E2E |

### GET `/subsequentenrollment/banks`

| | |
|---|---|
| **Auth** | Member or prospect JWT with `uii_member_id` |
| **Query** | `enAesKey` required |
| **Purpose** | List existing member banks (subsequent enrollment only) |

---

## 6. Submit — POST `/enrollments/enrollment/review-confirm-entered`

| | |
|---|---|
| **Auth** | Bearer `prospectJwt` |
| **Encryption** | **Yes** — full aggregate |
| **Required** | **Yes** — creates account |

**Mandatory sections in body:**

| Section | Key fields |
|---------|------------|
| `prospect` | username, password, plan, email, challenge Q/R |
| `owner` | name, ssn, dob, mailing + permanent address, phone |
| `beneficiary` | name, ssn, dob, address, `isCtznOrResalien` |
| `member` | email, `delivConfirms/Statements/TaxForms` = `E` |
| `account` | `prefix`, `ext`, `planId` (deprecated numeric ID) |
| `bank` | bankName, routingNumber, accountNumber, accountType |
| `enrollmentAllocations` | fundId + percentAlloc (100%) |
| `reviewConfirm` | `tcAccepted: true` (sets account state 91 vs 90) |

**Response (200):**

```json
[{
  "errors": [],
  "account": { "accountNumber": "..." }
}]
```

**Response header:** `x-enc-jwttoken` = member JWT with `uii_member_id`

**What happens in code:**
1. Re-runs ALL section validations
2. Generates account number
3. `accountapi/v1/accounts/create` — persists login, member, owner, bene, bank, allocations
4. Cassandra snapshot update
5. Upromise referral (if selected)
6. Returns member JWT

---

## 7. Partner / alternate flows (out of initial scope)

| Method | Path | Auth | Purpose |
|--------|------|------|---------|
| POST | `/enrollments/submit` | VANGUARD | Single-shot partner enrollment |
| POST | `/enrollments/enrollmentstarted` | None | Start event without prospect |
| POST | `/oauth/token` | None | Service OAuth |
| GET | `/upromiseaccount` | None | Upromise account exchange |
| POST | `/enrollments/subsequentenrollment/{event}` | Member/prospect JWT | Add account to existing member |

---

## 8. Environment host matrix

| Environment | Cloud BFF (enrollment) | Notes |
|-------------|------------------------|-------|
| Stage1 | `https://unite-bff-cloud.stage1.unite529.com` | **Team default** |
| QC4 | `https://unite-bff-cloud.qc4.unite529.com` | Encryption required; had 500 issues initially |
| Dev | `https://unite-bff-cloud.dev.unite529.com` | May allow plain bodies |
| Plan-specific Stage1 | e.g. `okd.stage1.acs529.com` | Some traunches use plan-specific hosts |

**Mobile login** (not enrollment): `unite-bff-wtn.stage1.acs529.com` — do not use for enrollment APIs.

---

## 9. Test case estimate

| Category | Count | Examples |
|----------|-------|----------|
| Smoke (GET only) | 4 | ping, plans, plan-by-id, usstates |
| Happy path E2E | 1 per plan | hawaii full enrollment |
| Negative — prospect | 3 | duplicate username, invalid plan, bad password |
| Negative — validation | 5 | invalid routing, SSN mismatch, allocation ≠ 100%, missing bene, missing bank |
| Optional steps | 2 | with/without recurring contribution, with/without routing verify |
| **Initial automation target** | **~15** | Start with 1 happy path + 3 negatives |
