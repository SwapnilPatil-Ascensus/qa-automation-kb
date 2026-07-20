# qTest Schema Assessment

**Assessment date:** 2026-07-20  
**Live API access:** **Blocked** — `QTEST_BASE_URL`, `QTEST_API_TOKEN`, `QTEST_PROJECT_ID` not set  
**qTest MCP:** **Not configured**

## Executive conclusion

| Question | Status | Finding |
|----------|--------|---------|
| Official/internal qTest MCP? | **Verified** | None in Cursor MCP catalog |
| REST API usable today? | **Blocked** | No credentials configured |
| Historical schema inferable? | **Partial (Stale)** | PDF export + KB module mapping only |
| Row-level test-case IDs available? | **Verified absent** | UP assessment noted IDs not exported |

## How qTest marks automated tests (inferred from evidence)

| Mechanism | Evidence | Status |
|-----------|----------|--------|
| **Test Cycle** `PRIME` / `CL-*` | qTest daily report PDF; spike docs | **Inferred** |
| **Test Run** `TR-*` | Regression report detail tables | **Inferred** |
| **Executed case count** | 744 aggregate in PRIME cycle | **Stale (2026-06-29)** |
| **Automation flag / custom field** | Not visible in available export | **Unknown** |
| **Repository mapping field** | Not in export; code has no qTest IDs | **Verified gap** |

**Do not assume** field names such as `Automation Status` or `Automation ID` without live schema pull. Recommended first API calls after access:

```
GET /api/v3/projects/{projectId}/settings/test-case-fields
GET /api/v3/projects/{projectId}/test-cases?size=1
GET /api/v3/projects/{projectId}/test-runs?size=1
```

## Expected retrievable objects (qTest REST v3 — Planned)

| Object | Expected endpoint family | Verified live? |
|--------|-------------------------|----------------|
| Projects | `/projects` | **Blocked** |
| Modules | `/modules` | **Blocked** |
| Requirements | `/requirements` | **Blocked** |
| Test cases | `/test-cases` | **Blocked** |
| Test-case versions | `/test-cases/{id}/versions` | **Blocked** |
| Test runs | `/test-runs` | **Blocked** |
| Test cycles / suites | `/test-cycles`, `/test-suites` | **Blocked** |
| Execution status | run `status` fields | **Blocked** |
| Automation identifiers | custom fields | **Unknown** |
| Linked Jira issues | integrations / links | **Unknown** |
| Custom fields | `/settings/*-fields` | **Unknown** |
| Last modified / owners | case metadata | **Unknown** |
| Tags | case tags | **Unknown** |
| Test steps | `/test-cases/{id}/test-steps` | **Blocked** |
| Release/build/environment | run attributes | **Unknown** |

## Known project context (Stale export)

| Attribute | Value | Source |
|-----------|-------|--------|
| Project name | Automation Unite | qTest daily report PDF |
| Cycle | PRIME | Same |
| Executed population | 744 test cases | Same, 2026-06-29 |
| Module breakdown | 15 provisional modules | `v2-row-level-mapping.csv` |

## Automation linkage model (recommended — Planned)

```
Jira issue key  ←→  qTest requirement  ←→  qTest test case (PID)
                                              ↓
                                    automation_id custom field
                                              ↓
                          repository: class#method or suite XML + TestNG name
```

Until custom fields are confirmed, use **deterministic secondary keys**:

- Jenkins target name ↔ suite XML filename
- TestNG `<test name=` ↔ qTest case name (fuzzy — never auto-verify)

## Data-quality implications

See [`qtest-data-quality-summary.csv`](qtest-data-quality-summary.csv) and [`qtest-readiness-assessment.md`](qtest-readiness-assessment.md).

---

*No qTest records created or modified. Assessment based on Stale export + KB methodology.*
