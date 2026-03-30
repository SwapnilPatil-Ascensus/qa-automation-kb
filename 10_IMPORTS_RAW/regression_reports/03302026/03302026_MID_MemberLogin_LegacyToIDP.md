# Bug Documentation: MID Member Login – Legacy URL / CSR (IDP transition impact)

**Naming:** `03302026_MID_MemberLogin_LegacyToIDP.md`  
**Location:** `10_IMPORTS_RAW/regression_reports/03302026/`  
**JIRA:** [JIRA-KEY – create ticket](https://ascensuscollegesavings.atlassian.net/browse/) · **Status:** Open

---

## Context/Background

V2 Stage 1 web login regression (**03/30/2026**) failed for **MID** during member login coverage. The **legacy member login URL** for MID returns **Page not found**, and **CSR** for MID no longer shows the **Update Password** link. Other plans in the same run behave as expected, so symptoms are **MID-specific**.

**Working hypothesis (for triage):** Legacy member login is being **retired or redirected** in favor of **IDP login** for some or all plans. If MID has already moved to IDP, **automation URLs, test data, and manual TCs** that still assume **legacy member login** will fail until suites are **repointed to IDP** and **MID** is either **removed from legacy-login suites** or **replaced with plans that still have legacy member login enabled**. **Brian Danilczyk** is being asked to confirm **which team owns plan-by-plan conversion** so the right **QA org** can **add/remove/update test cases** as part of **IDP enablement**.

---

## Issue Summary

| Item | Detail |
|------|--------|
| **Observed** | MID legacy login page **not found**; MID CSR **Update Password** link **missing**. |
| **Scope** | **MID only** in current regression; other plans OK. |
| **Automation** | Example: `T101_LoginPositive.feature` (MID) – see TestNG report and exception links below. |
| **Desired automation direction** | **Remove or replace MID** with plans that still have **legacy member login** enabled for V2 legacy-login suites; **move MID-related scenarios** to **IDP login** coverage where IDP is the supported path. |
| **Coordination** | Identify **owning team** for MID / IDP conversion (via Brian); that team’s **QA** should **track TC changes** for IDP enablement. |

---

## Steps to Reproduce (Env: Stage 1)

1. Open Stage 1 **CSR / member** flow for **MID** plan.
2. Navigate to legacy MID login URL: `https://mid.stage1.acs529.com/midtpl/auth/ll.cs`
3. **Observe:** Page responds with **Page not found** (or equivalent).
4. Log in to **CSR** for MID and review available links.
5. **Observe:** **Update Password** link is **not** displayed for MID.

---

## Error Message

**UI / page:** MID legacy login URL – **Page not found** (exact text per browser/report).

**Automation artifacts (hosted):**
- **TestNG report:** http://seleniumhubnt2:8081/reports/unite/20260330/stage1-web-login/#
- **Failed result HTML:** http://seleniumhubnt2:8081/reports/unite/20260330/stage1-web-login/mid.20260330012703369.T101_LoginPositive.feature.45_html_chrome_failedresult.html
- **Exception:** http://seleniumhubnt2:8081/reports/unite/20260330/stage1-web-login/mid.20260330012703394.T101_LoginPositive.feature.45_exception_failedresult.txt

*Paste exact exception text from the `.txt` link into JIRA if needed after download.*

---

## JIRA Bug (Copy-Paste Ready)

### Summary

MID Stage 1 – legacy member login URL returns Page not found; CSR Update Password link missing; V2 regression / IDP transition alignment (03/30/2026)

### Description

**Overview**  
During **V2 Stage 1** web login regression on **03/30/2026**, **MID**-specific failures were observed: the **legacy member login URL** (`https://mid.stage1.acs529.com/midtpl/auth/ll.cs`) returns **Page not found**, and in **CSR** for MID the **Update Password** link is **not visible**. **Other plans** in the same run **work as expected**, indicating **MID-specific** behavior or configuration.

**Hypothesis for triage**  
Legacy member login may be **deprecated or replaced by IDP** for MID. If so, **defect vs. expected cutover** must be confirmed with **product/platform owners**. **QA Automation** may need to **stop using MID in legacy-login suites** (replace with plans still on legacy member login) and **cover MID under IDP login** suites instead.

**Environment**  
- **Environment:** Stage 1  
- **Plan:** MID  
- **Suite context:** V2 regression – web login (e.g. `stage1-web-login`)

**Observed behavior**
- Legacy MID login URL: **Page not found**.
- CSR (MID): **Update Password** link **absent**.

**Expected behavior (if legacy still supported)**  
Legacy MID login page loads; CSR shows **Update Password** for MID consistent with other legacy-enabled plans.

**Expected behavior (if IDP is intended)**  
Document **supported entry points**; **automation and manual TCs** updated to **IDP**; legacy URLs removed from active regression or marked obsolete.

### Steps to Reproduce

1. Navigate to `https://mid.stage1.acs529.com/midtpl/auth/ll.cs` on Stage 1.
2. Observe page not found (or equivalent).
3. Access CSR for MID and confirm Update Password link presence/absence.

### Priority / Severity (suggested)

- **Priority:** High – Blocks MID login/password-related regression and may block sign-off for MID until scope is clarified.
- **Severity:** Major if legacy is still required; **Process/TC** if behavior is **intentional IDP cutover** pending suite/TC updates.

### Attachments / Links

- **TestNG report:** http://seleniumhubnt2:8081/reports/unite/20260330/stage1-web-login/#
- **Screenshot / HTML failure:** http://seleniumhubnt2:8081/reports/unite/20260330/stage1-web-login/mid.20260330012703369.T101_LoginPositive.feature.45_html_chrome_failedresult.html
- **Exception file:** http://seleniumhubnt2:8081/reports/unite/20260330/stage1-web-login/mid.20260330012703394.T101_LoginPositive.feature.45_exception_failedresult.txt
- **Local folder:** `10_IMPORTS_RAW/regression_reports/03302026/` (`Test Case Info.txt`)

### Test Data (key values)

- **Account Number:** A28826590  
- **Scenario reference:** `T101_LoginPositive.feature` (MID)

### Labels / Tags (suggested)

`mid`, `member-login`, `legacy-login`, `idp`, `regression`, `stage1`, `prime-v2`, `csr`, `web-login`

### Components (suggested)

- Member / Participant Login  
- IDP / Authentication (if cutover confirmed)  
- CSR (MID)  
- QA Automation – suite / test data alignment

---

## JIRA Bug

**[JIRA-KEY]** · *[Link after creation]*  
*Reference this link in all communications until the ticket is closed.*

---

## Questions or Concerns

- **Brian Danilczyk:** Which team **owns MID (and other) legacy → IDP conversions**? Who should **QA** coordinate with for **adding/removing TCs** during IDP enablement?
- **Product / platform:** Is MID **intentionally** off legacy member login on Stage 1? If yes, what is the **authoritative IDP URL** and **CSR** behavior for password management?

Contact: QA Automation Team

---

## Artifacts & Links

**Local (this folder):**
- `Test Case Info.txt`

**Hosted:**
- Report, screenshot HTML, and exception URLs listed in **Error Message** and **JIRA** sections above.

---

## Email Draft (Bug Handling Template)

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>  
*Note: If Brian Danilczyk is out of office, Valerie Gallegos will coordinate follow-up actions.*

**Subject:** Daily Regression Failed – MID Member Login (Legacy URL / CSR) & IDP Transition Alignment | Stage 1

---

Hi Team,

We hit failures in the latest **V2 Stage 1 web login** regression (**03/30/2026**) for **MID** only.

**Bug Summary:**
- **Symptoms:** Legacy MID member login URL **`https://mid.stage1.acs529.com/midtpl/auth/ll.cs`** returns **Page not found**. In **CSR** for MID, the **Update Password** link is **not shown**. Other plans in the same run are OK.
- **Working hypothesis:** **Legacy member login** may be **moving to IDP**; **V2 URLs and cases** that still use **member legacy login** will fail until **suites and TCs** are updated. Proposed direction: **remove or replace MID** with plans that still have **legacy member login** enabled for legacy-login suites, and **move MID coverage** to **IDP login** where applicable.
- **Coordination ask:** Please confirm via **Brian** (or reply-all) **which team owns plan conversions** so the correct **QA** can **add/remove TCs** as part of **IDP enablement**.
- **JIRA Bug:** [JIRA-KEY – link after creation]
- **TestNG report:** http://seleniumhubnt2:8081/reports/unite/20260330/stage1-web-login/#
- **Failure HTML:** http://seleniumhubnt2:8081/reports/unite/20260330/stage1-web-login/mid.20260330012703369.T101_LoginPositive.feature.45_html_chrome_failedresult.html
- **Exception:** http://seleniumhubnt2:8081/reports/unite/20260330/stage1-web-login/mid.20260330012703394.T101_LoginPositive.feature.45_exception_failedresult.txt
- **Test data:** Account **A28826590** · `T101_LoginPositive.feature` (MID)
- **Artifacts folder:** `10_IMPORTS_RAW/regression_reports/03302026/`
- **Environment:** Stage 1
- **Priority:** High

**Change Set Summary:**  
*(Add MR table here – GitLab for date range through 03/30/2026.)*

**CI/CD Control Policy:**  
Per team policy: main branch / pipeline expectations as applicable. Please confirm if this is **expected IDP cutover** vs. **defect**, and who owns **MID** remediation or **automation/TC realignment**.

Thanks,  
QA Automation Team

---

## Teams Message (channel – full team)

**MID – V2 login regression fail (03/30/2026) – legacy URL / CSR**

Hi Team,

**V2 Stage 1 web login** failed for **MID** only: legacy member URL **`https://mid.stage1.acs529.com/midtpl/auth/ll.cs`** → **Page not found**; **CSR** for MID → **Update Password** link missing. Other plans OK.

We suspect **legacy → IDP** transition: **automation** may need **MID pulled from legacy-login suites** (use plans still on legacy) and **MID cases moved to IDP**. **Need owning team** for conversions so **QA** can update **TCs** for IDP enablement.

**Links:** JIRA [JIRA-KEY] · Report http://seleniumhubnt2:8081/reports/unite/20260330/stage1-web-login/# · HTML http://seleniumhubnt2:8081/reports/unite/20260330/stage1-web-login/mid.20260330012703369.T101_LoginPositive.feature.45_html_chrome_failedresult.html

**Env:** Stage 1 | **Priority:** High

Please confirm **defect vs. expected cutover** and point us to **IDP entry** for MID if applicable.

Thanks,  
QA Automation Team

---

## Resolution Email Draft (Bug Resolution Follow-Up Template)

**To:** AGS Tech Leads, AGS Chapter Leads, AGS Development, Brian Danilczyk  
**Cc:** Rajib Akhter <Rajib.Akhter@ascensus.com>; Henry Dittmer <Henry.Dittmer@ascensus.com>; Phuong Huynh <Phuong.Huynh@ascensus.com>; Automation.Squad <Automation.Squad@ascensus.com>  
*Note: If Brian Danilczyk is out of office, Valerie Gallegos will coordinate follow-up actions.*

**Subject:** Resolved – Daily Regression [Passed / Updated] | MID Member Login (Legacy / IDP alignment) | Stage 1

---

Hello All,

The issue tracked as **[JIRA-KEY]** regarding **MID member login / CSR** on **Stage 1** (reported **03/30/2026**) has been **addressed** as follows:

**Original Bug Summary:**
- **Bug:** [JIRA-KEY – link]
- **Failure area:** Legacy MID login URL; MID CSR Update Password visibility; V2 regression
- **Environment:** Stage 1
- **Reported on:** 03/30/2026

**Resolution Summary:**
- **Root cause:** *[e.g. Intentional IDP cutover / misconfiguration / defect – fill in after triage]*
- **Fix / alignment:** *[e.g. Legacy URL restored / IDP documented / automation suites updated / MID swapped to IDP suite – fill in]*
- **Verified via:** *[Jenkins / manual / automation rerun – specify]*
- **TC / QA ownership:** *[Team name – per Brian / leadership confirmation]*
- **Note:** *[Branch / main unlock / suite changes – as applicable]*

Thank you for the support in triaging and closing this out.

Best regards,  
Automation QA Team

---

## Resolution & RCA (for JIRA – fill when closed)

| Field | Detail |
|--------|--------|
| **Root cause** | *[TBD]* |
| **Fix** | *[TBD]* |
| **Automation follow-up** | *[e.g. MID removed from legacy suite; IDP suite owns MID; test data updated]* |
| **Resolved by** | *[Names / teams]* |

---

## Teams message – Brian only (short ping)

*Copy/paste for a direct ping to Brian when you need immediate routing on ownership.*

Brian – **V2 Stage 1** failed **MID** member login today: legacy URL **`https://mid.stage1.acs529.com/midtpl/auth/ll.cs`** is **Page not found** and **CSR** has no **Update Password** for MID; other plans are fine. We’re treating this as likely **legacy → IDP** cutover. **Who owns plan conversions** (MID / others) so we know **which QA team** should **add/remove TCs** for IDP enablement, and whether we should **drop MID from legacy-login suites** and **move MID to IDP**? Need a quick pointer. Thanks.

---

**Reported By:** QA Automation Team  
**Date:** 03/30/2026  
**Environment:** Stage 1
