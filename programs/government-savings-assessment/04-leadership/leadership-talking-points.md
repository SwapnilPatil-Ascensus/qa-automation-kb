# Leadership Talking Points — July 21, 2026 Review

## Opening (30 seconds)

- GS has **real automation** — V3 nightly, large V2 corpus, MSC API program, metadataweb API, perf assets.  
- **We cannot responsibly quote one GS-wide %** today.  
- This rebuild **corrected headline numbers** to match verified evidence vs code-in-progress.

## Verified wins

1. **V3 UI** — GitLab scheduled regression; **379/436** scoped methods (**86.9%** inventory share).  
2. **Mobile 2** — **22/25 (88%)** — **July 14 sign-off baseline** (not superseded without new evidence).  
3. **Mobile 1 auth** — **1/27 (3.7%)** verified; foundation OKD+NMD complete.  
4. **GHA** — Dashboard vertical slice **validated** (Nexus pattern) — **not** "unimplemented."  
5. **Metadataweb API** — scheduled GitLab Stage 1.

## Corrected messaging (if challenged)

| If they heard… | Say… |
|--------------|------|
| "Mobile 2 is 100%" | **88% verified** (22/25); **96% projected** pending sign-off — not 100% (`mobilemembers` excluded by design). |
| "Mobile 1 is 22%" | **3.7% verified**; five more endpoints **in code** — sprint will produce evidence. |
| "No GitHub Actions" | **Dashboard slice validated externally**; module expansion in progress; repo not in our clone. |
| "GitLab blocks merges" | **Scheduled jobs fail on errors** — merge gate **not verified**. |

## Asks for leadership

1. **DevOps priority:** Mobile 2 GitLab nightly (QA-1405).  
2. **Sign-off window:** Fresh QC4 + Stage 1 for Mobile 2 after latest `main`.  
3. **Mobile 1 sprint air cover** — non-IDP endpoints this sprint.  
4. **Test data / Stage 1 fixture** for contribution detail/PUT.  
5. **BA capacity (~30–40%)** for denominators + qTest hygiene.  
6. **Quarterly GS automation roadmap** visibility.  
7. **Approve separate metrics** — never blend JaCoCo, business %, execution %, gate %.

## Closing narrative

> The team has meaningful automation across Government Savings. The current limitation is not the ability to build automation; it is establishing a consistent, traceable coverage model across Jira, qTest, repositories, and CI execution.

## Do not say

- "GS has X% coverage."  
- "Automation is complete."  
- "100% Mobile 2."  
- "GitHub isn't set up."
