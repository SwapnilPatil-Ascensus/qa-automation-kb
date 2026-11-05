# Inputs for Kevin — Data Call QC4 Preservation (QA Automation)

**Requester:** Kevin Daines  
**Contributor:** Swapnil Patil — QA Automation / Government Savings  
**Spreadsheet:** `Data Call - QC4 Preservation.xlsx`

---

## What Kevin is asking

After **QC4 refresh**, which **database objects and seed data** must be **preserved or re-applied** so each domain still works? Your job is not to own every `TU_*` metadata table — focus on what **breaks automation** if missing.

You already added **rows 3–5** (IDP + TA tables). Below expands those and adds **rationale** Kevin can paste into the Excel.

---

## Rows already in Excel (your comments — keep / refine)

| Row | AGS Domain | Table / object | Suggested refinement for Comments column |
|-----|------------|----------------|------------------------------------------|
| 3 | Contributions, Employer | `TA_*` | **Retain TA_LOGIN, TA_SESSION, TA_COOKIE, TAPI_* tables** — required for login/session and partner API auth used by automation and enrollment flows. Full TA_* reference data should be preserved or re-seeded post-refresh. |
| 4 | Contributions, Employer | IDP Auth Server tables | **Preserve IDP auth server data**: clients, APIs, credentials, applications. Without this, **IDP login fails for all IDP-enabled plans** in QC4 (NMD, etc.). |
| 5 | Contributions, Employer | `person.credentials`, `person.profile`, `client.*` | **Refresh/sync with Unite tables** after restore. Automation test users and OAuth clients must match QC4 plan config. |

---

## Additional rows to add (QA Automation)

Copy into new rows under **AGS Domain: `QA Automation`** or extend **IDP** / **Contributions, Employer** as appropriate.

| AGS Domain | Schema | Table / object | Filter / notes | Rationale |
|------------|--------|----------------|----------------|-----------|
| QA Automation | IDP | `client.Application`, `client.Credential`, `client.Secret` | Plans: **NMD**, **NY** (if IDP), automation OAuth clients | IDP token and redirect flows for web + mobile automation |
| QA Automation | IDP | `person.profile`, `person.credentials` | Automation test member UII IDs (NMD, okdirect, CSR users) | Login breaks if profiles wiped on refresh |
| QA Automation | Unite | `TA_LOGIN`, `TA_SESSION`, `TA_LOGIN_PASSWORD`, `TA_COOKIE` | Rows tied to known automation users | Session persistence for legacy and hybrid flows |
| QA Automation | Unite | `TAPI_PARTNER_AUTH`, `TAPI_ENTITLEMENT`, `TAPI_PARTNER_ENTITLEMENT_REL` (+ `_H` hist if needed) | Partner keys used by API tests | API gateway auth for enrollment/partner flows |
| QA Automation | Unite | `TU_ACCT`, `TU_MEMBER`, `TU_FUND_BALANCE` | Known automation accounts per plan (NMD, okdirect, NY); `enroll_status = 'A'`, `total_units > 0` where needed | Repeatable regression — withdrawals, dashboard, enrollment |
| QA Automation | Unite | `TU_TRAUNCH`, `TU_TRAUNCH_METADATA`, `TU_TRAUNCH_FUND` | Traunch IDs for **100089** (per UXE row) + automation plan traunches | Plan routing; missing metadata → legacy login fallback |
| QA Automation | Unite | Stored procedures (not tables) | `UP_ENROLLMENT.pkb`, `UP_ENROLLMENT_S1_1.pkb`, `UP_ACCOUNT_529_V2.pkb` | Align with Enrollments row — advisor enrollment API tested from QC4 |

**Do not duplicate** rows 11–136 (PHUONG metadata list) unless Kevin asks — those are **reference tables**; comment **“Support automation if preserved; QA does not own.”** if you must respond on them.

---

## Enablement items (NOT in Excel — tell Kevin separately)

Preservation alone does not fix QC4. These are **configuration** tasks post-refresh:

| Item | Owner | Notes |
|------|-------|-------|
| Reverse proxy per automation plan | Odyssey / Tandabany | ~1 week post-refresh |
| IDP client ID + properties deploy | Odyssey | Per NMD, NY, etc. |
| Load plan **metadata to QC4** | Odyssey | NY went legacy when metadata skipped |
| Mobile MSC login microservice | Infinity | 401 after IDP redirect |
| Auth server stability | Platform/DevOps | Service worker deploy broke login (Kevin meeting) |
| MFA off for automation users | Plan config | Unattended CI |

---

## One-paragraph summary for Kevin (email / Teams)

> **QA Automation** depends on QC4 for pipeline gates, Mobile2 API tests, IDP login regression, and enrollment API work. After refresh we need **IDP auth tables** (`client.*`, `person.credentials/profile`), **login/session tables** (`TA_LOGIN*`, `TA_SESSION*`, `TAPI_PARTNER_AUTH*`), and **known test accounts** (`TU_ACCT`/`TU_MEMBER`/`TU_FUND_BALANCE`) preserved or re-seeded. Data alone is not sufficient — **Odyssey** must re-enable **reverse proxy + client ID + metadata** for plans **NMD**, **NY**, and **okdirect**, and **Infinity** must keep **mobile MSC login** healthy. Suggest **~1 week** post-refresh for automation smoke (IDP web + mobile + Mobile2 dashboard) before calling QC4 stable for our pipelines.

---

## Priority order (if Kevin must phase work)

1. **Auth server up** + IDP tables preserved  
2. **NMD** IDP web login smoke  
3. **okdirect** non-IDP mobile2 dashboard  
4. **NMD** mobile IDP login  
5. Enrollment API test accounts + `UP_ENROLLMENT*` packages  
6. Broader metadata tables (PHUONG list) — lower priority for automation smoke  
