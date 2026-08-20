# Mobile Microservices API Automation — TODO Tracker

| ID | Priority | Task | Status | Dependency | Notes |
|----|----------|------|--------|------------|-------|
| TODO-READY-01 | High | GET Plans readiness analysis (`04-FIRST-ENDPOINT-READINESS.md`) | **Done** | — | Legacy + framework patterns documented; no Java added |
| TODO-READY-02 | High | Luis QC4 discussion checklist (`05-LUIS-QC4-DISCUSSION-CHECKLIST.md`) | **Done** | — | Manual Postman rows still Pending |
| TODO-POSTMAN-01 | Medium | Decide whether to create a sanitized Mobile MSC Postman template under tracked `postman/mobile/collections` | Deferred | Luis / Nick guidance | Do not commit raw local JSON |
| TODO-QC4-01 | High | Confirm correct QC4 Enrollment base URL | Open | Luis / developer | BFF vs direct microservice |
| TODO-QC4-02 | High | Confirm auth chain for Enrollment | Open | Luis / developer | Mobile JWT vs IDP exchange |
| TODO-QC4-03 | High | Validate `GET /enrollmentapi/v1/plans` manually in Postman | Open | QC4 route | Must return 200 before automation |
| TODO-AUTO-01 | High | Implement first GET Plans TestNG smoke test | Blocked | TODO-QC4-03 | Do not start yet |
| TODO-SEC-01 | Medium | Confirm whether pre-existing tracked QC4 Postman client credentials are active and should be rotated | Open | Nick / repository owner | Do not expose values; pre-existing asset not introduced by pilot |
| TODO-M2-01 | High | Inspect Mobile 2 Dashboard endpoint | Open | Postman + source repo | First real vertical slice |
| TODO-AUTH-01 | High | Confirm non-IDP JWT retrieval flow | **Done** | — | Mobile 2 shared-auth smoke PASS (QC4) |
| TODO-AUTH-02 | High | Confirm IDP token exchange flow | **Done** | — | Mobile 2 shared-auth smoke PASS (QC4) |
| TODO-AUTH-03 | High | Wire shared `MobileServerClient` into unite-mobile2 | **Done** | Release 0.8 | Mobile 1 already on shared client |
| TODO-AUTH-04 | Medium | Extract HTML reporting to shared module | **Done** | Release 0.8 | `mobile-ms-reporting` |
| TODO-M2-02 | High | Implement Mobile 2 Dashboard non-IDP smoke test | Blocked | Shared auth proven | First real API test |
| TODO-M2-03 | High | Mobile 2 shared-auth smoke (`Mobile2SharedAuthSmokeTest`) | **Done** | Release 0.8 | NON_IDP + IDP via `MobileServerClient` |
| TODO-ENC-01 | Medium | Obtain approved Enrollment encryption contract | Open | Dev team | Do not implement from assumptions |
| TODO-ENC-02 | Medium | Identify reusable encryption library or Postman pre-request script | Open | Dev team | Avoid custom crypto unless required |
| TODO-REBASE-01 | High | Rebase Mobile MS branch onto `main` and resolve conflicts | **Done** | — | See `99-CURSOR-STATUS-EXPORT.md` Rebase section |
| T-006 | P1 | Add `enrollment-service-uri` (or approved key) to config pattern | Blocked | TODO-QC4-01 | No secrets in Git |
| T-008 | P1 | Update `smoke-testng.xml` with API test class | Blocked | TODO-AUTO-01 | Keep bootstrap separate |
| T-009 | P1 | Update `regression-testng.xml` when smoke stable | Blocked | T-008 | |
| T-010 | P2 | Validate local script for smoke suite | Blocked | T-008 | `run-mobile-ms-local.ps1` |
| T-011 | P2 | Migrate content GET (`/content`) | Blocked | TODO-AUTO-01 | Wave 1 #2 |
| T-012 | P2 | Migrate metadata calendar GET (BFF auth check) | Blocked | TODO-QC4-02 | Not enrollment MS |
| T-013 | P2 | Migrate plan-by-id GET | Blocked | TODO-AUTO-01 | Wave 1 #4 |
| T-014 | P3 | Migrate bank-entered POST | Blocked | TODO-QC4-02, crypto SME | After 404 + encryption clarity |
| T-018 | — | Pipeline / CI integration | Deferred | Pilot stable | Explicitly out of scope |
