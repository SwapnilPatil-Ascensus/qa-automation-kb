# Publish-Mobile2ToNexus.ps1
# Lists files ready for Nexus maven-releases upload. Use Nexus UI or org deploy tooling.
#
# Nexus deploy credentials (QA convention):
#   User: build  (unitedeveloper is read-only on maven-releases — gets 403 on deploy)
#   Password: store locally only (e.g. $env:NEXUS_PASS or team vault) — never commit to git.
#   Upload path: maven-releases/jsonapi-mobile/jsonapi-mobile-mobile2/<version>/

param(
    [string]$RepoRoot = (Resolve-Path "$PSScriptRoot\..\..\..").Path,
    [string]$Version = "1.0.1",
    [string]$NexusBase = "http://nexusdmznt1.int.acs529.com:8081/repository/maven-releases",
    [string]$NexusUser = $(if ($env:NEXUS_USER) { $env:NEXUS_USER } else { "build" })
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
Write-Host "Nexus deploy user: $NexusUser (set NEXUS_USER / NEXUS_PASS for scripted upload)" -ForegroundColor Gray
Write-Host "After upload, set DevOps MOBILE2_VERSION=$Version" -ForegroundColor Green
