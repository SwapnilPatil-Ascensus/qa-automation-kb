# qTest Readiness Assessment

**Assessment date:** 2026-07-20

## Readiness scorecard

| Dimension | Rating | Status | Notes |
|-----------|--------|--------|-------|
| API connectivity | **Not ready** | Blocked | No `QTEST_*` env vars |
| MCP integration | **Not ready** | Not configured | No qTest MCP server |
| Export freshness | **Stale** | 21+ days | Last PDF 2026-06-29 |
| Row-level IDs | **Not ready** | Verified gap | Module aggregates only |
| Jira linkage quality | **Unknown** | Blocked | No Jira API |
| Automation field clarity | **Unknown** | Blocked | Schema not pulled |
| Repository crosswalk | **Not ready** | Verified gap | No IDs in test source |
| Leadership denominator | **Partial** | Stale | 744 V2 population only; V3 not qTest-keyed |

## Can qTest serve as scope denominator?

| Use case | Ready? | Recommendation |
|----------|--------|----------------|
| V2 UI regression inventory | **Partial** | Use 744 executed PRIME population with **module inclusion rules** — Stale until refresh |
| V3 UI regression | **No** | V3 uses TestNG in GitLab; qTest not authoritative |
| API endpoint coverage | **No** | Use approved endpoint catalog (Dinesh workbooks + code) |
| MSC Mobile 1/2 | **No** | qTest mapping not evidenced in repos |
| Performance journeys | **Planned** | QA-S-PERF-005 — linkage story open |
| GS-wide single % | **No** | Multiple frameworks; separate denominators required |

## Minimum remediation before automated intelligence

| # | Action | Owner type | Unblocks |
|---|--------|------------|----------|
| 1 | Provision read-only qTest API token + project ID | qTest admin | Live inventory pull |
| 2 | Export test-case custom fields (automation, Jira link) | QA tooling | Schema confirmation |
| 3 | Refresh PRIME cycle execution export | QA | Execution coverage (C) |
| 4 | Define approved in-scope regression suite IDs | BA + QA | Defensible denominator |
| 5 | Add `automation_id` to new/ maintained tests in code + qTest | QA Automation | Repository crosswalk |

## qTest MCP evaluation

| Option | Finding |
|--------|---------|
| Official Tricentis qTest MCP | **Not present** in environment |
| Internal custom MCP | **Not found** in workspace or MCP catalog |
| **Recommended path** | **Option A:** Python REST collector with env-based secrets (no token in source) |

## Expected environment variables (document only)

```
QTEST_BASE_URL=https://<tenant>.qtestnet.com
QTEST_API_TOKEN=<read-only-api-token>
QTEST_PROJECT_ID=<numeric-project-id>
```

Optional: `QTEST_PAGE_SIZE=100` for pagination control.

---

*Status: qTest is a necessary test-management source but **not reliable as sole GS denominator** without refresh, schema validation, and Jira linkage audit.*
