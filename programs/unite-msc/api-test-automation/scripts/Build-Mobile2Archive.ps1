# Build-Mobile2Archive.ps1
# Builds Mobile 2 JAR + archive ZIP for Nexus publish.

param(
    [string]$RepoRoot = (Resolve-Path "$PSScriptRoot\..\..\..").Path,
    [string]$Version = "1.0.1"
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
if (-not ($entries | Where-Object { $_ -like "*src/test/resources/sql/mobile.sql" })) {
    throw "VALIDATION FAILED: mobile.sql missing from archive ZIP"
}

Write-Host "BUILD OK" -ForegroundColor Green
Write-Host "  ZIP: $zip"
Write-Host "  JAR: $jar"
Write-Host "  mobile.sql: present in ZIP (plan.sql generated at CI via generate-resources)"
