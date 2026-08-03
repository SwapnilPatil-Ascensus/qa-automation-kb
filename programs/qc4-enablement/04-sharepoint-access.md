# SharePoint — GSSD Automation Squad

**URL:** https://ascensus0.sharepoint.com/sites/Government_Savings-_Software_Development/SitePages/GSSD-Automation-Squad-229118272.aspx

---

## Access verification (2026-07-31)

| Check | Result |
|-------|--------|
| Automated fetch from agent environment | **Blocked** — redirects to Microsoft SSO sign-in (`Trying to sign you in`) |
| Expected for internal SharePoint | Yes — requires **your Ascensus credentials** in browser |
| Agent can browse SharePoint on your behalf | **No** — you must open the link while logged into M365 |

**Action for you:** Open the link in Edge/Chrome while signed in to Ascensus SSO. If you get **Access Denied**, request **GSSD Automation Squad** site membership from your manager or SharePoint admin.

---

## What to look for on SharePoint (once you have access)

1. **QC4 Preservation** — live copy of Kevin's Excel (may be newer than local download)
2. **Automation squad** runbooks — env config, plan lists, DB refresh notes
3. **Pipeline project** docs — QC4 stability requirements from DevOps
4. Link this repo folder: `qa-automation-kb/programs/qc4-enablement/`

---

## Suggested SharePoint doc to add (after access)

| Page | Content |
|------|---------|
| **QC4 Automation Readiness** | Link to `02-qc4-stability-checklist.md` + smoke commands |
| **Preservation inputs** | Link to `03-kevin-excel-inputs.md` |
| **Plan matrix** | NMD / NY / okdirect — IDP flag, branding, fixture paths |

If you grant the agent a **exported copy** of SharePoint pages or sync the folder locally, we can diff against `Data Call - QC4 Preservation.xlsx` for updates.
