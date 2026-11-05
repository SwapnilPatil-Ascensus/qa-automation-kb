# Acceptance Criteria Template

## 1. Rules

| Rule | Enforcement |
|------|-------------|
| AC must be **testable** (pass/fail) | Tech Lead at DoR |
| Prefer **Given/When/Then** or **checklist** | PO authors |
| Each AC maps to **≤1** main test theme | QA review at refinement |

## 2. Template A — Checklist (fast)

```markdown
- [ ] [Observable behavior 1]
- [ ] [Observable behavior 2]
- [ ] [Error/edge case handled: …]
- [ ] [Telemetry/logging if required]
- [ ] [Docs/runbook updated if required]
```

## 3. Template B — Gherkin-style

```gherkin
Scenario: Happy path
  Given …
  When …
  Then …

Scenario: Validation failure
  Given …
  When …
  Then …
```

## 4. Template C — Non-functional (performance)

```markdown
- [ ] Scenario runs in [env] under [SLO] (define metric)
- [ ] No regression on [baseline job name]
- [ ] Results visible in [dashboard/report path]
```

## 5. WHO / WHEN

| Action | WHO | WHEN |
|--------|-----|------|
| Draft AC | PO | Before refinement |
| Challenge vague AC | Tech Lead + QA | Refinement |
| Lock AC for sprint | PO | Sprint planning start |

## 6. Forbidden patterns

| Bad | Why |
|-----|-----|
| “Works well” | Not testable |
| “Code reviewed” | Belongs in DoD, not AC |
| “No bugs” | Not a criterion |

**Version:** 1.0
