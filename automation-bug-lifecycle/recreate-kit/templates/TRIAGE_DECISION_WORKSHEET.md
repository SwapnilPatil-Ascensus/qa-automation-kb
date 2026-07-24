# Triage Decision Worksheet

Use before logging JIRA. One failure = one worksheet (save in evidence folder if helpful).

**Date:** _______________  
**Feature/area:** _______________  
**Environment:** _______________  
**Last green run:** _______________

---

## Failure summary

| Field | Value |
|-------|-------|
| Test / scenario name | |
| Error (one line) | |
| CI job / report URL | |
| Retry result | ☐ Pass ☐ Fail ☐ Not run |

---

## Classification (check ONE)

| ☐ | Type | Signals present? |
|---|------|------------------|
| ☐ | **Environment** | DB refresh, certs, OKD down, env-only failures |
| ☐ | **Flaky / false** | Pass on retry; timing; same TR failed+passed same day |
| ☐ | **Automation script** | Locator, wait, test data in script |
| ☐ | **Functional defect** | Reproducible locally; manual repro; app stack trace |

---

## Decision

| Question | Answer |
|----------|--------|
| Log JIRA? | ☐ Yes ☐ No ☐ Optional |
| Lock main? | ☐ Yes (critical + legit) ☐ No |
| Next prompt | ☐ 02 Prompt H ☐ Flakiness playbook ☐ Escalate env |

---

## Notes

_______________________________________________  
_______________________________________________

**If defect:** Run `scripts/new-evidence-folder.ps1` then Prompt H.
