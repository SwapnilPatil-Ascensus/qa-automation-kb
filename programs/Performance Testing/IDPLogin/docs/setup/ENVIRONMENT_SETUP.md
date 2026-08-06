# Environment Setup — IDP Login Performance Test

## Prerequisites

| Tool | Version / notes |
|------|-----------------|
| JMeter | 5.6.x (repo references 5.6.3) |
| Java | 8+ (match JMeter requirement) |
| Taurus | Optional — for CLI/BlazeMeter runs |
| Git access | `performance-test-automation` repo |
| Network | VPN + access to `*.stage1.acs529.com` |

## Repositories

| Repo | Path |
|------|------|
| Performance tests (GitLab) | `C:\Workspace\GitLab\Automation\performance-test-automation` |
| JMeter scripts | `performance/universal-platform/idp/jmeter/` |
| This KB package | `qa-automation-kb/programs/Performance Testing/IDPLogin/` |

## Local JMeter GUI setup

1. Install JMeter 5.6.3
2. Copy from this KB package to a working folder:
   - `scripts/jia-banner-post-login/idp-login-resources.jmx`
3. Copy from perf repo (same directory as JMX):
   - `idp-login-stage1.csv`
   - `authentication/` folder (required by `decryption.jmx` include)
4. Open `idp-login-resources.jmx` in JMeter
5. Enable **Environment Variables - Local (Stage 1)** OR set user-defined variables:
   - `env` = `stage1`
   - `encryption` = `false`
6. Thread group: 1 thread, 1 loop
7. Run → View Results Tree

### Domain resolution

Script builds host as `{plan-prefix}.stage1.acs529.com` from CSV. No hosts file changes needed if DNS resolves internally.

## Local Taurus setup

```bash
cd "scripts/jia-banner-post-login"
# Ensure idp-login-stage1.csv + authentication/ are in this folder or jmeter path
bzt idp-login-resources-local.yaml
```

## Jenkins setup (no changes required)

| Item | Value |
|------|-------|
| Job URL | http://jenkinsqant1:8080/view/Performance/job/AGSUP_ENDURANCE_THROUGHPUT/ |
| Agent | loadtestwt2 |
| Config path on agent | `/home/devops/agsup-endurance` |
| YAML | `universal/idp/jmeter/idp-login-resources-remote.yaml` |
| Docker image | `blazemeter/taurus:withplugins:latest` |

### Deploy updated JMX to Jenkins

1. Push JMX to `performance-test-automation` GitLab
2. Confirm how `agsup-endurance` syncs (git pull / CI deploy — ask DevOps)
3. Trigger manual build with parameters from [JENKINS_AND_BLAZEMETER.md](../reference/JENKINS_AND_BLAZEMETER.md)

## BlazeMeter

- Project: **AGS Automation Regression**
- Tests upload automatically when Jenkins runs Taurus with `blazemeter` reporting module
- Token configured on Jenkins agent (not in this KB)

## Test users

See [VALIDATION_TEST_USERS.md](../guides/VALIDATION_TEST_USERS.md)

## Troubleshooting

| Issue | Check |
|-------|-------|
| `decryption.jmx` not found | Copy `authentication/` folder next to JMX |
| CSV not found | `idp-login-${env}.csv` must match `env` variable |
| 401/403 on al/ao banners | Session cookie — confirm step 8 POST succeeded first |
| MFA blocking login | Use MFP-disabled `QAPERFTEST_*` users |
| Site unavailable | stage1 env issue — retry or check with platform |

## Proxy

Jenkins uses `http://webproxywt-vip.int.acs529.com:3128`. Local runs may need proxy settings in JMeter or Taurus if off VPN.
