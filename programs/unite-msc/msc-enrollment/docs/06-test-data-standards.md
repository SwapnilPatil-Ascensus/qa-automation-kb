# Test Data Standards

## Naming convention

Enrollment-created accounts should follow the same pattern as mobile1 disposable accounts so post-submit SQL lookup works.

### Username

```
QAAUTOTEST_ENR_{YYYYMMDD}_{HHMMSS}_{RRR}
```

| Part | Example | Notes |
|------|---------|-------|
| Prefix | `QAAUTOTEST_ENR_` | Identifies QA automation enrollment accounts |
| Date | `20260803` | `YYYYMMDD` |
| Time | `190530` | `HHMMSS` (24h) |
| Random | `427` | 3-digit random (100–999) |

**Full example:** `QAAUTOTEST_ENR_20260803_190530_427`

Alternative (Postman collection default): `enroll_{timestamp}_{random}` — works for uniqueness but won't match `QAAUTOTEST%` SQL. **Switch to QAAUTOTEST prefix for automation.**

### Email

```
qaa.enr.{username}@example.com
```

Example: `qaa.enr.QAAUTOTEST_ENR_20260803_190530_427@example.com`

Must be unique per run (tied to username).

### Password

| Context | Password | Notes |
|---------|----------|-------|
| Enrollment member login | `Test@123` | Standard for all QA enrollment accounts |
| OAuth service account | `Test@1234` | Framework auth only (not member login) |
| Mobile1 DB-seeded users | `Newton@123` | Pre-existing accounts only |

**Do not change** enrollment password from `Test@123`.

### SSN (must be unique per run)

Generate valid-format 9-digit SSNs that don't collide:

```
Owner:       9{MMDD}{RR}0   → e.g. 908034270 (9 + date + random + 0)
Beneficiary: 8{MMDD}{RR}1   → e.g. 808034271 (must differ from owner)
```

Rules:
- Owner and beneficiary SSN must **differ**
- Do not reuse SSNs across runs (use date+random in generation)
- Automation utility should check uniqueness if possible (optional Phase 2)

### Owner / beneficiary names

| Field | Default | Notes |
|-------|---------|-------|
| Owner first | `MSC` | |
| Owner last | `Owner` | |
| Beneficiary first | `MSC` | |
| Beneficiary last | `Beneficiary` | |

Names can be static; uniqueness comes from username/SSN.

### Address (Stage1 hawaii default)

| Field | Value |
|-------|-------|
| Street | `95 Wells Ave` |
| City | `Newton` |
| State | `MA` |
| Zip | `02459` |
| Phone | `5551234567` |
| Phone type | `C` (cell) |

### Bank (test)

| Field | Value |
|-------|-------|
| Bank name | `Chase` |
| Routing | `071000013` |
| Account | `654321` |
| Account type | `S` (savings) or `C` (checking) |
| isDomestic | `Y` |

### Plan (Stage1 default)

| Field | Value |
|-------|-------|
| `enrollment.planId` | `hawaii` |
| `enrollment.planDeprecatedId` | `100001` |
| `enrollment.fundId` | **From SQL** (API) or GET plan step 04 (Postman) — see [11-allocation-fund-sql.md](11-allocation-fund-sql.md) |
| `enrollment.account.prefix` | `180004006` |
| `enrollment.account.ext` | `01` |

#### Dynamic `fundId` (steps 12 & 13)

```sql
-- Traunch from branding
SELECT * FROM TU_TRAUNCH WHERE branding = 'hawaii';

-- Active fund for traunch
SELECT * FROM TU_TRAUNCH_FUND WHERE CTL_REC_STAT = 'A';

-- Combined (use in API automation)
SELECT tf.FUND_ID
FROM TU_TRAUNCH_FUND tf
INNER JOIN TU_TRAUNCH t ON t.TRAUNCH_ID = tf.TRAUNCH_ID
WHERE tf.CTL_REC_STAT = 'A'
  AND tf.STATE = 'Y'
  AND UPPER(t.BRANDING) = UPPER('hawaii');
```

Example Stage1 result: `FUND_ID = 1009030`, `TRAUNCH_ID = 100009` — verify in your environment.

### Challenge Q&A

| Field | Value |
|-------|-------|
| challengeQuestion | `sam` |
| challengeResponse | `sam` |

### changeId

Always `TEST_ID` for all entities (legacy convention).

---

## usernameHash

Computed once per run from username:

```
usernameHash = Base64( SHA-512( username ) )
```

Postman collection prerequest script handles this. Automation utility must compute the same.

---

## forceNewRun flag

Set `enrollment.forceNewRun = true` in Postman environment to regenerate username/email/runId before next collection run. Reset to `false` after generation.

---

## Test data utility (automation — to build)

Location (proposed): `api-test-automation/mobile/enrollment/src/main/java/enrollment/util/EnrollmentTestDataBuilder.java`

```java
public class EnrollmentTestDataBuilder {
    public String username();      // QAAUTOTEST_ENR_{date}_{time}_{rand}
    public String email();         // qaa.enr.{username}@example.com
    public String password();      // Test@123
    public String ownerSsn();      // unique 9-digit
    public String beneficiarySsn(); // unique, != owner
    public String usernameHash();  // Base64 SHA-512
    public String runId();         // timestamp_random
    public String fundId(String branding);  // SQL: TU_TRAUNCH + TU_TRAUNCH_FUND active FUND_ID
}
```

Reuse `jsonapi-core` random generators where possible (`$$random_person_ssn$$` pattern).

---

## Dynamic data from database (test setup)

Before each run, pull live values from Oracle using the per-endpoint SQL files in `sql/`:

| Test field | SQL file | Query |
|------------|----------|-------|
| `enrollment.planDeprecatedId`, `account.prefix` | `00-shared-plan-branding.sql` | Plan by branding |
| `enrollment.fundId` | `12-allocations-entered.sql` | Active fund for plan |
| `enrollment.bank.routing` | `09-verify-routing-number.sql` | Valid routing from `TU_BNK_INFO` |
| Owner/bene address | `07-owner-address-entered.sql` | Valid zip/state from `TU_USPS_ADDRESS_INFO` |
| Username free? | `05-create-prospect.sql` | 0 rows = available |
| `x-app-version` header | `get-x-app-version.sql` | `MIN_MOBILE_VERSION` code |

See `sql/README.md` for the full endpoint → downstream repo → table map.

---

## Manual test data (Postman)

1. Set `enrollment.forceNewRun = true`
2. Run any request in collection (prerequest generates username/email/hash)
3. **Manually update** owner/bene SSN in environment if re-running on same day
4. Encrypt payloads with fresh plaintext values
5. After successful run, note `enrollment.username` for SQL verification

---

## Accounts created via enrollment → used by mobile tests

Goal: enrollment creates accounts that mobile1/mobile2 tests can find via:

```sql
WHERE UPPER(L.USERNAME) LIKE 'QAAUTOTEST%'
  AND T.BRANDING = '$$branding$$'
```

This is why the `QAAUTOTEST_ENR_` prefix matters — it fits the existing `QAAUTOTEST%` SQL pattern in `mobile1/mobile.sql`.
