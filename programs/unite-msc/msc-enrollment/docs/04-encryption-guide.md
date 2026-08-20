# Encryption Guide

Stage1 and QC4 **require encrypted POST bodies**. GET endpoints work with plain JSON.

## Why Postman scripts failed (meeting findings)

| Issue | Symptom | Fix |
|-------|---------|-----|
| Empty body sent | HTTP 500 | Verify body in Postman console before send |
| Double encryption | Padding/decryption exception | Encrypt from **raw** env values, not already-encrypted vars |
| Wrong environment cert | Garbled decrypt | Use cert from same host you're posting to |
| Reused stale encrypted values | Decrypt failure | Regenerate from fresh plaintext each run |
| Too many owner fields at prospect | 500 / validation errors | Minimum: firstName, lastName, ssn, dob |

**Recommendation:** Do **not** use complex Postman prerequest encryption scripts. Use the `EncryptHelper` CLI instead and paste the encrypted JSON into the request body.

---

## Recommended approach: EncryptHelper CLI

Location: `api-test-automation/jsonapi/jsonapi-encryption`

### Build (one time)

```powershell
cd C:\Workspace\GitLab\api-test-automation\jsonapi\jsonapi-encryption
mvn package -DskipTests
```

### Encrypt a payload file

1. Put plain JSON in `encrypt.txt` (or use `-f` flag)
2. Run:

```powershell
java -cp target/jsonapi-encryption-*.jar core.encryption.runner.Runner `
  -m encrypt -e stage -s enrollment -f encrypt.txt
```

| Flag | Values | Notes |
|------|--------|-------|
| `-m` | `encrypt` / `decrypt` | Mode |
| `-e` | `stage`, `qc4`, `dev`, `local8080`, `local8200` | `stage` → `unite-bff-cloud.stage1.unite529.com` |
| `-s` | `enrollment` (default), `mobile1`, `mobile2` | Stream type |
| `-f` | file path | Plain JSON input |
| `-a` | AES key | Optional; auto-generated if omitted |

3. CLI fetches certificate from `/enrollmentapi/v1/certificate` automatically
4. Output: encrypted JSON printed to console + `aeskey.txt` saved for decrypt

### Decrypt a response

```powershell
java -cp target/jsonapi-encryption-*.jar core.encryption.runner.Runner `
  -m decrypt -f response.json
```

Uses `aeskey.txt` from the encrypt step.

---

## Encryption mechanics

```
┌─────────────┐     GET /certificate      ┌──────────────┐
│   Client    │ ─────────────────────────► │  RSA pub key │
└─────────────┘                          └──────────────┘
       │
       │ 1. Generate AES-256 key + IV
       │ 2. RSA-encrypt (key;iv) → encAesKey
       │ 3. AES-CBC encrypt each PII string field
       ▼
┌─────────────────────────────────────────┐
│  POST body: { encAesKey, usernameHash,  │
│    prospect: { plan: "hawaii" (plain) }, │
│    owner: { firstName: "<cipher>" } }  │
└─────────────────────────────────────────┘
```

### Fields encrypted (AES-CBC)

- Owner: firstName, lastName, ssn, dob, addresses, phone
- Beneficiary: same pattern
- Prospect: username, password, email, challengeQuestion, challengeResponse
- Bank: bankName, routingNumber, accountNumber, confirmAccountNumber
- BankInstruction: amount, frequency, dates

### Fields NOT encrypted

| Field | Treatment |
|-------|-----------|
| `prospect.plan` | Plaintext (may have `s:` prefix in some plans) |
| `usernameHash` | Base64(SHA-512(username)) — hashed, not encrypted |
| `planId` (root) | `null` at prospect; numeric at submit |
| `changeId` | Plaintext `TEST_ID` |
| `accountType`, `isDomestic` | Plaintext flags |
| `enrollmentAllocations.fundId` | Plaintext |
| `enrollmentAllocations.percentAlloc` | Plaintext |

---

## Postman workflow (simple, no scripts)

For each POST step:

1. Open plain payload from `postman/payloads/plain/NN-step-name.json`
2. Replace `{{variables}}` with current env values (unique username, SSNs, etc.)
3. Run EncryptHelper CLI → copy encrypted output
4. Paste into Postman request body
5. Set `Authorization: Bearer {{enrollment.prospectJwt}}` (steps 06+)
6. Send

**Same `aeskey.txt` session** can encrypt all steps in one run if you encrypt each plain file with the same `-a` key:

```powershell
# First call — generates key
java ... -m encrypt -e stage -s enrollment -f 05-prospects.json

# Subsequent calls — reuse key from aeskey.txt
java ... -m encrypt -e stage -s enrollment -f 06-owner-entered.json -a (Get-Content aeskey.txt)
```

---

## usernameHash generation

Only non-AES field that needs computation:

```
usernameHash = Base64( SHA-512( username ) )
```

The Postman collection computes this automatically in the collection prerequest script. When using CLI-only workflow, either:

- Keep the collection prerequest script (just for usernameHash + runId), or
- Compute manually / in test data utility

---

## Environment-specific certificates

| Environment | Certificate source |
|-------------|-------------------|
| Stage1 | `GET https://unite-bff-cloud.stage1.unite529.com/enrollmentapi/v1/certificate` |
| QC4 | `GET https://unite-bff-cloud.qc4.unite529.com/enrollmentapi/v1/certificate` |

**There is no shared certificate file.** Each environment returns its own dynamic key. EncryptHelper handles this when you pass `-e stage` or `-e qc4`.

---

## Java automation (TestNG)

In `api-test-automation/mobile/enrollment`:

```java
configureMobileEncryption(
    "https://unite-bff-cloud.stage1.unite529.com",
    MOBILE_TYPE.ENROLLMENT
);
// POJO with @MobileEncrypt fields
payload.createMobilePayload();
```

This replaces manual CLI + Postman for TestNG tests.

**Deep dive (framework internals):** [Mobile AES encryption flow](../../api-test-automation/docs/03-development/07-mobile-aes-encryption-flow.md) — sequence diagrams, `aesKey` vs `encAesKey`, class map, decrypt reuse, troubleshooting.
