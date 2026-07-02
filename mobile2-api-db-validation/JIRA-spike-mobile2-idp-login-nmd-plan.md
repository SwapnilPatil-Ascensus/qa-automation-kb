# JIRA Spike — Mobile2 IDP login investigation (NMD plan)

**Assignee:** Sunil Patil  
**Reporter:** Swapnil Patil  
**Epic:** QA-796 (UNITE-MSC Mobile Automation)  
**KB module:** `qa-automation-kb/mobile2-api-db-validation/`  
**Framework repo:** `api-test-automation` → `mobile/mobile1`, `mobile/mobile2`, `universal/jsonapi-auth`  
**Suggested Story Points:** 5  
**Time-box:** 3 days

---

## How to paste in Jira Cloud

1. Create issue → **Spike**
2. Paste **Summary** into the title field
3. Paste **Description** into the Description field (Markdown mode)
4. Paste **Acceptance Criteria** into the AC field (or under Description)
5. Add labels: `unite-msc`, `mobile2`, `spike`, `idp`, `auth`

---

## JIRA — Summary (title)

```
[UNITE-MSC][Mobile2][Spike] IDP login flow — NMD plan auth path and downstream endpoint reuse
```

---

## JIRA — Description (copy below)

**DESCRIPTION — copy below** ↓

## Problem

Mobile2 API automation currently validates endpoints using **NON_IDP** auth (`okdirect` plan) via a direct `POST /mobile1api/v1/mobilemembersession` call. Dashboard and other Mobile2 tests obtain a JWT and call `/mobile2api/v1/mobiledashboard`, etc.

Many production plans — including **NMD (NM Direct)** — use **IDP-enabled login**. The framework already has partial IDP support in Mobile 1 (`MobileBaseRequestTest`, PKCE path when `users.idpEnabled` is true), but **Mobile2 endpoint tests have not been proven end-to-end on an IDP plan**.

Until IDP login is understood and working for a plan like NMD, we cannot confidently reuse existing Mobile2 test patterns (dashboard, activity, etc.) across IDP-enabled plans.

## Goal (spike)

Time-box investigation to answer:

1. **What does it take** to authenticate Mobile2 API tests using an **IDP-enabled plan** (starting with **NMD / `nmdirect` branding**)?
2. Which **auth path** applies: PKCE + OAuth, `/idptokenexchange`, `/mobilememberidptoken`, or a combination?
3. Once IDP login succeeds, can we **reuse the existing Mobile2 endpoint test pattern** (JWT bearer + `X-App-Version`) for dashboard, activity, and other features without rewriting test logic?

## Background

### Current NON_IDP baseline (working)

| Item | Detail |
|------|--------|
| Plan | `okdirect` (`idpEnabled: false`) |
| Auth | `POST /mobile1api/v1/mobilemembersession` with `planId`, `username`, `password` |
| JWT | `_embedded.item.jwtToken` → Bearer on Mobile2 calls |
| Reference test | `mobile2.dashboard.MobileDashboardRequestTest#getMobileDashboard` |
| KB | `mobile2-api-db-validation/JIRA-story-mobile2-qc4-pipeline-dashboard.md` |

### IDP assets already in repo (not yet proven for Mobile2 E2E)

| Item | Location |
|------|----------|
| Mobile 1 base test — PKCE when `idpEnabled` | `mobile/mobile1/.../MobileBaseRequestTest.java` |
| Shared auth client | `universal/jsonapi-auth/.../MobileServerClient.java` |
| Endpoints | `/mobile1api/v1/mobilemembersession`, `/idptokenexchange`, `/mobilememberidptoken` |
| NMD user fixture | `mobile/mobile1/src/test/resources/user/qc4/nmdirect.json` (`idpEnabled: true`) |
| Hawaii IDP fixture | `mobile/mobile2/src/test/resources/user/qc4/hawaii.json` (`idpEnabled: true`) |
| Postman — IDP session | `postman/mobile/Mobile Endpoints (w- IDP Session).postman_collection.json` |
| Postman — PKCE flow | `postman/mobile/README.md` → "Authentication - PKCE (Authorize By Plan - Flow)" |
| Auth alignment doc | `mobile/project-documents/09-SHARED-AUTH-ALIGNMENT.md` |

### Mobile 1 IDP setup pattern (from `MobileBaseRequestTest`)

When `getUsers().isIdpEnabled()` is true:

1. Configure PKCE auth client: `authentication-uri`, `authentication-uri-ui`, `web-client-id`
2. Obtain OAuth access token via PKCE (`getAccessTokenByCode()`)
3. Exchange to mobile JWT via `getMobileToken(accessToken)` → `/mobilememberidptoken`
4. Set Bearer JWT on downstream Mobile1/Mobile2 API calls

Properties required (from `qc4.properties`):

- `mobile-authentication-uri`
- `authentication-uri`
- `authentication-uri-ui`
- `web-client-id`

### Known gap

Local setup guide states: **"Not available yet: NM Direct / IDP runs — do not use `nmdirect.json` for baseline validation."** (`mobile/project-documents/07-LOCAL-SETUP-AND-RUN-GUIDE.md`)

This spike closes that gap.

## Investigation scope

### In scope

- Trace and document the **full IDP login sequence** for NMD (`nmdirect` branding) on **QC4**
- Compare **Postman IDP collections** vs **framework `MobileServerClient`** vs **Mobile 1 `MobileHttpRestApiClient`**
- Identify required **properties**, **headers**, **user fixture fields**, and **environment config** (BFF host, OAuth client, MFA/OTP handling if any)
- Prove **one successful IDP login** → JWT acquisition for NMD plan member
- Prove **one downstream Mobile2 call** (dashboard GET) using that JWT — same pattern as existing NON_IDP test
- Document **blockers** (MFA, OTP, plan config, missing test accounts, BFF routing) in RAID or spike output
- Recommend **follow-up Story** for wiring IDP plan into Mobile2 regression suites

### Out of scope

- Implementing full Mobile2 regression for all features (separate Stories after spike)
- DB validation SQL changes (`mobile2-api-db-validation` SQL layer)
- Modifying UniteMSC / BFF source code
- ABLE or non-NMD IDP plans (document as future expansion only)

## Spike tasks

1. **Inventory** — Map auth paths: NON_IDP vs IDP vs PKCE+exchange; list endpoints and POJOs involved
2. **Postman parity** — Run IDP Postman collection for NMD/NM Direct on QC4; capture request sequence and tokens
3. **Framework trace** — Walk `MobileBaseRequestTest` → `MobileHttpRestApiClient` → `MobileServerClient` for `idpEnabled: true`
4. **NMD fixture** — Validate `nmdirect.json` test user credentials still work on QC4; note MFA/OTP requirements
5. **Vertical slice** — IDP login (NMD) → JWT → `GET /mobile2api/v1/mobiledashboard` (or activity endpoint)
6. **Reuse assessment** — Confirm whether existing Mobile2 test classes need only auth-setup changes vs per-endpoint rework
7. **Output doc** — Auth decision matrix: plan × auth path × properties × test harness changes

## Expected downstream reuse (post-spike)

Once IDP login is sorted for NMD:

| Feature | Existing test / feature | Reuse expectation |
|---------|-------------------------|-------------------|
| Dashboard | `MobileDashboardRequestTest` | Same GET; swap auth setup only |
| Activity | Legacy Cucumber / future Mobile2 tests | Same Bearer JWT pattern |
| Other Mobile2 APIs | `endpoint-registry.yaml` entries | Auth bootstrap only; endpoint logic unchanged |

## References

| Resource | Path |
|----------|------|
| Mobile 1 base test | `api-test-automation/mobile/mobile1/src/main/java/mobile1/MobileBaseRequestTest.java` |
| Shared auth client | `api-test-automation/universal/jsonapi-auth/.../MobileServerClient.java` |
| NMD user fixture | `api-test-automation/mobile/mobile1/src/test/resources/user/qc4/nmdirect.json` |
| Auth alignment | `api-test-automation/mobile/project-documents/09-SHARED-AUTH-ALIGNMENT.md` |
| QC4 dashboard story | `mobile2-api-db-validation/JIRA-story-mobile2-qc4-pipeline-dashboard.md` |
| Endpoint registry | `mobile2-api-db-validation/mappings/endpoint-registry.yaml` |
| RAID — IDP blocker | `docs/mobile-automation-program-hub/09-raid-log.md` (R2) |

## Stakeholders

- **Sunil** — spike owner, auth investigation, Postman/framework parity
- **Swapnil** — QA automation lead, spike review, follow-up Story creation
- **Nick / Dev** — confirm IDP plan config, MFA policy, test-account availability for NMD on QC4

---

## JIRA — Acceptance Criteria (copy below)

**ACCEPTANCE CRITERIA — copy below** ↓

- [ ] **Auth path documented** — written summary (Jira comment or KB doc) describing NON_IDP vs IDP vs PKCE+exchange flows with endpoint sequence diagram or numbered steps
- [ ] **NMD (nmdirect) IDP login proven on QC4** — evidence of successful JWT acquisition (Postman export, curl log, or passing test) with planId/branding documented
- [ ] **One Mobile2 downstream call succeeds** after IDP login — dashboard GET (`/mobile2api/v1/mobiledashboard`) or activity endpoint with Bearer JWT
- [ ] **Property and fixture checklist** — list of required `qc4.properties` keys, user JSON fields, and headers for IDP plans
- [ ] **Reuse assessment** — table showing which existing Mobile2 tests (dashboard, activity, etc.) can reuse current pattern with auth-setup change only
- [ ] **Blockers logged** — MFA/OTP, missing accounts, env config gaps captured in RAID or spike output with owner
- [ ] **Follow-up Story drafted** — at least one Story created (or draft linked) for wiring IDP auth into Mobile2 regression profile(s)

---

## Plain text fallback (if Markdown paste fails)

```
PROBLEM
Mobile2 tests use NON_IDP auth (okdirect). NMD and other plans require IDP login. Mobile 1 has PKCE/IDP support in MobileBaseRequestTest but Mobile2 endpoint tests are not proven on IDP plans.

GOAL
Investigate what it takes to login via IDP for NMD plan on QC4, then confirm existing Mobile2 tests (dashboard, activity) can reuse the same JWT bearer pattern.

IN SCOPE
- Trace IDP auth path (PKCE, idptokenexchange, mobilememberidptoken)
- Postman vs framework parity
- Prove NMD login + one Mobile2 GET on QC4
- Document properties, fixtures, blockers

OUT OF SCOPE
- Full feature regression, BFF code changes, DB validation SQL

REFERENCES
MobileBaseRequestTest.java, MobileServerClient, nmdirect.json, 09-SHARED-AUTH-ALIGNMENT.md, mobile2-api-db-validation KB
```

---

## Related work

| Item | Relationship |
|------|--------------|
| QA-796 epic | Parent |
| JIRA-story-mobile2-qc4-pipeline-dashboard | NON_IDP baseline (okdirect) — this spike extends to IDP |
| NEW-003 OTP/MFA IDP strategy | Related — MFA policy may affect NMD login |
| RAID R2 (IDP config blocks QC4) | May block spike — escalate if hit |
