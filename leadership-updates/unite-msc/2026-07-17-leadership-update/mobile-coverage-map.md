# Mobile coverage map — Unite MSC API automation

**Metric type:** API endpoint automation coverage (not Java line coverage)  
**Denominator:** Dinesh `API Endpoints - Mobile2.xlsx` business scope (**25** endpoints, excl. health/docs)  
**Last verified sign-off:** 2026-07-14 @ `7ccaf46`  
**Refresh status:** Post-07-14 merges (YTD, Banks GET-by-id) — **TBD / requires verification**

---

## Mobile 2 — executive scorecard

| Metric | Verified (2026-07-14) | Current (2026-07-17) |
|--------|----------------------:|---------------------:|
| Documented in-scope endpoints | 25 | 25 |
| Automated (L3+) | **22** | **TBD** (projected **24** if YTD + `GET mobilebanks/{id}` merged — verify) |
| Coverage % | **88.0%** | **TBD** (projected **≥96%** if above merges on `main`) |
| Master-suite wired endpoints | 20 | **TBD** — re-read `master-regression-testng.xml` |
| Master regression runs (OKD+NMD) | 34 | **TBD** — XML now lists **18** class slots × 2 brandings = **36** |
| QC4 evidence | Sign-off conditional pass | **TBD** — fresh `run-qc4-all-suites.ps1` |
| Stage 1 evidence | 36/40 master pass | **TBD** — fresh `run-stage1-all-suites.ps1` |
| IDP (`nmdirect`) | Supported on `main` | Verified in master XML |
| Non-IDP (`okdirect`) | Supported | Verified |
| Open MR / merge | Sign-off pending final MR | **TBD** — GitLab MR list |

**Leadership statement (safe):** Mobile 2 baseline coverage is **above 90% based on 2026-07-14 mapping (88%) with two known gaps closed in code since then (YTD, Banks GET-by-id) — pending refreshed sign-off run and formal approval.**

Do **not** claim 100% — `GET mobilemembers/{planId}/{username}` remains excluded (acceptance helper).

---

## Mobile 2 — by functional area

| Area | Endpoints | Automated (07-14) | Gap / exception | Evidence |
|------|:---------:|:-----------------:|-----------------|----------|
| Activity & Transactions | 3 | 3 | — | `16-mobile2-coverage-matrix.md` |
| Banks | 5 | 4 | `GET {id}` gap at sign-off; code exists post-07-15 | `MobileBanksRequestTest.getMobileBankById` |
| Content & Plans | 3 | 3 | — | |
| Contributions | 6 | 6 | Detail/PUT **Partial** on Stage 1 (QC4 fixture) | KB `dynamic-ext-id-fixture.md` |
| Dashboard | 3 | 1 | YTD gap at sign-off; class exists post-07-16 | `MobileYtdSummaryRequestTest` |
| Performance & Balance | 3 | 3 | Duplicate stackup class (by design) | |
| UGift | 2 | 2 | — | |

---

## Mobile 2 — pending / exceptions (sign-off + known issues)

| Item | Status | Notes |
|------|--------|-------|
| `GET mobileytdsummary/{ext}` | **Likely closed** (code on `main`) | Verify in updated matrix + QC4 run |
| `GET mobilebanks/{id}` | **Likely closed** (Sunil QA-1386) | Verify master/regression groups |
| `GET mobilemembers/{planId}/{username}` | **Excluded** | Acceptance-role helper |
| Contribution detail/PUT Stage 1 | **Open** | Env-specific 401; dynamic SQL designed (KB only) |
| DELETE contribution / PUT-DELETE banks | **Module-only** | Intentionally excluded from master |
| SQL L5 API–DB reconciliation | **Deferred** | Enhancement backlog |
| GitLab nightly job | **Not created** | DevOps story required |

---

## Mobile 2 — canonical test inventory (filesystem 2026-07-17)

**19 `*RequestTest` classes** under `mobile2/src/test/java`:

| Area | Class |
|------|-------|
| Activity | `MobileActivityRequestTest` |
| Banks | `MobileBanksRequestTest` |
| Balance / Performance / Stackup | `MobileBalanceTrendRequestTest`, `MobilePerformanceRequestTest`, `MobileStackupRequestTest` (×2 packages) |
| Content | `MobileContentRequestTest` |
| Contribution | 6 classes (list, check, detail, post, put, delete) |
| Dashboard | `MobileDashboardRequestTest`, `MobileYtdSummaryRequestTest` |
| Investment | `MobileInvestmentRequestTest` |
| Plans | `MobilePlansRequestTest` |
| Stackup | `stackup.MobileStackupRequestTest` |
| Transaction History | `MobileTransactionHistoryRequestTest` |
| UGift | `MobileUgiftRequestTest` |

**25 TestNG suite XMLs** | **30 Maven profiles** in `mobile2/pom.xml`

---

## Mobile 1 — executive scorecard

| Metric | Value | Evidence |
|--------|------:|----------|
| Documented business endpoint groups | **27** | `03-document-postman-coverage-matrix.md` |
| Automated | **1** | `POST /mobile1api/v1/mobilemembersession` |
| In progress (sprint 26.11) | Owner/profile reads, dashboard, beneficiary, MFA paths | `06-sprint-26.11-plan.md` stretch |
| Pending | Majority of M1 business surface | Matrix § Mobile 1 |
| Coverage % | **3.7%** (1/27) | Same |
| Auth foundation | **Complete** (OKD + NMD, dynamic SQL) | Sign-off §2; `Mobile1AuthenticationTest` |
| IDP token endpoint | **Not migrated** | `POST mobilememberidptoken` — planned |

**Sprint framing:** Mobile 1 non-IDP baseline this sprint; IDP hardening next sprint.

---

## Mobile 1 — category checklist

| Category | Endpoints (documented) | Status |
|----------|------------------------|--------|
| Authentication / session | `mobilemembersession`, `mobilememberidptoken` | Session **done**; IDP token **pending** |
| Dashboard | TBD per M1 inventory | **Pending** |
| Owner / profile | `mobileowner`, `mobileprofilemenu`, etc. | **Pending** |
| Beneficiary | `mobilebeneficiaryByExt/{ext}` | **Pending** |
| Phone MFA / device / biometric | Documented in Dinesh scope | **Pending — scope TBD** |
| Core services | Per Postman / workbook | **Pending** |

---

## Environment flexibility

| Environment | Mobile 2 status | Mobile 1 status |
|-------------|-----------------|-----------------|
| QC4 | Primary evidence base | Auth profiles `acceptance-qc4` |
| Stage 1 | 36/40 master (07-14); contribution fixture issue | `acceptance-stage1` profile exists |
| Stage 5 / Stage 2 | **TBD** | **TBD** — properties + test data |

Framework supports env switching via Maven profiles (`acceptance-qc4`, `acceptance-stage1`) once test data exists.
