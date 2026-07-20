# Integration Capability Matrix

**Assessment date:** 2026-07-20  
**Status labels:** Verified · Inferred · Planned · Stale · Unknown · Blocked

## Summary

| Status | Count | Systems |
|--------|------:|---------|
| **Available** | 4 | Local KB exports, Python utilities, Brave Search MCP, Snyk MCP |
| **Partial** | 2 | Jenkins (exported logs only), qTest (stale PDF export) |
| **Blocked** | 6 | Jira MCP, GitLab MCP/Git API, GitHub MCP, 1Password, Slack, HTTP MCP |
| **Not configured** | 5 | qTest MCP, qTest REST env, GitHub CLI, SonarQube API, Nexus API |

**Conclusion (Verified):** Live cross-system reconciliation **cannot be automated today** without credential remediation for Jira, qTest, and GitLab. Historical evidence and local repository scans remain usable for a **read-only prototype**.

## MCP servers discovered (Cursor environment)

| Server | Status | Tools | Notes |
|--------|--------|-------|-------|
| `user-jira` | **Blocked** | `mcp_auth` only | Discovery error; `mcp_auth` timed out (30s) |
| `user-gitlab` | **Blocked** | `mcp_auth` only | Discovery error |
| `user-git` | **Blocked** | `mcp_auth` only | Discovery error (GitHub) |
| `user-http` | **Blocked** | `mcp_auth` only | Discovery error |
| `user-slack` | **Blocked** | `mcp_auth` only | Discovery error |
| `user-1password` | **Blocked** | `mcp_auth` only | Discovery error |
| `user-brave-search` | **Available** | `brave_web_search`, `brave_local_search` | Public web research only |
| `user-Snyk` | **Available** | SCA/SAST/container tools | Security scanning; not coverage intelligence |
| **qTest MCP** | **Not configured** | — | No qTest server in MCP catalog |

## Environment variables (names only — values not inspected)

| Variable | Present | Purpose |
|----------|---------|---------|
| `QTEST_BASE_URL` | **No** | qTest instance URL |
| `QTEST_API_TOKEN` | **No** | qTest REST bearer token |
| `QTEST_PROJECT_ID` | **No** | Default project scope |
| `JIRA_URL` | **No** | Atlassian site |
| `JIRA_API_TOKEN` | **No** | Jira REST auth |
| `GITLAB_TOKEN` | **Yes** (length 26) | GitLab API — **401 Unauthorized** on `/api/v4/user` |
| `GITLAB_PERSONAL_ACCESS_TOKEN` | **No** | Alternate GitLab auth |
| `SONAR_TOKEN` | **No** | SonarQube API |
| `SONAR_HOST_URL` | **No** | SonarQube host |
| `NEXUS_URL` | **No** | Artifact repository |

## Per-system detail

See machine-readable export: [`integration-capability-matrix.csv`](integration-capability-matrix.csv)

### qTest — no MCP; REST not configured

- **Official qTest MCP:** **Not configured** in this Cursor environment.
- **REST API:** Expected env vars documented above. **Not set.**
- **Historical evidence (Stale):** `universal-platform-coverage/00-input-evidence/v2-qtest-jenkins/QAAuto_UniteRegression_Daily_Report.PDF` — 744 executed cases, PRIME cycle, 2026-06-29.

### Jira / Confluence — MCP blocked

- Configuration exists (`user-jira`) but live read access **not verified**.
- Jira scope for GS inferred from KB: ACS-I-2679..2690 (UP), QA-1405 (Mobile2 CI), QA-1313 (Mobile1).

### GitLab — MCP blocked; token invalid

- `glab` CLI **installed** (v1.107.0).
- REST probe returned **401** — token insufficient or expired.
- Local `.gitlab-ci.yml` files **Verified** in `api-test-automation` and `prime-test-automation`.

### Jenkins — partial (exports only)

- No API URL/token in environment.
- Console extracts and perf tracker in KB: `universal-platform-coverage/00-input-evidence/v2-qtest-jenkins/`, `mobile2-api-db-validation/docs/01-shared/unite-msc-performance-testing-tracker.md`.

### SonarQube / Nexus — not configured for audit

- UniteMSC CI sets `RUN_SONARQUBE: false`.
- Nexus URLs in POM `distributionManagement` only — no API access.

## Recommended extraction methods (by priority)

1. **Extend existing Python collectors** (`universal-platform-coverage/03-tools/`, `government-savings-automation-assessment/tools/`) — **Available now**
2. **qTest REST API v3** — after `QTEST_*` credentials approved
3. **Jira REST API** — after MCP or token fix
4. **GitLab REST / glab** — after valid PAT with `read_api`
5. **Jenkins exported configs** — continue until API access granted

---

*Evidence: GetMcpTools catalog, env scan, GitLab API probe, local repo YAML review — all 2026-07-20*
