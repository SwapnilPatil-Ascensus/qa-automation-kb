# Validation Strategy

## Principle: no mid-flow SQL

Per team direction:

- **Do not** query Oracle during wizard steps (no "field X in DB equals response Y")
- **Do not** validate Cassandra snapshots mid-flow
- **Only** assert on HTTP responses during the enrollment sequence
- **One SQL check** after `review-confirm-entered`: confirm account exists

This matches how mobile1 tests work — API assertions during flow, DB lookup only when needed at the end.

---

## Per-step response validations

### GET endpoints (01–04)

| Step | HTTP | Body assertions |
|------|------|-----------------|
| ping | 200 | `status` = `"OK"` |
| usstates | 200 | Array length > 0 |
| plans | 200 | Target plan `hawaii` present |
| plans/{id} | 200 | `fundId` extractable; save to env |

### POST create prospect (05)

| Assertion | Rule |
|-----------|------|
| HTTP status | 200 |
| `errors` | Empty array `[]` |
| `jwtToken` | Present, non-empty → save as `enrollment.prospectJwt` |
| `correlationId` | Present (optional capture for chaining) |

**Do not assert:** decrypted field values, DB state.

### Wizard steps (06–12)

| Assertion | Rule |
|-----------|------|
| HTTP status | 200 |
| `errors` | Empty array (if present) |
| Response time | < 30s (optional SLA) |

**Do not assert:** individual field round-trip (encrypted responses are hard to compare in Postman).

### review-confirm-entered (13)

| Assertion | Rule |
|-----------|------|
| HTTP status | 200 |
| `errors` | Empty array |
| `account.accountNumber` or confirmation | Present |
| Header `x-enc-jwttoken` | Present (member JWT) |

### Post-submit SQL (only DB check)

After step 13, verify account was created:

```sql
-- Pattern from mobile1: find QAAUTOTEST accounts by branding
SELECT L.USERNAME, A.UII_ACCT_ID || A.UII_ACCT_EXT AS accountId
FROM TU_ACCT A
INNER JOIN TU_MEMBER M ON A.UII_MEMBER_ID = M.UII_MEMBER_ID
INNER JOIN TA_APP_CONTEXT AC ON M.UII_MEMBER_ID = AC.APP_MEMBER_ID
INNER JOIN TA_LOGIN L ON AC.LOGIN_ID = L.LOGIN_ID
INNER JOIN TU_TRAUNCH T ON T.TRAUNCH_ID = A.TRAUNCH_ID
WHERE UPPER(L.USERNAME) = UPPER('{{enrollment.username}}')
  AND T.BRANDING = '{{enrollment.planId}}'
```

**Assert:** exactly 1 row returned with matching username.

For QC4 automation, reuse `get.mobile.auth.user` pattern from `mobile/mobile1/src/test/resources/sql/mobile.sql` with `QAAUTOTEST%` prefix.

---

## Negative test validations

| Scenario | Expected |
|----------|----------|
| Duplicate username | `errors` contains `USERNAME_NOT_AVAILABLE` |
| Invalid plan | HTTP 4xx or error in `errors[]` |
| Invalid routing number | `errors` on bank or routing verify |
| Allocation ≠ 100% | `errors` on allocations or review |
| Missing beneficiary at submit | `errors` on review-confirm |
| Member JWT on enrollment topic | HTTP 401 |
| Plain body on Stage1 POST | HTTP 500 or decryption error |

---

## Response decoding

Encrypted responses may contain encrypted fields. For automation:

1. Use `DecryptHelper` / CLI `-m decrypt` with saved `aeskey.txt`
2. Assert only on non-encrypted fields: `errors`, `jwtToken`, `correlationId`, `accountNumber`
3. Do not assert decrypted PII values match input (unnecessary; encryption round-trip is tested by 200 + empty errors)

---

## Postman test script template

Minimal scripts (avoid complex logic):

```javascript
// Every POST step
pm.test('HTTP 200', () => pm.response.to.have.status(200));

const body = pm.response.json();
if (Array.isArray(body) && body.length) {
    pm.test('No errors', () => {
        pm.expect(body[0].errors || []).to.eql([]);
    });
}

// Step 05 only — capture JWT
if (body[0]?.jwtToken) {
    pm.environment.set('enrollment.prospectJwt', body[0].jwtToken);
}

// Step 13 only — capture account
if (body[0]?.account?.accountNumber) {
    pm.environment.set('accountNumber', body[0].account.accountNumber);
}
```

---

## Test case matrix

| ID | Scenario | Steps | SQL check |
|----|----------|-------|-----------|
| ENR-001 | Happy path E2E hawaii | 01–05, 13 (shortcut) | Yes |
| ENR-002 | Happy path full wizard | 01–13 all | Yes |
| ENR-003 | Duplicate username | 05 twice same user | No |
| ENR-004 | Invalid routing | 10 or 09 | No |
| ENR-005 | GET smoke | 01–04 | No |
| ENR-006 | With recurring AIP | 01–05, 11, 13 | Yes |
| ENR-007 | Without bank (if plan allows) | varies | Yes |

**Phase 1 target:** ENR-001 + ENR-005 (2 tests).
**Phase 2:** ENR-002 + 3 negatives.
