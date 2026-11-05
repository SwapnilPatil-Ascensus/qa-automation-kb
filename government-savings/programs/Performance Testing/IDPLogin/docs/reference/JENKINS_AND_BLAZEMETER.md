# Jenkins & BlazeMeter Reference

## Jenkins

### Primary job

| | |
|---|---|
| **Name** | `AGSUP_ENDURANCE_THROUGHPUT` |
| **URL** | http://jenkinsqant1:8080/view/Performance/job/AGSUP_ENDURANCE_THROUGHPUT/ |
| **Latest referenced build** | [#597](http://jenkinsqant1:8080/view/Performance/job/AGSUP_ENDURANCE_THROUGHPUT/597/parameters/) |
| **Upstream trigger** | `AGSUP_IDP_REGRESSION_SUITE` (#677 in captured log) |
| **Schedule** | Timer (nightly, via upstream) |

### Parameters

| Parameter | Default | Maps to Taurus |
|-----------|---------|----------------|
| server | loadtestwt2 | Jenkins agent label |
| yaml | universal/idp/jmeter/idp-login-resources-remote.yaml | Taurus execution config |
| environment | stage1 | `jenv` → CSV suffix + domain |
| encrypted | false | `jencryption` |
| concurrency | 25 | `jmconcurrency` |
| duration | 1h | `jmhold` |
| ramp | 5m | `jmramp` |
| throughput | 600 | `jmthroughput` |

### Execution stack

```
Jenkins (loadtestwt2)
  └── Docker: blazemeter/taurus:withplugins:latest
        ├── setup/base_taurus.yaml
        ├── setup/stage1.properties  (env-specific hosts/secrets)
        └── universal/idp/jmeter/idp-login-resources-remote.yaml
              └── idp-login-resources.jmx
```

### Proxy

Taurus uses corporate proxy: `http://webproxywt-vip.int.acs529.com:3128`

### Build result note

Build #597 finished Jenkins **SUCCESS** even with ~0.44% errors — the pipeline uses `catchError` so BlazeMeter/Taurus exit code 0 does not fail the job. Review BlazeMeter for actual error rates.

## BlazeMeter

### Project structure

```
AGS Automation Regression
  └── IDP Test - Member Login (CS/API w/ Resources)
        └── Reports (24+ historical runs)
```

### Report naming

| Taurus field | Value |
|--------------|-------|
| report-name | IDP Test - Member Login |
| test | IDP Test - Member Login (CS/API w/ Resources) |
| project | AGS Automation Regression |

### Sample report (build #597 / master 82884601)

| Metric | Value |
|--------|-------|
| Duration | ~1h 5m |
| Max VUs | 25 |
| Avg throughput | 54.32 hits/s |
| Avg response time | 331 ms |
| 90th percentile | 944 ms |
| Error rate | 0.44% |
| Total samples | 211,514 |

### Public link (from log)

https://a.blazemeter.com/app/?public-token=iXVpLSTUX2U7VfFIxtuJ4czSBvGmGqK3HwqlpI7026fHggIs80#/masters/82884601/summary

## Recommended new Jenkins job (banner investigation)

Do **not** change the nightly endurance job parameters. Create a sibling job e.g. `AGSUP_IDP_BANNER_PERF` with:

| Parameter | Suggested value |
|-----------|-----------------|
| yaml | same `idp-login-resources-remote.yaml` (after script update) |
| environment | stage1 |
| concurrency | 50 |
| ramp | 5m |
| duration | 5m (confirm with stakeholders) |
| throughput | 600 (tune down if errors spike) |

## MCP / API access

| Tool | Status |
|------|--------|
| Jenkins MCP | **Not available** in Cursor |
| Jenkins HTTP | Reachable (`jenkinsqant1:8080` → 200) — read-only without API token |
| BlazeMeter API | Not configured in this workspace |

To automate job creation, need Jenkins API token + credential store on the agent.

## Screenshots in this folder

- `Jenkins job details 1.png` — parameters for build #598
- `Jenkins job details 2.png` — same (duplicate capture)
- `Perf regression - IDP Login test overview.png` — BlazeMeter history (25 users per run)
- `blazemeter report 1.png` — summary dashboard
- `blazemeter report 2.png` — transaction table (9 steps today)
