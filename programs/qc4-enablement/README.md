# QC4 Enablement — QA Automation context hub

**Owner:** Swapnil Patil (QA Automation)  
**Stakeholder:** Kevin Daines (value stream / QC4 preservation initiative)  
**Last updated:** 2026-07-31

## Purpose

Kevin is driving **QC4 stabilization and enablement** after the next **QC4 refresh**. Teams are filling in the **Data Call — QC4 Preservation** Excel with data/tables that must survive refresh. QA Automation must contribute inputs so **API/UI automation can run reliably in QC4** — not only IDP plans.

## Local artifacts

| File | Description |
|------|-------------|
| [QC4 Enablement Metting Transcript.txt](./QC4%20Enablement%20Metting%20Transcript.txt) | Kevin + Abhitosh + Luis + Tandabany — reverse proxy, ~1 week post-refresh, Odyssey/Infinity |
| [Data Call - QC4 Preservation.xlsx](./Data%20Call%20-%20QC4%20Preservation.xlsx) | Kevin's spreadsheet — preservation data call |
| [01-meeting-summary.md](./01-meeting-summary.md) | Meeting decisions and owners |
| [02-qc4-stability-checklist.md](./02-qc4-stability-checklist.md) | Full QA Automation stability checklist (beyond IDP) |
| [03-kevin-excel-inputs.md](./03-kevin-excel-inputs.md) | **Copy-paste rows and comments for Kevin's Excel** |
| [04-sharepoint-access.md](./04-sharepoint-access.md) | SharePoint link + access status |
| [05-reply-to-kevin-draft.md](./05-reply-to-kevin-draft.md) | Short email reply draft |

## Related prior discussions

| Source | Topic |
|--------|--------|
| [QC4-IDP-Setup-Discussion-transcript.txt](../programs/unite-msc/api-validation/ISSUES/07212026/QC4-IDP-Setup-Discussion-transcript.txt) | IDP plans, NMD/NY, mobile MSC 401, metadata gap |
| RT [514351](https://rt.acs529.com/Ticket/Display.html?id=514351) | QC4 mobile login ECONNRESET (resolved) |
| RT [511448](https://rt.acs529.com/Ticket/Display.html?id=511448) | Stage 1 refresh — env vs defect pattern |

## Quick answer — what Kevin needs from you

1. **Excel:** Confirm preservation rows for **IDP auth tables**, **TA_LOGIN/SESSION**, **TAPI partner auth**, and **automation test accounts** — see [03-kevin-excel-inputs.md](./03-kevin-excel-inputs.md).  
2. **Enablement (not just data):** IDP plans need **reverse proxy + client ID + properties + metadata in QC4** — Odyssey (web) + Infinity (mobile).  
3. **Priority plans for automation:** **NMD (`nmdirect`)**, **NY** (IDP or legacy per metadata), **okdirect** (non-IDP mobile2 baseline).  
4. **Timeline:** Work follows **QC4 refresh**; ~**1 week** enablement if no cross-team breakage (per Kevin meeting).
