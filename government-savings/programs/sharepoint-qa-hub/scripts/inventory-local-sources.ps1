# Inventory local documentation sources (no SharePoint login).
$ErrorActionPreference = "Stop"
$root = Resolve-Path (Join-Path $PSScriptRoot "..\..\..\qa-knowledge-base\10_IMPORTS_RAW")

function Count-Files($path, $filter) {
  if (-not (Test-Path -LiteralPath $path)) { return 0 }
  @(Get-ChildItem -LiteralPath $path -Recurse -File -Filter $filter -ErrorAction SilentlyContinue).Count
}

$hubs = @(
  @{ Name = "auto-qa-dochub"; Path = Join-Path $root "confluence_exports\auto-qa-dochub" },
  @{ Name = "Demand Planning Reports"; Path = Join-Path $root "confluence_exports\Demand Planning Reports" },
  @{ Name = "Performance hub"; Path = Join-Path $root "Performance QA – Home & Documentation Hub" }
)

Write-Host "10_IMPORTS_RAW inventory"
Write-Host "======================="
foreach ($h in $hubs) {
  $pdf = Count-Files $h.Path "*.pdf"
  $docx = Count-Files $h.Path "*.docx"
  $md = Count-Files $h.Path "*.md"
  Write-Host ("{0}: pdf={1} docx={2} md={3}" -f $h.Name, $pdf, $docx, $md)
}

$sp = Join-Path $root "sharepoint_exports"
if (Test-Path -LiteralPath $sp) {
  Write-Host ("sharepoint_exports: pdf={0} docx={1} md={2}" -f (Count-Files $sp "*.pdf"), (Count-Files $sp "*.docx"), (Count-Files $sp "*.md"))
} else {
  Write-Host "sharepoint_exports: (folder not created yet — drop OneDrive/PnP export here)"
}
