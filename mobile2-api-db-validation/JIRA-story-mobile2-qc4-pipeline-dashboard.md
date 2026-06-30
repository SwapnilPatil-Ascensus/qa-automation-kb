# JIRA Story — Mobile2 QC4 API validation pipeline (Dashboard first)

**Sprint:** Current (from this sprint onwards)  
**Collaborators:** Chaitanya (framework/DevOps), Swapnil Patil (QA Automation)  
**KB module:** `qa-automation-kb/mobile2-api-db-validation/`  
**Framework repo:** `ags-unitemsc` → `jsonapi-mobile-mobile2` (TestNG / RestAssured)

---

## JIRA — Summary (title)

```
[UNITE-MSC][Mobile2] QC4 API validation pipeline — Mobile Dashboard vertical slice (expand to all features)
```

---

## JIRA — Description (copy below)

Paste into Jira Description field (visual editor — **not** a code block). Use **Markdown** headings (`##`).

---

**DESCRIPTION — copy below** ↓

## Goal

Stand up **QC4 CI pipeline** for **Mobile2 REST API validation** in the `jsonapi-mobile-mobile2` framework (TestNG + RestAssured), starting with **Mobile Dashboard** as the reference vertical slice, then expanding to all remaining mobile2 Cucumber feature areas.

This sprint: fix **dashboard** end-to-end in QC4 (connectivity → auth → API test green). Follow-on: replicate pipeline pattern for other features.

## Background

- Cucumber coverage exists in `unite-mobile2` (UniteMSC); new framework validates API responses via TestNG (`MobileDashboardRequestTest`, etc.).
- **Knowledge base** documents API → DB mapping, endpoints, auth flow: `qa-automation-kb/mobile2-api-db-validation/`
- **QC4 mobile login** was restored (RT 514351). Verified auth + dashboard via curl against `unite-bff-wtn.qc4.unite529.com`.
- Initial pipeline failure was `java.net.ConnectException: Connection refused` at `getMobileToken` — runner could not reach BFF (wrong host in properties vs. pod network), not missing GitHub secrets.

## Scope — Phase 1 (this sprint)

**Feature:** Mobile Dashboard (`mobiledashboard.feature` reference)

| Step | Endpoint | Method |
|------|----------|--------|
| Auth / JWT | `/mobile1api/v1/mobilemembersession` | POST |
| Dashboard | `/mobile2api/v1/mobiledashboard` | GET |
| YTD (later in same feature) | `/mobile2api/v1/mobileytdsummary/{ext}` | GET |

**QC4 BFF base URL (authoritative for pipeline):**

`https://unite-bff-wtn.qc4.unite529.com`

**Test class (framework):**

`mobile2.dashboard.MobileDashboardRequestTest#getMobileDashboard`

**Test plan:** `okdirect` (loaded via `DatabaseResourceManager`)

## Scope — Phase 2 (subsequent stories / same epic)

Expand QC4 pipeline to remaining mobile2 features (priority order from KB `STATUS.md`):

1. mobilebank, mobilecontribution, mobileactivity
2. mobileTransactionHistory, mobilePerformance, mobileBalanceTrend
3. investment, mobileStackup, mobileugift, planselection
4. contentservice (external CMS — no DB validation)
5. e2e (cross-feature index)

Full endpoint registry: `mobile2-api-db-validation/mappings/endpoint-registry.yaml`

## Auth model (NON_IDP — okdirect)

**No GitHub secret / Bearer token required upfront** for member session POST.

Required headers:

- `Content-Type: application/json`
- `X-App-Version: 3.9.0` (or framework app version)

Body: `planId`, `username`, `password` → response JWT at `_embedded.item.jwtToken`

Dashboard GET uses: `Authorization: Bearer {jwtToken}` + `X-App-Version`

**No HTTP proxy** expected for `*.unite529.com` from on-prem GitHub runner pod (direct route).

## Pipeline / DevOps requirements

### Environment config

| Property / setting | Value / notes |
|------------------|---------------|
| BFF host | `https://unite-bff-wtn.qc4.unite529.com` |
| Mobile1 API prefix | `/mobile1api/v1/` |
| Mobile2 API prefix | `/mobile2api/v1/` |
| Environment profile | QC4 (`qc4.properties` or equivalent) |
| `-Dapi.host` | Must match BFF host; confirm `qc4.properties` does not override to `localhost:8443` at runtime |
| Token URL property | Confirm `MobileServerClient.getMobileToken` uses same BFF host (may differ from `api.host`) |
| Proxy | Not required for unite529.com; RestAssured ignores `HTTP_PROXY` env unless Java `-Dhttps.proxyHost` set |
| Secrets | Test creds in test data / properties for okdirect; no OAuth client secret for NON_IDP auth probe |

### Pre-flight probe (run inside pod before Maven)

**Step 1 — Auth (expect HTTP 200, jwtToken in body):**

```
curl -sk -X POST "https://unite-bff-wtn.qc4.unite529.com/mobile1api/v1/mobilemembersession" \
  -H "Content-Type: application/json" \
  -H "X-App-Version: 3.9.0" \
  -d '{"planId":"okdirect","username":"QAMSCAUTO_REG_1234567890","password":"Newton@123"}'
```

**Step 2 — Extract JWT (if jq available):**

```
JWT=$(curl -sk -X POST "https://unite-bff-wtn.qc4.unite529.com/mobile1api/v1/mobilemembersession" \
  -H "Content-Type: application/json" \
  -H "X-App-Version: 3.9.0" \
  -d '{"planId":"okdirect","username":"QAMSCAUTO_REG_1234567890","password":"Newton@123"}' \
  | jq -r '._embedded.item.jwtToken')
echo "JWT length: ${#JWT}"
```

**Step 3 — Dashboard (expect HTTP 200):**

```
curl -sk -w "\nHTTP_CODE:%{http_code}\n" \
  -X GET "https://unite-bff-wtn.qc4.unite529.com/mobile2api/v1/mobiledashboard" \
  -H "Authorization: Bearer ${JWT}" \
  -H "X-App-Version: 3.9.0"
```

**Probe interpretation:**

- **200** → BFF reachable from pod; proceed to Maven
- **Connection refused** → pod → BFF network/routing (DevOps), not test assertion failure
- **ECONNRESET** → infra/LB issue (see RT 514351 pattern)

### Local / CI Maven commands (framework repo)

Run from `jsonapi-mobile-mobile2` module root:

```
# Single dashboard test (QC4 profile — adjust -P/-D to match repo conventions)
mvn test -Dtest=MobileDashboardRequestTest#getMobileDashboard -Dspring.profiles.active=qc4
```

If properties file driven:

```
mvn test -Dtest=MobileDashboardRequestTest#getMobileDashboard \
  -Dapi.host=https://unite-bff-wtn.qc4.unite529.com
```

Confirm actual profile names with Chaitanya (`qc4.properties`, Maven `-P` flags in `ags-unitemsc` workflow).

### GitHub Actions / workflow checklist

- [ ] Run auth curl probe as first job step (fail fast on network)
- [ ] Set BFF base URL in workflow env or properties (not localhost)
- [ ] Log resolved token URL / api.host at test startup (diagnostics)
- [ ] On-prem runner pod can reach `unite-bff-wtn.qc4.unite529.com:443` (no proxy)
- [ ] Publish Surefire report artifact on failure
- [ ] Document okdirect test member availability in QC4

## API validation flow (dashboard)

```
POST /mobile1api/v1/mobilemembersession  →  JWT (_embedded.item.jwtToken)
GET  /mobile2api/v1/mobiledashboard      →  MobileDashboard (HAL _embedded.item)
```

Downstream (for future API–DB compare, not blocking Phase 1 pipeline):

- Account, Profile, Metadata gateways → see KB `docs/02-features/mobiledashboard/overview.md`
- SQL validation queries: `sql/account/`, `sql/profile/`, `sql/metadata/`, `sql/composite/mobiledashboard/`

## Known failure modes

| Symptom | Likely cause | Owner |
|---------|--------------|-------|
| Connection refused at getMobileToken | Wrong host (localhost:8443) or pod cannot reach BFF | DevOps / Chaitanya — properties + network |
| ECONNRESET | LB / BFF down | Platform (RT) |
| 401/403 with HTTP response | Auth/creds/JWT claims | QA + framework config |
| Assertion on dashboard fields | Test data / API response mismatch | QA — compare with KB `@md1` scenario |

## References

| Resource | Path / link |
|----------|-------------|
| KB README | `qa-automation-kb/mobile2-api-db-validation/README.md` |
| Dashboard overview | `docs/02-features/mobiledashboard/overview.md` |
| Endpoint registry | `mappings/endpoint-registry.yaml` |
| Auth flow | `docs/01-shared/auth-and-session.md` |
| Architecture | `docs/00-architecture/bff-orchestration-flow.md` |
| QC4 login incident | `ISSUES/06242026/` (RT 514351) |
| UniteMSC feature (read-only) | `mobiledashboard.feature`, `MobileDashboardStepdefs.java` |

## Out of scope (this story)

- Modifying UniteMSC source repos
- Full API–DB SQL compare in CI (Phase 1 = API smoke green; DB validation KB continues in parallel)
- IDP-enabled plans (okdirect is NON_IDP; IDP flows need separate auth story)

**DESCRIPTION — copy above** ↑

---

## Acceptance criteria

### Phase 1 — Dashboard (this sprint)

- [ ] Auth curl probe returns **HTTP 200** from GitHub runner pod (documented in workflow or runbook)
- [ ] Dashboard curl probe returns **HTTP 200** with valid JSON using JWT from auth step
- [ ] `MobileDashboardRequestTest#getMobileDashboard` passes in QC4 CI pipeline
- [ ] BFF base URL `https://unite-bff-wtn.qc4.unite529.com` configured in properties/workflow (not localhost)
- [ ] Diagnostic logging confirms token URL matches BFF host
- [ ] Surefire report published on failure
- [ ] KB reference linked in story / Confluence / README

### Phase 2 — Expand (follow-on stories)

- [ ] Pipeline template documented for additional features (bank, contribution, activity, …)
- [ ] One story per feature group or parameterized workflow per `endpoint-registry.yaml`
- [ ] contentservice marked external/no-DB in pipeline docs

---

## Sub-tasks (suggested)

| # | Task | Assignee |
|---|------|----------|
| 1 | Run auth + dashboard curl probes inside pod; confirm 200 | Chaitanya / DevOps |
| 2 | Fix `qc4.properties` / `-Dapi.host` / token URL for BFF host | Chaitanya |
| 3 | Wire GitHub workflow pre-flight + Maven dashboard test | Chaitanya |
| 4 | Validate okdirect test data loads (`Loading plan: okdirect`) | Swapnil |
| 5 | Align dashboard assertions with KB `@md1` / okdirect fixtures | Swapnil |
| 6 | Document runbook in KB (this file + workflow link) | Swapnil |
| 7 | Phase 2 — backlog stories per feature from `STATUS.md` | Swapnil + Chaitanya |

---

## Labels (suggested)

`unite-msc`, `mobile2`, `qc4`, `pipeline`, `github-actions`, `mobiledashboard`, `api-validation`

---

## Related

- RT 514351 — QC4 mobile login ECONNRESET (resolved)
- KB module: `mobile2-api-db-validation`

---

**Author:** Swapnil Patil  
**Last updated:** 2026-06-26
