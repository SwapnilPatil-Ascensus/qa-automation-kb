# Script Changes — Post-Login `.cs` Pages

**Status: IMPLEMENTED** in `scripts/jia-banner-post-login/idp-login-resources.jmx` (2026-08-03)

This document is the original specification. The script has been built — see [CHANGELOG.md](../../scripts/jia-banner-post-login/CHANGELOG.md).

## Background

Platform team reports performance lag in production after IDP login, suspected to involve **banner** and **redirect** requests that the current perf script does not exercise.

**Stakeholder request (Teams, Aug 2026):**

> 5 distinct plans with 50 users  
> 50 parallel customBannerMessage.cs  
> /ao/overview.cs  
> /al/list.cs  
> GET .../auth/customBannerMessage.cs  
> GET .../auth/sideBannerMessage.cs  
> GET .../al/customBannerMessage.cs ← needs logged-in session  
> GET .../ao/customBannerMessage.cs ← needs logged-in session  

Mayank confirmed: **4 from Dhruv + 2 from Mayank = 6 pages total**. `overview.cs` partial coverage via step 8 POST does **not** replace explicit GETs — add all 6.

## Pages to add

All paths use variables already in the script:

- Host: `${domain-host}` → `{plan-prefix}.{env}.acs529.com`
- Path prefix: `${plan-tpl}` → e.g. `/nytpl` for nyd, `/idtpl` for idd

| # | Sampler label | Method | Path | Logged-in session? | Source |
|---|---------------|--------|------|-------------------|--------|
| 1 | 8-1. Auth Custom Banner (CS) | GET | `${plan-tpl}/auth/customBannerMessage.cs` | No | Dhruv |
| 2 | 8-2. Auth Side Banner (CS) | GET | `${plan-tpl}/auth/sideBannerMessage.cs` | No | Dhruv |
| 3 | 8-3. AL Custom Banner (CS) | GET | `${plan-tpl}/al/customBannerMessage.cs` | **Yes** | Dhruv |
| 4 | 8-4. AO Custom Banner (CS) | GET | `${plan-tpl}/ao/customBannerMessage.cs` | **Yes** | Dhruv |
| 5 | 8-5. AO Overview (CS) | GET | `${plan-tpl}/ao/overview.cs` | **Yes** | Mayank |
| 6 | 8-6. AL List (CS) | GET | `${plan-tpl}/al/list.cs` | **Yes** | Mayank |

### Example URLs (NYD / stage1)

```
GET https://nyd.stage1.acs529.com/nytpl/auth/customBannerMessage.cs
GET https://nyd.stage1.acs529.com/nytpl/auth/sideBannerMessage.cs
GET https://nyd.stage1.acs529.com/nytpl/al/customBannerMessage.cs
GET https://nyd.stage1.acs529.com/nytpl/ao/customBannerMessage.cs
GET https://nyd.stage1.acs529.com/nytpl/ao/overview.cs
GET https://nyd.stage1.acs529.com/nytpl/al/list.cs
```

## JMeter implementation guidance

### Placement

In `idp-login-resources.jmx`, inside the **IDP Member Login** thread group:

1. After `GenericController` **8. Session/Overview (CS)** (and its child POST sampler)
2. Before `GenericController` **9. Logout (CS)**

Wrap in a new `GenericController` named e.g. **8-A. Post-Login Dashboard Pages (CS)**.

### Sampler defaults (match existing style)

```
Protocol: https
Port: 443
Domain: ${domain-host}
Method: GET
Follow redirects: true
Use keepalive: true
```

### Headers (session-required steps 3–6)

Copy header manager from step 8 or 9:

- `User-Agent`: Firefox 73
- `Accept`, `Accept-Language`, `Accept-Encoding`
- `x-sardine-session-key`: `${sardinekey}`
- Cookies: automatic via HTTP Cookie Manager

### Assertions

| Assertion | All steps |
|-----------|-----------|
| Response code 200 | Yes (adjust if redirect ends in 200) |
| Response does not contain "unavailable" | Recommended |

### Reporting

Use clear labels so BlazeMeter shows separate rows:

- `8-1. Auth Custom Banner (CS)`
- `8-2. Auth Side Banner (CS)`
- etc.

## Validation plan

| Stage | Users | Plans | Pass criteria |
|-------|-------|-------|---------------|
| Local smoke | 1 | nyd + 1 other | 0% errors on all 6 new labels |
| Jenkins (existing profile) | 25 | All in CSV | New labels appear; error % < 1% |
| Stakeholder run | 50 | 5 plans | p90/p95 captured for banner endpoints |
| Post-patch | 50 | 5 plans | Improved or stable vs baseline |

## Open items (confirm with Mayank / browser Network tab)

- [ ] Query string parameters on any of the 6 URLs?
- [ ] POST vs GET for any endpoint?
- [ ] Additional headers beyond cookies + sardine key?
- [ ] Expected response body format (JSON vs HTML) for assertion tuning?
- [ ] Exact 5 plans for the 50-user run
- [ ] Test duration: 5m total vs 5m ramp + hold?

## Files to modify

| File | Change |
|------|--------|
| `idp-login-resources.jmx` | Add 6 samplers (**primary** — Jenkins uses this) |
| `idp-login.jmx` | Add same 6 samplers (keep in sync for lighter runs) |

No YAML change required unless creating a dedicated job with different concurrency/duration.
