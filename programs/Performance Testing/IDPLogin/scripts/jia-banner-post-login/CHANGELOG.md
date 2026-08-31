# Changelog — idp-login-resources.jmx

## 2026-08-03 — Post-login banner pages (Jia investigation)

### Added

- Controller `8-A. Post-Login Dashboard Pages (CS)` after step 8 Session/Overview, before logout
- 6 GET samplers:
  - `8-A-1. Auth Custom Banner (CS)` → `${plan-tpl}/auth/customBannerMessage.cs`
  - `8-A-2. Auth Side Banner (CS)` → `${plan-tpl}/auth/sideBannerMessage.cs`
  - `8-A-3. AL Custom Banner (CS)` → `${plan-tpl}/al/customBannerMessage.cs`
  - `8-A-4. AO Custom Banner (CS)` → `${plan-tpl}/ao/customBannerMessage.cs`
  - `8-A-5. AO Overview (CS)` → `${plan-tpl}/ao/overview.cs`
  - `8-A-6. AL List (CS)` → `${plan-tpl}/al/list.cs`

### Per-sampler config

- Method: GET
- Domain: `${domain-host}`
- Follow redirects: true
- Headers: same as logout (User-Agent, Accept, x-sardine-session-key)
- Assertions: HTTP 200, response does not contain "unavailable"
- Cookie session: inherited from HTTP Cookie Manager after step 8 POST

### Unchanged

- Steps 1–8 (login flow, OAuth PKCE, session POST)
- Step 9 Logout
- CSV data source, domain setup, decryption, throughput timer

### BlazeMeter impact

Report will show **15 transaction labels** (was 9) when static login JS sub-samplers are excluded from summary.

### Source commit base

Generated from local `performance-test-automation` copy dated 2026-08-03.
