# Preeti — Quick Start: IDP Login + Post-Login Banner Pages

**Goal:** Deploy the updated JMeter script (6 new post-login `.cs` GETs), validate on **stage1**, then run the stakeholder load profile.

> **Script is ready** in `scripts/jia-banner-post-login/idp-login-resources.jmx` — you do not need to build it from scratch. Follow deploy steps below.

---

## Phase 1 — Deploy the script

### 1. Use the prepared script

| File | Path in this KB |
|------|-----------------|
| JMeter script (modified) | `scripts/jia-banner-post-login/idp-login-resources.jmx` |
| Deploy instructions | `scripts/jia-banner-post-login/DEPLOY.md` |
| Test data (unchanged) | `performance-test-automation/.../idp-login-stage1.csv` |
| Taurus YAML (optional) | `scripts/jia-banner-post-login/idp-login-resources-remote.yaml` |

Copy `idp-login-resources.jmx` into the GitLab `performance-test-automation` repo per [DEPLOY.md](../../scripts/jia-banner-post-login/DEPLOY.md).

### 2. What was added (already in the JMX)

Controller **8-A. Post-Login Dashboard Pages (CS)** — 6 GET samplers after step 8, before logout:

| Label | Path |
|-------|------|
| 8-A-1. Auth Custom Banner (CS) | `${plan-tpl}/auth/customBannerMessage.cs` |
| 8-A-2. Auth Side Banner (CS) | `${plan-tpl}/auth/sideBannerMessage.cs` |
| 8-A-3. AL Custom Banner (CS) | `${plan-tpl}/al/customBannerMessage.cs` |
| 8-A-4. AO Custom Banner (CS) | `${plan-tpl}/ao/customBannerMessage.cs` |
| 8-A-5. AO Overview (CS) | `${plan-tpl}/ao/overview.cs` |
| 8-A-6. AL List (CS) | `${plan-tpl}/al/list.cs` |

**Example for NYD on stage1:** `https://nyd.stage1.acs529.com/nytpl/auth/customBannerMessage.cs`

### 3. Validate against browser Network tab

Mayank confirmed all 6 pages appear in the **browser Network tab** during a manual IDP login. Before finalizing:

1. Open Firefox/Chrome DevTools → Network
2. Log in manually on stage1 for at least **nyd** (example plan from stakeholder chat)
3. Compare each `.cs` request for:
   - Exact URL path (query params?)
   - Request headers (especially cookies, `x-sardine-session-key`)
   - Response code expected (200?)
4. Mirror headers on session-required requests (copy from step 8 / logout samplers)

### 5. Assertions per new sampler

Minimum for each new GET:

- Response code **200** (or 302 if redirect chain — enable follow redirects)
- No "site unavailable" / 502 / 504 in body (reuse existing pattern from step 1)

Optional: add a lightweight body check if the response is JSON/HTML with a known marker.

### 6. Local smoke test (1 user, 1 plan)

```bash
# From performance-test-automation repo, with Taurus installed
cd performance/universal-platform/idp/jmeter
# Edit idp-login-resources-local.yaml or run with overrides:
bzt idp-login-resources-local.yaml -o modules.jmeter.variables.env=stage1 -o execution.0.concurrency=1 -o execution.0.hold-for=30s
```

**Pass criteria for smoke:**

- All 9 original steps + 6 new steps green
- Test at least **nyd** and one other plan (e.g. **njd** or **nmd**)
- Cookie/session carried through steps 8-3 through 8-6

---

## Phase 2 — Stage1 validation (current Jenkins profile)

Run with **existing** Jenkins parameters first (don't change load yet):

| Parameter | Value |
|-----------|-------|
| environment | `stage1` |
| yaml | `universal/idp/jmeter/idp-login-resources-remote.yaml` |
| concurrency | `25` |
| ramp | `5m` |
| duration | `1h` |
| throughput | `600` |
| encrypted | unchecked |

Trigger: [AGSUP_ENDURANCE_THROUGHPUT](http://jenkinsqant1:8080/view/Performance/job/AGSUP_ENDURANCE_THROUGHPUT/build?delay=0sec)

Or wait for upstream `AGSUP_IDP_REGRESSION_SUITE` to trigger it overnight.

**Check:** BlazeMeter report shows all 15 transaction labels (9 existing + 6 new) with acceptable error %.

---

## Phase 3 — Stakeholder load profile (after Phase 2 passes)

Per Arun/Mayank/Dhruv chat:

| Parameter | Target value | Notes |
|-----------|--------------|-------|
| Plans | **5 distinct** | Pick 5 from: njd, nyd, idd, iad, mdd, nmd, mod |
| Total users | **50 parallel** | ~10 per plan (stakeholder said "4 per plan" in one message — confirm with Arun) |
| Ramp | **5 minutes** | Same as current nightly |
| Duration | **5 minutes** hold (?) | Stakeholder said "within 5 minutes" — **confirm** if this means 5m total test or 5m ramp + longer hold |
| Focus | `customBannerMessage.cs` at 50 parallel | All 6 pages should still be in the script |

Suggested Jenkins overrides for this run:

```
concurrency=50
ramp=5m
duration=5m   # confirm with team
throughput=600  # may need tuning
```

Create a **separate Jenkins job** or one-off parameterized build so nightly endurance (25 users / 1h) is not disrupted.

---

## Phase 4 — Patch comparison (later)

1. **Baseline** — capture BlazeMeter report with current code (no patch)
2. **Apply patch** on stage1 (platform team)
3. **Re-run** same profile (GET + POST flows — step 8 POST session + new GETs)
4. Compare p90/p95 response times and error % for steps 8-1 through 8-6
5. Share results with Arun, Mayank, Dhruv on Teams

---

## Plans & test data

CSV column: `plan-prefix,username,password,account`

| plan-prefix | stage1 host | plan-tpl | Accounts in CSV |
|-------------|-------------|----------|-----------------|
| njd | njd.stage1.acs529.com | /njtpl | 114 |
| nyd | nyd.stage1.acs529.com | /nytpl | 216 |
| idd | idd.stage1.acs529.com | /idtpl | 108 |
| iad | iad.stage1.acs529.com | /iatpl | 72 |
| mdd | mdd.stage1.acs529.com | /mdtpl | 108 |
| nmd | nmd.stage1.acs529.com | /nmdtpl | 228 |
| mod | mod.stage1.acs529.com | /motpl | 174 |

Use **MFP-disabled** test users (same pool as current IDP login perf). Password in CSV: `Newton@123` (plaintext when `encrypted=false`).

**Ready-to-use accounts and login URLs:** [VALIDATION_TEST_USERS.md](VALIDATION_TEST_USERS.md)

## Related docs

- [DEPLOY.md](../../scripts/jia-banner-post-login/DEPLOY.md)
- [WORKFLOW.md](../workflow/WORKFLOW.md)

---

## Who to ask

| Question | Contact |
|----------|---------|
| Exact Network tab URLs / headers | Mayank (confirmed they exist on IDP login network tab) |
| Banner `.cs` endpoints | Dhruv (provided 4 auth/al/ao paths) |
| Load profile (50 users, 5 min) | Arun |
| Patch deployment timing | Platform team |

---

## Checklist

- [ ] Deploy `idp-login-resources.jmx` from `scripts/jia-banner-post-login/` to perf repo
- [ ] Browser Network tab used to verify URLs/headers for nyd (and at least 1 other plan)
- [ ] Local smoke: 1 user, 2 plans — all 15 steps green
- [ ] Jenkins stage1 run with current params — all labels in BlazeMeter
- [ ] Stakeholder run: 50 users, 5 plans — report shared
- [ ] Post-patch rerun scheduled
