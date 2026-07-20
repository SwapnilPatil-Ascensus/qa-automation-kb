# Government Savings — Technical Assessment (Live Validation)

**Validation timestamp:** 2026-07-20T18:15:00-04:00  
**Primary repositories:** `api-test-automation` @ `cee0de9`, `prime-test-automation` @ `93f8628`  
**Live CI APIs:** GitLab token **expired (401)** — YAML + local repo are primary evidence

---

## A. Technical assessment summary

### Mobile 2 — reconciled current result

| Metric layer | Numerator | Denominator | Result | Evidence |
|--------------|----------:|------------:|-------:|----------|
| **Implemented automation (code)** | **24** | **25** | **96.0%** | All business endpoints except `mobilemembers` have canonical L3+ tests on `main` @ `cee0de9` |
| **Automatable scope (excl. mobilemembers from denominator)** | **24** | **24** | **100%** | Same code; alternate denominator presentation |
| **Last execution-verified (sign-off)** | **22** | **25** | **88.0%** | `7ccaf46` @ 2026-07-14 — **stale for implementation** |
| **Scheduled CI integration** | **0** | **1** job | **0%** | No Mobile 2 job in `api-test-automation/.gitlab-ci.yml` |

**Denominator source:** Dinesh `API Endpoints - Mobile2.xlsx` — **25** documented business endpoints (excludes health/docs).

**Intentional exclusions from business automation numerator:**
- `GET /mobile2api/v1/mobilemembers/{planId}/{username}` — acceptance harness; smoke-only (`MobileMembersRequestTest`)

**Not uncovered — intentional suite placement:**
- `PUT`/`DELETE` `/mobile2api/v1/mobilebanks` — automated; **smoke/targeted only** (`mobile2-smoke-testng.xml`)
- `DELETE` `/mobile2api/v1/mobilecontribution/{ext}/{id}` — automated; **module/targeted only**; excluded from master

**Post-7ccaf46 implementation deltas (code, execution refresh pending):**
- `GET /mobile2api/v1/mobileytdsummary/{ext}` — `MobileYtdSummaryRequestTest` — **in master regression**
- `GET /mobile2api/v1/mobilebanks/{id}` — `getMobileBankById_returnsBank` — **in module + master class load**

**Full endpoint inventory:** `01-inventory/mobile2-endpoint-current-state.csv`

---

### Mobile 1 — reconciled current result

| Metric layer | Numerator | Denominator | Result | Evidence |
|--------------|----------:|------------:|-------:|----------|
| **Implemented automation (code)** | **6** | **27** | **22.2%** | Six `*RequestTest` classes on `main` @ `cee0de9` |
| **Executed verified** | **1** | **27** | **3.7%** | `POST mobilemembersession` historical evidence only |
| **Sign-off-ready** | **1** | **27** | **3.7%** | Pending QC4/Stage1 runs for five new endpoints |
| **Scheduled CI** | **0** | **1** | **0%** | No GitLab job |

**Implemented endpoints (code):**
1. `POST /mobile1api/v1/mobilemembersession`
2. `GET /mobile1api/v1/mobileowner`
3. `GET /mobile1api/v1/mobileOwnerMenu`
4. `GET /mobile1api/v1/mobileprofilemenu`
5. `GET /mobile1api/v1/mobilebeneficiaryByExt/{ext}`
6. `GET /mobile1api/v1/mobilebankinfobyroutingnum/{routingNum}`

**Full inventory:** `01-inventory/mobile1-endpoint-current-state.csv`

---

## CI/CD live validation (YAML-verified; live runs blocked)

| Platform | Job | Classification | Blocks merge/deploy? |
|----------|-----|----------------|----------------------|
| GitLab | `scheduled_regression_job` (prime) | Scheduled regression — hard-fail on run | **Not evidenced** |
| GitLab | `scheduled_metadataweb_stage1` | Scheduled regression — hard-fail on run | **Not evidenced** |
| GitLab | `stage5_smoke_job` | Manual smoke | No |
| GitLab | Mobile 2 nightly | **Not configured** | N/A |
| GitHub Actions | Mobile 2 Dashboard + Nexus | Deployment validation (externally validated) | Workflow fail blocks **that workflow** — repo not in clone |
| Jenkins | IDP perf / V2 UI | Unknown / inferred | **Not verified live** |

---

## Implementation status taxonomy (current)

| Status | Mobile 2 | Mobile 1 | V3 UI | V2 UI |
|--------|----------|----------|-------|-------|
| Verified automated + scheduled | 0 | 0 | Yes | Unknown |
| Verified automated + deployment/smoke | 1 (GHA slice) | 0 | Manual Stage5 | — |
| Verified automated + manual | Majority | 6 endpoints | — | Large corpus |
| Implemented; execution pending | YTD, banks GET-by-id | 5 endpoints | — | — |
| Intentionally excluded from master | PUT/DELETE banks, DELETE contrib | — | — | — |
| No validated automation | — | 21 endpoints | — | — |
| Unknown (live CI) | Schedule status | — | Live run TBD | Jenkins TBD |

---

## Automated tooling inventory

| Tool | Status | Role |
|------|--------|------|
| `live_validation_build.py` | **Available** | Endpoint CSV + metrics register |
| `generate_gs_assessment_deliverables.py` | **Available** | DOCX/XLSX/PDF |
| UP coverage Python tools | **Available** | V2/V3 inventory reconciliation |
| qTest REST / MCP | **Blocked** | No credentials |
| Jira MCP | **Blocked** | Discovery error |
| GitLab API / glab | **Blocked** | Expired token |
| JaCoCo (UniteMSC) | **Verified in POMs** | Service source-code coverage |
| SonarQube | **Disabled** on reviewed CI | `RUN_SONARQUBE: false` |

**Why not harmonized:** fragmented identifiers, no live ALM/CI feed, separate denominators, no central normalized register with freshness SLAs.

---

## Minimum architecture (unchanged recommendation)

Extend Python collectors → versioned JSON/CSV → reconciliation with confidence → leadership + technical workbooks. No large new application until register proves insufficient.

---

*Metric authority: `03-analysis/verified-metrics-register.csv` (rebuilt this validation)*
