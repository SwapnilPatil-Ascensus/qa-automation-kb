# Performance Testing

**Owner:** Priti Choudhary  
**Repository:** [performance-test-automation](https://gitlab.com/ascensus-gs/products/depot/qa-automation/automation/-/tree/main/performance-test-automation)  
**Jenkins view:** Performance dashboard on `jenkinsqant1`

---

## Department standards established

Priti defined and rolled out:

- Folder structure and naming conventions (`performance/{area}/{tool}/`)
- Definition of Done for perf test cases
- BlazeMeter/Taurus remote YAML patterns
- Jenkins `AGSUP_ENDURANCE_THROUGHPUT` job template
- Regression suite orchestration (parallel loadtestwt1 + loadtestwt2)

---

## Jenkins regression suite (scheduled)

| Scenario | YAML / JMX | Schedule | Added |
|----------|-----------|----------|-------|
| IDP Login Resources | `universal/idp/jmeter/idp-login-resources-remote.yaml` | Weekday regression | May 2026 |
| Auth Server Delay | `universal/idp/jmeter/auth-server-delay-remote.yaml` | Weekday regression | May 2026 |
| IDP Forgot Username | `universal/idp/jmeter/idp-forgot-username-remote.yaml` | Weekday regression | Apr 2026 |
| Legacy Non-IDP Login | `unite/legacy-login/jmeter/legacy-login.jmx` | Weekday regression | Jun 2026 |
| **Subtotal — scheduled UP/legacy** | | **4 scenarios × 2 servers** | |

### Unite MSC (parameterized — ad hoc → regression path)

| Scenario | JMX | Jenkins job | Status |
|----------|-----|-------------|--------|
| MSC Non-IDP Login → Dashboard | `unite-msc-non-idp-login.jmx` | `AGSUP_UNITE_MSC_ENDURANCE` | Baseline complete (QA-1229) |
| MSC IDP Login | `unite-msc-idp-login.jmx` | `AGSUP_UNITE_MSC_ENDURANCE` | In progress (QA-1228) |
| MSC Core GET Endpoints | `unite-msc-core-getEndpoints.jmx` | In repo | Not yet scheduled |

### Pipeline / Universal Platform microservices

| Area | JMX scripts in repo | Pipeline status |
|------|--------------------:|-----------------|
| Universal Enrollment | 6+ | Added to hub pipeline project |
| Universal Metadata | 2 | Added to hub pipeline project |
| Universal Account | 2 | Available |
| Universal Financial (withdrawal) | 1 | Available |

---

## Emergency delivery — barcode SYN-443

| Item | Detail |
|------|--------|
| Request | 1-week turnaround for barcode return-mail API perf |
| Deliverable | QC4 + Stage1 baselines at 30/45/60 SPM |
| MR | `perf-test-barcode-feature` (Aug 3, 2026) |
| Report | `programs/Performance Testing/barcode-syn-443/` |

---

## IDP login resources (JEA / proxy server)

Baseline perf tests created for IDP-related flows on JEA proxy server — supports cross-team IDP validation initiative.

---

## What's next (Q3 2026)

| Priority | Scenario | Target |
|----------|----------|--------|
| 1 | MSC IDP login perf — scheduled | Jul–Aug |
| 2 | MSC Contribution endpoints | Aug–Sep |
| 3 | MSC Banks high-traffic GETs | Sep |
| 4 | MSC Activity / transaction history | Sep–Oct |
| 5 | Nightly MSC perf job (after clean manual runs) | Q4 |

---

## Perf MR delivery

**10 MRs** by Priti to `automation` repo (Apr–Aug):

| MR | Description |
|----|-------------|
| `idp_forgot_username&Password` | IDP forgot flows |
| `idp_login_resources` | IDP login resources baseline |
| `perfTestLegacyLogin` | Legacy non-IDP login |
| `perfTest_unite_msc_login` | MSC non-IDP login |
| `perfTest_unite-msc-change` | Folder structure standardization |
| `msc-idp-login` | MSC IDP login JMX |
| `dataSetUp` | Test data setup |
| `regressionReportLocationUpdate` | Report path standardization |
| `updatePerfRegSuite` | Regression suite wiring |
| `perf-test-barcode-feature` | Barcode emergency |

---

## Evidence

- Regression suite Groovy: `evidence/jenkins/perf-regression-suite-details.txt`
- MSC endurance log: `evidence/jenkins/unite-msc-endurance-log.txt`
- Jenkins dashboard screenshot: `assets/screenshots/jenkins-perf-dashboard.png`
