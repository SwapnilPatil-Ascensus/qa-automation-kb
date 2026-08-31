# Maven Commands Index

**Authoritative run commands** are in module READMEs. This page is an index.

## Parent build

```powershell
mvn -f mobile/pom.xml clean install -DskipTests
```

## Module READMEs

| Module | Path |
|--------|------|
| Mobile 1 | `api-test-automation/mobile/mobile1/README.md` |
| Mobile 2 | `api-test-automation/mobile/mobile2/README.md` |
| Enrollment | `api-test-automation/mobile/enrollment/README.md` |

## Batch regression

```powershell
# From qa-automation-kb clone:
.\programs\unite-msc\api-test-automation\scripts\run-qc4-all-suites.ps1
.\programs\unite-msc\api-test-automation\scripts\run-stage1-all-suites.ps1
```

Scripts expect `$root = c:\Workspace\GitLab\api-test-automation`.

## Reports

```powershell
start mobile\mobile2\target\mobile-ms-report\index.html
```
