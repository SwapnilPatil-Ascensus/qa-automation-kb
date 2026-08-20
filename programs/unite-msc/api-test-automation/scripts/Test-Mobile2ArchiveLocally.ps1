# Test-Mobile2ArchiveLocally.ps1
# Extracts archive ZIP and runs Nexus CI Maven command (same as DevOps pipeline).

param(
    [string]$RepoRoot = (Resolve-Path "$PSScriptRoot\..\..\..").Path,
    [string]$Version = "1.0.1",
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
    "$($moduleDir.FullName)\src\test\resources\sql\mobile.sql",
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
