# 06 — Archive and lifecycle

## Source of truth

| State | Where |
|-------|--------|
| Authoring | `programs/sharepoint-qa-hub/pages/` |
| Evergreen procedures | `qa-knowledge-base/` and `automation-bug-lifecycle/` |
| Old Confluence dump | `qa-knowledge-base/10_IMPORTS_RAW/confluence_exports/auto-qa-dochub/` — **do not delete** |
| Live SharePoint | Numbered Site Pages `00`–`14`, tag `qa-auto-live` |
| SharePoint dump | Move under **99 Archive** (library folder or parent page), tag `qa-auto-archive`, **no left-nav** |

## When a new SharePoint page goes live

1. Put the published URL in [07-build-sequence.md](./07-build-sequence.md).
2. On the old dump page, add a 1-line redirect banner (Copilot Prompt 2).
3. After two sprints, remove dump pages from navigation only — keep files for audit.

## Retention

- PDFs in Git: keep. They are the legal/historical export.
- SharePoint Archive: keep until the team agrees the numbered hub has been used for a full quarter.
- Performance JMeter trees in `10_IMPORTS_RAW`: do not copy to SharePoint; point to GitLab.

## Secrets

If a file looks like a key, password, or `secretKey*`, it stays out of SharePoint and should be removed from Git in a later cleanup (out of scope here unless you ask).
