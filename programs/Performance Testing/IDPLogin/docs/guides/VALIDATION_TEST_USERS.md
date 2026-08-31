# Validation Test Users — IDP Login (stage1)

Sample accounts from `idp-login-stage1.csv` for **manual login validation** and **Network tab** capture before updating the JMeter script.

**Source file:** `C:\Workspace\GitLab\Automation\performance-test-automation\performance\universal-platform\idp\jmeter\idp-login-stage1.csv`

---

## Common login details

| Field | Value |
|-------|-------|
| Environment | `stage1` |
| Password (all users below) | `Newton@123` |
| Login URL pattern | `https://{plan}.stage1.acs529.com/{plan-tpl}/authentications/loginLandingIDP.cs` |
| User requirement | MFP-disabled (these `QAPERFTEST_*` accounts are in the perf CSV pool) |
| Jenkins `encrypted` param | `false` (passwords stored plaintext in CSV) |

---

## plan-tpl mapping

| plan-prefix | Host | plan-tpl |
|-------------|------|----------|
| nyd | nyd.stage1.acs529.com | `/nytpl` |
| njd | njd.stage1.acs529.com | `/njtpl` |
| nmd | nmd.stage1.acs529.com | `/nmdtpl` |
| idd | idd.stage1.acs529.com | `/idtpl` |
| iad | iad.stage1.acs529.com | `/iatpl` |
| mdd | mdd.stage1.acs529.com | `/mdtpl` |
| mod | mod.stage1.acs529.com | `/motpl` |

**Rule (from JMeter Domain Setup):** Plans `mod`, `iad`, and `idd` use the first 2 characters + `tpl` (e.g. `mod` → `/motpl`). All others use the full prefix + `tpl` (e.g. `nyd` → `/nytpl`).

---

## Recommended users by plan

### NYD (start here — stakeholder examples used nytpl)

| Username | Password | Account # | Login URL |
|----------|----------|-----------|-----------|
| `QAPERFTEST_119527095` | `Newton@123` | 343400368 | https://nyd.stage1.acs529.com/nytpl/authentications/loginLandingIDP.cs |
| `QAPERFTEST_119602220` | `Newton@123` | 343408360 | https://nyd.stage1.acs529.com/nytpl/authentications/loginLandingIDP.cs |

**Post-login pages to verify in Network tab:**

```
GET https://nyd.stage1.acs529.com/nytpl/auth/customBannerMessage.cs
GET https://nyd.stage1.acs529.com/nytpl/auth/sideBannerMessage.cs
GET https://nyd.stage1.acs529.com/nytpl/al/customBannerMessage.cs    ← needs session
GET https://nyd.stage1.acs529.com/nytpl/ao/customBannerMessage.cs    ← needs session
GET https://nyd.stage1.acs529.com/nytpl/ao/overview.cs
GET https://nyd.stage1.acs529.com/nytpl/al/list.cs
```

---

### NJD

| Username | Password | Account # | Login URL |
|----------|----------|-----------|-----------|
| `QAPERFTEST_103562251` | `Newton@123` | B16809316 | https://njd.stage1.acs529.com/njtpl/authentications/loginLandingIDP.cs |
| `QAPERFTEST_109092799` | `Newton@123` | B19680309 | https://njd.stage1.acs529.com/njtpl/authentications/loginLandingIDP.cs |

---

### NMD

| Username | Password | Account # | Login URL |
|----------|----------|-----------|-----------|
| `QAPERFTEST_164536845` | `Newton@123` | 965776296 | https://nmd.stage1.acs529.com/nmdtpl/authentications/loginLandingIDP.cs |
| `QAPERFTEST_173720700` | `Newton@123` | 962937227 | https://nmd.stage1.acs529.com/nmdtpl/authentications/loginLandingIDP.cs |

---

### IDD

| Username | Password | Account # | Login URL |
|----------|----------|-----------|-----------|
| `QAPERFTEST_120813614` | `Newton@123` | 587684564 | https://idd.stage1.acs529.com/idtpl/authentications/loginLandingIDP.cs |
| `QAPERFTEST_146012109` | `Newton@123` | 584793153 | https://idd.stage1.acs529.com/idtpl/authentications/loginLandingIDP.cs |

---

### IAD

| Username | Password | Account # | Login URL |
|----------|----------|-----------|-----------|
| `QAPERFTEST_138203550` | `Newton@123` | 450245387 | https://iad.stage1.acs529.com/iatpl/authentications/loginLandingIDP.cs |
| `QAPERFTEST_282424756` | `Newton@123` | 450245393 | https://iad.stage1.acs529.com/iatpl/authentications/loginLandingIDP.cs |

---

### MDD

| Username | Password | Account # | Login URL |
|----------|----------|-----------|-----------|
| `QAPERFTEST_156571725` | `Newton@123` | A63914663 | https://mdd.stage1.acs529.com/mdtpl/authentications/loginLandingIDP.cs |
| `QAPERFTEST_256732898` | `Newton@123` | A61203751 | https://mdd.stage1.acs529.com/mdtpl/authentications/loginLandingIDP.cs |

---

### MOD

| Username | Password | Account # | Login URL |
|----------|----------|-----------|-----------|
| `QAPERFTEST_181778840` | `Newton@123` | 547634761 | https://mod.stage1.acs529.com/motpl/authentications/loginLandingIDP.cs |
| `QAPERFTEST_204981287` | `Newton@123` | 545962878 | https://mod.stage1.acs529.com/motpl/authentications/loginLandingIDP.cs |

---

## Quick validation steps

1. Open the **NYD** login URL in Chrome or Firefox.
2. Log in with `QAPERFTEST_119527095` / `Newton@123`.
3. Open **DevTools → Network** and confirm all **6 `.cs` pages** fire after the dashboard loads.
4. Note exact URLs, query params, request headers (cookies, `x-sardine-session-key`), and expected response codes.
5. Repeat with **one other plan** (e.g. NJD or NMD) to confirm `${plan-tpl}` paths differ per plan.
6. After login, the overview should show account **343400368** for the NYD user above.

---

## Suggested 50-user / 5-plan split (perf run)

| Plan | Available accounts in CSV | Suggested users for load test |
|------|---------------------------|-------------------------------|
| nyd | 216 | 10 |
| nmd | 228 | 10 |
| njd | 114 | 10 |
| idd | 108 | 10 |
| mod | 174 | 10 |

**Total: 50 users.** Confirm final plan selection with Arun before the stakeholder run.

---

## Related docs

- [PRITI_QUICK_START.md](../guides/PRITI_QUICK_START.md) — script update and run phases
- [TEST_DATA.md](TEST_DATA.md) — full CSV schema and account counts
- [SCRIPT_CHANGES_REQUIRED.md](SCRIPT_CHANGES_REQUIRED.md) — spec (implemented)
