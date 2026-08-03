# ASTRO / SFRP — SQL execution in staging environments

**Source:** Internal document *How to update data using SQL.docx* (mirror: `guides/sql_staging_putty/source/How to update data using SQL.docx`).  
**Audience:** QA engineers (including offshore) running approved SQL on **ASTRO / SFRP** staging.

---

## 1. Overview

The source document describes **SFRP DB Update** using:

- A **`.SQL`** file you create.
- **`sudo -u astrojob`** with **`/astrofeedstage/qa/bin/runsqlfile.pl`**.
- Different **`--user`** values for different database connections (examples below).

**Why SQL Developer is not part of this procedure**

- The source document **does not** state a policy reason.
- It documents execution via **PuTTY** on the server and **`runsqlfile.pl`** only. Use that path unless your lead directs otherwise.

**Stage 1 / Stage 2 / Stage 4 mapping**

- The source document **does not** map ASTRO commands to Stage 1, 2, or 4 by name. It only shows **`asts02wtrw`** in the `--user` strings below. **Do not assume** stage numbers without confirmation from your lead.

---

## 2. Prerequisites

- PuTTY (or equivalent) access to the **ASTRO / SFRP feed staging** server (hostname **not** in the source document).
- Permission to run **`sudo -u astrojob ...`**.
- Understanding that **updates require a `SEQ_CHANGE_ID`** generated as described in §4.

---

## 3. Step-by-step (simple path)

### 3.1 Log in with PuTTY

1. Open **PuTTY**.
2. Connect to the server your team provides for **SFRP / ASTRO** staging execution.

*(Host/jump steps are not in the source document.)*

### 3.2 Where to save SQL files

The source document states: **Save all these files to Home folder** (your Linux home directory on that server).

### 3.3 File naming

The source document says: **Create .SQL file** and shows examples such as **`testsql7.sql`**, **`testca.sql`**, **`testil.sql`**.

### 3.4 Formatting rules (from the source document)

1. **New line after each SQL** — same note as UNITED: *"New line needed after each sql"* applies to how you structure statements in the file.
2. **Blank line at end** — follow the UNITED instruction in the same source file: *"one line space at the end"*.
3. **Semicolons** — examples use **`;`** after statements (e.g. `from dual;`, end of `UPDATE`).

---

## 4. Mandatory `SEQ_CHANGE_ID` (ASTRO / SFRP)

The source document states that **before updating anything** you need a **`SEQ_CHANGE_ID`**, obtained with:

```sql
select AST0CENTRAL.ASTRO_CENTRAL_UTILS.GENERATE_CHANGE_ID('Pkachhia_EE_Update3_OR') from dual;
```

**Important**

- **`'Pkachhia_EE_Update3_OR'`** is an **example** label from the source document. **Clarification:** The source does not define naming rules for this string. Confirm the **tag / label** format with your lead before using in production scripts.

Run the **`SELECT ... GENERATE_CHANGE_ID ...`** to obtain the new ID, then use that numeric value in your **`UPDATE`** (see example below).

### 4.1 Example `UPDATE` using `SEQ_CHANGE_ID` (from the source document)

The source document shows this pattern (note: **`413473003`** is the **example** ID from their sample — **you must replace** with the value returned from **`GENERATE_CHANGE_ID`** for your run):

```sql
UPDATE AST0CA.TS_ATC_TAX_1099R
SET CTL_REC_STAT = 'X', SEQ_CHANGE_ID = 413473003
WHERE PAYMENT_YEAR = 2024 AND CTL_REC_STAT = 'A';
```

**Not stated in the source document:** whether `UPDATE`, `SELECT`, and `GENERATE_CHANGE_ID` must live in the **same** `.sql` file or separate files. Align with your lead.

---

## 5. Commands — `runsqlfile.pl` (ASTRO / SFRP)

Examples **verbatim** from the source document (filenames and users):

```bash
sudo -u astrojob /astrofeedstage/qa/bin/runsqlfile.pl --user astqa0ca@asts02wtrw testsql7.sql --commit
```

The source also lists (as separate lines — **confirm with your lead** whether these are alternate examples or a required sequence):

```sql
select AST0CENTRAL.ASTRO_CENTRAL_UTILS.GENERATE_CHANGE_ID('Pkachhia_EE_Update3_OR') from dual;
```

```bash
sudo -u astrojob /astrofeedstage/qa/bin/runsqlfile.pl --user astqa0ca@asts02wtrw testca.sql --commit
```

```bash
sudo -u astrojob /astrofeedstage/qa/bin/runsqlfile.pl --user astqa0il@asts02wtrw testil.sql --commit
```

**Observations from the source (not explained further there)**

- **`--user`** uses a **space** before the connect string (`--user astqa0ca@asts02wtrw`), unlike the UNITED examples which use **`--user=...`**.
- Two different users appear: **`astqa0ca@asts02wtrw`** and **`astqa0il@asts02wtrw`** — use the one that matches the schema/database you are changing.

---

## 6. Troubleshooting (ASTRO / SFRP)

| Symptom / topic | What to check |
|-----------------|---------------|
| **Missing semicolon** | End each SQL statement with **`;`** per the examples. |
| **Missing blank line at end of file** | Add a final blank line (same source note as UNITED). |
| **Missing `--commit`** | Source examples include **`--commit`**. |
| **Missing / wrong `SEQ_CHANGE_ID`** | Run **`GENERATE_CHANGE_ID`** first; use the **returned** value in `UPDATE`, not a copied sample ID. |
| **Wrong `--user` / schema** | Match **`astqa0ca@asts02wtrw`** vs **`astqa0il@asts02wtrw`** to the correct database for your change. |
| **Permission or ORA errors** | Capture full `runsqlfile.pl` output; source document does not list fixes — escalate. |
| **Cannot `sudo -u astrojob`** | Escalate to infrastructure / lead. |

---

## 7. Gaps explicitly not in the source document

- Which **PuTTY host** to use for ASTRO/SFRP staging.
- How **Stage 1 / 2 / 4** map to **`asts02wtrw`** (if at all).
- Official naming convention for the string passed to **`GENERATE_CHANGE_ID`**.

---

*Generated from KB mirror of **How to update data using SQL.docx**; update this page when the Word source changes.*
