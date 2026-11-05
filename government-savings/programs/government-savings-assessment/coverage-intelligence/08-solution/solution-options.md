# Solution Options — Coverage Intelligence

**Assessment date:** 2026-07-20  
**Default recommendation:** **Option A** — extend existing Python utility

## Option A — Extend existing Python coverage utility

| Criterion | Assessment |
|-----------|------------|
| **Description** | Scheduled/local Python collectors: qTest REST, Jira REST/MCP, repo parsers, pipeline API parsers → CSV/Excel/JSON |
| **Delivery time** | 30–45 days to first automated register |
| **Maintenance cost** | **Low–Medium** — scripts in `qa-automation-kb` |
| **Security** | Env-based secrets; read-only tokens; git-excluded output |
| **Scalability** | Sufficient for GS scope (<20 repos) |
| **Reliability** | Depends on API stability; versioned JSON snapshots |
| **MCP dependency** | **Optional** — prefer REST for schedulers |
| **Auditability** | **High** — versioned artifacts + formulas in markdown |
| **Adoption ease** | **High** — builds on UP + GS assessment patterns |
| **Failure modes** | Token expiry; API pagination; schema drift |
| **Ownership** | QA Automation + tooling champion |
| **Verdict** | **Recommended** |

## Option B — CI-native reporting

| Criterion | Assessment |
|-----------|------------|
| **Description** | Each repo publishes normalized `coverage-metadata.json` as CI artifact; central aggregator |
| **Delivery time** | 60–90 days (requires DevOps per-repo changes) |
| **Maintenance cost** | **Medium** — distributed across teams |
| **Security** | GitLab artifact retention; no central DB |
| **Scalability** | **High** at scale |
| **Reliability** | **High** for execution evidence (C, D) |
| **MCP dependency** | None |
| **Auditability** | **High** per pipeline run |
| **Adoption ease** | **Medium** — needs template + compliance |
| **Failure modes** | Inconsistent metadata schema across repos |
| **Ownership** | DevOps + QA standards |
| **Verdict** | **Recommended as Phase 2** complement to Option A |

## Option C — Dedicated coverage intelligence service

| Criterion | Assessment |
|-----------|------------|
| **Description** | Central DB, scheduled collectors, reconciliation engine, dashboard, API, trend history |
| **Delivery time** | 6–12+ months |
| **Maintenance cost** | **High** |
| **Security** | DB access control; service account governance |
| **Scalability** | **High** |
| **Reliability** | Depends on platform team |
| **MCP dependency** | None (REST preferred) |
| **Auditability** | **High** if built correctly |
| **Adoption ease** | **Low** initially |
| **Failure modes** | Over-engineering; stale data if collectors fail silently |
| **Ownership** | Platform / QA engineering |
| **Verdict** | **Not recommended now** — Options A+B insufficient only if proven at 90-day review |

## Comparison matrix

| | Option A | Option B | Option C |
|---|:---:|:---:|:---:|
| Time to value | **Fast** | Medium | Slow |
| Cost | **Low** | Medium | High |
| Evidence quality | Good | **Best for execution** | Best (if maintained) |
| Fits read-only audit phase | **Yes** | Partial | No |
| Leadership reporting | **Yes** | Yes | Yes |

## Recommendation

**Phase 1 (0–30d):** Option A — read-only register from KB + repo parsers + manual refresh slots for qTest/Jira when creds arrive.  
**Phase 2 (30–90d):** Option B — CI artifact contract for `api-test-automation`, `prime-test-automation`, UniteMSC template.  
**Phase 3 (90d+):** Reassess Option C only if trend history and workflow ownership justify it.

---

*See `recommended-architecture.md`, `minimum-viable-implementation-plan.md`*
