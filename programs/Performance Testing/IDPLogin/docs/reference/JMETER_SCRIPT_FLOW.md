# JMeter Script Flow — idp-login-resources.jmx

Script: `performance/universal-platform/idp/jmeter/idp-login-resources.jmx`  
Test plan name: **IDP Member Login (CS/API)**

## Variables & setup

### CSV data (`idp-login-${env}.csv`)

| CSV column | JMeter variable | Usage |
|------------|-----------------|-------|
| plan-prefix | `plan-prefix` | Domain + template path |
| username | `userUsernameEncrypt` | Decrypted to `userUsername` |
| password | `userPasswordEncrypt` | Decrypted to `userPassword` |
| account | `account` | Assertion on overview page |

### Domain setup (JSR223 PreProcessor)

```groovy
domain-host  = {plan-prefix}.{env}.acs529.com     // e.g. nyd.stage1.acs529.com
cdn-host     = cdn.{env}.acs529.com
plan-tpl     = /{prefix}tpl                       // 2-char plans use first 2 chars: idd→/idtpl, mod→/motpl
sardine-api-host = api.sandbox.sardine.ai
```

### Environment properties (from Taurus/Jenkins)

| Property | Source | Example |
|----------|--------|---------|
| `env` | `jenv` | `stage1` |
| `encryption` | `jencryption` | `false` |
| `throughput` | `jmthroughput` | `600` |

## Transaction flow (reported in BlazeMeter)

| Step | Label | Method | Target | Key extractions / assertions |
|------|-------|--------|--------|------------------------------|
| 0 | Credential Decryption | JSR223 | — | Decrypt username/password if encrypted |
| 1 | LoginLanding (CS) | GET | `${plan-tpl}/authentications/loginLandingIDP.cs` | Extract client_id, auth/token endpoints, redirect_uri, scope. Assert 200, not "unavailable" |
| 2-1 | Authorize (IDP) | GET | `${authorization-host}${authorization-path}` | PKCE challenge/verifier, Sardine key. Assert 301/302. Extract login-host/path |
| 2-2..2-32 | Static Login Resources (JS) | GET | Various JS on `${domain-host}` and CDN | Assert 200. Hidden from main report labels (sub-samplers) |
| 3 | Login (IDP) - GET Login | GET | `${login-host}${login-path}` | Assert 200 |
| 4-1 | Login (IDP) - POST Login | POST | `${login-host}${login-path}` | username, password, x-sardine-session-key. Assert 301/302. Extract redirect URL |
| 4-2 | MFA - GET Request PIN | GET | `services/mfa/login/request-pin` | Assert 200 (MFP-disabled users skip actual MFA) |
| 4-3 | MFA - GET Verify PIN | GET | `services/mfa/login/verify-pin` | Assert 200 |
| 5 | Login (IDP) - GET Authorize Continue | GET | Redirect from POST login | Assert redirect chain |
| 6 | Callback/Token (CS) - Get Callback | GET | `${url}` (redirect URI) | Assert 200. **Extract `session-host`** from form action |
| 7 | Callback/Token (IDP) - Get Access Token | POST | `${token-host}${token-path}` | grant_type=authorization_code. Extract `access_token`, `signing_key` |
| 8 | Session/Overview (CS) | **POST** | `${session-host}` (= createSessionIDP.cs) | accessToken, x-sardine-session-key. Assert 200. Body contains "Welcome back", "My Accounts", `${account}` |
| 8-A-1 | Auth Custom Banner (CS) | GET | `${plan-tpl}/auth/customBannerMessage.cs` | Assert 200, not unavailable |
| 8-A-2 | Auth Side Banner (CS) | GET | `${plan-tpl}/auth/sideBannerMessage.cs` | Assert 200, not unavailable |
| 8-A-3 | AL Custom Banner (CS) | GET | `${plan-tpl}/al/customBannerMessage.cs` | Session cookie. Assert 200 |
| 8-A-4 | AO Custom Banner (CS) | GET | `${plan-tpl}/ao/customBannerMessage.cs` | Session cookie. Assert 200 |
| 8-A-5 | AO Overview (CS) | GET | `${plan-tpl}/ao/overview.cs` | Session cookie. Assert 200 |
| 8-A-6 | AL List (CS) | GET | `${plan-tpl}/al/list.cs` | Session cookie. Assert 200 |
| 8-1 | Static Overview Resource (JS) | GET | CDN JS files | Optional — may be enabled/disabled |
| 9 | Logout (CS) | GET | `${plan-tpl}/auth/lo.cs` | Assert 200 |

## Important notes

### Step 8 is POST; steps 8-A-* are the new GET pages

The BlazeMeter label "Session/Overview" is a **POST** to `createSessionIDP.cs`. Steps **8-A-1 through 8-A-6** are the new GET requests for banner and dashboard `.cs` pages (implemented in `scripts/jia-banner-post-login/idp-login-resources.jmx`).

### Cookie manager

- HTTP Cookie Manager is enabled at thread group level
- `clearEachIteration=false` — cookies persist through the login flow
- Session-required new pages (al/ao banners) depend on cookies set during step 8

### Throughput control

- `ConstantThroughputTimer` on step 1 caps overall request rate to `${throughput}` per minute

### Error handling

- Thread group: `on_sample_error=startnextloop` — one failed iteration does not stop the test
- Setup thread: `on_sample_error=stoptestnow` — key file load failure stops test

### Concurrent pool

Most HTTPSamplers use `concurrentPool=6` for connection reuse.

## Include files

- `authentication/decryption.jmx` — loaded in Setup Thread for credential decryption key

## Post-login pages (implemented)

Controller `8-A. Post-Login Dashboard Pages (CS)` — see `scripts/jia-banner-post-login/CHANGELOG.md`.

## Include files
