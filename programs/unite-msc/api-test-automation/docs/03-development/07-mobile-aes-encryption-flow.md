# Mobile AES Encryption — Framework Flow

How the **`api-test-automation`** framework generates, wraps, sends, and reuses AES keys for mobile MSC APIs (enrollment, mobile1, mobile2). Use this when writing or reviewing encrypted POST tests, debugging decrypt failures, or onboarding to `@MobileEncrypt` POJOs.

**Related docs**

| Doc | Scope |
|-----|--------|
| [Enrollment encryption (Postman / CLI)](../msc-enrollment/docs/04-encryption-guide.md) | Manual E2E, field lists, `EncryptHelper` CLI flags |
| [Enrollment wizard guide](../../../msc-enrollment/docs/12-automation-team-guide.md) | Step-by-step automation for enrollment |
| `api-test-automation/mobile/enrollment/ENROLLMENT-WIZARD-GUIDE.md` | In-repo wizard conventions |

---

## Two keys — do not confuse them

| Name | Where it lives | Format | Purpose |
|------|----------------|--------|---------|
| **`aesKey`** | Test-side only — `BaseMobilePOJO.aesKey` (not serialized to JSON) | `{base64AesKey};{base64Iv}` | Encrypt request fields; decrypt response fields in tests |
| **`encAesKey`** | Sent in the API JSON body | Base64(RSA-encrypted `aesKey` string) | Server decrypts with its private key to obtain the session AES key |

```text
  Test POJO                         API JSON body
  ┌─────────────────┐              ┌──────────────────────────┐
  │ aesKey (plain)  │──RSA wrap──► │ encAesKey (in payload)   │
  │ key;iv          │              │ + encrypted PII fields   │
  └─────────────────┘              └──────────────────────────┘
         │
         └── kept via getAesKey() for response decrypt
```

---

## End-to-end sequence (TestNG)

```mermaid
sequenceDiagram
    participant Test as Test class<br/>(e.g. OwnerEnteredTests)
    participant Base as EnrollmentBaseTest
    participant POJO as BaseMobilePOJO
    participant EH as EncryptHelper
    participant MEH as MobileEncryptionHelper
    participant Cert as BFF GET /certificate
    participant API as MSC API

    Note over Test,Base: Once per test class (@BeforeClass)
    Test->>Base: configureMobileEncryption(enrollment-uri, ENROLLMENT)
    Base->>Base: JsonApiResourceManager.setProperty<br/>MOBILE_ENVIRONMENT_URL, MOBILE_STREAM

    Note over Test,API: Per encrypted POST
    Test->>POJO: loadJsonFile(...) / build request
    Test->>Base: toEncryptedArrayPayload(request)
    Base->>POJO: createMobilePayload()

    POJO->>POJO: generateAesKey() if aesKey == null
    POJO->>EH: prepareMobileEncryption(url, stream, aesKey)
    EH->>MEH: prepare(url, stream, aesKey)
    MEH->>MEH: write aeskey.txt (debug/CLI)
    MEH->>Cert: GET {url}/{stream}api/v1/certificate
    Cert-->>MEH: RSA public certificate
    MEH->>MEH: RSA-encrypt aesKey → encAesKey
    MEH-->>POJO: MobileEncryptionSetup(cipher, encAesKey)

    POJO->>POJO: addMobileFields — encAesKey, usernameHash
    POJO->>POJO: encryptMobileFields (@MobileEncrypt)
    POJO-->>Base: JSON string
    Base-->>Test: "[" + json + "]"

    Test->>API: POST encrypted body (+ Bearer JWT if wizard step 2+)
    API-->>Test: response (some fields may be encrypted)

    opt Decrypt response in test
        Test->>POJO: response.setAesKey(request.getAesKey())
        Test->>POJO: response.decryptMobileFields()
    end
```

---

## `createMobilePayload()` flowchart

```mermaid
flowchart TD
    A[createMobilePayload called] --> B{aesKey set?}
    B -->|No| C[EncryptHelper.generateAesKey]
    B -->|Yes| D[Use existing aesKey]
    C --> E[Store on POJO via setAesKey]
    D --> E
    E --> F[EncryptHelper.prepareMobileEncryption]
    F --> G[Fetch RSA cert from BFF<br/>cached per env + stream]
    G --> H[RSA-encrypt aesKey → encAesKey]
    H --> I[Build AES Cipher]
    I --> J[addMobileFields]
    J --> K[Set encAesKey on POJO]
    J --> L[If username present → SHA-512 usernameHash]
    K --> M[copy POJO]
    L --> M
    M --> N[encryptMobileFields on copy]
    N --> O{Field has @MobileEncrypt?}
    O -->|String| P[EncryptHelper.encryptStringWithSetup]
    O -->|Nested BaseMobilePOJO| N
    O -->|List of POJOs| N
    O -->|Other| Q[Leave as-is]
    P --> R[convertToJson → return]
    Q --> R
```

---

## AES key generation

**Class:** `MobileEncryptionBootstrap.generateAesKeyWithIv()`  
**Called via:** `EncryptHelper.generateAesKey()` → `BaseMobilePOJO.generateAesKey()`

| Step | Detail |
|------|--------|
| Algorithm | AES-256 |
| IV | 16 random bytes |
| Output format | `Base64(keyBytes) + ";" + Base64(ivBytes)` |

**Manual override** (reuse same key across multiple encrypt calls in one test):

```java
request.setAesKey("existingBase64Key;existingBase64Iv");
request.createMobilePayload(); // uses provided key, does not regenerate
```

---

## Certificate fetch and RSA wrap

**Class:** `MobileEncryptionHelper.prepare()`

```text
GET {MOBILE_ENVIRONMENT_URL}/{MOBILE_STREAM}api/v1/certificate
     ↓
_embedded.item.certificate  (RSA public key PEM)
     ↓
RSA encrypt plain aesKey string (UTF-8 bytes)
     ↓
Base64 → encAesKey (sent in JSON)
```

| `MOBILE_STREAM` | API path segment | Example cert URL (Stage1) |
|-----------------|------------------|---------------------------|
| `ENROLLMENT` | `enrollmentapi/v1/` | `https://unite-bff-cloud.stage1.unite529.com/enrollmentapi/v1/certificate` |
| `MOBILE1` | `mobile1api/v1/` | `.../mobile1api/v1/certificate` |
| `MOBILE2` | `mobile2api/v1/` | `.../mobile2api/v1/certificate` |

Certificates are **cached in memory** per `{environmentUrl}:{stream}` for the JVM run.

---

## Test setup — configure once per class

**Enrollment example** (`EnrollmentBaseTest.setupBeforeAll`):

```java
configureMobileEncryption(getProperty("enrollment-uri"), MOBILE_TYPE.ENROLLMENT);
```

**`BaseRequestTest.configureMobileEncryption()`** stores:

| Property | Example |
|----------|---------|
| `MOBILE_ENVIRONMENT_URL` | `https://unite-bff-cloud.stage1.unite529.com` |
| `MOBILE_STREAM` | `ENROLLMENT` |

`BaseMobilePOJO.createMobilePayload()` reads these from `JsonApiResourceManager` at runtime.

---

## Building the request body

```text
EnrollmentBaseTest.toEncryptedArrayPayload(request)
    → "[" + request.createMobilePayload() + "]"
```

Enrollment BFF expects encrypted wizard POSTs as a **one-element JSON array**.

### Fields added automatically

| Field | When | How |
|-------|------|-----|
| `encAesKey` | Always (mobile POST) | RSA-wrapped AES key from setup |
| `usernameHash` | When plain `username` is set on POJO | `SHA-512(username)` → Base64 |

`username` is typically `@JsonIgnore` on the POJO — used only to compute the hash, not sent in JSON.

### Fields encrypted

Any field annotated with **`@MobileEncrypt`** (String, or `List<String>`). Encryption walks nested `BaseMobilePOJO` objects recursively.

**Enrollment POJOs with `@MobileEncrypt`:** `ProspectSectionPOJO`, `OwnerPOJO`, `BankPOJO`, `BeneficiaryPOJO`, `BankVerifyRoutingRequestPOJO.routingNumber`, `BankVerifyRoutingNumberResponsePOJO.routingNumber`, etc.

---

## Decryption flow

```mermaid
flowchart TD
    A[decryptMobileFields called] --> B{aesKey set on POJO?}
    B -->|No| C[Throws / fails decrypt]
    B -->|Yes| D[DecryptHelper.decryptString per @MobileEncrypt field]
    D --> E[MobileEncryptionBootstrap.createDecryptionCipher]
    E --> F[Decrypt.createAesCipher from qa-resource-encryption JAR]
    F --> G[Base64 decode → AES decrypt → plain string]
    G --> H[Set field on POJO]
```

**Skip during decrypt:** `encAesKey`, `encryptedAesKey`, numeric strings, literal `"null"`.

### Request → response reuse (enrollment example)

`VerifyBankRoutingNumberRequestTest`:

```java
HttpRestApiClientResponse response = client.invokeRestApi(
        RestType.POST, VERIFY_ROUTING_PATH, null,
        toEncryptedArrayPayload(request), BodyType.JSON, null);

BankVerifyRoutingNumberResponsePOJO responseBody =
        response.convertToListPOJO(BankVerifyRoutingNumberResponsePOJO.class).get(0);

responseBody.setAesKey(request.getAesKey());
responseBody.decryptMobileFields();
assertEquals(responseBody.getRoutingNumber(), routingNumber);
```

After `toEncryptedArrayPayload(request)`, **`request.getAesKey()`** holds the plain key used for that request.

---

## What is reused vs regenerated

```mermaid
flowchart LR
    subgraph Per test class
        A[configureMobileEncryption] --> B[MOBILE_ENVIRONMENT_URL + MOBILE_STREAM]
    end

    subgraph Per wizard step / POST
        C[new POJO from JSON] --> D[createMobilePayload]
        D --> E[New aesKey unless setAesKey called]
    end

    subgraph Across wizard steps
        F[ProspectSessionContext JWT] --> G[Steps 2+ Bearer auth]
    end

    E -.->|NOT shared across steps| G
```

| Artifact | Reused across wizard? | Notes |
|----------|----------------------|-------|
| Prospect JWT | **Yes** — `ProspectSessionContext` | Set in `ProspectRequestTest` |
| `aesKey` | **No** — new key per `createMobilePayload()` | Unless you call `setAesKey()` first |
| RSA certificate | **Yes** — JVM cache | Per env + stream |
| `aeskey.txt` | Side-effect file | Written on each `prepare()`; used by CLI decrypt |

---

## Class map (by layer)

```mermaid
flowchart TB
    subgraph Tests
        T1[EnrollmentBaseTest]
        T2[OwnerEnteredTests / ProspectRequestTest / ...]
        T3[VerifyBankRoutingNumberRequestTest]
    end

    subgraph jsonapi-core
        B1[BaseRequestTest]
        B2[BaseMobilePOJO]
        B3["@MobileEncrypt"]
        B4[JsonApiResourceManager]
    end

    subgraph jsonapi-encryption
        E1[EncryptHelper]
        E2[MobileEncryptionHelper]
        E3[MobileEncryptionBootstrap]
        E4[MobileEncryptionSetup]
        E5[DecryptHelper]
        E6[RunnerHelper]
        E7[Runner / Converter CLI]
        E8[EncryptionConstants.MOBILE_TYPE]
    end

    subgraph External JAR
        X1[qa-resource-encryption<br/>Encrypt / Decrypt]
    end

    T2 --> T1 --> B1
    T2 --> B2
    T3 --> B2
    B2 --> E1
    B1 --> B4
    E1 --> E2 --> E3 --> X1
    E5 --> E3 --> X1
    E2 --> E6
    B2 --> E5
```

| Class | Module | Responsibility |
|-------|--------|----------------|
| `BaseRequestTest` | jsonapi-core | `configureMobileEncryption()` — env properties |
| `EnrollmentBaseTest` | mobile/enrollment | Calls configure + `toEncryptedArrayPayload()` |
| `BaseMobilePOJO` | jsonapi-core | `aesKey` field; `createMobilePayload()` / `decryptMobileFields()` |
| `@MobileEncrypt` | jsonapi-encryption | Marks encryptable String fields |
| `EncryptHelper` | jsonapi-encryption | Public API: generate, prepare, encrypt string |
| `MobileEncryptionHelper` | jsonapi-encryption | Cert fetch, RSA wrap, JSON field encryption |
| `MobileEncryptionBootstrap` | jsonapi-encryption | AES key+IV generation, cipher factory |
| `MobileEncryptionSetup` | jsonapi-encryption | Holds `Cipher` + `encryptedAesKey` for one request |
| `DecryptHelper` | jsonapi-encryption | `decryptString()`, JSON decrypt |
| `Encrypt` / `Decrypt` | qa-resource-encryption | Low-level `createAesCipher`, `createRsaCipher`, Base64 |
| `RunnerHelper` | jsonapi-encryption | Read/write `aeskey.txt`, `encrypt.txt`, `decrypt.txt` |
| `Runner` | jsonapi-encryption | CLI encrypt/decrypt (`-m encrypt|decrypt`) |
| `EncryptionConstants` | jsonapi-encryption | `MOBILE_TYPE`, environment URL resolution |

---

## CLI path (Postman / manual)

Same crypto stack, invoked outside TestNG:

```powershell
cd C:\Workspace\GitLab\api-test-automation\jsonapi\jsonapi-encryption
mvn package -DskipTests

java -cp target/jsonapi-encryption-*.jar core.encryption.runner.Runner `
  -m encrypt -e stage -s enrollment -f encrypt.txt
```

```mermaid
flowchart LR
    A[encrypt.txt plain JSON] --> B[Runner.main]
    B --> C[EncryptHelper.encrypt]
    C --> D[MobileEncryptionHelper.prepare]
    D --> E[aeskey.txt written]
    D --> F[Encrypted JSON to console]
    F --> G[Paste into Postman body]

    H[response.json] --> I[Runner -m decrypt]
    E --> I
    I --> J[Plain JSON to console]
```

| CLI flag | Encrypt | Decrypt |
|----------|---------|---------|
| `-m` | `encrypt` | `decrypt` |
| `-e` | `stage`, `qc4`, `dev`, `local8080`, `local8200` | — |
| `-s` | `enrollment`, `mobile1`, `mobile2` | — |
| `-f` | Input file | Input file |
| `-a` | Optional AES key (auto-generated if omitted) | AES key (default: `aeskey.txt`) |

See [Enrollment encryption guide](../msc-enrollment/docs/04-encryption-guide.md) for Postman workflow and field lists.

---

## Enrollment wizard — encryption touchpoints

```text
ProspectRequestTest          → toEncryptedArrayPayload (new aesKey)
EnrollmentContentRequestTest → GET only (no encryption)
OwnerEnteredTests            → toEncryptedArrayPayload (new aesKey)
BankEnteredRequestTests      → toEncryptedArrayPayload (new aesKey)
BeneficiaryEnteredTests      → toEncryptedArrayPayload (new aesKey)
VerifyBankRoutingNumberRequestTest → encrypt + decrypt response with request.getAesKey()
AllocationsEnteredRequestTests → toEncryptedArrayPayload (new aesKey)
```

---

## Troubleshooting

| Symptom | Likely cause | Check |
|---------|--------------|-------|
| `Failed to add mobile fields` / cert error | Wrong `enrollment-uri` or stream | `configureMobileEncryption` URL matches target env |
| Decrypt returns garbage | Wrong `aesKey` on response POJO | `setAesKey(request.getAesKey())` from **same** request |
| `Invalid AES key` | Malformed key string | Must be `base64Key;base64Iv` |
| Padding exception in Postman | Double encryption or stale cipher text | Encrypt from plain JSON only; regenerate |
| `usernameHash` missing | `username` not set on POJO before encrypt | `request.setUsername(...)` before `createMobilePayload()` |
| `aeskey.txt` out of sync | Multiple parallel tests writing same file | File is debug aid; tests use in-memory `getAesKey()` |

---

## Source file index (`api-test-automation`)

| Path | Role |
|------|------|
| `jsonapi/jsonapi-core/src/main/java/core/pojo/common/BaseMobilePOJO.java` | Core encrypt/decrypt POJO logic |
| `jsonapi/jsonapi-core/src/main/java/core/test/BaseRequestTest.java` | `configureMobileEncryption()` |
| `jsonapi/jsonapi-encryption/src/main/java/core/encryption/helper/EncryptHelper.java` | Encryption facade |
| `jsonapi/jsonapi-encryption/src/main/java/core/encryption/helper/MobileEncryptionHelper.java` | Cert + RSA + field encrypt |
| `jsonapi/jsonapi-encryption/src/main/java/core/encryption/helper/MobileEncryptionBootstrap.java` | Key generation |
| `jsonapi/jsonapi-encryption/src/main/java/core/encryption/helper/DecryptHelper.java` | Decryption |
| `jsonapi/jsonapi-encryption/src/main/java/core/encryption/runner/Runner.java` | CLI entry point |
| `jsonapi/jsonapi-encryption/docs/Readme.txt` | JAR build and CLI notes |
| `mobile/enrollment/src/test/java/EnrollmentBaseTest.java` | `toEncryptedArrayPayload()` |
| `mobile/enrollment/src/test/java/VerifyBankRoutingNumberRequestTest.java` | Request → response aesKey reuse |
| `jsonapi/jsonapi-core/src/test/java/core/pojo/common/BaseMobilePOJOTest.java` | Unit tests for `BaseMobilePOJO` |

---

## Maintenance

- Update this doc when `BaseMobilePOJO`, `MobileEncryptionHelper`, or enrollment encrypt patterns change.
- Keep [msc-enrollment encryption guide](../msc-enrollment/docs/04-encryption-guide.md) aligned for Postman/CLI; link here for Java/TestNG internals.
