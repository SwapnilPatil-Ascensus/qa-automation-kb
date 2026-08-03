# Status update checklist

When completing work on a feature:

1. Update the feature row in `STATUS.md`:
   - Scenarios: `{done}/{total}`
   - SQL files: `{done}/{planned}`
   - Docs: `{overview + mapping + flow + scenarios index}`
   - Composite queries count
   - Status: Not Started → In Progress → Done

2. Add a detail subsection if the feature has notable blockers (on-prem, multi-backend).

3. Set **Last updated** date at top of `STATUS.md`.

Example row after mobiledashboard complete:

```markdown
| mobiledashboard | 15/15 | 8/8 | 4/4 | 2/2 | Done |
```
