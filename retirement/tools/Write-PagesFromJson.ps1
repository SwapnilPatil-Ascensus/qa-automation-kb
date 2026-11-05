<#
  Writes SharePoint pages (already converted to Markdown by the in-browser exporter) to disk.
  Input JSON = array of { id, title, cat, created, modified, author, editor, url, md, imgs }.
  Usage: .\Write-PagesFromJson.ps1 -InFile <json> -OutRoot <folder> [-Site "Team White"]
#>
param(
  [Parameter(Mandatory)] [string]$InFile,
  [Parameter(Mandatory)] [string]$OutRoot,
  [string]$Site = 'Team White SharePoint'
)
$raw = Get-Content -Raw -Encoding UTF8 $InFile
$obj = $raw | ConvertFrom-Json
if ($obj -is [string]) { $obj = $obj | ConvertFrom-Json }
elseif ($obj.PSObject.Properties.Name -contains 'result') { $v = $obj.result.value; if ($v -is [string]) { $obj = $v | ConvertFrom-Json } else { $obj = $v } }

function Get-Slug([string]$t) {
  $s = $t -replace '[\\/:*?"<>|\[\]#%&{}$!`''@+=]', ' '
  $s = ($s -replace '\s+', ' ').Trim() -replace ' ', '-'
  if ($s.Length -gt 70) { $s = $s.Substring(0, 70).TrimEnd('-') }
  if (-not $s) { $s = 'page' }
  return $s
}

$used = @{}
$index = @{}
foreach ($p in $obj) {
  $dir = Join-Path $OutRoot $p.cat
  if ($p.cat -like '06-*') { $dir = Join-Path $dir ([datetime]$p.created).Year }
  New-Item -ItemType Directory -Force -Path $dir | Out-Null
  $slug = Get-Slug $p.title
  $key = "$dir|$slug".ToLower()
  if ($used.ContainsKey($key)) { $slug = "$slug-$($p.id)" }
  $used[$key] = 1
  $path = Join-Path $dir "$slug.md"
  $fm = @(
    "# $($p.title)", '',
    "> Source: [$Site]($($p.url)) | Created: $(([datetime]$p.created).ToString('yyyy-MM-dd')) | Last modified: $(([datetime]$p.modified).ToString('yyyy-MM-dd')) | Author: $($p.author) | Last editor: $($p.editor)", '',
    '---', ''
  ) -join "`n"
  $body = if ($p.md) { $p.md } else { '*(page is a parent/container page with no body text of its own)*' }
  [System.IO.File]::WriteAllText($path, $fm + "`n" + $body + "`n", (New-Object System.Text.UTF8Encoding($false)))
  if (-not $index.ContainsKey($p.cat)) { $index[$p.cat] = New-Object System.Collections.ArrayList }
  [void]$index[$p.cat].Add([pscustomobject]@{ Title = $p.title; Rel = ($path.Substring($OutRoot.Length).TrimStart('\') -replace '\\', '/'); Modified = ([datetime]$p.modified).ToString('yyyy-MM-dd') })
}
$index.GetEnumerator() | Sort-Object Name | ForEach-Object { "{0}: {1} pages" -f $_.Name, $_.Value.Count }
$index.GetEnumerator() | ForEach-Object { $_.Value } | ConvertTo-Json -Depth 3 | Set-Content -Encoding UTF8 (Join-Path $OutRoot '_page-index.json')
