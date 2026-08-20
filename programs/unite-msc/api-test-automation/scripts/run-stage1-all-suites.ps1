# Run all Mobile 1 + Mobile 2 Stage 1 suite profiles (Java 17, Stage 1 DB via LT12800.properties)
$ErrorActionPreference = 'Continue'
$env:JAVA_HOME = 'C:\Users\swpatil\scoop\apps\openjdk17\current'
$env:PATH = "$env:JAVA_HOME\bin;C:\Program Files\apache-maven-3.9.9\bin;" + [Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User')

$root = 'c:\Workspace\GitLab\api-test-automation'

# mobile2 depends on the installed mobile1 JAR (rowNumber auth mapping); install before mobile2 suites
mvn -f "$root\mobile\mobile1\pom.xml" install -DskipTests -q

$hostFile = "$root\mobile\mobile1\src\test\resources\config\LT12800.properties"
$hostCopy = "$root\mobile\mobile2\src\test\resources\config\LT12800.properties"
if (Test-Path $hostFile) { Copy-Item $hostFile $hostCopy -Force }

$script:results = @()
$log = "$root\mobile\stage1-all-suites-results.log"
'' | Set-Content $log

function Run-Suite {
    param($Module, $Profile)
    $pom = if ($Module -eq 'mobile1') { "$root\mobile\mobile1\pom.xml" } else { "$root\mobile\mobile2\pom.xml" }
    if ($Module -eq 'mobile1') {
        $cmd = "mvn -f `"$pom`" test `"-P$Profile`" `"-Dmobile.ms.report.environment=Stage1`""
    } else {
        $cmd = "mvn -f `"$pom`" test `"-P$Profile,acceptance-stage1`" `"-Dmobile.ms.report.environment=Stage1`""
    }
    Write-Host "`n========== $Module : $Profile (Stage1) ==========" | Tee-Object -FilePath $log -Append
    $out = Invoke-Expression $cmd 2>&1
    $outText = ($out | Out-String)
    $pass = ($outText -match 'BUILD SUCCESS') -and ($outText -notmatch 'BUILD FAILURE')
    $testMatch = [regex]::Match($outText, 'Tests run: (\d+), Failures: (\d+), Errors: (\d+), Skipped: (\d+)')
    $tests = if ($testMatch.Success) {
        "run=$($testMatch.Groups[1].Value) fail=$($testMatch.Groups[2].Value) err=$($testMatch.Groups[3].Value) skip=$($testMatch.Groups[4].Value)"
    } else { 'n/a' }
    $line = [PSCustomObject]@{ Module = $Module; Profile = $Profile; Pass = $pass; Tests = $tests }
    $script:results += $line
    "$Module | $Profile | Pass=$pass | $tests" | Tee-Object -FilePath $log -Append
    if (-not $pass) { $out | Select-String -Pattern 'FAILURE|ERROR|No QAAUTOTEST|401|SSLHandshake|ORA-' | Select-Object -First 5 | Tee-Object -FilePath $log -Append }
}

Run-Suite mobile1 acceptance-stage1

$m2Profiles = @(
    'mobile-ms-master-regression','mobile-ms-master-integration',
    'mobile-ms-dashboard-regression','mobile-ms-dashboard-integration',
    'mobile-ms-activity-regression','mobile-ms-activity-integration',
    'mobile-ms-banks-regression','mobile-ms-banks-integration',
    'mobile-ms-content-regression','mobile-ms-content-integration',
    'mobile-ms-contribution-regression','mobile-ms-contribution-integration',
    'mobile-ms-investment-regression','mobile-ms-investment-integration',
    'mobile-ms-plans-regression','mobile-ms-plans-integration',
    'mobile-ms-transactionhistory-regression','mobile-ms-transactionhistory-integration',
    'mobile-ms-ugift-regression','mobile-ms-ugift-integration',
    'mobile-ms-stackup-regression','mobile-ms-stackup-integration',
    'mobile-ms-balancetrend-regression','mobile-ms-balancetrend-integration'
)
foreach ($p in $m2Profiles) { Run-Suite mobile2 $p }

if (Test-Path $hostCopy) { Remove-Item $hostCopy -Force }

"`n=== STAGE1 SUMMARY ===" | Tee-Object -FilePath $log -Append
$script:results | Format-Table -AutoSize | Out-String | Tee-Object -FilePath $log -Append
$script:results | Export-Csv "$root\mobile\stage1-all-suites-results.csv" -NoTypeInformation
Write-Host "Passed: $(($script:results | Where-Object Pass).Count) / $($script:results.Count)"
