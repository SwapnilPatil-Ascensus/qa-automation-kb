# Environment Guide

## Hosts

| Purpose | Stage1 | QC4 | Dev |
|---------|--------|-----|-----|
| **Enrollment API** | `https://unite-bff-cloud.stage1.unite529.com` | `https://unite-bff-cloud.qc4.unite529.com` | `https://unite-bff-cloud.dev.unite529.com` |
| Mobile login (NOT enrollment) | `https://unite-bff-wtn.stage1.acs529.com` | `https://unite-bff-wtn.qc4.unite529.com` | — |
| CDN (fund images) | `cdn.stage1.acs529.com` | — | — |

**Critical:** `mobile/enrollment` config today points `mobile-authentication-uri` to `unite-bff-wtn`. Enrollment tests need a separate `enrollment-uri` → `unite-bff-cloud`.

---

## Stage1 (team default)

| Setting | Value |
|---------|-------|
| Host | `unite-bff-cloud.stage1.unite529.com` |
| Plan | `hawaii` |
| x-app-version | `1.8.0` minimum; `3.1.0+` for some plans |
| POST encryption | **Required** |
| DB for post-check | Limited — may need QC4 DB or service team confirmation |
| Status | **Approved for enrollment testing** (Aug 2026 meeting) |

## QC4

| Setting | Value |
|---------|-------|
| Host | `unite-bff-cloud.qc4.unite529.com` |
| POST encryption | **Required** |
| DB | `d01.oracle.acs529.com:1521:Q04` (in `qc4.properties`) |
| Status | Initial 500 on create-prospect; defer until Stage1 stable |

## Plan-specific Stage1 hosts

Some traunches use plan-branded hosts:

| Plan | Branding | Stage1 host |
|------|----------|-------------|
| Hawaii | `hawaii` | `unite-bff-cloud.stage1.unite529.com` |
| Oklahoma Direct | `okdirect` | `okd.stage1.acs529.com` |
| NJ Direct | `njdirect` | `njd.stage1.acs529.com` |
| Nevada Unique | `unique` | `ssga.stage1.acs529.com` |

Start with `hawaii` on cloud BFF; expand plans in Phase 3.

---

## Environment variables (Postman)

See `postman/Enrollment-Stage1.postman_environment.json`:

| Variable | Static / generated | Purpose |
|----------|-------------------|---------|
| `enrollment.host.url` | Static | Base URL |
| `enrollment.planId` | Static | Plan branding |
| `enrollment.username` | Generated | Unique per run |
| `enrollment.email` | Generated | Unique per run |
| `enrollment.usernameHash` | Generated | SHA-512 hash |
| `enrollment.prospectJwt` | From step 05 | Bearer token |
| `enrollment.fundId` | From step 04 | Allocation target |
| `enrollment.forceNewRun` | Manual toggle | Force new username |

---

## x-app-version

Fetched from DB in automation:

```sql
-- mobile.sql: get.mobile.min.version
SELECT tc.code_id, tc.description
FROM tu_codes tc
WHERE tc.type = 'MIN_MOBILE_VERSION' AND tc.ctl_rec_stat = 'A'
```

For Postman, use `1.8.0` (Stage1 env default). Update if GET `/plans/{id}` returns 426.

---

## Splunk debugging

Available for backend log investigation (per meeting). Query enrollment service logs by correlation ID from response when debugging 500 errors.

---

## Can steps be skipped per environment?

| Step | Stage1 | QC4 | Dev |
|------|--------|-----|-----|
| certificate (via CLI) | Required for encrypt | Required | May skip |
| usstates | Optional | Optional | Optional |
| wizard steps 06–12 | Optional | Optional | Optional |
| recurring contribution | Optional | Optional | Optional |
| routing verify | Optional | Optional | Optional |

No environment allows skipping encryption on POST for Stage1/QC4.
