# Auth and session

How mobile2 Cucumber tests authenticate and how that maps to validation.

## Member session bootstrap

Stepdefs (`MobileDashboardStepdefs.java`):

```java
// Acceptance test JWT — no member password in BFF call
GET {MOBILE2_SERVICE_URL}/mobile2api/v1/mobilemembers/{planId}/{username}
→ AccountGateway.getMember(identity, planId, username)
→ unite-account GET /accountapi/v1/members/{planId}/{username}
```

Returns `MobileMember` with `id` (uii_member_id) stored in `Mobile2World`.

**DB validation:** resolve same member via `ta_login.username` + account `traunch_id` (see `sql/account/resolve-member-by-username.sql`).

## Verified factors

```java
@Given("Mobile2 request has Identity with verified factors {string} and {string}")
```

Sets `Mobile2World.verifiedFactors` (e.g. `PASSWORD`, `SMS`).

Dashboard and other member endpoints use:

```java
Mobile2BaseStepDefs.jwtMemberRequestWithVerifiedFactors(scenario, memberId, verifiedFactors)
```

JWT encodes member identity + verified factor claims required by BFF filters.

## JWT roles by gateway call

| Operation | Role | Gateway method |
|-----------|------|----------------|
| Member data reads | MEMBER | `BaseGatewayUtil.getMemberJwtToken` |
| Username lookup in tests | ASCENSUS_COLLABORATOR | `getTrustedCollaboratorJwtToken` |
| Acceptance mobilemembers | Test harness token | `jwtAcceptanceTestRequest` |

Validation SQL runs **without JWT** — use direct JDBC with test DB credentials.

## mobilemembers endpoint

| Property | Value |
|----------|-------|
| BFF path | `GET /mobile2api/v1/mobilemembers/{planId}/{username}` |
| planId | Plan branding (e.g. `upromise`), not traunch numeric id |
| Response | `MobileMember` in `_embedded.item` |
| Key field | `id` → uii_member_id for subsequent calls |

## Test users (recurring fixtures)

| planId | username | password (feature) | traunchId |
|--------|----------|-------------------|-----------|
| upromise | ssgauser01 | Letmein11 | 100001 |

Use these consistently across validation bind variables.

## Skip auth DB

`unite-auth` and IdP issue tokens — no SQL validation for auth flows in this KB.
