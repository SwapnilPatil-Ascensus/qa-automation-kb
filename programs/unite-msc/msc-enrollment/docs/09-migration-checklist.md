# Migration Checklist — Legacy to New Automation

Checklist for migrating MSC enrollment from legacy Cucumber (`unite-enrollment`) + manual Postman to `api-test-automation/mobile/enrollment`.

---

## What we're migrating from

| Asset | Location | Keep? |
|-------|----------|-------|
| Enrollment service source | `unite-enrollment` | Reference only — don't duplicate |
| Cucumber features (13 files) | `unite-enrollment/src/test/resources/features/` | Port scenarios to TestNG |
| Cucumber stepdefs | `unite-enrollment/src/test/java/enrollment/` | Port logic to TestNG tests |
| `BeanUtils.setEncryptedProperties()` | Legacy crypto | Replace with `BaseMobilePOJO.createMobilePayload()` |
| Dinesh's Postman collection | `msc-enrollment/postman/` | Manual testing reference |
| Plain Postman (old) | `msc-enrollment/archive/` | Archive |

## What we're migrating to

| Asset | Location |
|-------|----------|
| TestNG tests | `api-test-automation/mobile/enrollment/src/test/java/` |
| Encryption | `jsonapi-encryption` (`MOBILE_TYPE.ENROLLMENT`) |
| Test data builder | `mobile/enrollment/src/main/java/enrollment/util/` |
| SQL (post-check only) | `mobile/enrollment/src/test/resources/sql/enrollment.sql` |
| Config | `stage1.properties` + new `enrollment-uri` |

---

## Step-by-step migration

### 1. Encryption utility

- [ ] Confirm `jsonapi-encryption` JAR builds (`mvn package`)
- [ ] Verify CLI encrypt/decrypt works against Stage1: `-m encrypt -e stage -s enrollment`
- [ ] In Java tests: `configureMobileEncryption(enrollmentUri, MOBILE_TYPE.ENROLLMENT)`
- [ ] **Do not** port Postman prerequest encryption scripts
- [ ] **Do not** port `BeanUtils.setEncryptedProperties()` from legacy

### 2. Test data utility

- [ ] Create `EnrollmentTestDataBuilder` with:
  - [ ] `QAAUTOTEST_ENR_{date}_{time}_{rand}` username
  - [ ] Unique email per username
  - [ ] `Test@123` password
  - [ ] Unique owner + beneficiary SSN
  - [ ] `usernameHash` = Base64(SHA-512(username))
- [ ] Wire into POJO builders via `$$token$$` replacement or direct setters

### 3. Payload formation

- [ ] Create plain JSON templates per step (done in `postman/payloads/plain/`)
- [ ] Map legacy Cucumber data tables → JSON fixtures
- [ ] Use `BaseMobilePOJO` + `@MobileEncrypt` for field-level encryption
- [ ] Keep `prospect.plan` plaintext; `planId` null at prospect, numeric at submit

### 4. Headers

- [ ] `Content-Type: application/json`
- [ ] `x-app-version` from `get.mobile.min.version` SQL or config
- [ ] `Authorization: Bearer {prospectJwt}` for wizard POSTs
- [ ] No `x-enc-aeskey` header needed if `encAesKey` in body (both supported)

### 5. JWT lifecycle

- [ ] Capture `jwtToken` from create-prospect response
- [ ] Reuse same token for all steps 06–13
- [ ] Capture `x-enc-jwttoken` from review-confirm header (member JWT)
- [ ] Do not use member JWT for first enrollment

### 6. Workflow porting

| Legacy Cucumber | New TestNG |
|-----------------|------------|
| `enrollment.feature` happy path | `EnrollmentHappyPathTest` |
| `owner.feature` | `EnrollmentOwnerValidationTest` |
| `beneficiaries.feature` | `EnrollmentBeneficiaryValidationTest` |
| `bankinstruction.feature` | `EnrollmentBankValidationTest` |
| `enrollmentallocation.feature` | `EnrollmentAllocationTest` |
| `subsequentenrollment.feature` | Phase 5 (deferred) |
| `vanguard.feature` | Out of scope |

### 7. Validations

- [ ] Port response assertions only (status, errors, JWT, accountNumber)
- [ ] **No** mid-flow SQL (per team direction)
- [ ] Add post-submit SQL: find account by `QAAUTOTEST_ENR_*` username
- [ ] Port `get.mobile.auth.user` pattern from mobile1 for account lookup

### 8. Environment config

- [ ] Add `enrollment-uri=https://unite-bff-cloud.stage1.unite529.com` to `stage1.properties`
- [ ] Add `enrollment-uri=https://unite-bff-cloud.qc4.unite529.com` to `qc4.properties`
- [ ] Keep `mobile-authentication-uri` for mobile login tests (separate concern)

### 9. CI integration

- [ ] Add enrollment smoke to `bootstrap-testng.xml` / `smoke-testng.xml`
- [ ] Wire `acceptance-stage1` Maven profile
- [ ] Document run command in `mobile/enrollment/README.md`

### 10. Postman handoff

- [ ] Keep Postman collection for manual debugging
- [ ] Document EncryptHelper workflow (not Postman scripts)
- [ ] Plain payloads in `postman/payloads/plain/` as source of truth for JSON shape

---

## What NOT to migrate

| Item | Reason |
|------|--------|
| Cassandra cleanup stepdefs | Integration test infra; not needed for acceptance tests |
| `PrivateCloudPKI` direct usage | Replaced by jsonapi-encryption |
| Full 13-feature Cucumber suite at once | Phased: happy path first |
| Universal web enrollment tests | Different API (`aws-account-web`) |
| QC4 as primary | Stage1 first per team decision |
| Complex Postman prerequest scripts | Source of 500/padding errors |

---

## Success criteria

1. TestNG creates account via enrollment API on Stage1
2. Account findable via `QAAUTOTEST%` SQL pattern
3. Password `Test@123` works for created login
4. No SQL queries during wizard steps
5. Postman collection still works for manual debugging with EncryptHelper
