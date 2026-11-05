# Confluence parent page: AM Troubleshooting Guide

Use this as the **body** for the parent Confluence page that sits **above** individual troubleshooting articles. Paste into Confluence and add **child pages** (or links) for each issue guide.

---

## Suggested Confluence title

**AM Troubleshooting Guide — QA Automation**

---

## Short description (page excerpt / blurb)

Central hub for **QA Automation (AM)** troubleshooting: Oracle Stage access, framework configuration, and recurring failure patterns. Open a **child page** for step-by-step workarounds, DDL, and validation. Content is mirrored from the internal knowledge-base repo for offline editing; **Confluence is the published source** for offshore and partner teams.

---

## Page body (copy/paste)

### Purpose

This space collects **practical fixes** and **runbooks** that do not belong in day-to-day regression docs. Typical topics:

- Oracle Stage **schema privileges** and **QA-only tables**
- **Staging SQL execution** via **PuTTY** and **`runsqlfile.pl`** (UNITED and ASTRO/SFRP) when SQL Developer is not the approved path
- **Prime V2 / V3** automation settings (e.g. `BaseClass`, placeholders, JVM args)
- **Evidence** (sample errors, ticket templates, DBA emails) attached to each issue

### How to use this page

1. Find your topic in **Child pages** below (or in the page tree).
2. Follow the linked guide end-to-end: **root cause → workaround → code/DB steps → validation**.
3. If something is missing, ask the **AM automation lead** to add a new child page and KB folder under `issues/<issue_id>/`.

### Child pages (living documents)

| Child page title | What it covers |
|------------------|----------------|
| **UNITED — SQL execution in staging environments** | PuTTY + `runsqlfile.pl` for Stage 1 / 2 / 4 (`backoff`, `uii0qa@uiis01/02/04`); file location, formatting, `--commit`. |
| **ASTRO / SFRP — SQL execution in staging environments** | PuTTY + `astrojob` + `runsqlfile.pl`; **SEQ_CHANGE_ID** via `GENERATE_CHANGE_ID`; CA/IL user examples. |
| **Stage QA financial transaction tables — user schema workaround (`$$QA_SCHEMA$$`)** | Offshore users without shared-schema INSERT on `UII0`/UIC: create `QA_FIN_TXN` / `QA_FIN_INSTRUCTION` in **your** schema; update `performQueryReplacements` + `-Dqa.oracle.schema`; DDL and validation. |

*Add a new row and a new Confluence child page each time a new `issues/<issue_id>/` folder is created in the KB.*

**Source Word doc (SQL runbook):** KB `guides/sql_staging_putty/source/How to update data using SQL.docx`

### Ownership & updates

| Item | Detail |
|------|--------|
| **Owner** | QA Automation program lead *(name in Confluence)* |
| **KB mirror** | Repo path: `10_IMPORTS_RAW/AM Troubleshooting Guide/` |
| **When to update** | After a repeatable incident, DBA/process change, or framework change that affects offshore |

### Related (optional links on Confluence)

- Prime automation GitLab project(s) — V2/V3  
- Jira QA boards  
- AGS / access request process (if applicable)

---

## Confluence page tree (recommended)

```text
AM Troubleshooting Guide — QA Automation          ← THIS PARENT PAGE
├── UNITED — SQL execution in staging environments
├── ASTRO / SFRP — SQL execution in staging environments
├── Stage QA financial transaction tables — user schema workaround ($$QA_SCHEMA$$)
└── (future) <next issue title>
```

---

## For editors (repo)

- Parent write-up source: `CONFLUENCE_PARENT_AM_TROUBLESHOOTING_GUIDE.md`  
- Index of issues: `README.md`  
- SQL staging runbook: `guides/sql_staging_putty/` (Confluence pages + `source/How to update data using SQL.docx`)  
- Per-issue content: `issues/<issue_id>/CONFLUENCE_*.md` and attachments

After adding an issue in Git, **sync this parent page** (child table + page tree) so Confluence matches the KB.
