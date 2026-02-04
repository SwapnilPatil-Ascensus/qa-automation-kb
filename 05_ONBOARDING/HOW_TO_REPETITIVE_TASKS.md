# How to Use Repetitive Tasks (Templates & Prompts)

This doc tells you **where things live** and **exact steps** for the tasks we do over and over: bug reporting (JIRA + email + Teams) and the bi-weekly leadership update for Persistent. Use it when you forget locations or steps.

---

## Quick Reference: Where Is What?

| What you need | Location |
|---------------|----------|
| **All prompts (Bug, Leadership, RCA, etc.)** | `00_SYSTEM/PROMPTS.md` |
| **Bug documentation template** | `10_IMPORTS_RAW/regression_reports/[DATE]/BUG_DOCUMENTATION_TEMPLATE.md` (copy from an existing date folder if missing) |
| **Bug process (naming, folder structure)** | `10_IMPORTS_RAW/regression_reports/BUG_REPORTING_PROCESS.md` |
| **Email template for “failure” (first email)** | `10_IMPORTS_RAW/confluence_exports/Bug Handling/1. Handling Process When a Bug Is Found or Regression Fails (QA Automation).pdf` |
| **Email template for “resolved” (resolution email)** | `10_IMPORTS_RAW/confluence_exports/Bug Handling/1b. 🔁 Automation Bug Resolution Follow-Up Process & Resolution Notification.pdf` |
| **Leadership update template** | `06_TEMPLATES/PERSISTENT_LEADERSHIP_UPDATE_TEMPLATE.md` |
| **Leadership update prompt** | `00_SYSTEM/PROMPTS.md` → section **F2) Persistent Bi-Weekly Leadership Update** |
| **Example leadership update (format reference)** | `10_IMPORTS_RAW/confluence_exports/Demand Planning Reports/14. QA Automation Program – Leadership Working Update (As of 02042026).md` |
| **JIRA ticket template (generic)** | `06_TEMPLATES/JIRA_TICKET_TEMPLATE.md` |

---

## Task 1: Bug Report (JIRA + Email Draft + Teams Message)

**When:** A regression or test failure happens and you need to log a bug and notify people.

**What you get:** One markdown file that contains (1) JIRA copy-paste content, (2) email draft for “failure,” (3) Teams message, and later (4) resolution email when the bug is fixed.

### Step 1: Put all evidence in one folder

1. Open or create the folder for **that day’s run**:  
   `10_IMPORTS_RAW/regression_reports/[MMDDYYYY]/`  
   Example: `10_IMPORTS_RAW/regression_reports/02032026/`
2. Put in that folder:
   - Screenshots (e.g. `UE Failure.png`)
   - Exception or failure log (e.g. `*.feature_exception_failedresult.txt`)
   - Test case / test data (e.g. `*testcase_information.txt` or `Test Data.txt`)
   - Any TestNG or report link (you can paste the URL in the doc)

### Step 2: Create the bug doc (JIRA + email + Teams)

1. Open **Cursor** and open this repo.
2. Open `00_SYSTEM/PROMPTS.md` and find the prompt **“H) Bug Report: JIRA + Email + Teams”**.
3. Copy that prompt, then **paste your details** where it says to paste:
   - Date (MMDDYYYY)
   - Feature/area (e.g. Universal Enrollment, IDP Login)
   - Short summary of what failed and the error (and paste the exact exception if you have it)
   - TestNG or report link
   - Path to the folder where you put the artifacts (e.g. `10_IMPORTS_RAW/regression_reports/02032026`)
4. Run the prompt. Cursor will create **one new file** in that same folder, named:  
   `[MMDDYYYY]_[Feature]_[IssueType].md`  
   Example: `02032026_UniversalEnrollment_BadSqlGrammarException.md`
5. That file will contain:
   - **JIRA block** – copy-paste into JIRA (Summary, Description, Steps, Expected/Actual, Environment, Priority, Attachments, etc.)
   - **Email draft** – for the “failure” email (to leads/dev); follow the Bug Handling PDF template
   - **Teams message** – short version for Teams
   - **Resolution section** – leave empty until the bug is fixed

### Step 3: Create the JIRA ticket and send email/Teams

1. In JIRA: create a new bug, paste the JIRA block from the .md file. Attach the screenshot(s) from the folder.
2. Copy the **email draft** from the .md file into your email; add the JIRA link once the ticket is created. Send to the usual list (see Bug Handling PDF).
3. Copy the **Teams message** from the .md file into Teams; add the JIRA link.

### Step 4: When the bug is fixed (resolution email)

1. Get the **RCA** (root cause and who fixed it) from the dev or your notes.
2. Open the same bug .md file. Find the **“Resolution Email Draft”** section (or add it using the resolution template from the Bug Handling PDF “1b. Automation Bug Resolution Follow-Up…”).
3. Fill in: Root cause, Fix implemented by, Verified via, Branch status (e.g. main unlocked), Note.
4. Send the resolution email to the same audience as the failure email.
5. In the .md file, update the **JIRA** line at the top with the real ticket (e.g. QA-435) and “Status: Closed” so you have one place that points to the ticket.

**File naming rule:**  
`[MMDDYYYY]_[FeatureName]_[IssueType].md`  
Example: `02032026_UniversalEnrollment_BadSqlGrammarException.md`

---

## Task 2: Bi-Weekly Leadership Update (Confluence Page + PSL Summary)

**When:** Every **alternate week** when Persistent has the meeting with the client.

**What you get:** (1) A detailed Confluence-style page, and (2) the “5. Automation Team” block to paste on the main PSL page.

### Step 1: Prepare your brief update

Write a short note (bullet points are fine) about:
- What the team **did** in the last two weeks (V2, V3, API, performance, platform support, etc.)
- What is **in progress** or **next**
- Any **risks** or **ask for leadership** (e.g. unplanned support load, intake)

You don’t need to write full sentences; the prompt will turn this into the right format.

### Step 2: Run the leadership update prompt

1. Open **Cursor** and this repo.
2. Open `00_SYSTEM/PROMPTS.md` and go to **F2) “Persistent Bi-Weekly Leadership Update”**.
3. Copy the **entire** F2 prompt (the block that starts with “Persistent bi-weekly leadership update task…”).
4. **Replace** these placeholders at the top of the prompt with **this** period’s values:
   - `[START]` = first day of the 2-week period (e.g. Jan 22, 2026)
   - `[END]` = last day (e.g. Feb 4, 2026)
   - `[LAST_SHARE_DATE]` = date of the last share-out (e.g. Jan 21)
   - `[MMDDYYYY]` = date of **this** update (e.g. 02042026)
   - `[NEXT_NUMBER]` = next report number (e.g. 14 → next is 15)
5. **Paste your brief update** where it says `[BRIEF UPDATE PASTE BELOW]`.
6. Run the prompt in Cursor.

### Step 3: Where the output goes

1. Cursor will create (or update) **one file**:  
   `10_IMPORTS_RAW/confluence_exports/Demand Planning Reports/[NEXT_NUMBER]. QA Automation Program – Leadership Working Update (As of [MMDDYYYY]).md`  
   Example: `15. QA Automation Program – Leadership Working Update (As of 02182026).md`
2. That file has two parts:
   - **Part 1:** Full Confluence-style page (sections 1–10). Use it to update Confluence or share as the detailed reference.
   - **Part 2:** **“PSL Page Summary”** – the “5. Automation Team” block. Copy that whole block and paste it into the **main PSL page** (MAIN - PSL - Persistent Updates) in the QA Automation section.

### Step 4: Double-check before you publish

- Dates in the doc match the period and “since last” date.
- PSL block has: Detailed Reference, One-Line Summary, Key Highlights, In Progress / Next Focus, Initiatives & Execution Highlights, Call-Out for Leadership.

**Template to look at (structure only):**  
`06_TEMPLATES/PERSISTENT_LEADERSHIP_UPDATE_TEMPLATE.md`  
**Example of a finished update:**  
`10_IMPORTS_RAW/confluence_exports/Demand Planning Reports/14. QA Automation Program – Leadership Working Update (As of 02042026).md`

---

## Summary Checklist

**Bug (failure):**
- [ ] Evidence in `10_IMPORTS_RAW/regression_reports/[MMDDYYYY]/`
- [ ] Run Bug prompt in Cursor with date, feature, error, folder path, report link
- [ ] New file created: `[MMDDYYYY]_[Feature]_[Issue].md`
- [ ] Copy JIRA block → create JIRA ticket → attach screenshot
- [ ] Copy email draft → add JIRA link → send
- [ ] Copy Teams message → add JIRA link → post

**Bug (resolved):**
- [ ] Get RCA; open same bug .md file
- [ ] Fill Resolution Email Draft (root cause, fix by, verified, branch, note)
- [ ] Send resolution email; update JIRA link/status in .md if needed

**Leadership update (bi-weekly):**
- [ ] Write brief update (what did / in progress / risks)
- [ ] Open PROMPTS.md → F2, copy prompt, set [START]/[END]/[LAST_SHARE_DATE]/[MMDDYYYY]/[NEXT_NUMBER], paste update
- [ ] Run prompt → get one .md with Confluence page + PSL block
- [ ] Use Confluence page for Confluence or detailed reference; copy PSL block to main PSL page

---

**If you forget this doc:** It’s at `05_ONBOARDING/HOW_TO_REPETITIVE_TASKS.md`. All prompts are in `00_SYSTEM/PROMPTS.md` (Bug = **H) Bug Report: JIRA + Email + Teams**; Leadership = **F2) Persistent Bi-Weekly Leadership Update**).
