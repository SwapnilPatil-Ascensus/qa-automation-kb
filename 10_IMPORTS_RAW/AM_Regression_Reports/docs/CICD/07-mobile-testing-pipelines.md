# CI/CD – Mobile Testing Pipelines (Jenkins)

**Status:** **Needs Review** / **Not actively maintained**  
**Platform:** **Jenkins** (jobs reported to exist)

---

## Purpose

Automated testing of **mobile** applications (native or hybrid) via jobs integrated with **Jenkins**.

---

## Scope

- **Historical / existing:** Jenkins jobs are **already created** (per team).
- **Current operations:** **Unclear** — team is **not actively maintaining** mobile automation at this time.

---

## Framework / technology

**Needs Validation** — e.g. Appium, Espresso, XCUITest, or third-party device cloud. **Not evidenced** in **qa-automation-kb**.

---

## Pipeline platform

| Item | Detail |
|------|--------|
| Platform | **Jenkins** (per team) |
| Job names | **Needs Validation** |

---

## Current status

| Aspect | Status |
|--------|--------|
| Jobs exist | **Likely** — **Needs Validation** in Jenkins UI |
| Maintenance | **Not actively maintained** |
| Readiness for use | **Needs Review** — expect **validation**, **cleanup**, and **ownership** transfer before relying on results |

---

## Execution schedule

**Needs Validation** — unknown if any schedule is still enabled.

---

## Coverage / suites / modules

**Needs Validation** — document app versions, devices, and suites when ownership resumes.

---

## Dependencies

- **Device lab** or cloud (BrowserStack, Sauce, etc.) — **Needs Validation**.
- **Signing**, **provisioning**, and **test accounts** for mobile.
- Jenkins **plugins** and agents compatible with mobile toolchains.

---

## Known issues / risks

- **Stale** jobs may **fail** for reasons unrelated to app quality (SDK drift, expired certs).
- **No owner** → no triage path for failures.

---

## Ownership / support model

- **Today:** **Needs Validation** — assign **primary owner** before next execution.
- **Handoff:** If ownership moves to a new squad, plan **knowledge transfer** + **credential** rotation.

---

## Future direction

- **Option A:** **Reactivate** with explicit owner, updated stack, and smoke-only scope.
- **Option B:** **Disable** jobs in Jenkins and mark **Legacy** until strategy returns.
- **Option C:** Consolidate under **GitLab** or **GitHub** if mobile CI standardizes there — **Needs Validation** against org standards.

---

## Open questions / validation needed

- Which **apps** (iOS/Android) and **branches** are targeted?
- Last **green** run date and **logs**.
- Whether mobile should align with **V3** test data strategy.

---

## References from repo

- **None in qa-automation-kb** for mobile projects — add repo links when identified.
