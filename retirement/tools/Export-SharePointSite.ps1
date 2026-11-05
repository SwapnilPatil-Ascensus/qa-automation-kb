#Requires -Version 5.1
<#
.SYNOPSIS
  Bulk-export a SharePoint Online site into retirement/sharepoint-export/ for offline agent search.

.DESCRIPTION
  Uses PnP.PowerShell with INTERACTIVE login (your SSO + MFA in a browser window).
  Does not store passwords in the repo. Run locally on your Ascensus laptop.

.EXAMPLE
  .\Export-SharePointSite.ps1 -SiteUrl "https://ascensus0.sharepoint.com/sites/Government_Savings-_Software_Development"
#>
param(
    [Parameter(Mandatory = $true)]
    [string] $SiteUrl,

    [string] $OutRoot = (Join-Path (Split-Path $PSScriptRoot -Parent) "sharepoint-export")
)

$ErrorActionPreference = "Stop"

function Ensure-PnP {
    if (-not (Get-Module -ListAvailable -Name PnP.PowerShell)) {
        Write-Host "Installing PnP.PowerShell for current user (one-time)..."
        Install-Module PnP.PowerShell -Scope CurrentUser -Force -AllowClobber
    }
    Import-Module PnP.PowerShell -ErrorAction Stop
}

Ensure-PnP

$siteSlug = ($SiteUrl -replace 'https?://', '' -replace '[\\/:]+', '_').Trim('_')
$dest = Join-Path $OutRoot $siteSlug
New-Item -ItemType Directory -Force -Path $dest | Out-Null

Write-Host "Connecting to $SiteUrl (interactive SSO — complete sign-in in the browser)..."
Connect-PnPOnline -Url $SiteUrl -Interactive

Write-Host "Listing Site Pages..."
$pages = Get-PnPListItem -List "Site Pages" -PageSize 500 -Fields "FileLeafRef", "Title", "Modified"
$manifest = @()
foreach ($p in $pages) {
    $name = $p.FieldValues.FileLeafRef
    if (-not $name) { continue }
    $rel = "SitePages/$name"
    $local = Join-Path $dest $rel
    $dir = Split-Path $local -Parent
    New-Item -ItemType Directory -Force -Path $dir | Out-Null
    try {
        Get-PnPFile -Url $rel -Path $dir -Filename $name -AsFile -ErrorAction Stop
        $manifest += [pscustomobject]@{ Type = "SitePage"; Path = $rel; Title = $p.FieldValues.Title; Modified = $p.FieldValues.Modified }
    } catch {
        Write-Warning "Skip page: $rel — $($_.Exception.Message)"
    }
}

Write-Host "Exporting default Documents library (may take a while)..."
$docRoot = Join-Path $dest "SharedDocuments"
New-Item -ItemType Directory -Force -Path $docRoot | Out-Null
try {
    Get-PnPFolder -Url "Shared Documents" -ErrorAction Stop | Out-Null
    # Recursive download via PnP batch — flatten one level of common onboarding folders
    $folders = @("Shared Documents", "Documents")
    foreach ($folderUrl in $folders) {
        try {
            $folder = Get-PnPFolder -Url $folderUrl
            Get-PnPFolderItem -FolderSiteRelativeUrl $folderUrl -ItemType File -Recursive -ErrorAction SilentlyContinue | ForEach-Object {
                $target = Join-Path $docRoot ($_.Name)
                if (-not (Test-Path $target)) {
                    try {
                        Get-PnPFile -Url $_.ServerRelativeUrl -Path $docRoot -Filename $_.Name -AsFile -ErrorAction Stop
                        $manifest += [pscustomobject]@{ Type = "File"; Path = $_.ServerRelativeUrl; Title = $_.Name; Modified = $_.TimeLastModified }
                    } catch {
                        Write-Warning "Skip file: $($_.ServerRelativeUrl)"
                    }
                }
            }
        } catch { }
    }
} catch {
    Write-Warning "Documents library export partial or skipped: $($_.Exception.Message)"
}

$manifest | Export-Csv -Path (Join-Path $dest "_export-manifest.csv") -NoTypeInformation -Encoding UTF8
Write-Host "Done. Files under: $dest"
Write-Host "Commit export to git only if policy allows (no secrets/PII)."

Disconnect-PnPOnline
