# QC4 Enablement meeting summary

**Source:** `QC4 Enablement Metting Transcript.txt`  
**Attendees (known):** Kevin Daines, Abhitosh Fani, Luis Fontalvo Romero, Tandabany Anbanandan; Swapnil invited  
**Related prior call:** [QC4 IDP Setup — 2026-07-21](../programs/unite-msc/api-validation/ISSUES/07212026/QC4-IDP-Setup-Discussion-transcript.txt)

---

## Why this initiative exists

Leadership wants **QC4 to become a stable lower environment** for **shift-left testing** and the **pipeline project** (DevOps CI gates). Today:

- Active dev deploys in QC4 cause **false automation failures**
- **IDP plans** are not consistently enabled in QC4
- **Metadata** is often loaded in Stage only, not QC4
- **Mobile Unite MSC** login breaks independently of web IDP login

Kevin is reviving an **Aha feature** (originally IDP-only) to enable **broader QC4 coverage** through the **value stream**, coordinated with **Odyssey** (web/IDP login) and **Infinity** (mobile).

---

## Decisions from Kevin's meeting

| Topic | Decision |
|-------|----------|
| **Timing** | Enablement work **follows QC4 refresh** |
| **Effort** | ~**1 week** after refresh if nothing breaks; longer if cross-team fixes needed |
| **Per-plan setup** | Plans are **mostly configured** — remaining work is **reverse proxy** + **application seed data** |
| **Teams** | **Odyssey** + **Infinity** in value stream; **Abhitosh** stays involved (observer) |
| **Current blocker** | **Auth server** changes in QC4 (service worker deploy) — **login not working** at time of meeting |
| **Scope expansion** | From “IDP plans only” → **get everything enabled** where feasible |

---

## Technical enablement steps (per plan)

From Abhitosh / Cole / Tandabany (July 21 + Kevin meeting):

1. Create **IDP client** and application in auth admin
2. Add **properties** to source / deployment config
3. Update **reverse proxy** settings for the plan
4. Deploy → plan works in QC4
5. **One-time** per plan — should not need ongoing maintenance unless someone changes config or **credentials/certs expire**

---

## Known pain points (automation-specific)

| Issue | Symptom | Owner hint |
|-------|---------|------------|
| IDP not enabled for plan | Blank page, 401, redirect to wrong login | Odyssey / Tandabany — reverse proxy + client ID |
| Metadata not in QC4 | Plan reverts to **legacy** login (e.g. NY) | Odyssey — load metadata to QC4, not Stage-only |
| Mobile MSC login | Web IDP works; **mobile 401** after redirect | **Infinity** (Luis) — Unite MSC microservice |
| Expired app credential/cert | Worked until date X, then all new accounts fail | Check auth admin portal; Odyssey |
| Auth server deploy | Login down across plans | DevOps / auth team (service worker per meeting) |
| Shared QC4 DB drift | Intermittent failures, wrong plan state | Env health checks; preserve automation test data on refresh |

---

## Plans QA Automation cares about

| Plan | Branding | IDP? | Use case |
|------|----------|------|----------|
| **NMD** | `nmdirect` | Yes | Mobile2 IDP spike, perf, IDP login regression |
| **NY** | NY Direct | Was IDP; may show legacy if metadata missing | Alternate IDP test data |
| **okdirect** | Oklahoma Direct | No | Mobile2 non-IDP baseline, dashboard API tests |

Cole/Tandabany offered to create stories to enable requested plans in QC4 — **list sent in chat** (confirm exact plan list with Kevin).

---

## What Kevin is collecting (Excel)

**Data Call — QC4 Preservation:** each team lists **DB tables / data** that must be **retained or re-seeded** after QC4 refresh so their domain still works.

Your inputs are in [03-kevin-excel-inputs.md](./03-kevin-excel-inputs.md).
