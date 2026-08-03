# Draft reply to Kevin Daines

**Subject:** QC4 Preservation — QA Automation inputs

---

Hi Kevin,

Thanks for including me on the QC4 enablement discussion. Here are **QA Automation inputs** for the **Data Call — QC4 Preservation** spreadsheet and the broader enablement work.

**Data to preserve after QC4 refresh (automation-critical):**

- **IDP:** `client.Application`, `client.Credential`, `client.Secret`, `person.profile`, `person.credentials` — without these, IDP login fails for our target plans (NMD and others).
- **Login / session:** `TA_LOGIN*`, `TA_SESSION*`, `TA_COOKIE`, `TA_APP_CONTEXT`, and `TAPI_PARTNER_AUTH*` / `TAPI_ENTITLEMENT*` — needed for login and API partner auth flows.
- **Test accounts:** Known automation members/accounts in `TU_ACCT`, `TU_MEMBER`, `TU_FUND_BALANCE` (NMD, okdirect, NY, CSR users) — we need repeatable data, not random refresh snapshots.
- **Enrollment:** Stored proc packages `UP_ENROLLMENT*.pkb` / `UP_ACCOUNT_529_V2.pkb` (same as Enrollments row in the sheet).

**Enablement beyond preservation (for stable automation):**

Preserving data is necessary but not sufficient. Post-refresh we still need **Odyssey** to re-apply **reverse proxy + IDP client/properties + plan metadata in QC4** for **NMD**, **NY**, and **okdirect**, and **Infinity** for **mobile MSC login** (we've seen web IDP work while mobile returns 401). Auth server stability after refresh is also a gate — login was down during the service worker deploy mentioned on the call.

**Priority plans for automation:** NMD (`nmdirect`, IDP), okdirect (non-IDP Mobile2 baseline), NY (IDP when metadata is loaded).

**Timing:** Aligns with your **~1 week post-refresh** estimate; we can run an automation smoke (IDP web + Mobile2 dashboard + one IDP mobile path) to sign off QC4 for pipelines.

I've documented details in our KB: `programs/qc4-enablement/` (checklist + Excel row-level inputs). Happy to walk through on a quick call or add rows directly to the Excel if you send the live SharePoint link.

Thanks,  
Swapnil
