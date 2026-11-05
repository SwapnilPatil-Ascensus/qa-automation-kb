# Filters and JQL

## 1. Naming

```text
[Team] — [Purpose]
Example: QA-Auto — Current Sprint Open Work
```

**WHO creates:** SM or delegate **WHEN:** onboarding + per reporting need.

## 2. Standard filters (customize `PROJ`)

**Current sprint — not done**

```jql
project = PROJ AND sprint in openSprints() AND statusCategory != Done
ORDER BY rank ASC
```

**Ready for refinement**

```jql
project = PROJ AND status = Ready AND "Story Points" is EMPTY
ORDER BY rank ASC
```

**Blocked**

```jql
project = PROJ AND status = Blocked
ORDER BY updated DESC
```

**My work this sprint**

```jql
project = PROJ AND sprint in openSprints() AND assignee = currentUser()
ORDER BY status ASC, updated DESC
```

**Recently done (7 days)**

```jql
project = PROJ AND statusCategory = Done AND resolved >= -7d
ORDER BY resolved DESC
```

## 3. Replace placeholders

| Placeholder | Your value |
|-------------|------------|
| `PROJ` | Project key |
| `Ready`, `Blocked` | Exact status names from your workflow |
| `Story Points` | Custom field name or ID from Jira |

## 4. Saved filter ownership

| Rule | Enforcement |
|------|-------------|
| Team-critical filters | Owned by SM; documented here |
| Personal filters | User-owned; not governance |

**Version:** 1.0
