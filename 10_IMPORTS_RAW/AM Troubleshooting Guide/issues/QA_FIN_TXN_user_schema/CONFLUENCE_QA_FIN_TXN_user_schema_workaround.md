# Stage QA financial transaction tables — offshore user schema workaround (`$$QA_SCHEMA$$`)

**Audience:** Offshore QA automation engineers (Oracle Stage 1)  
**Applies to:** Prime **V2** and **V3** Java test automation using `$$QA_SCHEMA$$` for `QA_FIN_TXN` / `QA_FIN_INSTRUCTION` (and related patterns)  
**KB issue folder:** `10_IMPORTS_RAW/AM Troubleshooting Guide/issues/QA_FIN_TXN_user_schema/`  
**Automation code (not in this KB repo):** Edits are made in the **Prime automation** Git repository at the paths below.

---

## 1. Overview

Transaction-related tests insert and read **QA-only** financial tables. In Stage, those SQL statements are often built with a **schema prefix** (historically shared schemas such as **UII0** / **UIC**). Many offshore accounts **do not have INSERT/UPDATE** on that shared schema, so tests fail with Oracle permission errors or inconsistent behavior. **DBA access cannot be assumed** to expand shared-schema privileges for every user.

**Approved workaround:** Create **`QA_FIN_TXN`** and **`QA_FIN_INSTRUCTION`** in **your own Oracle user schema**, then configure automation so `$$QA_SCHEMA$$` expands to **`YOUR_USER.`** (not `UII0.`) on Stage.

**Reference DDL:** Pramod’s “Team Tables” email and the maintained script in this issue folder: `Create QA_FIN_TXN tables DDL.sql`.

---

## 2. Root cause

### 2.1 Why inserts fail against the shared schema

1. **Privilege gap:** Offshore users may have general Stage access but **not** `INSERT`/`UPDATE` on objects in **UII0** (or equivalent shared QA schema).
2. **Wrong object target:** SQL generated as `INSERT INTO UII0.QA_FIN_INSTRUCTION ...` runs as **your** session; without privileges, Oracle returns **`ORA-01031: insufficient privileges`** (or similar).
3. **Trigger / sequence mismatch:** If tables exist in the shared schema but **triggers or sequences** differ from the Pramod DDL, you can see **`ORA-01400: cannot insert NULL`** into `SEQ_QA_FIN_TXN_ID` or related columns when the **BEFORE INSERT** trigger does not populate keys as expected (see sample errors in this folder).

### 2.2 How schema resolution works in automation

- SQL text in the framework uses the placeholder **`$$QA_SCHEMA$$`** where a schema prefix is required on Stage.
- In **`BaseClass.performQueryReplacements`** (near the end of the method), that placeholder is replaced before the statement runs.
- **Current behavior (before fix):** On Stage, `$$QA_SCHEMA$$` is replaced with a **fixed** shared schema prefix (e.g. **`UII0.`**), so all users hit the same shared objects.

**Files to update (Prime automation repo — same logic, two locations):**

| Stream | File path |
|--------|-----------|
| **V2** | `prime/source/com/cs529/qa/prime/core/BaseClass.java` |
| **V3** | `prime/prime-core/src/main/java/core/test/BaseClass.java` |

> **Note:** This knowledge base does not contain `BaseClass.java`. Confirm the exact snippet in your branch; replace only the `$$QA_SCHEMA$$` block as shown in §5.

---

## 3. Workaround steps (offshore engineer checklist)

### Step 1 — Obtain your Oracle Stage username

Use the same user you use in **SQL Developer** (or PuTTY/sqlplus) for Stage 1. Example shape: `SPATIAL_SPAGHETTI` (uppercase is typical in Oracle metadata).

### Step 2 — Prepare the DDL script

1. Open `Create QA_FIN_TXN tables DDL.sql` (in this issue folder).
2. **Edit the `PUBLIC SYNONYM` lines** so they point to **your** schema, not another user’s. The checked-in sample references **`SPATIL`** — replace with **your** username, e.g.:

```sql
CREATE OR REPLACE PUBLIC SYNONYM QA_FIN_TXN FOR YOUR_USER.QA_FIN_TXN;
CREATE OR REPLACE PUBLIC SYNONYM QA_FIN_INSTRUCTION FOR YOUR_USER.QA_FIN_INSTRUCTION;
```

3. Run the script **connected as `YOUR_USER`** so `CREATE TABLE` creates objects in **your** schema.

> **Important:** If your organization restricts **public synonyms** or **`GRANT ... TO PUBLIC`**, coordinate with DBA; the intent remains: **objects live in your schema** and your session can `INSERT`/`SELECT`/`UPDATE` them.

### Step 3 — Execute the DDL on Stage 1

1. Connect to **Stage 1** as **your** user.
2. Run the full script in **SQL Developer** (Worksheet → Run Script), or use **sqlplus** / PuTTY if SQL Developer blocks multi-statement scripts.

**If SQL Developer will not run the script:** Use the **UNITED** staging SQL runbook (PuTTY + `runsqlfile.pl`): KB `guides/sql_staging_putty/CONFLUENCE_PAGE_UNITED_sql_execution_staging.md` and source `guides/sql_staging_putty/source/How to update data using SQL.docx`.

### Step 4 — Align automation with your schema

1. Apply the **code change** in §5 to **both** V2 and V3 `BaseClass.java` (same method: `performQueryReplacements`).
2. Pass your schema into the JVM (recommended) — see §5 **After** example using **`-Dqa.oracle.schema=YOUR_USER`**.
3. Re-run a failing scenario (e.g. `MemberSingleContribution.feature`).

### Step 5 — (Optional) Service ticket path

If policy requires **shared-schema** access instead of user objects, use `instructions to create ticket.txt` in this folder as a **template** for an AGS/access ticket. Historical example: `[AGS #500647] Stage DB  Schema_ Access.eml`. **This workaround avoids depending on that approval** for daily automation.

---

## 4. Sample SQL execution (sqlplus-style)

Replace `YOUR_USER` / password / TNS with your environment values.

```text
sqlplus YOUR_USER/your_password@STAGE1_TNS_ALIAS

@Create_QA_FIN_TXN_tables_DDL.sql

-- sanity checks (optional)
SELECT table_name FROM user_tables WHERE table_name IN ('QA_FIN_TXN','QA_FIN_INSTRUCTION');
SELECT synonym_name, table_owner, table_name FROM user_synonyms WHERE synonym_name IN ('QA_FIN_TXN','QA_FIN_INSTRUCTION');
```

---

## 5. Code changes (`performQueryReplacements`)

### 5.1 Location

- **V2:** `prime/source/com/cs529/qa/prime/core/BaseClass.java` → method **`performQueryReplacements`** (near the end).
- **V3:** `prime/prime-core/src/main/java/core/test/BaseClass.java` → same method name.

### 5.2 Before (current pattern)

```java
if(query.contains("$$QA_SCHEMA$$")) {
    query = isStageEnvironment() ? query.replace("$$QA_SCHEMA$$", "UII0.") : query.replace("$$QA_SCHEMA$$", "");
}
```

This forces every engineer to use the **UII0** (shared) schema on Stage.

### 5.3 After (user schema via JVM property)

Use a **dedicated system property** so each offshore engineer sets **their** Oracle user **without** editing code.

```java
if (query.contains("$$QA_SCHEMA$$")) {
    if (isStageEnvironment()) {
        String qaSchema = System.getProperty("qa.oracle.schema", "").trim();
        if (qaSchema.isEmpty()) {
            throw new IllegalStateException(
                "Stage automation requires -Dqa.oracle.schema=<ORACLE_USERNAME> (your Stage user, e.g. SPATIAL_SPAGHETTI)");
        }
        String prefix = qaSchema.toUpperCase().endsWith(".") ? qaSchema.toUpperCase() : qaSchema.toUpperCase() + ".";
        query = query.replace("$$QA_SCHEMA$$", prefix);
    } else {
        query = query.replace("$$QA_SCHEMA$$", "");
    }
}
```

**Run configuration example (IDE or Maven):**

```text
-Dqa.oracle.schema=SPATIAL_SPAGHETTI
```

**Team lead / US users** with shared-schema access can set `-Dqa.oracle.schema=UII0` if they intentionally use the shared objects.

> If your team prefers a **config file** or **environment variable** instead of `-D`, implement the same string in one place only—keep behavior identical: Stage must resolve to **`SCHEMA.`** or empty non-Stage.

---

## 6. Validation

1. **DB:** As your user, `SELECT COUNT(*) FROM QA_FIN_TXN;` and `QA_FIN_INSTRUCTION` succeed (may be zero rows).
2. **Automation:** Run one previously failing transaction test (e.g. contribution flow). No `ORA-01031` on `UII0.QA_FIN_*`.
3. **Placeholder:** Breakpoint or log the SQL **after** `performQueryReplacements`; confirm `$$QA_SCHEMA$$` became **`YOUR_USER.`** on Stage.
4. **ORA-01400:** If NULL PK/FK persists, confirm **triggers** `TRG_QA_FIN_TXN` and `TRG_QA_FIN_INSTRUCTION` exist on **your** tables and that inserts follow order: parent **`QA_FIN_TXN`** then child **`QA_FIN_INSTRUCTION`** where applicable.

---

## 7. Sample errors (from team)

**Dinesh** — `ORA-01400` inserting into `UII0.QA_FIN_INSTRUCTION` (`SEQ_QA_FIN_TXN_ID`): see `Error reported by Dinesh.txt`.

**Venkatesh** — same symptom on `MemberSingleContribution.feature`: see `Error reported by Venkatesh.txt`.

---

## 8. References in this issue folder

| File | Purpose |
|------|---------|
| `Create QA_FIN_TXN tables DDL.sql` | Tables, sequences, triggers, grants, synonyms (edit owner in synonym) |
| `Team Tables.eml` | Original DDL context from Pramod |
| `instructions to create ticket.txt` | Template for access ticket (optional path) |
| `[AGS #500647] Stage DB  Schema_ Access.eml` | Example ticket thread |
| `Error reported by Dinesh.txt` / `Error reported by Venkatesh.txt` | Failure evidence |

**External:** Link **`How to update data using SQL.docx`** on Confluence when SQL Developer limitations require PuTTY/sqlplus.

---

*Document version: aligned with KB layout `issues/QA_FIN_TXN_user_schema/`. Update V2/V3 paths if the automation repo structure changes.*
