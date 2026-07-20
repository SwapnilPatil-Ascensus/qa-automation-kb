# Government Savings Coverage Intelligence Assessment

**Assessment date:** 2026-07-20  
**Type:** Read-only feasibility audit  
**Git status:** Excluded via `.gitignore` — local artifacts only

## Purpose

Evidence-backed investigation for an automated GS **coverage intelligence** capability — distinguishing source-code (A), business (B), execution (C), CI-integration (D), and gate (E) metrics.

## Start here

| Document | Audience |
|----------|----------|
| [Executive summary](10-leadership/executive-summary.md) | Leadership |
| [Feasibility report](10-leadership/automated-coverage-feasibility-report.md) | Technical + program |
| [Michael Blake response draft](10-leadership/michael-blake-response-draft.md) | Email-ready |
| [Action items](10-leadership/action-item-proposal.md) | Program tracking |

## Folder structure

| Folder | Contents |
|--------|----------|
| `01-connectivity/` | MCP + API capability matrix |
| `02-qtest/` | Schema, data quality, readiness |
| `03-jira/` | Scope assessment, denominator options, link quality |
| `04-repositories/` | Repo, test, identifier inventories |
| `05-pipelines/` | Pipeline jobs, source-code coverage, CI gate audit |
| `06-model/` | Metric definitions, denominator matrix, recommended model |
| `07-reconciliation/` | Cross-system prototype + gaps |
| `08-solution/` | Options, architecture, MVP plan, security |
| `09-governance/` | Gate strategy, governance, freshness |
| `10-leadership/` | Reports, summaries, decision log |
| `tools/` | `generate_coverage_intelligence_assessment.py` |

## Regenerate CSV / XLSX

```powershell
cd c:\Workspace\GitLab\qa-automation-kb\coverage-intelligence-assessment\tools
python generate_coverage_intelligence_assessment.py
```

## Related baselines

| Baseline | Path |
|----------|------|
| GS automation assessment (Jul 2026) | `../government-savings-automation-assessment/` |
| Universal Platform coverage | `../universal-platform-coverage/` |
| Unite MSC leadership pack | `../leadership-updates/unite-msc/2026-07-17-leadership-update/` |

## Constraints honored

- Read-only — no external ALM/CI writes  
- No credentials in artifacts  
- No commit/push of assessment output  
- Conclusions labeled: Verified · Inferred · Planned · Stale · Unknown · Blocked  

---

*Confidential — Internal Use · Ascensus Government Savings QA Automation*
