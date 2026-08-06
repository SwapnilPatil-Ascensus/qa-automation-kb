# Baseline Results — Build #597 (Aug 3, 2026)

Source: `BlazeMeter report extract.csv` and Jenkins log for `AGSUP_ENDURANCE_THROUGHPUT` build triggered by `AGSUP_IDP_REGRESSION_SUITE` #677.

## Run configuration

| Parameter | Value |
|-----------|-------|
| Environment | stage1 |
| Concurrency | 25 VUs |
| Ramp | 5 minutes |
| Duration | 1 hour |
| Throughput cap | 600 req/min |
| Script | idp-login-resources.jmx |
| BlazeMeter master | [82884601](https://a.blazemeter.com/app/#/masters/82884601) |

## Overall

| Metric | Value |
|--------|-------|
| Total samples | 211,514 |
| Avg response time | 331 ms |
| Avg hits/s | 54.32 |
| 90th percentile | 944 ms |
| 95th percentile | 1,419 ms |
| 99th percentile | 2,354 ms |
| Max response time | 300,032 ms (5 min timeout) |
| Error % | 0.44% |
| Avg bandwidth | 935.43 KB/s |

## Per-transaction breakdown

| # | Transaction | Samples | Avg RT (ms) | 90% line (ms) | 95% line (ms) | Error % |
|---|-------------|---------|-------------|---------------|---------------|---------|
| 1 | LoginLanding (CS) | 23,617 | 53 | 64 | 201 | 0.00% |
| 2 | Authorize (IDP) | 23,617 | 18 | 21 | 23 | 0.00% |
| 3 | Login (IDP) - GET Login | 23,616 | 20 | 24 | 27 | 0.03% |
| 4 | Login (IDP) - POST Login | 23,606 | 324 | 369 | 400 | 0.01% |
| 5 | Login (IDP) - GET Authorize Continue | 23,603 | 36 | 48 | 55 | 0.02% |
| 6 | Callback/Token (CS) - Get Callback | 23,598 | 90 | 193 | 269 | 0.00% |
| 7 | Callback/Token (IDP) - Get Access Token | 23,596 | 249 | 276 | 294 | 0.03% |
| 8 | **Session/Overview (CS)** | 23,588 | **1,653** | **2,236** | **2,696** | **3.83%** |
| 9 | Logout (CS) | 22,673 | 542 | 797 | 936 | 0.02% |

## Key observations

### Step 8 is the bottleneck

- **Highest avg response time:** 1,653 ms (5× the overall average)
- **Highest error rate:** 3.83% — errors include `Bad Gateway`, `Precondition Failed`, connection failures to `nyd.stage1.acs529.com`
- **99th percentile:** 8,768 ms on overview step

This aligns with stakeholder reports of lag after login. Adding banner `.cs` GETs after this step will show whether those endpoints add further latency.

### Sample funnel (drop-off)

| Step | Samples | Drop from previous |
|------|---------|-------------------|
| 1. LoginLanding | 23,617 | — |
| 8. Session/Overview | 23,588 | -29 |
| 9. Logout | 22,673 | -915 |

Most drop-off happens between overview and logout — failures/timeouts on step 8 prevent logout.

### Errors in final summary (from Jenkins log tail)

Common errors across steps during this run:

- `Non HTTP response message: nyd.stage1.acs529.com:443 failed to respond`
- `Bad Gateway`
- `Precondition Failed`

Suggests intermittent stage1 / load-related issues during the 1h soak — not necessarily script bugs.

## Use as baseline

When the 6 new pages are added:

1. Re-run with **same** Jenkins params (25 users, 1h) for apples-to-apples
2. Compare new transaction rows (8-1 through 8-6) against step 8 overview
3. For stakeholder sign-off, run **50 users / 5 plans / 5 min** profile separately
4. After platform patch, re-run both profiles and compare p90/p95

## Visual references

- `blazemeter report 1.png` — summary graphs (25 VU steady state)
- `blazemeter report 2.png` — transaction table showing 9 steps
- `Perf regression - IDP Login test overview.png` — historical runs (all 25 users)
