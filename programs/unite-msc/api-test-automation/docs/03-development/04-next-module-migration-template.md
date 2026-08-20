# Next Module Migration Template

Use when porting **Activities**, **Content**, **Banks**, or other Mobile 2 areas from legacy functional sources into canonical `mobile/`.

## Principles

1. **Canonical root only:** `mobile/mobile2/` — never recreate `mobile-microservices/`.
2. **Legacy as reference:** Old Cucumber WAR tests and Postman collections are **functional reference only** — do not copy Cucumber structure blindly.
3. **Lean first slice:** One happy-path TestNG test + POJO conversion + minimal business asserts (mirror Dashboard).
4. **Shared auth:** Extend `MobileBaseRequestTest`; use `setTestUser("1")` for Hawaii non-IDP baseline.
5. **SQL later:** Add DB reconciliation only when dev provides SQL / source mapping.
6. **Reporting:** Add `MobileMsHtmlReportListener` to suite XML; use `@Test(description=...)` or `MobileMsReportCaseRegistry`.
7. **Secrets:** Never log or report raw tokens, passwords, or account numbers.

## Recommended Layout (new module)

```text
mobile/mobile2/
├── testsuites/<module>-integration-testng.xml
├── testsuites/<module>-regression-testng.xml   # optional until >1 test
├── src/test/java/mobile2/<module>/
│   ├── <Module>RequestTest.java
│   └── pojo/                                   # one POJO per file, extend BasePOJO
├── src/test/resources/user/qc4/hawaii.json     # reuse unless module needs new fixture
└── pom.xml                                     # add profile ids: mobile-ms-<module>-integration
```

## Step-by-Step

| Step | Action |
|------|--------|
| 1 | Read legacy behavior (Cucumber feature / old `unite-mobile2` if in git history) — note endpoints, happy path, key fields |
| 2 | Create POJOs for response fragments (HAL `_embedded` pattern if applicable) |
| 3 | Create `<Module>RequestTest extends MobileBaseRequestTest` with `@BeforeMethod(groups={"setup"})` inherited |
| 4 | One `@Test(description="...")` — GET/POST with `client.invokeRestApi`, status + POJO asserts |
| 5 | Add TestNG suite XML with `branding=hawaii`, `JsonApiResourceManager`, `MobileMsHtmlReportListener` |
| 6 | Add Maven profile(s) in `mobile/mobile2/pom.xml` pointing at suite XML |
| 7 | Document commands in `07-LOCAL-SETUP-AND-RUN-GUIDE.md` and coverage in `11-DASHBOARD-COVERAGE-MATRIX.md` (or module-specific matrix) |
| 8 | Run QC4 validation; verify `target/mobile-ms-report/index.html` — no secrets |

## Test Pattern (sketch)

```java
public class ActivitiesRequestTest extends MobileBaseRequestTest {
    @Override protected MOBILE_TYPE getStream() { return MOBILE_TYPE.MOBILE2; }

    @Test(description = "GET activities returns expected contract")
    public void getActivities() throws Exception {
        setTestUser("1");
        HttpRestApiClientResponse response = client.invokeRestApi(
            RestType.GET, "/mobile2api/v1/...", null, null, BodyType.NOTAPPLICABLE, null);
        assertEquals(response.getStatusCode(), HTTP_STATUS_CODES.OK.code);
        // POJO asserts — prefer assertThat when comparing full objects
    }
}
```

## What not to port from old `mobile-microservices`

| Old artifact | Action |
|--------------|--------|
| `MobileDashboardClient` / module-specific clients | Use `MobileHttpRestApiClient` via base class |
| Large assertion helper classes | Inline or small private methods until ≥3 tests need sharing |
| `MobileApiReportTrace` | Use listener + optional `setAuthMetadata` |
| 8-test regression upfront | Start with 1 test; expand with matrix doc |
| Auth negative tests in module suite | Keep in auth scope (`mobile/mobile1`) |
| Duplicate `MobileHttpRestApiClient` under mobile2 | Use `mobile/mobile1` dependency |

## Documentation Checklist (per module)

- [ ] Row in `10-LEGACY-TO-NEW-MIGRATION.md`
- [ ] Coverage table (new file or extend `11-DASHBOARD-COVERAGE-MATRIX.md`)
- [ ] Run commands in `07-LOCAL-SETUP-AND-RUN-GUIDE.md`
- [ ] `mobile/mobile2/README.md` updated
- [ ] Out-of-scope items listed (SQL, IDP, negatives)

## Profile Naming Convention

Keep existing `mobile-ms-*` profile ids where already established (Dashboard). New modules:

- `mobile-ms-<module>-integration`
- `mobile-ms-<module>-regression` (when multiple regression tests exist)

Align suite `name` attribute with report portal subtitles (listener uses suite name heuristics).
