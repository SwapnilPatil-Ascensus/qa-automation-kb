# QC4 stability checklist — QA Automation perspective

What must be true for **API and UI automation** to run reliably in QC4. This is broader than IDP — use for Kevin's initiative, pipeline design, and regression triage.

---

## 1. Authentication & IDP (highest impact)

| # | Requirement | Why automation needs it |
|---|-------------|-------------------------|
| A1 | **IDP enabled** for target plans (NMD, others per suite) | IDP login / PKCE / mobile IDP flows fail without plan-level IDP |
| A2 | **Reverse proxy** configured per plan | Abhitosh: missing proxy = plan won't route in QC4 |
| A3 | **Client ID / application** in IDP + properties deployed | Token exchange and redirect URIs |
| A4 | **Valid credentials/certs** (not expired) | NMD worked until ~2026-07-10 then broke — likely config/cert |
| A5 | **Metadata loaded in QC4** (not Stage-only) | NY reverted to legacy when QC4 metadata stopped loading |
| A6 | **MFA disabled or bypassed** for automation test users | Blocks unattended CI login |
| A7 | **Auth server stable** (no breaking service-worker deploys) | Kevin meeting: login down during auth server change |

**Teams:** Odyssey (web IDP), Infinity (mobile app), Tandabany/Cole (plan enablement)

---

## 2. Mobile / Unite MSC (API automation)

| # | Requirement | Why |
|---|-------------|-----|
| M1 | **Unite MSC / mobile login microservice** healthy on QC4 BFF | Web IDP can work while mobile returns **401** |
| M2 | **BFF base URL** stable (`unite-bff-wtn.qc4.unite529.com` or current canonical) | Pipeline and RestAssured config |
| M3 | **Non-IDP path** (`okdirect`) for Mobile2 baseline | IDP spike separate; need green slice without IDP |
| M4 | **Test members** exist in QC4 DB with known passwords | `user/qc4/*.json` fixtures |

**Teams:** Infinity (Luis/Rich), DevOps (RT 514351 pattern)

---

## 3. Data preservation (Kevin Excel / DB refresh)

| # | Data domain | Tables / objects | Automation dependency |
|---|-------------|------------------|------------------------|
| D1 | IDP auth | `client.*`, `person.credentials`, `person.profile` | Login for all IDP plans |
| D2 | Login/session | `TA_LOGIN*`, `TA_SESSION*`, `TA_COOKIE`, `TA_APP_CONTEXT` | Session-based flows, legacy paths |
| D3 | Partner API auth | `TAPI_PARTNER_AUTH*`, `TAPI_ENTITLEMENT*`, `TAPI_PARTNER_ENTITLEMENT_REL*` | API gateway / partner auth tests |
| D4 | Plan metadata | `TU_TRAUNCH*`, `TU_CODES`, fund/txn metadata (`TENV_*`, `TU_TXN_*`, etc.) | Plan routing, enrollment, withdrawals |
| D5 | Test accounts | `TU_ACCT`, `TU_MEMBER`, `TU_FUND_BALANCE` (known automation accounts) | Repeatable regression — not random prod-like data |
| D6 | Enrollment packages | `UP_ENROLLMENT*.pkb`, `UP_ACCOUNT_529_V2.pkb` | Advisor enrollment API (QC4 POST path per Excel) |
| D7 | CSR test users | Per DB refresh scripts in `docs/DB Refresh/` | V2/V3 CSR regression |

**Note:** Excel rows 11–136 are **reference/metadata tables** (tagged PHUONG) — automation benefits if preserved but **D1–D5 are critical path**.

---

## 4. Environment & pipeline discipline

| # | Requirement | Why |
|---|-------------|-----|
| E1 | **QC4 reserved for stable validation** — dev work in separate env | Abhitosh: reduces false failures in nightly regression |
| E2 | **No daily deploy removing auth bypass / config** without notice | SYN-443 barcode: JAR removed → 404/503 |
| E3 | **Env-health probe** in CI before suite run | Distinguish outage vs test failure |
| E4 | **Documented plan list** enabled for automation | Avoid testing plans not configured in QC4 |
| E5 | **Splunk/read access** for triage (optional RT) | Faster root cause on 5xx/timeouts |

---

## 5. Automation suites affected

| Suite | Repo / path | QC4 dependency |
|-------|-------------|----------------|
| V2/V3 nightly regression | `prime-test-automation` | IDP login, enrollment, CSR |
| Universal Enrollment API | `api-test-automation` | Enrollment APIs, IDP tokens |
| Mobile2 API | `api-test-automation/mobile/mobile2` | BFF auth + dashboard |
| Unite MSC perf | `performance-test-automation` | IDP + non-IDP login YAML |
| Performance regression (future) | Jenkins / GitLab | Stage 1 preferred today; QC4 for PR gates |

---

## 6. Suggested “definition of stable” for QC4 (QA sign-off)

QC4 is **automation-ready** when:

- [ ] **≥1 IDP plan** (NMD) and **≥1 non-IDP plan** (okdirect) pass login smoke
- [ ] **Mobile2 dashboard** API test green on QC4 CI
- [ ] **IDP web login** smoke green for NMD (no blank page)
- [ ] **Metadata** present in QC4 for automation plans (not legacy fallback)
- [ ] **Preservation list** applied on refresh for D1–D5
- [ ] **No known auth-server outage** / post-refresh enablement complete (~1 week per Kevin)

---

## 7. Open actions (Swapnil)

| Action | Owner |
|--------|-------|
| Submit Excel inputs to Kevin | Swapnil — [03-kevin-excel-inputs.md](./03-kevin-excel-inputs.md) |
| Confirm plan list in chat → Cole stories | Swapnil + Kevin |
| Escalate mobile MSC 401 if still failing | Infinity via Rajib if needed |
| Request auth admin portal access | RT — triage expired clients |
| Link preservation doc to SharePoint squad page | After SharePoint access confirmed |
