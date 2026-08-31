# Unite MSC — Status Update for Kevin Daines

**Date:** Thursday, August 20, 2026  
**From:** Swapnil Patil / QA Automation (AM Squad)  
**Re:** Unite MSC test coverage — enrollment progress & program close-out plan  
**Previous update:** [2026-08-07-kevin-status-update.md](2026-08-07-kevin-status-update.md)

---

## Email draft *(leadership — send this)*

**To:** Kevin Daines  
**Cc:** Rajeev, Henry *(as needed)*  
**Subject:** Unite MSC — Weekly Status (Aug 2026)

Hi Kevin,

Quick update on Unite MSC since our August 7 note.

**Where we stand**

| Area | Status | Coverage |
|------|--------|----------|
| Mobile 2 | Complete | **100%** (25/25 endpoints) |
| Mobile 1 | Complete | **100%** (26/26 endpoints) |
| Enrollment | In progress | **60%** of endpoint catalog (15/25) · **94%** of core happy-path flow (15/16 steps) |
| CI / Pipelines | In parallel | M1/M2 validated on Stage1; GitLab nightly in flight; enrollment CI to follow |

**Mobile 1 & 2** are ready for sign-off — automated, suite-routed, and available on Stage1/QC4.

**Enrollment** has moved forward meaningfully. The team has TestNG automation in place for prospect through allocations (owner, bank, beneficiary, routing, allocations, plus bootstrap smoke tests). Against our Postman/Excel source of truth, **one core step remains — submit (`review-confirm-entered`)** — before we can automate full account creation on Stage1. Postman E2E already passes this step; we are closing the same gap in Java this sprint.

**This sprint — coding complete (not full program close):**
- Submit step + suite wiring (okdirect / newyork)
- Stage1 green end-to-end run with post-submit account verification

**Following sprint — program close-out (~1 dedicated resource):**
- Documentation, coverage metrics, enhancement backlog
- qTest manual cases *(in progress)*, Postman→Bruno handover, KT to sustaining team
- GitLab enrollment job, sign-off package

**Rest of squad** can pivot to the next priority in parallel once enrollment coding lands — we are **not walking away from MSC entirely**; one person wraps up handover for about a sprint.

Partner/subsequent/OAuth flows remain out of scope per the endpoint catalog.

Happy to fill out your Friday list or join a brief call if useful.

Thanks,  
Swapnil

---

## Email draft *(detailed reference — do not send)*

**To:** Kevin Daines  
**Cc:** Rajeev/Rajib, Henry *(as needed)*  
**Subject:** Unite MSC — Enrollment Progress & Sprint Close-Out Plan (Aug 2026)

Hi Kevin,

Following up on our August 7 update — here is where Unite MSC stands today, with enrollment as the active focus.

### Overall

| Area | Status | Coverage (approx.) |
|------|--------|-------------------|
| **Mobile 2** | **Complete** | **100%** — 25/25 in-scope business endpoints |
| **Mobile 1** | **Complete** | **100%** — 26/26 in-scope business endpoints |
| **Enrollment** | **In progress — not complete** | **15/25 endpoints coded (60%)** vs Excel catalog; **15/16 minimum happy-path steps** — **submit missing, so no account is created** |
| **CI / Pipelines** | **In parallel** | Mobile 1/2 Stage1 validated; GitLab nightly MSC job in flight; **enrollment not yet wired to GitLab CI** |

### What's available today

**Mobile 2 — done.** All 25 documented business endpoints are automated with master integration and regression suites. Ready for sign-off and ongoing use on QC4 and Stage1.

**Mobile 1 — done.** All 26 in-scope business endpoints are coded and routed to module regression, integration, or smoke suites per endpoint behavior. Final sign-off package is ready alongside Mobile 2.

**Enrollment — progress since Aug 7, but not done.** We have working TestNG classes for most wizard steps, but compared against `Enrollment End Points.xlsx` (source of truth) the automation **does not yet complete an enrollment**. Postman E2E passes all main-flow steps including submit; Java stops at allocations. Until `review-confirm-entered` is coded and green on Stage1, enrollment cannot be called complete.

**What is coded today (13 test classes + shared base):**

| Category | Test class | Endpoint | In suites |
|----------|------------|----------|-----------|
| Smoke / bootstrap | `EnrollmentPingRequestTest` | GET `/health/liveness`, GET `/ping` | smoke |
| | `EnrollmentCertificateRequestTest` | GET `/certificate` | smoke |
| | `EnrollmentUsStatesRequestTest` | GET `/usstates` | smoke |
| | `EnrollmentCountryRequestTest` | GET `/country` | smoke |
| | `EnrollmentPlansRequestTest` | GET `/plans`, GET `/plans/{planId}` | smoke |
| Wizard step 1 | `ProspectRequestTest` | POST `/enrollments/prospects` | regression + integration |
| Wizard step 2 | `EnrollmentContentRequestTest` | GET `/content` | regression + integration |
| Wizard step 3 | `OwnerEnteredTests` | POST `…/owner-entered` | regression + integration |
| Wizard step 4 | `OwnerAddressEnteredRequestTest` | POST `…/owner-address-entered` | regression + integration |
| Wizard step 5 | `BankEnteredRequestTests` | POST `…/bank-entered` | regression + integration |
| Wizard step 6 | `BeneficiaryEnteredTests` | POST `…/beneficiary-entered` | regression + integration |
| Wizard step 7 | `VerifyBankRoutingNumberRequestTest` | POST `/verify/routingnumber` | regression + integration *(okdirect only in NY block)* |
| Wizard step 8 | `AllocationsEnteredRequestTests` | POST `…/allocations-entered` | regression + integration |

**TestNG suites wired:**

- `enrollment-smoke-testng.xml` — bootstrap GETs (Stage1)
- `enrollment-regression-testng.xml` — full wizard for **okdirect + newyork** (Stage1)
- `enrollment-integration-testng.xml` — same wizard for **okdirect + newyork** (QC4)
- Maven profiles: `mobile-ms-enrollment-smoke`, `-regression`, `-integration`, `-localhost`

**The one remaining coding step for a complete E2E account-creation flow:**

| Step | Endpoint | Status |
|------|----------|--------|
| Submit | POST `/enrollments/enrollment/review-confirm-entered` | **Not started** — blocks account creation and post-submit SQL verification |

**Gaps vs Excel / Postman (see full matrix below):**

- **Blocking:** `review-confirm-entered` — Postman PASSED, Excel marks old collection **Not Assigned / Not started**, no Java test
- **In Postman happy path, not in Java:** `enrollmentstarted`, `recurring-contribution-entered`, `enrollmentallocationfunds/get` (optional skips in Postman, but present in E2E collection)
- **Suite inconsistency:** `VerifyBankRoutingNumberRequestTest` in okdirect regression block only — **missing from newyork block**
- **Out of scope (Postman failing):** subsequent enrollment (401), Vanguard submit (401), Upromise, OAuth

### Sprint goal — enrollment coding complete by end of this sprint

| Deliverable | Target | Owner |
|-------------|--------|-------|
| `ReviewConfirmEnteredRequestTest` — submit step with full aggregate payload | **This sprint** | Dinesh / enrollment dev |
| Register submit in regression + integration + localhost suite XMLs (okdirect, newyork, nmdirect) | **This sprint** | Dinesh |
| Stage1 green run — okdirect + newyork full wizard through account creation | **This sprint** | Dinesh |
| Post-submit SQL check — account findable via `QAAUTOTEST_ENR_*` pattern | **This sprint** | Dinesh |

**Exit criteria for "coding done":** One automated enrollment creates a real account on Stage1; regression suite runs prospect → submit without manual steps.

### Wrap-up sprint — 1 dedicated resource (not full-team exit)

**“Closing MSC” does not mean the squad walks away.** One resource (~1 sprint) finishes handover while the rest of the squad can pivot to the next priority in parallel.

| Item | Detail | Suggested owner |
|------|--------|-----------------|
| **Documentation** | Coverage metrics, enhancement backlog, KB runbooks, README | Close-out resource |
| **Manual test cases** | Map Postman E2E / Excel → qTest *(already in progress)* | Sunil |
| **Postman → Bruno** | Convert collections for manual/regression team | Close-out resource |
| **Handover / KT** | Repo walkthrough, run commands, sign-off package | Close-out resource |
| **GitLab CI job** | Enrollment smoke + regression nightly (QA-1405 pattern) | Close-out resource + DevOps |
| **Optional hardening** | Negatives, QC4 proof — as time allows | Close-out resource |
| **Program sign-off** | Deliver to named ACM / sign-off owners | Leadership |

**Explicitly out of next-sprint scope:** subsequent enrollment, Vanguard submit, Upromise, OAuth — deferred per endpoint catalog §7.

### Pipelines — still in parallel

| Component | Status |
|-----------|--------|
| Mobile 2 GitLab nightly | In flight (QA-1405, QA-1544–1549) — DevOps coordination |
| Mobile 1 workflow onboarding | Auth foundation complete; business endpoints wiring to GHA hub pipeline |
| **Enrollment GitLab job** | **Not yet created** — follows once submit step is green locally |
| GitHub Actions — module pipelines | Mobile 2 vertical slices validated; master regression expansion ongoing |

### Timeline

| Milestone | Target |
|-----------|--------|
| Enrollment wizard **coding** (through submit) | **End of current sprint** |
| Stage1 E2E account creation automated | **End of current sprint** |
| Program close-out (docs, qTest, Bruno, KT, sign-off) | **~1 sprint after coding — 1 resource** |
| MSC program sign-off | End of close-out sprint |
| Next program (main squad) | Can start in parallel once coding lands |
| Steady-state ownership | Sustaining team post-handoff *(ACM TBD)* |

Happy to walk through the Friday list or join a quick call if helpful.

Thanks,  
Swapnil

---

## Teams message draft *(optional — shorter)*

Hi Kevin — Unite MSC update (Aug 20):

**M1 & M2: 100%** — ready for sign-off.

**Enrollment: 60% catalog / 94% core flow** — submit step **this sprint** (coding complete).

**Wrap-up (~1 resource, ~1 sprint after):** docs, qTest, Bruno, KT/handover — **not a full squad exit**.

Happy to fill out the Friday list.

— Swapnil

---

## One-page summary (for Friday list / attachments)

### Program: Unite MSC API Test Automation

**Repository:** `api-test-automation/mobile/` (GitLab)  
**KB / docs:** `programs/unite-msc/`  
**Postman source of truth:** `programs/unite-msc/api-test-automation/postman/EnrollmentE2E/`  
**Endpoint catalog:** `Enrollment End Points.xlsx` — **25 endpoints** (14 GET, 11 POST)

### Coverage snapshot

| Module | Endpoints (scope) | Automated | % | Available for use? |
|--------|-------------------|-----------|---|------------------|
| Mobile 2 | 25 business APIs | 25 | **100%** | Yes — master regression + integration suites |
| Mobile 1 | 26 business APIs | 26 | **100%** | Yes — module suites; master wiring in progress |
| Enrollment — core E2E wizard | 16 min. happy-path steps (Postman modules 1–11) | 15 | **94% coded — submit missing** | Wizard runs through allocations; **no account created** |
| Enrollment — full Excel catalog | 25 endpoints | 15 | **60%** | 5 optional not coded; 5 out-of-scope (401/failing in Postman) |

### Enrollment — implemented vs remaining

**Implemented (15 endpoints / 13 test classes):**

```
Smoke:     liveness, ping, certificate, usstates, country, plans, plans/{id}
Wizard:    prospects, content, owner-entered, owner-address-entered,
           bank-entered, beneficiary-entered, verify/routingnumber,
           allocations-entered
```

**Remaining for coding complete (this sprint):**

```
Wizard:    review-confirm-entered  ← ONLY blocking item for E2E account creation
```

**Remaining for program close-out (~1 sprint, 1 dedicated resource):**

```
Documentation:  coverage metrics, enhancement backlog, KB/runbooks, KT
Manual/Ops:     qTest cases (in progress), Postman→Bruno collection, sign-off package
Automation:     GitLab CI job; negatives/QC4 as time allows
Note:           Rest of squad can start next priority in parallel — not a full-team exit from MSC
```

### TestNG suite inventory

| Suite file | Plans | Steps | Environment |
|------------|-------|-------|-------------|
| `enrollment-smoke-testng.xml` | okdirect | 5 GET bootstrap | Stage1 |
| `enrollment-regression-testng.xml` | okdirect, newyork | 8 wizard steps | Stage1 |
| `enrollment-integration-testng.xml` | okdirect, newyork | 8 wizard steps | QC4 |
| `localhost-testng.xml.example` | okdirect, newyork, nmdirect | full wizard template | local |

### Progress since Aug 7 update

| Aug 7 reported | Aug 20 actual |
|----------------|---------------|
| Enrollment ~15%, vertical slice starting | **15/16 minimum happy-path steps coded**; framework, POJOs, encryption, suites in place — **submit not started** |
| First E2E vertical slice this sprint | **Wizard steps landed individually**; no suite runs prospect → submit; **no account created in automation** |
| Pipeline end sprint + half next | On track — enrollment CI queued behind submit |

### Expected completion

| Item | ETA | Who |
|------|-----|-----|
| Enrollment **coding** (submit step) | **End of current sprint** | Enrollment dev |
| Stage1 automated account creation | **End of current sprint** | Enrollment dev |
| Program **close-out** (docs, qTest, Bruno, KT, sign-off) | **~1 sprint after coding** | **1 dedicated resource** |
| MSC program sign-off | End of close-out sprint | Close-out resource + named sign-off owners |
| Steady-state ownership | Post-handoff | Sustaining team *(ACM TBD)* |
| Next program (e.g. Atlas) | Can start in parallel once coding lands | **Rest of squad** |

### Reference

- Aug 7, 2026: Previous Kevin update — `leadership/2026-08-07-kevin-status-update.md`
- Aug 14, 2026: Rajib/Henry biweekly — enrollment ~30%, Sprint 26.13 focus
- Endpoint Excel: `programs/unite-msc/api-test-automation/postman/EnrollmentE2E/Enrollment End Points.xlsx`
- Implementation plan: `programs/unite-msc/msc-enrollment/docs/08-implementation-plan.md`
- Repo README: `api-test-automation/mobile/enrollment/README.md`

---

## Endpoint gap analysis — Excel vs Java (Aug 20, 2026)

**Source of truth:** `Enrollment End Points.xlsx` (25 endpoints) aligned to Postman `Enrollment -E2E` (20 main-flow requests, modules 01–11).

### Summary

| View | Coded | Total | % | Notes |
|------|-------|-------|---|-------|
| **Full Excel catalog** | 15 | 25 | **60%** | Includes partner/subsequent/oauth rows |
| **In-scope E2E (excl. partner/subsequent/oauth)** | 15 | 16 | **94%** | Only submit missing |
| **Postman modules 01–11 (main happy path)** | 15 | 20 | **75%** | 5 Postman steps have no Java test |
| **Regression suite (okdirect wizard only)** | 8 | 9 | **89%** | Missing submit; smoke/bootstrap not in regression |
| **Regression suite (newyork wizard only)** | 7 | 9 | **78%** | Missing verify-routing **and** submit |

**Bottom line:** Postman can create an account end-to-end. Java automation **cannot** — it stops at allocations. That is why enrollment is not done.

### Endpoint-by-endpoint matrix

| # | Category | Method | Endpoint | Postman status | Old collection sprint | Java coded? | Test class | Gap |
|---|----------|--------|----------|----------------|----------------------|-------------|------------|-----|
| 1 | Health & Setup | GET | `/enrollmentapi/health/liveness` | PASSED | — | **Yes** | `EnrollmentPingRequestTest` | — |
| 2 | Health & Setup | GET | `/enrollmentapi/v1/ping` | PASSED | S-Current Sprint -Done | **Yes** | `EnrollmentPingRequestTest` | — |
| 3 | Setup & Metadata | GET | `/enrollmentapi/v1/certificate` | PASSED | — | **Yes** | `EnrollmentCertificateRequestTest` | — |
| 4 | Setup & Metadata | GET | `/enrollmentapi/v1/usstates` | PASSED | — | **Yes** | `EnrollmentUsStatesRequestTest` | — |
| 5 | Setup & Metadata | GET | `/enrollmentapi/v1/country` | PASSED | — | **Yes** | `EnrollmentCountryRequestTest` | — |
| 6 | Plan Selection | GET | `/enrollmentapi/v1/plans` | PASSED | S-Current Sprint -Done | **Yes** | `EnrollmentPlansRequestTest` | — |
| 7 | Plan Selection | GET | `/enrollmentapi/v1/plans/{planId}` | PASSED | S-Current Sprint -Done | **Yes** | `EnrollmentPlansRequestTest` | — |
| 8 | Content | GET | `/enrollmentapi/v1/content?…` | PASSED | — | **Yes** | `EnrollmentContentRequestTest` | — |
| 9 | Mobile Login (Optional) | POST | `/mobile1api/v1/mobilemembersession` | PASSED | — | **No** | — | Optional; different API |
| 10 | Enrollment Start | POST | `/enrollmentapi/v1/enrollments/enrollmentstarted` | PASSED | — | **No** | — | In Postman module 06; web flow |
| 11 | Prospect | POST | `/enrollmentapi/v1/enrollments/prospects` | PASSED | D-Current Sprint -Done | **Yes** | `ProspectRequestTest` | — |
| 12 | Owner | POST | `…/owner-entered` | PASSED | V-Current Sprint -Done | **Yes** | `OwnerEnteredTests` | — |
| 13 | Owner | POST | `…/owner-address-entered` | PASSED | — | **Yes** | `OwnerAddressEnteredRequestTest` | — |
| 14 | Beneficiary | POST | `…/beneficiary-entered` | PASSED | V-Current Sprint -Done | **Yes** | `BeneficiaryEnteredTests` | — |
| 15 | Bank & Funding | POST | `/verify/routingnumber` | PASSED | V- Current Sprint -InProgress | **Yes** | `VerifyBankRoutingNumberRequestTest` | Coded but **omitted from newyork regression suite** |
| 16 | Bank & Funding | POST | `…/bank-entered` | PASSED | D-Current Sprint -Done | **Yes** | `BankEnteredRequestTests` | — |
| 17 | Bank & Funding | POST | `…/recurring-contribution-entered` | PASSED | — | **No** | — | In Postman module 09; optional skip |
| 18 | Investment | POST | `/enrollmentallocationfunds/get` | PASSED | — | **No** | — | In Postman module 10; optional (SQL fund lookup used instead) |
| 19 | Investment | POST | `…/allocations-entered` | PASSED | D-Current Sprint -In Progress | **Yes** | `AllocationsEnteredRequestTests` | Code exists; Excel still In Progress |
| 20 | Submit | POST | `…/review-confirm-entered` | PASSED | **Not Assigned - Not started** | **No** | — | **BLOCKER — no account creation** |
| 21 | Subsequent Enrollment | GET | `/subsequentenrollment/banks` | Not Working - 401 | — | **No** | — | Out of scope |
| 22 | Subsequent Enrollment | POST | `…/subsequentenrollment/review-confirm-entered` | Not Working - 401 | — | **No** | — | Out of scope |
| 23 | Partner Integration | POST | `/enrollments/submit` | Not Working - 401 | — | **No** | — | Out of scope (Vanguard) |
| 24 | Partner Integration | GET | `/upromiseaccount` | Authorization Failed | — | **No** | — | Out of scope |
| 25 | OAuth | POST | `/oauth/token` | Not Working - 401 | — | **No** | — | Out of scope |

### What “done properly” requires

1. **`ReviewConfirmEnteredRequestTest`** — full aggregate payload, member JWT header capture, account number assertion
2. **Register submit** in all three suite XMLs (okdirect, newyork, nmdirect blocks)
3. **Fix newyork regression** — add `VerifyBankRoutingNumberRequestTest` (parity with okdirect)
4. **Stage1 green proof** — full wizard creates `QAAUTOTEST_ENR_*` account; post-submit SQL check
5. **Decide on optional Postman steps** — document skip vs automate for `enrollmentstarted`, `recurring-contribution-entered`, `enrollmentallocationfunds/get`
6. **CI + manual handover** — GitLab job, qTest cases, Bruno collection (next sprint)

### Postman vs regression suite scope mismatch

| Layer | What it covers |
|-------|----------------|
| Postman E2E (modules 01–11) | Bootstrap GETs → prospect → all wizard POSTs → **submit** (20 requests) |
| `enrollment-smoke-testng.xml` | Bootstrap GETs only (liveness, ping, cert, usstates, country, plans) — **no wizard** |
| `enrollment-regression-testng.xml` | Wizard from prospect → allocations — **no bootstrap, no submit** |

So even after individual step classes landed, **no single suite runs a complete enrollment today**.

---

## Notes for Swapnil (internal — do not send)

- **Lead with:** M1/M2 done; enrollment **not complete** — Postman passes, Java stops at allocations.
- **Coverage % to use with Kevin:** full Excel = **60% (15/25)**; minimum happy path = **94% (15/16)** but **0% E2E completion** until submit runs green.
- **"Avinash dynasty"** in voice note likely = enrollment workstream / team — keep email focused on program status, not individual names unless asked.
- **Allocations** marked "In Progress" in Excel — code exists; confirm green on Stage1 before calling done in Friday list.
- **NY regression block** omits `VerifyBankRoutingNumberRequestTest` — **not intentional for parity**; fix when closing submit.
- **Post-submit SQL** and **EnrollmentTestDataBuilder** from migration checklist still partially open — bundle with submit delivery.
- **Bruno/Postman handover** — user explicitly called out manual team owns collection compilation; keep in next-sprint table.
- Last local surefire run (Aug 14) skipped tests due to DB listener not available — not a code failure; Stage1 run needed for evidence.
