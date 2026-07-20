# Security and Access Requirements

**Assessment date:** 2026-07-20  
**Principle:** Read-only first; least privilege; no secrets in repository

## Required access (read-only)

| System | Role | Scopes / permissions | Env var names (document only) |
|--------|------|---------------------|------------------------------|
| **qTest** | Read-only API user | View projects, test cases, runs, requirements | `QTEST_BASE_URL`, `QTEST_API_TOKEN`, `QTEST_PROJECT_ID` |
| **Jira** | Read-only | Browse projects, issues, links | `JIRA_URL`, `JIRA_API_TOKEN` or `JIRA_EMAIL` + `JIRA_API_TOKEN` |
| **Confluence** | Read-only (optional) | View approved scope pages | `CONFLUENCE_URL`, `CONFLUENCE_API_TOKEN` |
| **GitLab** | Reporter / read_api | Read pipelines, schedules, artifacts | `GITLAB_TOKEN` or `GITLAB_PERSONAL_ACCESS_TOKEN` |
| **GitHub** | Read-only (if used) | Actions read, metadata | `GH_TOKEN` |
| **Jenkins** | Read-only (optional) | View jobs, console, artifacts | `JENKINS_URL`, `JENKINS_USER`, `JENKINS_API_TOKEN` |
| **SonarQube** | Browse | View coverage on projects | `SONAR_HOST_URL`, `SONAR_TOKEN` |

## Current gaps (Verified 2026-07-20)

| System | Status |
|--------|--------|
| qTest | **Not configured** |
| Jira MCP | **Blocked** |
| GitLab token | **Invalid** (401) |
| Sonar | **Not configured** |
| Jenkins API | **Not configured** |

## Security controls for collectors

1. **Never** commit tokens — use OS env or approved secret store  
2. **Never** print token values in logs or assessment artifacts  
3. Store output in **git-excluded** `coverage-intelligence-assessment/`  
4. Collectors must be **read-only** — no POST/PUT/DELETE to TM or ALM tools  
5. Rotate tokens on 90-day cadence (recommended)  
6. Snyk/Brave MCP — not authorized for production credential retrieval  
7. Audit trail: each snapshot includes `collected_at`, `collector_version`, `source_system`  

## Approval required before install

| Item | Needs approval? |
|------|-----------------|
| New Python package (`requests`, `openpyxl` already used) | **No** if already in GS tooling |
| New MCP server | **Yes** — document need first |
| Jenkins agent / GitLab runner changes | **Yes** — DevOps |
| Central database (Option C) | **Yes** — Security + Architecture |

## Data classification

| Data type | Handling |
|-----------|----------|
| Test case names / IDs | Internal — OK in git-excluded assessment |
| Pipeline results | Internal |
| Credentials | **Never persist** |
| PII in test data | Exclude from collectors; redact if found |

---

*No credentials were exposed or persisted during this audit.*
