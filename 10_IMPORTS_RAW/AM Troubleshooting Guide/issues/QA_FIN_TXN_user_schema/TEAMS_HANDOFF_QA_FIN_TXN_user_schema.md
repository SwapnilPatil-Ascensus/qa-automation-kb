# Teams handoff — QA_FIN_TXN / user schema workaround

Copy the block below into Teams.

---

**QA automation — Stage transaction tests & shared schema (offshore)**

We documented the workaround for **UII0 / shared-schema** INSERT issues on transaction flows (`QA_FIN_TXN`, `QA_FIN_INSTRUCTION`, `ORA-01400` / privilege errors).

**Please use this as the single reference:**  
https://confluence.ascensus.com/pages/viewpage.action?pageId=378705164

**What you need to do**

1. Run the **DDL** in **your** Oracle Stage user (fix **synonym owner** in the script — not someone else’s schema).
2. After the framework change lands: set **`-Dqa.oracle.schema=<YOUR_ORACLE_USER>`** on local/CI runs (your Stage username, e.g. uppercase).
3. **`BaseClass.performQueryReplacements`** — V2 and V3 paths are listed in the Confluence page; keep in sync with `main`/shared branch when you pull.

**KB mirror (DDL + sample errors):** repo `10_IMPORTS_RAW/AM Troubleshooting Guide/issues/QA_FIN_TXN_user_schema/`

Ping me if SQL Developer blocks script runs — use **UNITED** PuTTY + `runsqlfile.pl` steps: Confluence parent → **UNITED — SQL execution in staging** (KB: `guides/sql_staging_putty/`).

Thanks.

---
