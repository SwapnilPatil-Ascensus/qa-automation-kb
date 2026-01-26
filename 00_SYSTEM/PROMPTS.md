# Prompt Library

## Purpose

This document provides copy/paste-ready Cursor prompts for QA automation tasks. These are your "buttons" - use them directly in Cursor chat.

## How to Use

1. Copy the prompt you need
2. Paste into Cursor chat
3. Replace any `[PLACEHOLDER]` values with your specific information
4. Execute the prompt

---

## A) One-Time "Project Bootstrap" Prompt

**Use this in Cursor chat after opening the repo:**

```
You are the repo's documentation architect.

Task:
1) Read: 00_SYSTEM/ROLE.md, 00_SYSTEM/CONSTRAINTS.md
2) Create initial curated skeleton content for:
   - 01_CONTEXT/CURRENT_STATE.md
   - 03_ARCHITECTURE/OVERVIEW.md
   - 04_EXECUTION/DAILY_REGRESSION.md
   - 05_ONBOARDING/ONBOARDING_7_DAY.md
   - 06_TEMPLATES/LEADERSHIP_UPDATE_TEMPLATE.md
3) Keep each file concise and table-driven.
4) Insert placeholders where org-specific details are missing, tagged [NEED_INPUT].

Output: directly write the files in the repo.
```

---

## B) "Ingest Confluence Export → Curated Docs" Prompt

**After you drop exports into `10_IMPORTS_RAW/confluence_exports/`:**

```
Ingest task:
- Use ONLY the files under 10_IMPORTS_RAW/confluence_exports/.
- Extract and normalize content into the curated structure (03_ARCHITECTURE, 04_EXECUTION, 05_ONBOARDING, 07_GOVERNANCE_VISIBILITY).
- Do not copy raw text blindly. Rewrite into standardized format.

Rules:
- Any missing information becomes [NEED_INPUT].
- Any sensitive content becomes [REDACT_NEEDED].
- Update 00_SYSTEM/SOURCES.md with what was imported and mapped.

Start with onboarding and daily regression first.
```

---

## C) "Ingest Chats → Decisions + Worklog + Standards" Prompt

**After you paste chat exports/summaries into `10_IMPORTS_RAW/chats_exports/`:**

```
Ingest chats task:
- Read files under 10_IMPORTS_RAW/chats_exports/.
- Produce:
  1) 09_DECISIONS_WORKLOG/DECISIONS.md (bullet ADRs: Decision, Why, Options considered, Impact)
  2) 09_DECISIONS_WORKLOG/WORKLOG.md (dated bullets grouped by month)
  3) 02_STANDARDS/DOC_STANDARDS.md (rules implied by the chats)

Constraints:
- No names/PII unless already safe and required. Prefer roles over names.
- Keep it concise and auditable.
```

---

## D) "Gap Finder" Prompt (Find What's Missing)

**Run weekly:**

```
Gap analysis:
Scan curated docs (01-07 folders).
Create/refresh:
- 11_BACKLOG/DOC_GAPS.md with:
  - Missing pages
  - Missing sections within pages
  - Conflicts or outdated statements
  - Suggested owner (role) and priority (P0/P1/P2)

Output should be a table with: Area | Gap | Risk | Priority | Owner | Next action.
```

---

## E) "Confluence-Ready Page Generator" Prompt

**Use anytime:**

```
Create a Confluence-ready page for: [TOPIC]
Source: use only repository content.
Format:
- Purpose
- Scope
- Preconditions
- Step-by-step (table)
- Definition of Done
- Troubleshooting
- FAQs
- Links (repo paths)

Keep it short and execution-first.
```

---

## F) "Leadership Update" Prompt (1-Minute Status)

**Using repo facts only:**

```
Using repo facts only, generate a leadership update for: [WEEK/DATE].
Max 6 bullets:
- Progress
- Risks/blocks
- Decisions needed
- Next week focus
Also output a 1-line headline summary.
```

---

## G) "RCA from Evidence" Prompt

**Given evidence (logs/failed tests summary):**

```
RCA assistant:
Given this evidence (logs/failed tests summary pasted below), produce:
- Problem statement
- Likely causes (ranked)
- Validation steps
- Fix options (low-risk first)
- Prevent recurrence (standards + pipeline guards)
Then update 04_EXECUTION/RCA_PROCESS.md if a new pattern is discovered.

[PASTE EVIDENCE BELOW]
```

---

## Additional Quick Prompts

### Test Development

#### Create Page Object
```
Create a Page Object class for [page name] following POM pattern.
Include:
- WebElement locators
- Action methods
- Verification methods
- Follow naming conventions from 02_STANDARDS/NAMING_CONVENTIONS.md
```

#### Create Test Scenario
```
Create a Cucumber test scenario for [feature/functionality].
Follow BDD best practices and use Gherkin syntax.
Include:
- Given/When/Then steps
- Test data considerations
- Expected validations
```

#### Create API Test
```
Create a REST Assured API test for [endpoint].
Include:
- Request setup
- Response validation
- Error handling
- Test data management
```

### Test Execution

#### Analyze Test Results
```
Analyze the test execution results and identify:
- Failed tests and root causes
- Flaky tests
- Performance issues
- Recommendations for fixes
```

#### Generate Execution Report
```
Generate a test execution report using 06_TEMPLATES/EXEC_REPORT_TEMPLATE.md.
Include:
- Execution summary
- Pass/fail statistics
- Failed test details
- Recommendations
```

### Debugging

#### Investigate Flaky Test
```
Investigate the flaky test [test name].
Follow the process in 04_EXECUTION/FLAKINESS_PLAYBOOK.md.
Identify:
- Root cause
- Fix recommendations
- Prevention strategies
```

## Best Practices

1. **Be specific**: Include context about what you're working on
2. **Reference standards**: Always mention relevant standards documents
3. **Request templates**: Ask for templates when creating new documents
4. **Maintain consistency**: Use established patterns and conventions
5. **Use placeholders**: Replace `[PLACEHOLDER]` values before executing

## Notes

- All prompts assume you're working within this repository context
- Prompts follow the non-negotiables from `00_SYSTEM/ROLE.md`
- Output should be execution-ready (Confluence/Jira/pipeline ready)
- Prefer tables/checklists over paragraphs
