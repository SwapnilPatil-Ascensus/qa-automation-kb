# Perf testing update template

Copy sections into [unite-msc-performance-testing-tracker.md](../docs/01-shared/unite-msc-performance-testing-tracker.md) when status changes.

## Quick update checklist

- [ ] Jenkins job URL / parameter change?
- [ ] New YAML or JMX in `performance-test-automation/performance/mobile/unite-msc/`?
- [ ] Scripts deployed to loadtestwt1 / loadtestwt2?
- [ ] Jira ticket status change (QA-1228, QA-1229, QA-1230)?
- [ ] Nightly schedule enabled/disabled?
- [ ] Changelog row added with date

## Changelog entry format

```markdown
| YYYY-MM-DD | Brief change | Name |
```

## Sprint row format

```markdown
| **QA-XXXX** | [Perf Testing][Unite-MSC-AUTH] Summary | Priti | N | **Status** | Notes |
```

## New script row format

```markdown
| `script.jmx` + `-remote.yaml` | BlazeMeter name | Flow description | Jenkins job | **Status** |
```
