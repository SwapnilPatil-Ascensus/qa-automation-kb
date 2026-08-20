# Mobile 2 — Nexus Archive + GitHub Actions Pipeline Guide

Guide for **QA (publish)** and **DevOps (consume)** using the Mobile 2 Maven archive published to Nexus.

**Primary use case:** run **Mobile 2** API tests from a pre-built artifact without cloning the full `api-test-automation` repo.

---

## 1. Overview

| Role | Action |
|------|--------|
| **QA / Automation** | Build → package archive ZIP → validate locally → publish to Nexus |
| **DevOps** | Download ZIP → extract → run Maven profile → collect HTML report |

### Artifact flow

```text
api-test-automation (source)
  mvn -f mobile/mobile2/pom.xml clean package -DskipTests
    └── target/jsonapi-mobile-mobile2-<version>-archive.zip
          └── upload to Nexus maven-releases
                └── pipeline downloads ZIP → extract → generate-resources surefire:test
```

---

## 2. Maven profile reference (Mobile 2)

Naming standard: **`mobile-ms-<module>-<integration|regression>`**

| Profile ID | TestNG suite | Test class |
|------------|--------------|------------|
| `mobile-ms-dashboard-integration` | `dashboard-integration-testng.xml` | `MobileDashboardRequestTest` |
| `mobile-ms-dashboard-regression` | `dashboard-regression-testng.xml` | `MobileDashboardRequestTest` |
| `mobile-ms-activity-integration` | `activity-integration-testng.xml` | `MobileActivityRequestTest` |
| `mobile-ms-activity-regression` | `activity-regression-testng.xml` | `MobileActivityRequestTest` |
| `mobile-ms-banks-integration` | `banks-integration-testng.xml` | `MobileBanksRequestTest` |
| `mobile-ms-banks-regression` | `banks-regression-testng.xml` | `MobileBanksRequestTest` |
| `mobile-ms-content-integration` | `content-integration-testng.xml` | `MobileContentRequestTest` |
| `mobile-ms-content-regression` | `content-regression-testng.xml` | `MobileContentRequestTest` |
| `mobile-ms-contribution-integration` | `contribution-integration-testng.xml` | `MobileContributionRequestTest` |
| `mobile-ms-contribution-regression` | `contribution-regression-testng.xml` | `MobileContributionRequestTest` |
| `mobile-ms-master-integration` | `master-integration-testng.xml` | All 5 modules (5 tests) |
| `mobile-ms-master-regression` | `master-regression-testng.xml` | All 5 modules (5 tests) |
| `mobile-ms-nexus-ci` | (helper — combine with any profile above) | Skips compiler for archive runs |

> **Note:** `mobile-ms-integration` was renamed to **`mobile-ms-dashboard-integration`**. Update pipelines accordingly.

All active suites use **Oklahoma Direct** (`okdirect`). Hawaii tests remain in XML but are `enabled="false"` (IDP on QC4).

---

## 3. Nexus coordinates

| Field | Value |
|-------|-------|
| **Repository** | `maven-releases` |
| **GroupId** | `jsonapi-mobile` |
| **ArtifactId** | `jsonapi-mobile-mobile2` |
| **Version** | `1.0.0` → bump to `1.0.1` after assembly fix (see §5) |
| **Archive classifier** | `archive` (ZIP) |

### Download URL pattern

```text
http://nexusdmznt1.int.acs529.com:8081/repository/maven-releases/jsonapi-mobile/jsonapi-mobile-mobile2/${VERSION}/jsonapi-mobile-mobile2-${VERSION}-archive.zip
```

### Related artifacts (resolved by Maven from Nexus — do not bundle in ZIP)

| Artifact | Purpose |
|----------|---------|
| `jsonapi-mobile-build:1.0.0:pom` | Parent POM |
| `jsonapi-mobile-mobile1:1.0.0:jar` | Shared auth base |
| `jsonapi-mobile-reporting:1.0.0:jar` | HTML report listener |
| `jsonapi-core`, `jsonapi-auth`, `jsonapi-lib` | Framework + QC4 config unpack |

### Files **not** in the ZIP (must exist at runtime)

| Item | How pipeline gets it |
|------|----------------------|
| `ci_settings.xml` | Checkout from repo or org template — **use absolute path** |
| `src/test/resources/config/qc4.properties` | `generate-resources` unpacks from `jsonapi-lib` |
| `src/main/resources/security/*` | `generate-resources` unpacks from `jsonapi-lib` |

---

## 4. What is inside the archive ZIP?

Built by `assembly/archive-mobile2-jsonapi.xml` during `mvn package`:

| Path in ZIP | Contents |
|-------------|----------|
| `pom.xml` | Module POM + all profiles |
| `target/classes/`, `target/test-classes/` | Pre-compiled `.class` files |
| `src/test/resources/user/qc4/*.json` | User fixtures (`okdirect`, `hawaii`) |
| `src/test/resources/sql/plan.sql` | Mobile min-version DB query (**required**) |
| `testsuites/*.xml` | All integration/regression/master suites |

**No Java sources** — do **not** run `mvn clean test` on the extracted archive.

---

## 5. QA — PowerShell: build archive

Script: `programs/unite-msc/api-test-automation/scripts/Build-Mobile2Archive.ps1`

```powershell
# Build-Mobile2Archive.ps1
# Builds Mobile 2 JAR + archive ZIP for Nexus publish.

param(
    [string]$RepoRoot = (Resolve-Path "$PSScriptRoot\..\..\..").Path,
    [string]$Version = "1.0.0"
)

$ErrorActionPreference = "Stop"

Write-Host "==> Building Mobile 2 parent (install dependencies)..." -ForegroundColor Cyan
mvn -f "$RepoRoot\mobile\pom.xml" clean install -DskipTests
if ($LASTEXITCODE -ne 0) { throw "Parent build failed" }

Write-Host "==> Packaging Mobile 2 archive..." -ForegroundColor Cyan
mvn -f "$RepoRoot\mobile\mobile2\pom.xml" clean package -DskipTests
if ($LASTEXITCODE -ne 0) { throw "Mobile2 package failed" }

$zip = "$RepoRoot\mobile\mobile2\target\jsonapi-mobile-mobile2-$Version-archive.zip"
$jar = "$RepoRoot\mobile\mobile2\target\jsonapi-mobile-mobile2-$Version.jar"

if (-not (Test-Path $zip)) { throw "Archive ZIP not found: $zip" }

Add-Type -AssemblyName System.IO.Compression.FileSystem
$entries = [System.IO.Compression.ZipFile]::OpenRead($zip).Entries | ForEach-Object { $_.FullName }
if (-not ($entries | Where-Object { $_ -like "*src/test/resources/sql/plan.sql" })) {
    throw "VALIDATION FAILED: plan.sql missing from archive ZIP"
}

Write-Host "BUILD OK" -ForegroundColor Green
Write-Host "  ZIP: $zip"
Write-Host "  JAR: $jar"
Write-Host "  plan.sql: present in ZIP"
```

**One-liner from repo root:**

```powershell
mvn -f mobile/pom.xml clean install -DskipTests
mvn -f mobile/mobile2/pom.xml clean package -DskipTests
```

Output:

```text
mobile/mobile2/target/jsonapi-mobile-mobile2-1.0.0-archive.zip
mobile/mobile2/target/jsonapi-mobile-mobile2-1.0.0.jar
```

---

## 6. QA — PowerShell: validate archive locally (before Nexus push)

Script: `programs/unite-msc/api-test-automation/scripts/Test-Mobile2ArchiveLocally.ps1`

Simulates what DevOps runs. **Requires QC4 mobile + DB up** for tests to pass; when QC4 is down, still validates ZIP layout and Maven startup.

```powershell
# Test-Mobile2ArchiveLocally.ps1
# Extracts archive ZIP and runs Nexus CI Maven command (same as DevOps pipeline).

param(
    [string]$RepoRoot = (Resolve-Path "$PSScriptRoot\..\..\..").Path,
    [string]$Version = "1.0.0",
    [string]$TestProfile = "mobile-ms-dashboard-integration,mobile-ms-nexus-ci"
)

$ErrorActionPreference = "Stop"

$zip = "$RepoRoot\mobile\mobile2\target\jsonapi-mobile-mobile2-$Version-archive.zip"
$ciSettings = "$RepoRoot\ci_settings.xml"
$extractRoot = "$RepoRoot\mobile\mobile2\target\mobile2-verify"

if (-not (Test-Path $zip)) {
    Write-Host "ZIP not found - run Build-Mobile2Archive.ps1 first" -ForegroundColor Yellow
    & "$PSScriptRoot\Build-Mobile2Archive.ps1" -RepoRoot $RepoRoot -Version $Version
}

if (-not (Test-Path $ciSettings)) {
    throw "ci_settings.xml not found at: $ciSettings"
}

Write-Host "==> Extracting archive..." -ForegroundColor Cyan
if (Test-Path $extractRoot) { Remove-Item $extractRoot -Recurse -Force }
New-Item -ItemType Directory -Path $extractRoot | Out-Null
Expand-Archive -Path $zip -DestinationPath $extractRoot -Force

$moduleDir = Get-ChildItem $extractRoot -Directory | Select-Object -First 1
if (-not $moduleDir) { throw "No version root folder inside ZIP" }

Write-Host "Module dir: $($moduleDir.FullName)" -ForegroundColor Gray

$checks = @(
    "$($moduleDir.FullName)\pom.xml",
    "$($moduleDir.FullName)\src\test\resources\sql\plan.sql",
    "$($moduleDir.FullName)\src\test\resources\user\qc4\okdirect.json",
    "$($moduleDir.FullName)\target\test-classes\mobile2\dashboard\MobileDashboardRequestTest.class"
)
foreach ($path in $checks) {
    if (-not (Test-Path $path)) { throw "Missing required file: $path" }
    Write-Host "  OK: $path" -ForegroundColor DarkGreen
}

Write-Host "==> Running Nexus CI (profile: $TestProfile)..." -ForegroundColor Cyan
Push-Location $moduleDir.FullName
try {
    mvn --settings $ciSettings `
        generate-resources surefire:test `
        "-P$TestProfile" `
        "-Denvironment.properties=qc4.properties" `
        "-DskipTests=false"
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Tests failed (QC4 may be down - check logs above)" -ForegroundColor Yellow
        exit $LASTEXITCODE
    }
    Write-Host "ALL TESTS PASSED" -ForegroundColor Green
}
finally {
    Pop-Location
}
```

**Manual quick test (Dashboard integration):**

```powershell
$RepoRoot = "C:\Workspace\GitLab\api-test-automation"
$Version = "1.0.0"
cd "$RepoRoot\mobile\mobile2\target\mobile2\jsonapi-mobile-mobile2-$Version"

mvn --settings "$RepoRoot\ci_settings.xml" `
  generate-resources surefire:test `
  "-Pmobile-ms-dashboard-integration,mobile-ms-nexus-ci" `
  "-Denvironment.properties=qc4.properties" `
  "-DskipTests=false"
```

> `ci_settings.xml` is **not** inside the ZIP. Always pass the **absolute path** to the repo copy.

**When QC4 is down:** expect auth/SSL/connection failures after `Loading plan: okdirect` — that still confirms archive + SQL + config unpack work.

---

## 7. QA — Publish to Nexus

### 7.0 Credentials (QA convention)

| Item | Value |
|------|--------|
| **Repository** | `maven-releases` |
| **Deploy user** | **`build`** — use this account for all QA uploads to `maven-releases` |
| **Read-only** | `unitedeveloper` (Maven `~/.m2/settings.xml`) can browse/download but returns **403** on deploy |
| **Password** | Team-shared; set `$env:NEXUS_PASS` locally or use Nexus UI — **do not commit** to git |

Upload path (same layout as existing releases):

`maven-releases/jsonapi-mobile/jsonapi-mobile-mobile2/<version>/`

### 7.1 Files to upload

| File | Nexus path segment |
|------|-------------------|
| `jsonapi-mobile-mobile2-<version>.pom` | `.../jsonapi-mobile-mobile2/<version>/` |
| `jsonapi-mobile-mobile2-<version>.jar` | same |
| `jsonapi-mobile-mobile2-<version>-archive.zip` | same |

Also publish if changed: `jsonapi-mobile-build-<version>.pom`, `jsonapi-mobile-mobile1-<version>.jar`, `jsonapi-mobile-reporting-<version>.jar`.

### 7.2 PowerShell helper (manual upload checklist)

Script: `programs/unite-msc/api-test-automation/scripts/Publish-Mobile2ToNexus.ps1`

```powershell
# Publish-Mobile2ToNexus.ps1
# Lists files ready for Nexus maven-releases upload. Use Nexus UI or org deploy tooling.

param(
    [string]$RepoRoot = (Resolve-Path "$PSScriptRoot\..\..\..").Path,
    [string]$Version = "1.0.1",
    [string]$NexusBase = "http://nexusdmznt1.int.acs529.com:8081/repository/maven-releases"
)

$ErrorActionPreference = "Stop"
$target = "$RepoRoot\mobile\mobile2\target"
$groupPath = "jsonapi-mobile/jsonapi-mobile-mobile2/$Version"

$files = @(
    "$target\jsonapi-mobile-mobile2-$Version.pom",
    "$target\jsonapi-mobile-mobile2-$Version.jar",
    "$target\jsonapi-mobile-mobile2-$Version-archive.zip"
)

foreach ($local in $files) {
    if (-not (Test-Path $local)) { throw "Missing: $local (run Build-Mobile2Archive.ps1 first)" }
    $name = Split-Path $local -Leaf
    Write-Host "Upload: $local"
    Write-Host "   URL: $NexusBase/$groupPath/$name" -ForegroundColor Cyan
}

Write-Host ""
Write-Host "After upload, set DevOps MOBILE2_VERSION=$Version" -ForegroundColor Green
```

### 7.3 Versioning

| Change | Action |
|--------|--------|
| Test code, suites, fixtures, assembly | Bump `jsonapi-mobile-mobile2` version (e.g. `1.0.0` → `1.0.1`) |
| Parent / mobile1 / reporting change | Bump `jsonapi-mobile-build` + siblings |

---

## 8. DevOps — Run tests from extracted archive

### 8.1 Extract

```bash
VERSION=1.0.1
curl -fSL -o mobile2.zip \
  "${NEXUS_BASE}/jsonapi-mobile/jsonapi-mobile-mobile2/${VERSION}/jsonapi-mobile-mobile2-${VERSION}-archive.zip"
unzip -q mobile2.zip -d mobile2
cd mobile2/jsonapi-mobile-mobile2-${VERSION}
```

### 8.2 Maven command (required pattern)

```bash
mvn --settings /path/to/ci_settings.xml \
  generate-resources surefire:test \
  -Pmobile-ms-dashboard-integration,mobile-ms-nexus-ci \
  -Denvironment.properties=qc4.properties \
  -DskipTests=false
```

| Flag / profile | Purpose |
|----------------|---------|
| `generate-resources` | Unpacks QC4 config, certs, framework SQL |
| `surefire:test` | Run TestNG without recompile |
| `mobile-ms-<module>-integration\|regression` | Picks TestNG suite |
| `mobile-ms-nexus-ci` | Skips compiler (archive has no `.java`) |
| **No `clean`** | Would delete pre-built `.class` files |

### 8.3 Example profiles

```bash
# Dashboard integration
-Pmobile-ms-dashboard-integration,mobile-ms-nexus-ci

# All modules regression (5 tests)
-Pmobile-ms-master-regression,mobile-ms-nexus-ci
```

---

## 9. GitHub Actions workflow

```yaml
name: Mobile 2 QC4

on:
  workflow_dispatch:
    inputs:
      mobile2_version:
        description: "Nexus jsonapi-mobile-mobile2 version"
        required: true
        default: "1.0.1"
      test_profile:
        description: "Maven profile (without nexus-ci — added automatically)"
        required: true
        default: "mobile-ms-dashboard-integration"
        type: choice
        options:
          - mobile-ms-dashboard-integration
          - mobile-ms-dashboard-regression
          - mobile-ms-master-integration
          - mobile-ms-master-regression

env:
  NEXUS_BASE: http://nexusdmznt1.int.acs529.com:8081/repository/maven-releases

jobs:
  mobile2-tests:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4
        with:
          repository: ascensus-gs/products/depot/qa-automation/api-test-automation
          sparse-checkout: ci_settings.xml
          sparse-checkout-cone-mode: false

      - uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: "17"

      - name: Download and extract Mobile 2 archive
        env:
          VERSION: ${{ inputs.mobile2_version }}
        run: |
          curl -fSL -u "${{ secrets.NEXUS_USER }}:${{ secrets.NEXUS_PASS }}" \
            -o mobile2.zip \
            "${NEXUS_BASE}/jsonapi-mobile/jsonapi-mobile-mobile2/${VERSION}/jsonapi-mobile-mobile2-${VERSION}-archive.zip"
          unzip -q mobile2.zip -d mobile2-workspace

      - name: Run tests
        working-directory: mobile2-workspace/jsonapi-mobile-mobile2-${{ inputs.mobile2_version }}
        run: |
          mvn --settings "${{ github.workspace }}/ci_settings.xml" \
            generate-resources surefire:test \
            -P"${{ inputs.test_profile }},mobile-ms-nexus-ci" \
            -Denvironment.properties=qc4.properties \
            -DskipTests=false -e

      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: mobile2-report-${{ inputs.mobile2_version }}
          path: |
            mobile2-workspace/jsonapi-mobile-mobile2-${{ inputs.mobile2_version }}/target/mobile-ms-report/
            mobile2-workspace/jsonapi-mobile-mobile2-${{ inputs.mobile2_version }}/target/surefire-reports/
```

---

## 10. Reports

| Output | Path |
|--------|------|
| HTML dashboard | `target/mobile-ms-report/index.html` |
| Surefire JUnit | `target/surefire-reports/TEST-*.xml` |

---

## 11. Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `ci_settings.xml does not exist` | Relative path from extracted folder | Use **absolute path** to repo `ci_settings.xml` |
| `File not found: src/test/resources/sql/plan.sql` | Old ZIP (pre `archive-mobile2-jsonapi.xml`) | Rebuild archive; bump version; republish |
| `File not found: src/main/resources/sql/plan.sql` | Skipped `generate-resources` | Always run `generate-resources` before `surefire:test` |
| `COMPILATION ERROR` | Used `clean test` on archive | Use `generate-resources surefire:test` + `mobile-ms-nexus-ci` |
| `SSLHandshakeException` / connection errors | QC4 mobile down or network | Wait for QC4 RT; archive layout may still be valid if `Loading plan: okdirect` appears |
| Wrong profile / 0 tests | Typo in profile name | Use `mobile-ms-dashboard-integration` (not `mobile-ms-integration`) |

---

## 12. Related docs

| Document | Topic |
|----------|-------|
| `mobile/mobile2/README.md` | Profile table + local run commands |
| `docs/02-daily-usage/01-local-setup-and-run-guide.md` | Local QC4 setup |
| `docs/02-daily-usage/03-html-reporting-guide.md` | Report validation |
| `ci_settings.xml` | Nexus mirror |

---

*Document owner: Mobile MSC QA. Notify DevOps when `MOBILE2_VERSION` changes.*
