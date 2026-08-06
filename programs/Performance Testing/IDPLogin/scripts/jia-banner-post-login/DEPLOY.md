# Deploy — JMeter Script to performance-test-automation

## Steps for Preeti

### 1. Back up current script

```text
performance/universal-platform/idp/jmeter/idp-login-resources.jmx
→ idp-login-resources.jmx.bak
```

### 2. Copy new script

Copy from this KB folder:

```text
qa-automation-kb/programs/Performance Testing/IDPLogin/scripts/jia-banner-post-login/idp-login-resources.jmx
```

To GitLab repo:

```text
performance-test-automation/performance/universal-platform/idp/jmeter/idp-login-resources.jmx
```

### 3. (Optional) Update YAML test name

If you want BlazeMeter to show the new test description, update `idp-login-resources-remote.yaml`:

```yaml
test: IDP Test - Member Login (CS/API w/ Resources + Post-Login Pages)
```

Or copy from this folder's `idp-login-resources-remote.yaml`.

### 4. Commit & push

```bash
git add performance/universal-platform/idp/jmeter/idp-login-resources.jmx
git commit -m "feat(idp-perf): add post-login banner and dashboard .cs pages"
git push
```

### 5. Jenkins deploy

The Jenkins job `AGSUP_ENDURANCE_THROUGHPUT` pulls from `/home/devops/agsup-endurance` on `loadtestwt2`. Confirm with DevOps how that directory syncs from GitLab — may need a pull/deploy on the agent before running.

### 6. Smoke test before full run

| Step | Action |
|------|--------|
| Local | JMeter GUI, 1 user, nyd account — all 15 labels green |
| Jenkins | Run `AGSUP_ENDURANCE_THROUGHPUT` with concurrency=1, duration=5m (manual params) |
| Full | Restore normal params (25 users, 1h) or stakeholder profile (50 users, 5 plans) |

## Files you do NOT need to change

- `idp-login-stage1.csv`
- `idp-login.jmx` (lighter script — update separately only if still used)
- `authentication/decryption.jmx`
- Jenkins `base_taurus.yaml`, `stage1.properties`

## Rollback

Restore `idp-login-resources.jmx.bak` and redeploy to Jenkins agent.
