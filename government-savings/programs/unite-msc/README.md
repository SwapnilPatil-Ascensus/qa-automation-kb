# Unite MSC

One program folder. Six places to look.

```
unite-msc/
├── README.md          ← you are here
├── leadership/        ← decks, emails, Kevin/Rajib updates
├── mobile-1/          ← Mobile 1 sign-off + mapping + L5 SQL handoff (not implemented)
├── mobile-2/          ← Mobile 2 sign-off + mapping + L5 SQL analysis
├── enrollment/        ← Enrollment handoff (QA-893) + coverage + SQL
├── traceability/      ← QA-1942 legacy → TestNG matrix (CSV + Word)
└── sharepoint/        ← parent/child pages, Copilot prompts, upload manifest
```

**Code is not here.** Runtime is GitLab `api-test-automation` (`mobile/mobile1`, `mobile/mobile2`, `mobile/enrollment`).

| If you need | Open |
|-------------|------|
| Status for leadership | `leadership/` |
| Mobile 1 Word sign-off | `mobile-1/signoff/` |
| Mobile 2 Word sign-off | `mobile-2/signoff/` |
| Enrollment handover pack | `enrollment/README.md` |
| SQL field-level (QA-1054) — **not implemented** | `mobile-2/sql-field-validation/` (M1: `mobile-1/sql-field-validation/`) |
| Complete SharePoint publishing pack | `sharepoint/README.md` |
| Enrollment-only legacy prompts | `enrollment/sharepoint/` |
| Legacy → canonical matrix (QA-1942) | `traceability/` |

Old copies (`api-test-automation` KB dump, `program-hub`, `msc-enrollment`, `api-validation`, `enrollment-handoff-qa-893`) were removed on purpose — not archived.
