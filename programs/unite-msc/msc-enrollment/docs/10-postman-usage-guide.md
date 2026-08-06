# Postman Usage Guide

Simple step-by-step for running MSC enrollment E2E on Stage1.

---

## Prerequisites

1. **Postman** installed
2. **EncryptHelper CLI** built from `api-test-automation/jsonapi/jsonapi-encryption`
3. Import from `postman/`:
   - `Enrollment-E2E-Stage1.postman_collection.json`
   - `Enrollment-Stage1.postman_environment.json`
4. Select **Enrollment Stage1** environment

---

## One-time setup

### Build encryption tool

```powershell
cd C:\Workspace\GitLab\api-test-automation\jsonapi\jsonapi-encryption
mvn package -DskipTests -q
$JAR = Get-ChildItem target\jsonapi-encryption-*.jar | Select-Object -First 1
```

---

## Every new test run

### Step A — Generate unique test data

1. In Postman environment, set `enrollment.forceNewRun` = `true`
2. Send **any** request (e.g. 01 Ping) — prerequest script generates:
   - `enrollment.username` = `QAAUTOTEST_ENR_{date}_{time}_{rand}`
   - `enrollment.email`
   - `enrollment.usernameHash`
3. Set `enrollment.forceNewRun` back to `false`
4. **Update SSNs** in environment if re-running same day:
   - `enrollment.owner.ssn` — unique 9 digits
   - `enrollment.beneficiary.ssn` — different from owner

### Step B — Run GET steps (no encryption)

Run in order — these work as-is:

| # | Request | Captures |
|---|---------|----------|
| 01 | Ping | — |
| 02 | GET usstates | — |
| 03 | GET plans | — |
| 04 | GET plan by ID | `enrollment.fundId` |

### Step C — Encrypt & send POST steps

For **each POST request** (05, 06–12, 13):

1. Open matching plain payload: `postman/payloads/plain/NN-*.json`
2. Replace `{{variable}}` placeholders with environment values
3. Save as `encrypt.txt`
4. Encrypt:

```powershell
java -jar $JAR -m encrypt -e stage -s enrollment -f encrypt.txt
```

5. Copy encrypted JSON from console → paste into Postman request body
6. For steps 06+: ensure **Authorization** tab has Bearer `{{enrollment.prospectJwt}}`
7. Send

**Tip:** After first encrypt, reuse same AES key for all steps in the run:

```powershell
$key = Get-Content aeskey.txt
java -jar $JAR -m encrypt -e stage -s enrollment -f 06-owner-entered.json -a $key
```

### Step D — Capture JWT (step 05)

After create-prospect succeeds, test script saves `enrollment.prospectJwt` automatically. Verify in environment before continuing.

### Step E — Submit (step 13)

Same encrypt workflow. After success:
- Check `errors` = `[]`
- Note `accountNumber` in environment
- Check response header `x-enc-jwttoken` (member JWT)

---

## Shortcut path (fewer steps)

For quick smoke test:

1. Run GET steps 01–04
2. Encrypt & send step 05 (prospects)
3. Encrypt & send step 13 only (review-confirm with full aggregate)

Skip wizard steps 06–12. The submit endpoint validates everything.

---

## Troubleshooting

| Problem | Check |
|---------|-------|
| HTTP 500 on POST | Body empty? Encrypted for Stage1? Double-encrypted? |
| `USERNAME_NOT_AVAILABLE` | Set `forceNewRun=true`, regenerate username |
| HTTP 401 on wizard | Step 05 failed? `prospectJwt` empty? Using member JWT? |
| Padding/decrypt error | New cert needed — re-run encrypt with fresh plaintext |
| HTTP 426 on GET plan | Increase `x-app-version` to `3.1.0` |
| Empty body in console | Paste encrypted JSON into Body tab (raw JSON) |

---

## Manual payload creation (without template files)

Minimum create-prospect body (before encryption):

```json
[{
  "planId": null,
  "usernameHash": "{{enrollment.usernameHash}}",
  "prospect": {
    "username": "{{enrollment.username}}",
    "password": "{{enrollment.password}}",
    "plan": "{{enrollment.planId}}",
    "email": "{{enrollment.email}}",
    "challengeQuestion": "{{enrollment.challengeQuestion}}",
    "challengeResponse": "{{enrollment.challengeResponse}}"
  },
  "owner": {
    "firstName": "{{enrollment.owner.firstName}}",
    "lastName": "{{enrollment.owner.lastName}}",
    "ssn": "{{enrollment.owner.ssn}}",
    "dob": "{{enrollment.owner.dob}}",
    "changeId": "TEST_ID"
  }
}]
```

Encrypt this JSON, paste result into Postman, send.

---

## What the collection scripts do (minimal)

| Script | Location | Purpose |
|--------|----------|---------|
| Prerequest | Collection level | Generate username/email/hash when `forceNewRun=true` |
| Test | Step 05 | Capture `prospectJwt` |
| Test | Step 13 | Assert no errors; capture account number |
| Test | All | HTTP 200 check |

**No encryption scripts in collection** — by design.

---

## Decrypting responses (optional)

If response fields look encrypted:

```powershell
# Save response body to response.json
java -jar $JAR -m decrypt -f response.json
# Uses aeskey.txt from encrypt step
```

For automation, only assert on `errors`, `jwtToken`, and `accountNumber` — no need to decrypt PII.
