# Confluence parent page: AM Squad work summary

This file defines the **parent Confluence page** for AM Squad documentation, how it relates to **child pages**, and where the **source markdown** lives in this repo.

---

## Parent page

| Field | Value |
|--------|--------|
| **Title** | **AM Squad Teams summary – Work Summary** |
| **Purpose** | Single landing spot for **QA Automation (AM Squad)** leadership-facing updates: **who the team is** (capabilities) and **what the team did this month** (contribution, workstreams, risks, next steps). |
| **Suggested short description** *(Confluence page excerpt / intro)* | Central hub for the **QA Automation** squad’s **monthly work summary** and **team capability profile**. Use this page to navigate to recurring reports and stable reference material for resource planning and stakeholder updates. |
| **Audience** | Engineering leadership, program management, chapter leads, and anyone needing a quick link to automation status and team skills. |
| **Owner** | QA Automation program lead *(e.g., Swapnil Patil — adjust to your Confluence owner field)* |
| **Review cadence** | **Capability profile:** update when hiring, role changes, or major skill shifts occur. **Monthly report:** new child page (or version) each reporting period (e.g., monthly). |

### Parent page body (paste-friendly starter)

Use 3–4 short paragraphs or bullets on the parent page itself:

1. **What this space is:** Aggregated **work summary** and **capability** information for the **QA Automation** squad under the AM Squad reporting structure.
2. **How to use it:** Open the **child pages** below—**Capability Profile** for skills/roles; **Monthly Report** for period activity, GitLab/Jira references, and next steps.
3. **Source of truth in repo:** Markdown and JSON under `10_IMPORTS_RAW/AMSquad Team Reports/` (see mapping table below). Confluence pages are the published copy for the wider org.

Optional: embed or link the **QA** Jira boards ([Scrum](https://ascensuscollegesavings.atlassian.net/jira/software/c/projects/QA/boards/2515), [Kanban](https://ascensuscollegesavings.atlassian.net/jira/software/c/projects/QA/boards/1292)) and [GitLab contribution analytics](https://gitlab.com/groups/ascensus-gs/products/depot/qa-automation/-/contribution_analytics?start_date=2026-02-28) from the latest monthly report.

---

## Child pages (recommended hierarchy)

Order children so **stable reference** comes first, then **time-bound** reports.

| Order | Child page title | What it contains | Source in repo |
|-------|------------------|------------------|----------------|
| 1 | **QA Automation Squad Team Capability Profile** | Per-member **experience, strengths, technical skills, current focus, capability positioning**; team coverage snapshot (UI, API, performance, pipelines). | `Team Details/team_capability_profile.md` |
| 2 | **QA Automation Team Monthly Report – 03/30/2026** | Executive summary, contribution/GitLab context, per-member updates, workstreams, risks, next steps, references. | `03302026/confluence_report.md` |

### Future child pages (same parent)

Add a **new child page per reporting month** (do not overwrite history):

| Naming pattern | Example |
|----------------|---------|
| `QA Automation Team Monthly Report – MM/DD/YYYY` | QA Automation Team Monthly Report – 04/30/2026 |

Supporting artifacts for each month can stay in a dated folder:

- `10_IMPORTS_RAW/AMSquad Team Reports/[MMDDYYYY]/`  
  - `confluence_report.md`, `teams_summary.md`, `leadership_email.md`, `monthly_report_data.json`, `prompt_reuse_notes.md`, screenshots, notes.

**Optional third child** (if you split comms):

| Title | Use |
|--------|-----|
| **QA Automation – Monthly package (Teams & email snippets)** | Short links to `teams_summary.md` and `leadership_email.md` for the latest month only, or redirect to the monthly report §appendix. Usually unnecessary if the monthly Confluence page already embeds or links them. |

---

## Visual hierarchy (matches Confluence tree)

```text
AM Squad Teams summary – Work Summary          ← PARENT
├── QA Automation Squad Team Capability Profile   ← CHILD (stable)
└── QA Automation Team Monthly Report – 03/30/2026   ← CHILD (Mar 2026)
    └── (future) QA Automation Team Monthly Report – [next date]
```

*Add future monthly reports as **siblings** under the same parent, not nested under the old month, unless you prefer a “Monthly reports” intermediate page.*

---

## Intermediate page (optional)

If the parent must cover **more than QA Automation** later (e.g., other AM Squad teams), either:

- Keep **one parent** and add child pages per squad (**QA Automation**, **other squad**, …), or  
- Add an intermediate page **“QA Automation Squad”** under the parent, then hang **Capability Profile** and **Monthly reports** under that intermediate page.

For the **current** scope (QA Automation only), **two children under the parent** is enough.

---

## Checklist when publishing

- [ ] Create parent **AM Squad Teams summary – Work Summary** in the right Confluence space.  
- [ ] Paste parent intro (section above).  
- [ ] Create child from `team_capability_profile.md` (import or copy markdown).  
- [ ] Create child from `03302026/confluence_report.md` for March 2026.  
- [ ] Attach or link **GitLab contribution screenshots** referenced in that month’s report.  
- [ ] On the **parent**, add **Children display** macro or manual links to both children.  
- [ ] Next month: add new child page from new `[MMDDYYYY]/confluence_report.md`; update parent “latest month” link if you maintain one.

---

## Folder map (repo)

```text
10_IMPORTS_RAW/AMSquad Team Reports/
├── Confluence Docs/                    ← this spec
│   └── PARENT_PAGE_AM_SQUAD_WORK_SUMMARY.md
├── Team Details/
│   └── team_capability_profile.md      ← Capability Profile (child 1)
└── 03302026/                           ← March 2026 month package
    ├── confluence_report.md            ← Monthly report (child 2)
    ├── teams_summary.md
    ├── leadership_email.md
    ├── monthly_report_data.json
    └── prompt_reuse_notes.md
```
