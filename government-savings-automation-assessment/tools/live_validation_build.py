#!/usr/bin/env python3
"""Build live-validation CSVs and verified-metrics-register from current repo evidence."""

from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VALIDATION_TS = "2026-07-20T18:15:00-04:00"
API_REPO = Path(r"C:\Workspace\GitLab\api-test-automation")
API_COMMIT = "cee0de9"
PRIME_COMMIT = "93f8628"

# Mobile 2 — 25 documented business endpoints (Dinesh workbook); evidence from code @ cee0de9 + master XML
M2_ENDPOINTS = [
    ("M2-01", "GET", "/mobile2api/v1/mobileactivity/{ext}", "MobileActivityRequestTest", "getMobileActivity_returnsActivitySummary", "Y", "N", "okdirect,newyork", "QC4,Stage1", "dynamic ext", "Y", "N", "Y", "N", "Implemented — master regression", "Verified automated manually executable", "cee0de9", "master-regression-testng.xml"),
    ("M2-02", "GET", "/mobile2api/v1/mobiletransactionhistory/{ext}", "MobileTransactionHistoryRequestTest", "getMobileTransactionHistory_returnsTransactions", "Y", "N", "okdirect,newyork", "QC4,Stage1", "static ext 01", "Y", "N", "Y", "N", "Implemented — master regression", "Verified automated manually executable", "cee0de9", "master-regression-testng.xml"),
    ("M2-03", "GET", "/mobile2api/v1/investments/{ext}", "MobileInvestmentRequestTest", "getMobileInvestments_returnsInvestments", "Y", "N", "okdirect,newyork", "QC4,Stage1", "static ext 01", "Y", "N", "Y", "N", "Implemented — master regression", "Verified automated manually executable", "cee0de9", ""),
    ("M2-04", "GET", "/mobile2api/v1/mobilebanks", "MobileBanksRequestTest", "getMobileBanks_filterDomesticBanks_returnsBanks", "Y", "N", "okdirect", "QC4,Stage1", "dynamic", "Y", "N", "Y", "N", "Implemented — master regression", "Verified automated manually executable", "cee0de9", ""),
    ("M2-05", "GET", "/mobile2api/v1/mobilebanks/{id}", "MobileBanksRequestTest", "getMobileBankById_returnsBank", "Y", "N", "okdirect", "QC4,Stage1", "dynamic bank id", "Y", "N", "Y", "N", "Implemented — master regression (added post 7ccaf46)", "Implemented — execution evidence pending refresh", "cee0de9", "Added Sunil QA-1386 lineage"),
    ("M2-06", "POST", "/mobile2api/v1/mobilebanks", "MobileBanksRequestTest", "postMobileBanks_addsDomesticBank_returnsBanks", "Y", "N", "okdirect", "QC4,Stage1", "dynamic", "Y", "N", "Y", "N", "Implemented — master regression", "Verified automated manually executable", "cee0de9", ""),
    ("M2-07", "PUT", "/mobile2api/v1/mobilebanks", "MobileBanksRequestTest", "putMobileBanks_updatesDomesticBank_returnsBanks", "Y", "N", "okdirect", "QC4,Stage1", "dynamic", "N", "Y", "N", "N", "Implemented — smoke/targeted only (destructive)", "Verified automated manually executable", "cee0de9", "mobile2-smoke-testng.xml; excluded from master by design"),
    ("M2-08", "DELETE", "/mobile2api/v1/mobilebanks", "MobileBanksRequestTest", "deleteMobileBanks_deletesDomesticBank_returnsBanks", "Y", "N", "okdirect", "QC4,Stage1", "dynamic", "N", "Y", "N", "N", "Implemented — smoke/targeted only (destructive)", "Verified automated manually executable", "cee0de9", "mobile2-smoke-testng.xml"),
    ("M2-09", "GET", "/mobile2api/v1/content", "MobileContentRequestTest", "getContent_commonSavingTips_returnsContent", "Y", "N", "okdirect,newyork", "QC4,Stage1", "query params", "Y", "N", "Y", "N", "Implemented — master regression", "Verified automated manually executable", "cee0de9", ""),
    ("M2-10", "GET", "/mobile2api/v1/plans", "MobilePlansRequestTest", "getMobilePlans_returnsPlans", "Y", "N", "okdirect,newyork", "QC4,Stage1", "static", "Y", "N", "Y", "N", "Implemented — master regression", "Verified automated manually executable", "cee0de9", ""),
    ("M2-11", "GET", "/mobile2api/v1/plans/{id}", "MobilePlansRequestTest", "getMobilePlanById_returnsPlan", "Y", "N", "okdirect,newyork", "QC4,Stage1", "dynamic plan id", "Y", "N", "Y", "N", "Implemented — master regression", "Verified automated manually executable", "cee0de9", ""),
    ("M2-12", "GET", "/mobile2api/v1/mobilecontribution", "MobileContributionRequestTest", "getMobileContribution_returnsContributionOptions", "Y", "N", "okdirect,newyork", "QC4,Stage1", "static", "Y", "N", "Y", "N", "Implemented — master regression", "Verified automated manually executable", "cee0de9", ""),
    ("M2-13", "GET", "/mobile2api/v1/mobilecontributioncheck", "MobileContributionCheckRequestTest", "getMobileContributionCheck_returnsShowContributionFlag", "Y", "N", "okdirect,newyork", "QC4,Stage1", "static", "Y", "N", "Y", "N", "Implemented — master regression", "Verified automated manually executable", "cee0de9", ""),
    ("M2-14", "GET", "/mobile2api/v1/mobilecontribution/{ext}/{id}", "MobileContributionDetailRequestTest", "getMobileContributionById_returnsRecurringContribution", "Y", "N", "okdirect,newyork", "QC4,Stage1", "dynamic SQL fixture", "Y", "N", "Y", "N", "Implemented — master regression; Stage1 partial", "Implemented — Stage1 401 known (fixture)", "cee0de9", "QC4 fixture 472560"),
    ("M2-15", "POST", "/mobile2api/v1/mobilecontribution", "MobileContributionPostRequestTest", "postMobileContribution_createsRecurringContribution", "Y", "N", "okdirect,newyork", "QC4,Stage1", "dynamic", "Y", "N", "Y", "N", "Implemented — master regression", "Verified automated manually executable", "cee0de9", ""),
    ("M2-16", "PUT", "/mobile2api/v1/mobilecontribution/{ext}/{id}", "MobileContributionPutRequestTest", "putMobileContributionById_updatesRecurringContribution", "Y", "N", "okdirect,newyork", "QC4,Stage1", "dynamic SQL fixture", "Y", "N", "Y", "N", "Implemented — master regression; Stage1 partial", "Implemented — Stage1 401 known (fixture)", "cee0de9", ""),
    ("M2-17", "DELETE", "/mobile2api/v1/mobilecontribution/{ext}/{id}", "MobileContributionDeleteRequestTest", "deleteMobileContributionById_removesAutomationOwnedContribution", "Y", "N", "okdirect", "QC4", "dynamic", "Y", "N", "N", "N", "Implemented — module/targeted only (destructive)", "Verified automated manually executable", "cee0de9", "Excluded from master by design"),
    ("M2-18", "GET", "/mobile2api/v1/mobiledashboard", "MobileDashboardRequestTest", "getMobileDashboard", "Y", "N", "okdirect,newyork", "QC4,Stage1", "dynamic", "Y", "N", "Y", "N", "Implemented — master regression", "Verified automated manually executable", "cee0de9", ""),
    ("M2-19", "GET", "/mobile2api/v1/mobileytdsummary/{ext}", "MobileYtdSummaryRequestTest", "getMobileYtdSummary_returnsYtdContributionSummary", "Y", "N", "okdirect,newyork", "QC4,Stage1", "dynamic ext", "Y", "Y", "Y", "N", "Implemented — master + smoke (added post 7ccaf46)", "Implemented — execution evidence pending refresh", "cee0de9", "master-regression L20-29; smoke suite"),
    ("M2-20", "GET", "/mobile2api/v1/mobilemembers/{planId}/{username}", "MobileMembersRequestTest", "getMobileMembers_returnsMemberForHarness", "Y", "N", "okdirect", "QC4", "acceptance harness", "N", "Y", "N", "N", "Harness test — excluded from business automation numerator", "Implemented smoke-only — intentional exclusion", "cee0de9", "Sign-off scope exclusion"),
    ("M2-21", "GET", "/mobile2api/v1/mobilebalancetrend/{ext}", "MobileBalanceTrendRequestTest", "getMobileBalanceTrend_returnsBalanceTrend", "Y", "N", "okdirect,newyork", "QC4,Stage1", "dynamic", "Y", "N", "Y", "N", "Implemented — master regression", "Verified automated manually executable", "cee0de9", ""),
    ("M2-22", "GET", "/mobile2api/v1/mobileperformance/{ext}", "MobilePerformanceRequestTest", "getMobilePerformance_returnsPerformance", "Y", "N", "okdirect,newyork", "QC4,Stage1", "dynamic", "Y", "N", "Y", "N", "Implemented — master regression", "Verified automated manually executable", "cee0de9", ""),
    ("M2-23", "GET", "/mobile2api/v1/mobilestackup/{planId}", "MobileStackupRequestTest", "getMobileStackup_returnsStackup", "Y", "N", "okdirect,newyork", "QC4,Stage1", "branding as planId", "Y", "N", "Y", "N", "Implemented — master regression (duplicate class in 2 packages)", "Verified automated manually executable", "cee0de9", "balancetrend + stackup packages"),
    ("M2-24", "GET", "/mobile2api/v1/mobileugift", "MobileUgiftRequestTest", "getMobileUgift_returnsUgiftPage", "Y", "N", "okdirect,newyork", "QC4,Stage1", "static", "Y", "N", "Y", "N", "Implemented — master regression", "Verified automated manually executable", "cee0de9", ""),
    ("M2-25", "PATCH", "/mobile2api/v1/mobileugift/{ext}", "MobileUgiftRequestTest", "patchMobileUgift_assignsUgiftId", "Y", "N", "okdirect,newyork", "QC4,Stage1", "static ext 01", "Y", "N", "Y", "N", "Implemented — master regression", "Verified automated manually executable", "cee0de9", ""),
]

M1_ENDPOINTS = [
    ("M1-01", "POST", "/mobile1api/v1/mobilemembersession", "Mobile1AuthenticationTest", "getValidMemberSession", "Y", "N", "okdirect,nmdirect", "QC4,Stage1", "dynamic SQL auth", "Y", "N", "Y", "N", "Implemented — auth regression", "Executed verified (historical)", "cee0de9", "Baseline verified endpoint"),
    ("M1-02", "GET", "/mobile1api/v1/mobileowner", "MobileOwnerRequestTest", "getMobileOwner_returnsOwner", "Y", "N", "okdirect,nmdirect", "QC4,Stage1", "dynamic", "Y", "N", "Y", "N", "Implemented — profileowner suites", "Implemented — execution evidence pending", "cee0de9", "QA-1313 commit"),
    ("M1-03", "GET", "/mobile1api/v1/mobileOwnerMenu", "MobileOwnerMenuRequestTest", "getMobileOwnerMenu_returnsMenu", "Y", "N", "okdirect,nmdirect", "QC4,Stage1", "dynamic", "Y", "N", "Y", "N", "Implemented — profileowner suites", "Implemented — execution evidence pending", "cee0de9", ""),
    ("M1-04", "GET", "/mobile1api/v1/mobileprofilemenu", "MobileProfileMenuRequestTest", "getMobileProfileMenu_returnsMenu", "Y", "N", "okdirect,nmdirect", "QC4,Stage1", "dynamic", "Y", "N", "Y", "N", "Implemented — profileowner suites", "Implemented — execution evidence pending", "cee0de9", ""),
    ("M1-05", "GET", "/mobile1api/v1/mobilebeneficiaryByExt/{ext}", "MobileBeneficiaryByExtRequestTest", "getBeneficiaryByExt_returnsBeneficiary", "Y", "N", "okdirect,nmdirect", "QC4,Stage1", "dynamic ext", "Y", "N", "Y", "N", "Implemented — beneficiary suites", "Implemented — execution evidence pending", "cee0de9", ""),
    ("M1-06", "GET", "/mobile1api/v1/mobilebankinfobyroutingnum/{routingNum}", "MobileBankInfoByRoutingNumRequestTest", "getBankInfoByRoutingNum_returnsBank", "Y", "N", "okdirect,nmdirect", "QC4,Stage1", "static routing", "Y", "N", "Y", "N", "Implemented — bankinfo suites", "Implemented — execution evidence pending", "cee0de9", ""),
]

M2_HEADER = [
    "endpoint_id", "http_method", "path", "test_class", "test_method", "positive_test", "negative_test",
    "branding_support", "environment_support", "test_data", "module_regression", "smoke_suite",
    "master_regression", "deployment_validation", "execution_model", "implementation_status",
    "evidence_commit", "notes",
]

M1_HEADER = M2_HEADER


def write_csv(path: Path, header: list[str], rows: list[list]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


def count_m2_implemented() -> tuple[int, int, str]:
    """Return numerator, denominator, formula note for business automation (sign-off rules)."""
    denom = 25
    # Business numerator: endpoints with L3+ automation excluding mobilemembers (M2-20)
    numer = sum(1 for e in M2_ENDPOINTS if e[0] != "M2-20" and "Implemented" in e[14])
    return numer, denom, f"{numer}/{denom}"


def main() -> None:
    write_csv(ROOT / "01-inventory" / "mobile2-endpoint-current-state.csv", M2_HEADER, list(M2_ENDPOINTS))
    write_csv(ROOT / "01-inventory" / "mobile1-endpoint-current-state.csv", M1_HEADER, list(M1_ENDPOINTS))

    m2_num, m2_den, m2_formula = count_m2_implemented()
    m2_pct = round(100.0 * m2_num / m2_den, 1)

    metrics = [
        ["M-M2-IMPL", "Unite MSC", "Implemented automation", "Mobile 2 business endpoint automation (code)", str(m2_num), str(m2_den), f"{m2_pct}%", "business endpoints", m2_formula, VALIDATION_TS, API_COMMIT, f"{API_REPO}/mobile/mobile2", "Verified", "High", "Yes", "Excludes mobilemembers from numerator; destructive ops counted as implemented"],
        ["M-M2-EXEC", "Unite MSC", "Executed coverage", "Mobile 2 last documented master run", "22", "25", "88.0%", "business endpoints", "22/25", "2026-07-14", "7ccaf46", "17-mobile2-api-automation-signoff.md", "Stale", "Medium", "Conditional", "Superseded for implementation; execution refresh pending"],
        ["M-M2-CI", "Unite MSC", "CI integration", "Mobile 2 GitLab scheduled job", "0", "1", "0%", "scheduled jobs", "0/1", VALIDATION_TS, API_COMMIT, ".gitlab-ci.yml", "Verified gap", "High", "Yes", "QA-1405"],
        ["M-M1-IMPL", "Unite MSC", "Implemented automation", "Mobile 1 endpoint automation (code)", "6", "27", "22.2%", "business endpoints", "6/27", VALIDATION_TS, API_COMMIT, "mobile/mobile1", "Verified", "High", "Yes", "Current code replaces 1/27 historical baseline for implementation"],
        ["M-M1-EXEC", "Unite MSC", "Executed coverage", "Mobile 1 execution-verified endpoints", "1", "27", "3.7%", "business endpoints", "1/27", "2026-07-09", "baseline", "03-document-postman-coverage-matrix.md", "Verified", "High", "Yes", "Session/auth only until fresh runs"],
        ["M-M1-CI", "Unite MSC", "CI integration", "Mobile 1 GitLab scheduled job", "0", "1", "0%", "scheduled jobs", "0/1", VALIDATION_TS, API_COMMIT, ".gitlab-ci.yml", "Verified gap", "High", "Yes", ""],
        ["M-V3-UI", "Universal Platform", "Inventory share", "V3 scoped TestNG nightly share", "379", "436", "86.9%", "TestNG methods", "379/436", "2026-07-01", "SME", "universal-platform-coverage", "Verified", "High", "Yes", "Not requirement coverage"],
        ["M-V2-UI", "Universal Platform", "Inventory share", "V2 UP-scoped qTest share", "268", "744", "36.0%", "qTest cases", "268/744", "2026-06-29", "qTest PDF", "universal-platform-coverage", "Stale", "High", "Yes", ""],
        ["M-V3-CI", "Universal Platform", "Scheduled regression", "V3 GitLab scheduled job", "1", "1", "100%", "scheduled job", "1/1", VALIDATION_TS, PRIME_COMMIT, "prime-test-automation/.gitlab-ci.yml", "Verified", "High", "Yes", "Hard-fail on run; not MR gate"],
        ["M-META-CI", "Universal Platform", "Scheduled regression", "Metadataweb API GitLab job", "1", "1", "100%", "scheduled job", "1/1", VALIDATION_TS, API_COMMIT, "api-test-automation/.gitlab-ci.yml", "Verified", "High", "Yes", ""],
        ["M-GHA-M2", "Unite MSC", "Deployment validation", "GHA Dashboard vertical slice", "1", "1", "100%", "validated slice", "1/1", "2026-07", "external", "17-MOBILE2-NEXUS-GITHUB-ACTIONS-PIPELINE.md", "Verified external", "Medium", "Yes", "Workflow repo not in clone"],
    ]
    mheader = ["metric_id", "gs_domain", "metric_type", "label", "numerator", "denominator", "formula", "unit", "counting_unit", "as_of_date", "commit_or_build", "evidence_path", "verification_status", "confidence", "leadership_safe", "notes"]
    write_csv(ROOT / "03-analysis" / "verified-metrics-register.csv", mheader, metrics)

    # implemented vs executed register
    ier = [
        ["M2", "Implemented automation", m2_num, m2_den, f"{m2_pct}%", API_COMMIT, "Code + suite XML", "Verified"],
        ["M2", "Executed (last sign-off)", 22, 25, "88.0%", "7ccaf46", "Sign-off package", "Stale"],
        ["M2", "Master regression scope", 20, 25, "80.0%", API_COMMIT, "Stable endpoints in master; destructive excluded", "Verified"],
        ["M1", "Implemented automation", 6, 27, "22.2%", API_COMMIT, "6 test classes on main", "Verified"],
        ["M1", "Executed verified", 1, 27, "3.7%", "baseline", "Auth session historical", "Verified"],
        ["M1", "Scheduled CI", 0, 27, "0%", API_COMMIT, "No GitLab job", "Verified"],
    ]
    write_csv(ROOT / "03-analysis" / "implemented-vs-executed-register.csv", ["platform", "metric_layer", "numerator", "denominator", "result", "commit", "evidence", "status"], ier)

    # suite placement
    suite_rows = []
    for e in M2_ENDPOINTS:
        placement = []
        if e[10] == "Y": placement.append("module_regression")
        if e[11] == "Y": placement.append("smoke")
        if e[12] == "Y": placement.append("master_regression")
        suite_rows.append([e[0], e[2], e[3], ",".join(placement) or "targeted_only", e[14]])
    write_csv(ROOT / "03-analysis" / "suite-placement-register.csv", ["endpoint_id", "path", "test_class", "suite_placement", "execution_model"], suite_rows)

    # live validation register
    live = [
        ["LV-001", "api-test-automation", API_COMMIT, "mobile/mobile2", "25 endpoints inventoried", "Verified", VALIDATION_TS],
        ["LV-002", "api-test-automation", API_COMMIT, "mobile/mobile1", "6 endpoints implemented", "Verified", VALIDATION_TS],
        ["LV-003", "GitLab API", "N/A", "pipelines", "401 expired token", "Blocked", VALIDATION_TS],
        ["LV-004", "prime-test-automation", PRIME_COMMIT, ".gitlab-ci.yml", "scheduled_regression_job present", "Verified", VALIDATION_TS],
        ["LV-005", "Jira MCP", "N/A", "user-jira", "Discovery error", "Blocked", VALIDATION_TS],
        ["LV-006", "qTest REST", "N/A", "env", "QTEST_* not set", "Blocked", VALIDATION_TS],
    ]
    write_csv(ROOT / "00-review" / "live-validation-register.csv", ["id", "system", "commit_or_ref", "path", "finding", "status", "timestamp"], live)

    pipeline = [
        ["GitLab", "scheduled_regression_job", "prime-test-automation", "schedules", "Unknown live", "Stage1", "mvn test UE+Unite", "stage1-ue-regression-test; stage1-unite-regression-master", "V3 UI", "JUnit", "always", "N", "exit 1", "scheduled regression hard-fail", "None verified", "Unknown", "Unknown", "YAML verified", VALIDATION_TS],
        ["GitLab", "scheduled_metadataweb_stage1", "api-test-automation", "schedules", "Unknown live", "Stage1", "mvn test metadataweb", "stage1-api-metadata-pipeline", "metadata API", "JUnit", "always", "N", "maven fail", "scheduled regression hard-fail", "None verified", "Unknown", "Unknown", "YAML verified", VALIDATION_TS],
        ["GitLab", "stage5_smoke_job", "prime-test-automation", "manual", "Manual", "Stage5", "smoke profiles", "stage5-*-smoke-test", "V3 smoke", "JUnit", "always", "N", "exit 1", "manual smoke", "Deployment prep", "On demand", "Unknown", "manual", VALIDATION_TS],
        ["GitLab", "Mobile2 nightly", "api-test-automation", "N/A", "Not configured", "QC4/Stage1", "planned mvn mobile2 master", "mobile-ms-master-regression", "Mobile 2 API", "Surefire", "N/A", "N/A", "N/A", "none", "N/A", "N/A", "N/A", "Absent in YAML", VALIDATION_TS],
        ["GitHub Actions", "Mobile2 Dashboard slice", "external repo", "deploy trigger", "Unknown live", "QC4", "Nexus consume + dashboard profile", "mobile-ms-dashboard-integration", "Mobile 2 deploy validation", "HTML report", "Unknown", "Unknown", "workflow fail", "deployment validation", "Deploy path", "Unknown", "Unknown", "Doc + leadership validation", VALIDATION_TS],
        ["Jenkins", "AGSUP_IDP_REGRESSION_SUITE", "performance-test-automation", "cron weekdays", "Inferred", "load servers", "Taurus", "IDP perf", "UP perf", "perf metrics", "Unknown", "Unknown", "Unknown", "scheduled perf", "None", "Stale doc", "Unknown", "KB tracker", VALIDATION_TS],
        ["Jenkins", "V2 UI regression", "unite-test-automation", "Unknown", "Unknown", "Stage1", "Ant targets", "regression-*-daily", "V2 UI", "TestNG HTML", "Unknown", "Unknown", "Unknown", "unknown", "Unknown", "Unknown", "Unknown", "Not verified live", VALIDATION_TS],
    ]
    write_csv(ROOT / "00-review" / "pipeline-live-validation.csv", ["platform", "job_name", "repository", "trigger", "schedule_live", "environment", "command", "profile", "scope", "artifacts", "retention", "allow_failure", "failure_behavior", "gate_classification", "deployment_relation", "latest_run", "latest_result", "evidence", "validated_at"], pipeline)

    print(f"Mobile 2 implemented automation: {m2_formula} = {m2_pct}%")
    print(f"Mobile 1 implemented automation: 6/27 = 22.2%")
    print(f"Wrote artifacts under {ROOT}")


if __name__ == "__main__":
    main()
