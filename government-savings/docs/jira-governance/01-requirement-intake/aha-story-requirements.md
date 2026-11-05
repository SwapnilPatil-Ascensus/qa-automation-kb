# Aha! → Jira Story Requirements

*Skip or adapt if your org does not use Aha!*

## 1. Objective

Every Aha!-sourced initiative maps to Jira with **no loss** of intent and **traceable IDs**.

## 2. WHO / WHEN

| Action | WHO | WHEN |
|--------|-----|------|
| Enable / verify Aha!–Jira integration | Tool admin | Before go-live |
| Map Aha! release → Jira `fixVersion` | PO | Per release planning |
| Accept synced Epic/Story | PO | Within 2 days of sync |
| Fix sync errors | SM + PO | Same day |

## 3. Field mapping (template)

| Aha! | Jira | Rule |
|------|------|------|
| Initiative / Release | Epic / fixVersion | 1:1 naming convention: `REL-2026-Q1` |
| Feature name | Story summary | Prefix `[Aha-###]` if ID visible |
| Feature description | Story description | Copy + link to Aha! URL |
| Acceptance criteria | Story AC field or checklist | Must sync; no empty AC for dev Stories |
| Status | Map via integration matrix | Do not hand-edit in both tools conflictingly |

## 4. Story quality gate from Aha!

Before a synced Story enters **refinement**:

| Check | Owner |
|-------|--------|
| AC present and testable | PO |
| Epic link correct | PO |
| No duplicate Jira key | SM |

## 5. Template — Jira description footer (paste)

```text
Source: Aha! [Feature name] — [URL]
Aha ID: [id]
```

**Version:** 1.0
