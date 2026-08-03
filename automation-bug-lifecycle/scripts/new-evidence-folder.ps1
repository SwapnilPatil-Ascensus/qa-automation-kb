#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Create a new regression evidence folder with templates.

.DESCRIPTION
    Bootstraps automation-bug-lifecycle/evidence/regression-reports/[MMDDYYYY]/
    with checklist, bug template, and triage worksheet.

.PARAMETER Date
    Folder date in MMDDYYYY format (e.g. 07242026)

.PARAMETER Feature
    Feature name for documentation (e.g. UniversalEnrollment)

.EXAMPLE
    .\new-evidence-folder.ps1 -Date "07242026" -Feature "UniversalEnrollment"
#>
param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^\d{8}$')]
    [string]$Date,

    [Parameter(Mandatory = $true)]
    [string]$Feature
)

$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ModuleRoot = Split-Path -Parent $ScriptDir

$EvidenceRoot = Join-Path $ModuleRoot "evidence\regression-reports"
$TargetDir = Join-Path $EvidenceRoot $Date
$TemplatesDir = Join-Path $ModuleRoot "templates"

if (-not (Test-Path $EvidenceRoot)) {
    New-Item -ItemType Directory -Path $EvidenceRoot -Force | Out-Null
}

if (Test-Path $TargetDir) {
    Write-Host "Folder already exists: $TargetDir" -ForegroundColor Yellow
    Write-Host "Adding missing templates only (will not overwrite existing files)."
} else {
    New-Item -ItemType Directory -Path $TargetDir -Force | Out-Null
    Write-Host "Created: $TargetDir" -ForegroundColor Green
}

function Copy-IfMissing($Source, $DestName) {
    $dest = Join-Path $TargetDir $DestName
    if (-not (Test-Path $dest)) {
        Copy-Item $Source $dest
        Write-Host "  + $DestName"
    }
}

Copy-IfMissing (Join-Path $TemplatesDir "BUG_DOCUMENTATION_TEMPLATE.md") "BUG_DOCUMENTATION_TEMPLATE.md"
Copy-IfMissing (Join-Path $TemplatesDir "TRIAGE_DECISION_WORKSHEET.md") "TRIAGE_DECISION_WORKSHEET.md"

$readmeSrc = Join-Path $TemplatesDir "EVIDENCE_FOLDER_README.md"
$readmeDest = Join-Path $TargetDir "README.md"
if (-not (Test-Path $readmeDest)) {
    $content = Get-Content $readmeSrc -Raw
    $content = $content -replace '\[MMDDYYYY\]', $Date
    $content = $content -replace '\[Feature / area\]', $Feature
    Set-Content -Path $readmeDest -Value $content -Encoding UTF8
    Write-Host "  + README.md (customized)"
}

$checklistDest = Join-Path $TargetDir "EVIDENCE_CHECKLIST.md"
if (-not (Test-Path $checklistDest)) {
    @"
# Evidence Checklist — $Date — $Feature

- [ ] Screenshot(s) saved to this folder
- [ ] Exception log (.txt) saved
- [ ] Test data reference saved
- [ ] CI console log saved (optional)
- [ ] TestNG report URL recorded in README.md
- [ ] Triage completed (see TRIAGE_DECISION_WORKSHEET.md)
- [ ] Bug doc created: ${Date}_${Feature}_[IssueType].md

## Prompts (automation-bug-lifecycle/prompts/)

1. Triage → 01-triage-regression-failure.md
2. Defect → 02-bug-report-prompt-h.md
3. Change set → GitLab PM + 03-gitlab-change-set.md
4. Resolution → 04-resolution-email.md
"@ | Set-Content -Path $checklistDest -Encoding UTF8
    Write-Host "  + EVIDENCE_CHECKLIST.md"
}

Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "  1. Add screenshots, logs, and test data to: $TargetDir"
Write-Host "  2. Run triage prompt: automation-bug-lifecycle/prompts/01-triage-regression-failure.md"
Write-Host "  3. If defect: run 02-bug-report-prompt-h.md in Cursor with images attached"
Write-Host ""
Write-Host "Suggested bug doc name: ${Date}_${Feature}_[IssueType].md"
