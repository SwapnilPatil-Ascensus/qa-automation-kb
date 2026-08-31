# JMeter Script — Post-Login Banner Pages (Jia investigation)

Updated `idp-login-resources.jmx` with **6 GET requests** after session/overview creation and before logout.

## Files in this folder

| File | Purpose |
|------|---------|
| `idp-login-resources.jmx` | **Modified JMeter script** — hand to Preeti |
| `idp-login-resources-remote.yaml` | Taurus config for Jenkins/BlazeMeter (optional test name update) |
| `idp-login-resources-local.yaml` | 1-user local smoke test |
| `DEPLOY.md` | How to install into `performance-test-automation` repo |
| `CHANGELOG.md` | What changed vs baseline script |
| `_build_jmx.py` | Regenerator (re-run if upstream JMX changes) |

## What was added

New controller: **8-A. Post-Login Dashboard Pages (CS)** with 6 GET samplers:

| Label | Path |
|-------|------|
| 8-A-1. Auth Custom Banner (CS) | `${plan-tpl}/auth/customBannerMessage.cs` |
| 8-A-2. Auth Side Banner (CS) | `${plan-tpl}/auth/sideBannerMessage.cs` |
| 8-A-3. AL Custom Banner (CS) | `${plan-tpl}/al/customBannerMessage.cs` |
| 8-A-4. AO Custom Banner (CS) | `${plan-tpl}/ao/customBannerMessage.cs` |
| 8-A-5. AO Overview (CS) | `${plan-tpl}/ao/overview.cs` |
| 8-A-6. AL List (CS) | `${plan-tpl}/al/list.cs` |

Inserted **before** `9. Logout (CS)`. All other steps unchanged.

## YAML changes required?

| File | Change needed? |
|------|----------------|
| `idp-login-resources-remote.yaml` | **Optional** — only if you want updated BlazeMeter test name. Script path stays `idp-login-resources.jmx`. |
| `idp-login-stage1.csv` | **No** — same test data |
| `stage1.properties` (Jenkins) | **No** |
| `base_taurus.yaml` (Jenkins) | **No** |
| `authentication/decryption.jmx` | **No** |

**Minimum deploy:** replace `idp-login-resources.jmx` in the GitLab repo. YAML is optional.

## Quick local test

1. Copy this folder's `idp-login-resources.jmx` next to your JMeter install or into the perf repo `jmeter/` folder.
2. Copy `idp-login-stage1.csv` from `performance-test-automation/.../jmeter/` into the same directory.
3. Copy `authentication/` folder (for decryption.jmx) — required by include controller.
4. Open in JMeter GUI → run 1 thread, 1 loop with `env=stage1`.
5. Or: `bzt idp-login-resources-local.yaml` from this folder.

## Source

Built from: `C:\Workspace\GitLab\Automation\performance-test-automation\performance\universal-platform\idp\jmeter\idp-login-resources.jmx`

Regenerate: `python _build_jmx.py`
