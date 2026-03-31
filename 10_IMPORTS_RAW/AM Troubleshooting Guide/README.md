# AM Troubleshooting Guide (KB mirror)

This folder holds **issue-specific** troubleshooting material for QA automation (Oracle, Stage access, framework notes). Each issue lives under `issues/<issue_id>/`.

**Confluence parent page (intro + child index):** [CONFLUENCE_PARENT_AM_TROUBLESHOOTING_GUIDE.md](CONFLUENCE_PARENT_AM_TROUBLESHOOTING_GUIDE.md)

## SQL staging (PuTTY + runsqlfile.pl)

| Topic | KB path |
|--------|---------|
| Source Word doc | [guides/sql_staging_putty/source/How to update data using SQL.docx](guides/sql_staging_putty/source/How%20to%20update%20data%20using%20SQL.docx) |
| UNITED — Confluence markdown | [guides/sql_staging_putty/CONFLUENCE_PAGE_UNITED_sql_execution_staging.md](guides/sql_staging_putty/CONFLUENCE_PAGE_UNITED_sql_execution_staging.md) |
| ASTRO/SFRP — Confluence markdown | [guides/sql_staging_putty/CONFLUENCE_PAGE_ASTRO_SFRP_sql_execution_staging.md](guides/sql_staging_putty/CONFLUENCE_PAGE_ASTRO_SFRP_sql_execution_staging.md) |

## Index

| Issue ID | Title | Confluence / guide |
|----------|--------|-------------------|
| `QA_FIN_TXN_user_schema` | Stage QA financial transaction tables — offshore user schema + `$$QA_SCHEMA$$` | [CONFLUENCE_QA_FIN_TXN_user_schema_workaround.md](issues/QA_FIN_TXN_user_schema/CONFLUENCE_QA_FIN_TXN_user_schema_workaround.md) |

## Adding a new issue

1. Create `issues/<short_issue_name>/`.
2. Add evidence (errors, DDL, emails, screenshots) and a **Confluence-ready** `CONFLUENCE_*.md`.
3. Add a row to the table above.

## Note

The **Prime Java automation source** (`BaseClass.java`, etc.) is **not** in this repository; paths in each guide point to the **automation Git repo** (V2/V3) where edits are applied.
