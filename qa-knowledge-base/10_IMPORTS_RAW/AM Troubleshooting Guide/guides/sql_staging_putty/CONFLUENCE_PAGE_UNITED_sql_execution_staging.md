# UNITED — SQL execution in staging environments

**Source:** Internal document *How to update data using SQL.docx* (mirror: `guides/sql_staging_putty/source/How to update data using SQL.docx`).  
**Audience:** QA engineers (including offshore) running approved SQL on **UNITED** staging.

---

## 1. Overview

The source document describes running SQL on the **staging feed server** using **PuTTY** and **`runsqlfile.pl`** with a **`backoff`** service user.

**Why SQL Developer is not part of this procedure**

- The source document **does not** explain corporate policy.
- It **only** documents execution via **PuTTY** on the server and **`runsqlfile.pl`**. Treat that as the **approved operational path** for the changes it covers unless your lead specifies otherwise.

**Environments covered in the source document (UNITED)**

- **Stage 1** — `uii0qa@uiis01`
- **Stage 2** — `uii0qa@uiis02`
- **Stage 4** — `uii0qa@uiis04`

---

## 2. Prerequisites

- PuTTY (or equivalent) access to the **correct staging server** for Stage 1, 2, or 4 (obtain hostname / jump host from your team; **not** in the source document).
- Permission to run the **`sudo -u backoff ...`** command (if you cannot sudo, escalate to your lead).
- Your SQL file placed in the **Linux home path** your team uses. The source example uses **`/home/swpatil`** — replace with **your** assigned home directory if different.

---

## 3. Step-by-step (simple path)

### 3.1 Log in with PuTTY

1. Open **PuTTY**.
2. Connect to the **staging server** for the target stage (**Stage 1, 2, or 4**), per infrastructure instructions from your team.

*(The source document does not list hostnames or bastion steps.)*

### 3.2 Where to create / place the SQL file

Per the source document:

- Put your SQL file under the home folder — example given: **`/home/swpatil`** on the **Stage 1** server (use the same pattern for your user if your path differs).

### 3.3 File naming and content

The source document shows the **`runsqlfile.pl`** invocation with this path as the last argument:

```text
/home/swpatil/sql
```

So in the example, the file to execute is named **`sql`** (no `.sql` extension in the example path). **Clarification:** If your team standard is `something.sql`, confirm the **exact path** you pass to `runsqlfile.pl` with your lead. **Do not guess** a different name without confirmation.

### 3.4 Formatting rules (from the source document)

1. **New line after each SQL statement** — the source states: *"New line needed after each sql"*.
2. **Blank line at the end of the file** — the source states: *"then one line space at the end"*.
3. **Semicolons** — the source examples use **`;`** at the end of SQL statements (e.g. after `from dual;`). Terminate each statement with **`;`** consistent with those examples.

### 3.5 Commands — execute SQL (UNITED)

Run the command for the **stage you are targeting** (from the source document).

**Stage 1**

```bash
sudo -u backoff /stagefeeds/qa/bin/runsqlfile.pl --user=uii0qa@uiis01 --commit /home/swpatil/sql
```

**Stage 2**

```bash
sudo -u backoff /stagefeeds/qa/bin/runsqlfile.pl --user=uii0qa@uiis02 --commit /home/swpatil/sql
```

**Stage 4**

```bash
sudo -u backoff /stagefeeds/qa/bin/runsqlfile.pl --user=uii0qa@uiis04 --commit /home/swpatil/sql
```

**Notes**

- Replace **`/home/swpatil/sql`** with your **actual file path** if your home directory or filename differs.
- **`--commit`** is shown in the source document on every example line — keep it unless your lead instructs otherwise.

---

## 4. Example SQL file layout (illustrative)

The source document does not include a full UNITED sample file. Structure yours to satisfy its rules: one statement per block with newlines, **`;`** terminators, blank line at end.

```sql
-- Example shape only — replace with approved DBA/lead-provided SQL

UPDATE your_schema.your_table
SET your_column = 'Y'
WHERE id = 123;

```

*(Blank line after last line, as required.)*

---

## 5. Troubleshooting (UNITED)

| Symptom / topic | What to check |
|-----------------|---------------|
| **Missing semicolon** | Ensure each SQL statement ends with **`;`** as in the source examples. |
| **Missing blank line at end of file** | Add **one** blank line after the last statement (source: *"one line space at the end"*). |
| **Missing `--commit`** | Source examples always include **`--commit`**. If omitted, behavior may not match the documented path — align with your lead. |
| **Wrong user / schema** | Verify the **`--user=uii0qa@uiis0x`** segment matches **Stage 1 (`uiis01`)**, **Stage 2 (`uiis02`)**, or **Stage 4 (`uiis04`)** per the tables above. |
| **Wrong path to SQL file** | Confirm the file exists at the path passed as the last argument (example **`/home/swpatil/sql`**). |
| **Permission errors / ORA-***** | Capture full output from `runsqlfile.pl` and escalate with your lead / DBA; the source document does not list ORA codes or fixes. |
| **Cannot `sudo -u backoff`** | Access / sudoers issue — not documented; escalate to infrastructure / lead. |

---

## 6. Gaps explicitly not in the source document

- Hostnames, VPN, or jump-server steps for PuTTY.
- Whether the SQL file **must** be named `sql` or may be `*.sql`.
- Validation / rollback procedures after the script runs.

---

*Generated from KB mirror of **How to update data using SQL.docx**; update this page when the Word source changes.*
