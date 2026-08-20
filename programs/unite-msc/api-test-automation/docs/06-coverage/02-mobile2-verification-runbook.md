# Mobile 2 — Verification, Mapping & Multi-Plan Runbook

**Purpose:** Single source of truth for Cursor (or humans) working in **`api-test-automation`** to verify Mobile 2 coverage, run QC4/Stage 1 suites across brandings, and update sign-off evidence.  
**Location:** Knowledge base (`qa-automation-kb/programs/unite-msc/api-test-automation`).  
**Companion:** [Cursor prompt — Mobile2 verification](../03-development/04-cursor-prompts/mobile2-verification.md) — paste into a new Cursor chat opened in `api-test-automation`.

---

## 1. What to verify (every session)

| Check | How | Pass criteria |
|-------|-----|---------------|
| Git baseline | `git rev-parse --short HEAD` + `git log -5 -- mobile/mobile2` | Note commit; compare to last verified |
| Endpoint map | Section 3 below vs `*RequestTest.java` + suite XMLs | 24/24 in-scope automated |
| Master suite XML | `mobile/mobile2/testsuites/master-regression-testng.xml` | All stable endpoints wired OKD + NYD (YTD included; banks OKD only) |
| SQL fixtures | `mobile/mobile2/src/test/resources/sql/mobile.sql` | `get.mobile.auth.user`, `get.mobile.contribution.fixture` |
| QC4 master | Maven command §5 | **40/40** tests (expected after YTD wired + dynamic fixture) |
| Stage 1 master | Maven command §5 + DB tunnel | **40/40** tests |
| Banks PUT/DELETE | `banks-smoke-testng.xml` only | `functional` group — **not** in master |
| Contrib DELETE | `contribution-regression-testng.xml` okdirect only | **not** in master |
| Docs delta | `local-mobile-api-audit/16` + `17` | Refresh after code/run changes |

---

## 2. Three-repo crosswalk (identity key: HTTP method + `/mobile2api/v1` path)

| Phase | Source | Path |
|-------|--------|------|
| **A — Legacy** | Cucumber `unite-mobile2` | `C:\Workspace\GitLab\MobileAutomation\UniteMSC\unite-mobile2` |
| **B — Postman** | `unite-mobile2-postman_collection.json` | `local-mobile-api-audit/00-source-artifacts/original/` |
| **B — Postman (repo)** | Partial MSC app collection | `postman/mobile/mobile-msc/MSC-Mobile-app.postman_collection.json` |
| **C — Dinesh** | `API Endpoints - Mobile2.xlsx` | Sign-off denominator (**25** business; **24** after exclusion) |
| **Canonical** | TestNG | `mobile/mobile2/src/test/java/mobile2/**` |

**Excluded from denominator:** `GET /mobile2api/v1/mobilemembers/{planId}/{username}` — acceptance-role helper; Postman expects 401 with member JWT.

**Designed, not in master regression (by design):**

| Endpoint | Suite | Group |
|----------|-------|-------|
| `PUT /mobilebanks` | `banks-smoke-testng.xml` | `functional` |
| `DELETE /mobilebanks` | `banks-smoke-testng.xml` | `functional` |
| `DELETE /mobilecontribution/{ext}/{id}` | `contribution-regression-testng.xml` | okdirect only |

---

## 3. Endpoint mapping snapshot (in-scope = 24)

| Area | Method | Path | Canonical class / method | Module | Master | Notes |
|------|--------|------|--------------------------|:------:|:------:|-------|
| Dashboard | GET | `/mobiledashboard` | `MobileDashboardRequestTest.getMobileDashboard` | ✓ | ✓ | |
| Dashboard | GET | `/mobileytdsummary/{ext}` | `MobileYtdSummaryRequestTest.getMobileYtdSummary_*` | ✓ | **verify** | Was missing from master @ 719be4d |
| Activity | GET | `/mobileactivity/{ext}` | `MobileActivityRequestTest` | ✓ | ✓ | |
| Transactions | GET | `/mobiletransactionhistory/{ext}` | `MobileTransactionHistoryRequestTest` | ✓ | ✓ | |
| Investments | GET | `/investments/{ext}` | `MobileInvestmentRequestTest` | ✓ | ✓ | |
| Banks | GET | `/mobilebanks` | `MobileBanksRequestTest.getMobileBanks_*` | ✓ | ✓ | okdirect module |
| Banks | GET | `/mobilebanks/{id}` | `MobileBanksRequestTest.getMobileBankById_*` | ✓ | ✓ | QA-1386 |
| Banks | POST | `/mobilebanks` | `MobileBanksRequestTest.postMobileBanks_*` | ✓ | ✓ | |
| Banks | PUT | `/mobilebanks` | `MobileBanksRequestTest.putMobileBanks_*` | smoke | No | intentional |
| Banks | DELETE | `/mobilebanks` | `MobileBanksRequestTest.deleteMobileBanks_*` | smoke | No | intentional |
| Content | GET | `/content` | `MobileContentRequestTest` | ✓ | ✓ | |
| Plans | GET | `/plans` | `MobilePlansRequestTest` | ✓ | ✓ | |
| Plans | GET | `/plans/{id}` | `MobilePlansRequestTest` | ✓ | ✓ | |
| Contribution | GET | `/mobilecontribution` | `MobileContributionRequestTest` | ✓ | ✓ | |
| Contribution | GET | `/mobilecontributioncheck` | `MobileContributionCheckRequestTest` | ✓ | ✓ | |
| Contribution | GET | `/mobilecontribution/{ext}/{id}` | `MobileContributionDetailRequestTest` | ✓ | ✓ | dynamic SQL fixture |
| Contribution | POST | `/mobilecontribution` | `MobileContributionPostRequestTest` | ✓ | ✓ | |
| Contribution | PUT | `/mobilecontribution/{ext}/{id}` | `MobileContributionPutRequestTest` | ✓ | ✓ | dynamic SQL fixture |
| Contribution | DELETE | `/mobilecontribution/{ext}/{id}` | `MobileContributionDeleteRequestTest` | okdirect | No | intentional |
| Balance | GET | `/mobilebalancetrend/{ext}` | `MobileBalanceTrendRequestTest` | ✓ | ✓ | |
| Performance | GET | `/mobileperformance/{ext}` | `MobilePerformanceRequestTest` | ✓ | ✓ | |
| Stackup | GET | `/mobilestackup/{id}` | `balancetrend` + `stackup` `MobileStackupRequestTest` | ✓ | ✓ | duplicate class — hygiene |
| UGift | GET | `/mobileugift` | `MobileUgiftRequestTest` | ✓ | ✓ | |
| UGift | PATCH | `/mobileugift/{ext}` | `MobileUgiftRequestTest` | ✓ | ✓ | |

**Coverage math:** 24 automated / 24 in-scope = **100% endpoint automation** (excl. `mobilemembers`).

---

## 4. Branding / plan matrix

Master and module suites use TestNG `<parameter name="branding" value="..."/>`:

| Branding param | Plan type | IDP | Voucher | Suites |
|----------------|-----------|:---:|---------|--------|
| `okdirect` | Oklahoma Direct (non-IDP) | No | okd | All modules; Banks **okdirect only** |
| `newyork` | New York Direct (IDP) | Yes | nyd | All except Banks module (banks okdirect-only); replaces `nmdirect` (NMD unstable) |

**Auth chain:** `mvn -f mobile/mobile1/pom.xml install -DskipTests` **before** any mobile2 run.

**SQL branding token:** `$$branding$$` in `get.mobile.auth.user` and `get.mobile.contribution.fixture` (`mobile/mobile2/src/test/resources/sql/mobile.sql`).

**Test user:** Most tests use `setTestUser("1")` → row `rowNumber=1` from SQL for current branding.

### Multi-plan verification (when expanding beyond okdirect + nmdirect)

1. Confirm `get.mobile.auth.user` returns `QAAUTOTEST%` users for target `TU_TRAUNCH.BRANDING`.
2. For contribution detail/PUT, confirm `get.mobile.contribution.fixture` returns `accountExt` + `apiContributionId` (`TU_BNK_INSTRUCTION.SEQ_PAY_ID`) per user.
3. Run module profile first, then master leg for that branding.
4. Banks: only exercise under `okdirect` unless product adds IDP bank support.

---

## 5. Run commands

**Prerequisite (always):**

```powershell
cd C:\Workspace\GitLab\api-test-automation
mvn -f mobile/mobile1/pom.xml install -DskipTests
```

### QC4 — master regression (primary gate)

```powershell
mvn -f mobile/mobile2/pom.xml test `
  "-Pmobile-ms-master-regression,acceptance-qc4" `
  "-Dmobile.ms.report.environment=QC4"
```

**Expected:** Tests run: **40**, Failures: **0** (after YTD wired to master).

### Stage 1 — master regression

Requires Stage 1 DB reachable (`LT12800.properties` / tunnel). Script copies host file for mobile2.

```powershell
mvn -f mobile/mobile2/pom.xml test `
  "-Pmobile-ms-master-regression,acceptance-stage1" `
  "-Dmobile.ms.report.environment=Stage1"
```

Or full matrix:

```powershell
.\programs\unite-msc\api-test-automation\scripts\run-qc4-all-suites.ps1
.\programs\unite-msc\api-test-automation\scripts\run-stage1-all-suites.ps1
```

Outputs: `mobile/qc4-all-suites-results.csv`, `mobile/stage1-all-suites-results.csv`, HTML at `mobile/mobile2/target/mobile-ms-report/index.html`.

### Banks smoke (PUT/DELETE only)

```powershell
mvn -f mobile/mobile2/pom.xml test `
  "-Pmobile-ms-banks-smoke,acceptance-qc4" `
  "-Dmobile.ms.report.environment=QC4"
```

### Per-module QC4 (debug one area)

```powershell
mvn -f mobile/mobile2/pom.xml test `
  "-Pmobile-ms-dashboard-regression,acceptance-qc4" `
  "-Dmobile.ms.report.environment=QC4"
```

Replace profile: `mobile-ms-{dashboard|activity|banks|content|contribution|investment|plans|transactionhistory|ugift|balancetrend|stackup}-{integration|regression}`.

---

## 6. Known open items (pre-lock checklist)

| # | Item | Severity | Verify by |
|---|------|----------|-----------|
| 1 | YTD in `master-regression-testng.xml` | P1 | Master test count = 40; dashboard block includes `MobileYtdSummaryRequestTest` |
| 2 | Fresh QC4 master evidence | P1 | Surefire + HTML report; commit hash in notes |
| 3 | Fresh Stage 1 master evidence | P1 | 40/40; contribution fixture SQL works both brandings |
| 4 | NMD Banks block in master vs okdirect-only banks module | P2 | NMD banks tests pass or block removed |
| 5 | Duplicate `MobileStackupRequestTest` | P2 | Optional dedup |
| 6 | GitLab nightly (`QA-1405`) | P1 ops | `.gitlab-ci.yml` scheduled job |
| 7 | Refresh `local-mobile-api-audit/16` + `17` | P1 docs | After runs green |
| 8 | SQL L5 / qTest linkage | P3 deferred | Not blocking endpoint % |

---

## 7. Lock criteria (“Mobile 2 off”)

| Criterion | Required |
|-----------|:--------:|
| 24/24 in-scope endpoints automated L3+ | ✓ |
| Master regression green QC4 + Stage 1 (40/40) | |
| PUT/DELETE banks + DELETE contrib documented exclusions | ✓ |
| `mobilemembers` formally excluded | ✓ |
| Nightly GitLab job live | |
| Sign-off `17` + DOCX approved | |
| Then → Mobile 1 scope | |

---

## 8. After each verification run — update these

| Artifact | Action |
|----------|--------|
| `local-mobile-api-audit/16-mobile2-coverage-matrix.md` | Refresh scorecard + gap table |
| `local-mobile-api-audit/17-mobile2-api-automation-signoff.md` | Update evidence dates, pass counts, commit |
| `local-mobile-api-audit/14-done-vs-previous-audit.md` | Delta vs prior run |
| `mobile/mobile2/README.md` | Counts if suite sizes changed |
| This file §3 snapshot | Commit hash + master YTD status |

---

## 9. Related docs

| Doc | Location |
|-----|----------|
| DevOps CI guide | `local-mobile-api-audit/15-devops-mobile2-integration-pipeline-guide.md` |
| Nexus / GHA | `17-MOBILE2-NEXUS-GITHUB-ACTIONS-PIPELINE.md` |
| Module README | `mobile/mobile2/README.md` |
| Jira nightly story | QA-1405 |
| KB leadership map (read-only) | `qa-automation-kb/leadership-updates/unite-msc/.../mobile-coverage-map.md` |

---

*Ascensus QA Automation · Unite MSC Mobile 2 · Operational runbook (tracked in git)*
