# Current IDP Login Performance Test — Overview

## What this test does

End-to-end **IDP (OAuth PKCE) member login** on Universal Platform plans:

1. Hits the plan's login landing page (ColdFusion `.cs`)
2. Completes OAuth authorization code flow with the IDP
3. Creates a logged-in session (POST `createSessionIDP.cs`)
4. Validates account overview content
5. Logs out

The **resources** variant (`idp-login-resources.jmx`) also loads static JS assets during the IDP login page (polyfills, banner.js, sardine-sdk.js, etc.) to better simulate real browser load. **Jenkins uses this variant.**

## Jenkins job

| Field | Value |
|-------|-------|
| Job name | `AGSUP_ENDURANCE_THROUGHPUT` |
| View | [Performance](http://jenkinsqant1:8080/view/Performance/) |
| URL | http://jenkinsqant1:8080/view/Performance/job/AGSUP_ENDURANCE_THROUGHPUT/ |
| Trigger | Upstream `AGSUP_IDP_REGRESSION_SUITE` (timer-driven, nightly) |
| Agent | `loadtestwt2` |
| Working dir | `/home/devops/agsup-endurance` |
| Runner | Docker `blazemeter/taurus:withplugins:latest` |

### Default parameters (build #598)

| Parameter | Value | Description |
|-----------|-------|-------------|
| server | `loadtestwt2` | Execution server |
| yaml | `universal/idp/jmeter/idp-login-resources-remote.yaml` | Taurus config |
| environment | `stage1` | Target env (`jenv` → CSV `idp-login-stage1.csv`) |
| encrypted | `false` | CSV passwords are plaintext |
| concurrency | `25` | Parallel virtual users |
| duration | `1h` | Hold time after ramp |
| ramp | `5m` | Ramp-up to full concurrency |
| throughput | `600` | Max requests/minute (Constant Throughput Timer) |

### Docker command (from log)

```bash
docker run --rm --privileged \
  -e jmconcurrency=25 -e jmhold=1h -e jmramp=5m -e jmthroughput=600 -e jencryption=false \
  -v /home/devops/agsup-endurance:/bzt-configs \
  --env-file setup/stage1.properties \
  blazemeter/taurus:withplugins:latest \
  setup/base_taurus.yaml universal/idp/jmeter/idp-login-resources-remote.yaml
```

## BlazeMeter

| Field | Value |
|-------|-------|
| Project | AGS Automation Regression |
| Test name | IDP Test - Member Login (CS/API w/ Resources) |
| Latest master ID (from log) | [82884601](https://a.blazemeter.com/app/#/masters/82884601) |
| Public report | https://a.blazemeter.com/app/?public-token=iXVpLSTUX2U7VfFIxtuJ4czSBvGmGqK3HwqlpI7026fHggIs80#/masters/82884601/summary |

## Two JMeter scripts

| Script | YAML | Used by | Difference |
|--------|------|---------|------------|
| `idp-login.jmx` | `idp-login-remote.yaml` | Manual / lighter runs | Core login flow only |
| `idp-login-resources.jmx` | `idp-login-resources-remote.yaml` | **Jenkins nightly** | Adds ~30 static JS GETs on login page |

## Authentication model

- **OAuth 2.0 Authorization Code + PKCE** (S256 challenge)
- **Sardine** session key generated per iteration (`x-sardine-session-key`)
- **MFA steps** exist in script (4-2, 4-3: request-pin / verify-pin) — test users should be **MFP-disabled** so MFA does not block
- Credentials from CSV → decrypted if `encryption=true` (Jenkins sets `false`)
- Per-plan host: `${plan-prefix}.${env}.acs529.com` (e.g. `nyd.stage1.acs529.com`)

## What's missing in production Jenkins (gap driving this work)

The script deployed to Jenkins today goes straight from step **8. Session/Overview** to **logout** without hitting banner/dashboard `.cs` pages.

**Updated script available** in this KB: `scripts/jia-banner-post-login/idp-login-resources.jmx` — adds 6 GET requests. Pending deploy by Preeti.

## Related functional regression

Functional IDP login tests exist in the automation regression suite (`IDPLogin.feature`) — separate from this perf test but share the same auth flow and test user pools.
