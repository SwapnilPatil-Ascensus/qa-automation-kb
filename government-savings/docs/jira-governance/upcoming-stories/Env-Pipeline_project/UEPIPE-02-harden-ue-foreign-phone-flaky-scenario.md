# UEPIPE-02 — Harden UE “Foreign Phone” integration scenario (flake / timeout)

**Status:** Draft · **Suggested Story Points:** **5** · **Epic:** [QA-600](https://ascensuscollegesavings.atlassian.net/browse/QA-600)

**Labels:** `automation`, `prime-v3`, `stage1`, `universal-enrollment`, `flaky`, `ENVP`, `QA-Board-View`

**Blocks:** Reliable green runs for UEPIPE-01 pipeline gate.

---

## Copy — Jira Summary

```
[ENVP][UE] Stabilize Foreign Phone universal enrollment scenario (#firstName timeout)
```

---

## Copy — Description

```markdown
## Problem
`mvn test -P stage1-ue-integration-test` in `unite/universal-enrollment`: scenario *Single Universal Enrollment with Enrollment of Individual Account with Foreign Phone* (`UniversalEnrollmentPositive.feature` ~line 41) fails intermittently.

**Symptom:** `WebDriverWait` **30 s** timeout waiting for `#firstName` (`SeleniumDriver.findElement` → `completeUniAccountOwnerInformation` → `completeNextGenAccountOwnerInformation`).

**Retry pattern observed:** Run 1 PASS, Run 2 FAIL, Run 3 PASS — build still **failed** (retry did not clear overall failure).

## Goal
Make this scenario **reliably pass** under **parallel Chrome** (suite uses `parallel="tests"` / multi-traunch load) OR document and implement agreed **quarantine** policy with PO/Tech lead sign-off (only if product defect ruled out).

## Investigation angles
- Traunch-specific URL / slower load when parallel with other tests.
- Locator stability (`#firstName` vs dynamic DOM / NextGen flow).
- Wait strategy vs fixed 30 s (explicit wait for correct page state).
- Test data / phone format / validation blocking render.

## Out of scope
- Rewriting entire UE feature set (stay focused on this scenario or shared helper).

## Evidence paths (local)
`prime-test-automation/unite/unite-universal-enrollment/target/surefire-reports/` — `testng-failed.xml`, HTML under `old/` if applicable.
```

---

## Copy — Acceptance Criteria

```markdown
h3. Must pass

* ( ) Root cause documented in Story comment (or linked doc): traunch, parallel vs serial behavior, locator vs performance.
* ( ) Fix **or** approved quarantine with risk note and owner; if quarantine, suite gate must remain honest (no hidden skip without visibility).
* ( ) **5 consecutive** green runs on reference CI **or** agreed statistical bar (e.g. 0 failures in N nightly runs) — number agreed with QA lead.
* ( ) If code change: MR reviewed; no new broad timeouts without justification.
```

---

## Copy — Sub-tasks (optional)

**Summary:** `[UE][Sub] Reproduce Foreign Phone failure — serial vs parallel`  
**Summary:** `[UE][Sub] Fix waits/locators or test data for Foreign Phone flow`  
**Summary:** `[UE][Sub] Align Surefire retry policy with pipeline pass/fail (see UEPIPE-03)`
