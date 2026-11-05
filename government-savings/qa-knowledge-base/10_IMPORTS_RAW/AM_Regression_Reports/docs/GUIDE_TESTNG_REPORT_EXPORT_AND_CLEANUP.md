# TestNG HTML exports – cleanup, folders, and naming

Saving a TestNG report from the browser (or “Webpage, complete”) almost always creates **extra junk**: a sidecar folder of assets, duplicate filenames, and clutter in **Downloads**. Use this guide before pointing Cursor (or teammates) at a report path for doc refresh.

> **Repo note:** `AM_Regression_Reports/reports/` is **gitignored** (large, regenerable). This file lives under **`docs/`** so it **is** versioned. Optional `reports/**/README.md` copies can mirror the short policy locally.

---

## 1. What the browser creates (“junk”)

| Artifact | Typical name | What to do |
|----------|--------------|------------|
| Main HTML | `index.html` or suite title + `.html` | **Keep** (rename per convention below). |
| Asset folder | Same base name + `_files/` (Chrome/Edge) or `index_files/` | **Either** delete if you only need metrics in Markdown (report may look plain offline) **or** keep folder **next to** the HTML with matching basename. |
| Duplicates | `index (1).html`, `…(2).html` | **Delete** extras after you confirm which run is correct. |
| Zip from CI | Single archive | Extract into a **dated** or **run-labeled** subfolder, then rename HTML. |

**Cleanup checklist (before commit / before sharing path with AI)**

1. Delete **`(1)` / `(2)`** duplicates and stray partial downloads.
2. If policy is **HTML-only in KB folder**: delete `*_files/` and accept unstyled local view, **or** open report from **GitLab/Jenkins** for full styling.
3. Move the canonical HTML out of **Downloads** into `AM_Regression_Reports/reports/v2/` or `reports/v3/` (see layout below).
4. Rename file to the **team convention** (section 3).
5. Update **module Markdown** “Report & artifacts” / “Latest report summary” paths if filenames changed.

---

## 2. Folder layout (recommended)

| Path | Use |
|------|-----|
| `AM_Regression_Reports/reports/v2/` | V2 / Jenkins module exports (e.g. per-suite HTML). |
| `AM_Regression_Reports/reports/v3/` | V3 / GitLab combined or UE+IDP exports. |
| `AM_Regression_Reports/reports/archive/` *(optional)* | Older runs; optional `YYYYMMDD/` subfolders. |

**Do not** leave long-term copies only in **Downloads** or on the desktop—paths in docs should point under `reports/`.

---

## 3. File naming convention

| Rule | Example |
|------|---------|
| Prefer **ASCII**; avoid `? * | " < >` and very long Unicode titles. | Good: `Regression-Test-Suite-Enrollments-1.html` |
| Align with **TestNG suite display name** when practical (shorten if > ~80 chars). | `Regression Test Suite - Enrollments` → `Regression-Test-Suite-Enrollments-1.html` |
| Multiple tabs/views of same run | Suffix `-1`, `-2`, `-3` (match existing module docs). |
| Combined V3 report | e.g. `Regression-FrontOffice-Stage1-IDP-UE-1.html` — **consistent** across refreshes. |
| Optional run id | `...-YYYYMMDD` or `...-jobid` **suffix** if you keep multiple runs side by side. |

**Windows tip:** If the browser saved `Regression Test (Front Office) in Stage1 - IDP Login & UE.html`, that is fine if stable; otherwise normalize hyphens/spaces per team preference.

---

## 4. `_files` folder decision

| Choice | When |
|--------|------|
| **Delete `_files/`** | You only need **counts / pass-fail** for Markdown refresh; styling offline does not matter. |
| **Keep `_files/` next to HTML** | You need **offline** pixel-perfect report; expect **large** diffs if ever un-ignored—usually avoid checking in. |

---

## 5. After cleanup – update documentation

1. Note the **final path** in the module `.md` under `docs/v2/modules/` or `docs/v3/modules/`.
2. Run prompt **I)** in `00_SYSTEM/PROMPTS.md` with that path as **TestNG report**.
3. If you added a **new** doc page, run prompt **J)** to refresh **parent / master** files and the **navigation flowchart**.

---

## 6. Related

- Module template: [TEMPLATE_REGRESSION_MODULE_CONFLUENCE.md](TEMPLATE_REGRESSION_MODULE_CONFLUENCE.md)
- Master doc index: [00-automation-regression-master-overview.md](00-automation-regression-master-overview.md)
- Prompts: `00_SYSTEM/PROMPTS.md` — **I)** module refresh, **J)** parent/master sync
