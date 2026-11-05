# Builds a "listen" HTML page from a Markdown document.
# Open the generated HTML in Microsoft Edge and press Ctrl+Shift+U (Read aloud).
# Natural voices: Edge > Read aloud > Voice settings. Mermaid diagrams are replaced by a short note.
#
# Usage:
#   .\Build-ListenPage.ps1 -InFile "..\..\00-getting-started\DAY-1-RETIREMENT-BRIEF.md" -OutFile ".\DAY-1-RETIREMENT-BRIEF.html" -Title "Day 1 Retirement brief"

param(
    [Parameter(Mandatory = $true)][string]$InFile,
    [Parameter(Mandatory = $true)][string]$OutFile,
    [string]$Title = ''
)

$ErrorActionPreference = 'Stop'
$inFull = (Resolve-Path $InFile).Path
$outFull = [IO.Path]::GetFullPath((Join-Path (Get-Location) $OutFile))
if (-not $Title) { $Title = [IO.Path]::GetFileNameWithoutExtension($inFull) }

$md = [IO.File]::ReadAllText($inFull, [Text.Encoding]::UTF8)
$json = ConvertTo-Json -InputObject $md
$json = $json.Replace('</', '<\/')

# Relative base so images and links in the Markdown still resolve from the listen folder
$outDir = [IO.Path]::GetDirectoryName($outFull) + '\'
$inDir = [IO.Path]::GetDirectoryName($inFull) + '\'
$base = (New-Object Uri $outDir).MakeRelativeUri((New-Object Uri $inDir)).ToString()
if (-not $base.EndsWith('/')) { $base += '/' }
if ($base -eq '') { $base = './' }

$htmlTitle = [Net.WebUtility]::HtmlEncode($Title)

$template = @'
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<base href="__BASE__">
<style>
  body { font-family: "Segoe UI", Arial, sans-serif; font-size: 20px; line-height: 1.65; max-width: 880px; margin: 0 auto; padding: 0 24px 80px; color: #1f1f1f; }
  .bar { position: sticky; top: 0; background: #fff8e1; border-bottom: 1px solid #f0d98a; padding: 10px 0; font-size: 15px; }
  h1 { font-size: 1.9em; margin-top: 0.8em; }
  h2 { margin-top: 1.6em; border-bottom: 2px solid #e5e5e5; padding-bottom: 4px; }
  h3 { margin-top: 1.3em; }
  table { border-collapse: collapse; font-size: 0.85em; margin: 12px 0; }
  th, td { border: 1px solid #cfcfcf; padding: 6px 10px; vertical-align: top; text-align: left; }
  th { background: #f3f6fa; }
  code { background: #f2f2f2; padding: 1px 4px; border-radius: 3px; font-size: 0.9em; }
  pre { background: #f5f5f5; padding: 12px; white-space: pre-wrap; }
  img { max-width: 100%; border: 1px solid #ddd; margin: 8px 0; }
  blockquote { border-left: 4px solid #9ecbff; margin-left: 0; padding-left: 14px; color: #444; }
</style>
</head>
<body>
<div class="bar"><b>Listen mode:</b> press <b>Ctrl+Shift+U</b> in Microsoft Edge to read this page aloud (Read aloud). Pick a Natural voice in the Read aloud settings. Diagrams are skipped in audio.</div>
<main id="content"><p>Loading document...</p></main>
<script id="md" type="application/json">__MD_JSON__</script>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<script>
  var raw = JSON.parse(document.getElementById('md').textContent);
  var cleaned = raw.replace(/```mermaid[\s\S]*?```/g, '\n_(Diagram in the Markdown version. Skipped in audio.)_\n');
  var el = document.getElementById('content');
  if (window.marked) {
    el.innerHTML = marked.parse(cleaned);
  } else {
    el.innerHTML = '';
    var pre = document.createElement('pre');
    pre.textContent = cleaned;
    el.appendChild(pre);
  }
</script>
</body>
</html>
'@

$html = $template.Replace('__TITLE__', $htmlTitle).Replace('__BASE__', $base).Replace('__MD_JSON__', $json)
[IO.File]::WriteAllText($outFull, $html, (New-Object Text.UTF8Encoding $false))
Write-Output "Wrote $outFull (images base: $base)"
