# Mobile 2 — Stage 1 Dashboard Regression Runbook

Quick guide to run **`dashboard-regression-testng.xml`** against **Stage 1** from a local `api-test-automation` checkout.

| Item | Value |
|------|-------|
| **Suite file** | `mobile/mobile2/testsuites/dashboard-regression-testng.xml` |
| **Maven profile** | `mobile-ms-dashboard-regression` + `acceptance-stage1` |
| **Tests** | 2 legs — OKD (`okdirect`) + NYD (`newyork`), method `getMobileDashboard` |
| **API** | `GET /mobile2api/v1/mobiledashboard` |

---

## 1. Prerequisites

| Requirement | Details |
|-------------|---------|
| **Repo** | `api-test-automation` cloned locally |
| **Java** | JDK **17** |
| **Maven** | 3.9+ |
| **Network** | Reach Stage 1 BFF: `https://unite-bff-wtn.stage1.acs529.com` |
| **Stage 1 DB tunnel** | Oracle tunnel on **`localhost:41521`** (service `UIIS01`) |
| **Host config file** | `<hostname>.properties` — see §2 (machine-specific; **not committed to git**) |

---

## 2. Host properties file (`<hostname>.properties`)

The framework auto-selects a host file named after your computer:

| OS | Property used | Example filename |
|----|---------------|------------------|
| **Windows** | `%COMPUTERNAME%` | `LT12800.properties` |
| **Linux / macOS** | `$HOSTNAME` (if set) | `my-runner.properties` |

Maven logs which file it picked:

```text
Setting host properties: LT12800.properties
```

You can override explicitly with `-Dhost.properties=<filename>`.

### 2.1 Create the file

Create **one file per machine** under **mobile1** (copy to **mobile2** before each run):

```text
mobile/mobile1/src/test/resources/config/<hostname>.properties
mobile/mobile2/src/test/resources/config/<hostname>.properties   ← copy before run
```

**Example** — Windows machine `LT12800`:

`mobile/mobile1/src/test/resources/config/LT12800.properties`

```properties
######################### Settings for Stage 1 ###########################
TBID=stage1
UNITEDATABASEURL=localhost:41521:UIIS01
UNITEUSERNAME=<your_stage1_db_user>
UNITEPASSWORD=<your_stage1_db_password>
```

> Tests load auth users and min app version from Oracle. Stage 1 DB is internal; the tunnel maps it to `localhost:41521`.

### 2.2 Start the Stage 1 DB tunnel

Start your usual Oracle tunnel to Stage 1 so **`localhost:41521`** is listening.

If the tunnel is down, tests fail with:

```text
ORA-12541: Cannot connect. No listener at host localhost port 41521
```

### 2.3 Install Mobile 1 (required before mobile2)

From repo root:

```powershell
cd C:\Workspace\GitLab\api-test-automation
mvn -f mobile/mobile1/pom.xml install -DskipTests
```

**Expected:** `BUILD SUCCESS`

Re-run after any `mobile1` code changes.

---

## 3. Run dashboard regression on Stage 1

```powershell
cd C:\Workspace\GitLab\api-test-automation

# Copy host file to mobile2 if you only maintain it under mobile1
Copy-Item mobile\mobile1\src\test\resources\config\<hostname>.properties `
          mobile\mobile2\src\test\resources\config\<hostname>.properties -Force

mvn -f mobile/mobile2/pom.xml test `
  "-Pmobile-ms-dashboard-regression,acceptance-stage1" `
  "-Dhost.properties=<hostname>.properties" `
  "-Dmobile.ms.report.environment=Stage1"
```

**Example** (machine name `LT12800`):

```powershell
Copy-Item mobile\mobile1\src\test\resources\config\LT12800.properties `
          mobile\mobile2\src\test\resources\config\LT12800.properties -Force

mvn -f mobile/mobile2/pom.xml test `
  "-Pmobile-ms-dashboard-regression,acceptance-stage1" `
  "-Dhost.properties=LT12800.properties" `
  "-Dmobile.ms.report.environment=Stage1"
```

If you omit `-Dhost.properties`, Maven uses `%COMPUTERNAME%.properties` (Windows) or `$HOSTNAME.properties` (Linux) automatically — only when that file exists under `src/test/resources/config/`.

### What each flag does

| Flag / profile | Purpose |
|----------------|---------|
| `mobile-ms-dashboard-regression` | Runs `dashboard-regression-testng.xml` |
| `acceptance-stage1` | Unpacks **`stage1.properties`** (Stage 1 BFF + auth server URLs) |
| `-Dhost.properties=<hostname>.properties` | DB connection via tunnel (`localhost:41521`) |
| `-Dmobile.ms.report.environment=Stage1` | Labels HTML report as Stage 1 |

---

## 4. Expected results

| Leg | Branding | Auth | Typical Stage 1 outcome |
|-----|----------|------|-------------------------|
| OKD non-IDP Dashboard regression | `okdirect` | Direct mobile login | **May fail** if no `QAAUTOTEST%` user matches SQL filters (active bank + periodic instruction) |
| NYD IDP Dashboard regression | `newyork` | IDP (PKCE + token exchange) | **Should pass** (~5–10s) when tunnel + Stage 1 services are up |

**Healthy Maven summary:**

```text
Tests run: 2, Failures: 0, Errors: 0, Skipped: 0
BUILD SUCCESS
```

---

## 5. View reports

```powershell
start mobile\mobile2\target\mobile-ms-report\index.html
```

Surefire XML: `mobile/mobile2/target/surefire-reports/`

---

## 6. Troubleshooting

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| `ORA-12541` on `localhost:41521` | DB tunnel not running | Start Stage 1 tunnel; confirm port **41521** |
| Wrong host file / QC4 DB used | Missing or wrong `-Dhost.properties` | Pass `-Dhost.properties=<hostname>.properties` |
| `No QAAUTOTEST mobile authentication data exists for branding okdirect` | No OKD test data on Stage 1 | Data gap — NYD leg can still validate; seed OKD user |
| `Failed to get login token` on **newyork** | Stage 1 auth/BFF issue | Check auth server + BFF; confirm `acceptance-stage1` profile |
| `Connection reset` on login | BFF down or network | Retry; confirm Stage 1 mobile stack is up |

---

## 7. Pre-run checklist

- [ ] Stage 1 DB tunnel up (`localhost:41521`)
- [ ] `<hostname>.properties` in `mobile/mobile1` and copied to `mobile/mobile2`
- [ ] `mvn -f mobile/mobile1/pom.xml install -DskipTests` succeeded
- [ ] Command uses **`acceptance-stage1`** (+ optional `-Dhost.properties=<hostname>.properties`)
- [ ] Review `target/mobile-ms-report/index.html`

---

## 8. Stage 1 vs QC4

| | **Stage 1** | **QC4** |
|---|-------------|---------|
| Profile | `acceptance-stage1` | `acceptance-qc4` |
| Host file | `<hostname>.properties` (tunnel) | `qc4.properties` |
| BFF | `unite-bff-wtn.stage1.acs529.com` | `unite-bff-wtn.qc4.unite529.com` |
| IDP (`newyork`) | **Works** on Stage 1 | **Unstable** on QC4 |

---

## Related docs

| Document | Topic |
|----------|-------|
| `07-LOCAL-SETUP-AND-RUN-GUIDE.md` | QC4 local setup |
| `18-MOBILE2-VERIFICATION-AND-MAPPING-RUNBOOK.md` | Full Mobile 2 verification matrix |
| `scripts/run-stage1-mobile2-rerun.ps1` | Batch Stage 1 mobile2 profiles |
