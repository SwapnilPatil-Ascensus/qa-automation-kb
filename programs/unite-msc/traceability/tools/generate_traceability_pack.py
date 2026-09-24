#!/usr/bin/env python3
"""QA-1942 — legacy-to-canonical traceability pack (CSV + MD + Word)."""

from __future__ import annotations

from datetime import date
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "deliverables"
SIGNOFF_DATE = date.today().strftime("%B %d, %Y")
NAVY = RGBColor(0x00, 0x30, 0x57)
TEAL = RGBColor(0x00, 0x7A, 0x8C)
GREEN = RGBColor(0x2E, 0x7D, 0x32)
GRAY = RGBColor(0x61, 0x61, 0x61)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_BG = "E8EEF4"
GREEN_BG = "E8F5E9"
AMBER_BG = "FFF3E0"
RED_BG = "FFEBEE"

CSV_HEADERS = [
    "module",
    "endpoint_id",
    "method",
    "path",
    "delta",
    "legacy_cucumber",
    "postman_collection",
    "postman_request",
    "bruno_request",
    "java_class",
    "java_method",
    "suite",
    "plants",
    "improvements",
    "notes",
]

# delta: unchanged | improved | newly_added | excluded | missing
# bruno: always — (none in api-test-automation as of 2026-09-15)
ROWS = [
    # Mobile 1 — Dinesh GS inventory had 6 rows; canonical has 26
    ("Mobile 1", "M1-01", "POST", "/mobile1api/v1/mobilemembersession", "improved",
     "mobilemembersession.feature", "Mobile1", "Login (mobilemembersession)", "—",
     "Mobile1AuthenticationTest", "getValidMemberSession", "integration+regression", "okdirect,nmdirect",
     "multi_plan;assertions", "Auth foundation; OKD + NMD legs"),
    ("Mobile 1", "M1-02", "GET", "/mobile1api/v1/mobilememberusername", "newly_added",
     "— (not in Cucumber inventory)", "Mobile1", "GET mobilememberusername", "—",
     "MobileMemberUsernameGetRequestTest", "getMobileMemberUsername_returnsUsername", "auth-regression", "okdirect",
     "data_creation", "Not in Dinesh 6-row GS inventory"),
    ("Mobile 1", "M1-03", "GET", "/mobile1api/v1/mobileowner", "improved",
     "mobileowner.feature", "Mobile1", "GET mobileowner", "—",
     "MobileOwnerRequestTest", "getMobileOwner_returnsOwner", "profileowner-*", "okdirect,nmdirect",
     "multi_plan;assertions", "POJO assertions vs Cucumber"),
    ("Mobile 1", "M1-04", "GET", "/mobile1api/v1/mobileOwnerMenu", "improved",
     "mobileownermenu.feature", "Mobile1", "GET mobileOwnerMenu", "—",
     "MobileOwnerMenuRequestTest", "getMobileOwnerMenu_returnsOwnerMenu", "profileowner-*", "okdirect,nmdirect",
     "multi_plan;assertions", ""),
    ("Mobile 1", "M1-05", "GET", "/mobile1api/v1/mobileprofilemenu", "improved",
     "mobileprofilemenu.feature", "Mobile1", "GET mobileprofilemenu", "—",
     "MobileProfileMenuRequestTest", "getMobileProfileMenu_returnsProfileMenu", "profileowner-*", "okdirect,nmdirect",
     "multi_plan;assertions", ""),
    ("Mobile 1", "M1-06", "PUT", "/mobile1api/v1/mobileowner", "improved",
     "mobileowner.feature", "Mobile1", "PUT mobileowner", "—",
     "MobileOwnerPutRequestTest", "putMobileOwner_updatesOwnerProfile_returnsOk", "mobile1-smoke", "okdirect",
     "assertions", "Postman folder ran this; Java smoke only (mutating)"),
    ("Mobile 1", "M1-07", "GET", "/mobile1api/v1/mobilebeneficiaryByExt/{ext}", "improved",
     "mobilebeneficiary.feature", "Mobile1", "GET mobilebeneficiaryByExt/{ext}", "—",
     "MobileBeneficiaryByExtRequestTest", "getMobileBeneficiaryByExt_returnsBeneficiary", "beneficiary-*", "okdirect",
     "data_creation;assertions", "Dynamic ext"),
    ("Mobile 1", "M1-08", "POST", "/mobile1api/v1/mobilecloseaccount/{ext}", "improved",
     "mobilecloseaccount.feature", "Mobile1", "POST mobilecloseaccount/{ext} (preClosureCheck)", "—",
     "MobileCloseAccountPostRequestTest", "postMobileCloseAccount_preClosureCheck", "beneficiary-regression", "okdirect",
     "assertions", "preClosureCheck=true"),
    ("Mobile 1", "M1-09", "POST", "/mobile1api/v1/mobilecloseaccount/{ext}", "newly_added",
     "mobilecloseaccount.feature (actual close)", "Mobile1", "— (not a happy-path Postman run)", "—",
     "MobileActualCloseAccountPostRequestTest", "postMobileActualCloseAccount_closesAccount", "mobile1-smoke", "nmdirect",
     "assertions", "Destructive smoke — NMD only"),
    ("Mobile 1", "M1-10", "GET", "/mobile1api/v1/mobilebankinfobyroutingnum/{routingNum}", "unchanged",
     "mobilebankinfo.feature", "Mobile1", "GET mobilebankinfobyroutingnum/{routingNum}", "—",
     "MobileBankInfoByRoutingNumRequestTest", "getMobileBankInfoByRoutingNum_returnsBankInfo", "bankinfo-*", "okdirect",
     "none", "Aligned with M2 routing 011000138"),
    ("Mobile 1", "M1-11", "POST", "/mobile1api/v1/mobilememberbiometric", "improved",
     "mobilememberbiometric.feature", "Mobile1", "POST mobilememberbiometric", "—",
     "MobileMemberBiometricPostRequestTest", "postMobileMemberBiometric_enrollsToken", "memberbiometric-*", "okdirect",
     "assertions", ""),
    ("Mobile 1", "M1-12", "GET", "/mobile1api/v1/mobilememberbiometric", "improved",
     "mobilememberbiometric.feature", "Mobile1", "GET mobilememberbiometric (biometric-only)", "—",
     "MobileMemberBiometricGetRequestTest", "getMobileMemberBiometric_returnsBiometricToken", "memberbiometric-*", "okdirect",
     "assertions", ""),
    ("Mobile 1", "M1-13", "DELETE", "/mobile1api/v1/mobilememberbiometric", "improved",
     "mobilememberbiometric.feature", "Mobile1", "DELETE mobilememberbiometric (skipped in Postman)", "—",
     "MobileMemberBiometricDeleteRequestTest", "deleteMobileMemberBiometric_removesBiometricToken", "mobile1-smoke", "okdirect",
     "assertions", "Postman marked skipped; Java smoke runs it"),
    ("Mobile 1", "M1-14", "POST", "/mobile1api/v1/requestPhoneNumberAuthentication", "unchanged",
     "mobilerequestPhoneNumberAuthentication.feature", "Mobile1", "POST requestPhoneNumberAuthentication", "—",
     "MobileRequestPhoneNumberAuthenticationPostRequestTest", "postRequestPhoneNumberAuthentication_returnsOwnerPhoneDetails",
     "phoneauthentication-*", "okdirect", "none", "May trigger SMS outside QC4"),
    ("Mobile 1", "M1-15", "POST", "/mobile1api/v1/mobilememberdevices", "improved",
     "— (device steps in push/device services)", "Mobile1", "POST mobilememberdevices/{deviceUuid}", "—",
     "MobileMemberDeviceRequestTest", "postMobileMemberDevice_registersDevice", "memberdevice-*", "okdirect",
     "data_creation;assertions", "Postman path includes deviceUuid; Java uses framework device helper"),
    ("Mobile 1", "M1-16", "POST", "/mobile1api/v1/mobilememberpushnotificationtokens", "improved",
     "mobilememberpushnotificationtoken.feature", "Mobile1", "POST mobilememberpushnotificationtokens", "—",
     "MobileMemberDeviceRequestTest", "postMobileMemberPushNotificationToken_registersToken", "memberdevice-*", "okdirect",
     "assertions", ""),
    ("Mobile 1", "M1-17", "PUT", "/mobile1api/v1/mobilememberpushnotificationtokens", "improved",
     "mobilememberpushnotificationtoken.feature", "Mobile1", "PUT mobilememberpushnotificationtokens", "—",
     "MobileMemberDeviceRequestTest", "putMobileMemberPushNotificationToken_updatesToken", "memberdevice-*", "okdirect",
     "assertions", ""),
    ("Mobile 1", "M1-18", "GET", "/mobile1api/v1/mobilememberpushnotificationtokens/deviceuuid/{deviceUuid}", "improved",
     "mobilememberpushnotificationtoken.feature", "Mobile1", "GET mobilememberpushnotificationtokens/deviceuuid/{uuid}", "—",
     "MobileMemberDeviceRequestTest", "getMobileMemberPushNotificationToken_returnsRegisteredToken", "memberdevice-*", "okdirect",
     "data_creation", ""),
    ("Mobile 1", "M1-19", "GET", "/mobile1api/v1/mobilememberdevices", "improved",
     "—", "Mobile1", "GET mobilememberdevices/{deviceUuid}", "—",
     "MobileMemberDeviceRequestTest", "getMobileMemberDevice_returnsRegisteredDevice", "memberdevice-*", "okdirect",
     "assertions", ""),
    ("Mobile 1", "M1-20", "PATCH", "/mobile1api/v1/mobilemembers", "improved",
     "mobileMember.feature", "Mobile1", "PATCH mobilemembers (password-change - skipped)", "—",
     "MobileChangePasswordRequestTest", "patchMobileMembers_changesPasswordAndRelogin", "mobile1-smoke", "okdirect",
     "data_creation;assertions", "Postman skipped; Java smoke + re-login"),
    ("Mobile 1", "M1-21", "POST", "/mobile1api/v1/mobilecsrasmembersession", "improved",
     "mobilecsrasmembersession.feature", "Mobile1", "POST mobilecsrasmembersession (csr-only)", "—",
     "MobileCsrAsMemberSessionRequestTest", "postMobileCsrAsMemberSession_returnsSession", "csrasmember-*", "okdirect",
     "assertions", "Public endpoint; INVALID_CREDENTIALS without real CSR token"),
    ("Mobile 1", "M1-22", "POST", "/mobile1api/v1/idptokenexchange", "newly_added",
     "— (legacy Cucumber had no IDP feature)", "Mobile1", "IDP Token Exchange", "—",
     "MobileIdpTokenExchangeRequestTest", "postIdpTokenExchange_returnsAccessToken", "memberidptoken-*", "nmdirect",
     "idp;multi_plan", "PKCE → IDP token; not in Dinesh 6-row list"),
    ("Mobile 1", "M1-23", "POST", "/mobile1api/v1/mobilememberidptoken", "newly_added",
     "—", "Mobile1", "POST mobilememberidptoken (idp-login-only / not run)", "—",
     "MobileMemberIdpTokenRequestTest", "postMobileMemberIdpToken_returnsMemberSession", "memberidptoken-*", "nmdirect",
     "idp", "Java automated; Postman folder was Not Run; QC4 often 401 on automation JWT"),
    ("Mobile 1", "M1-24", "GET", "/mobile1api/v1/mobilemembersession/{id}", "newly_added",
     "mobilemembersession.feature (partial)", "Mobile1", "GET mobilemembersession/{id}", "—",
     "MobileMemberSessionByIdRequestTest", "getMobileMemberSessionById_returnsSession", "membersession-smoke", "okdirect",
     "assertions", "Not in Dinesh 6-row list"),
    ("Mobile 1", "M1-25", "POST", "/mobile1api/v1/mobilemembersession/validateBiometricToken", "improved",
     "mobilememberbiometric.feature", "Mobile1", "POST validateBiometricToken (Not Run folder)", "—",
     "MobileMemberSessionValidateBiometricTokenRequestTest", "postValidateBiometricToken_returnsMemberSession",
     "membersession-smoke", "okdirect", "assertions", "Postman not run; Java smoke"),
    ("Mobile 1", "M1-26", "POST", "/mobile1api/v1/mobilemembersessionpin", "newly_added",
     "— (no GET in legacy API)", "Mobile1", "POST mobilemembersessionpin", "—",
     "MobileMemberSessionPinRequestTest", "postMobileMemberSessionPin_returnsSessionPin", "membersessionpin-*", "okdirect",
     "assertions", "1-factor member JWT"),
    ("Mobile 1", "OPS-M1-HEALTH", "GET", "/health/* and /coreservicehealth/* and /openapi.json", "excluded",
     "mobileCoreHealthCheck.feature", "Mobile1", "Docs & Health + Core Service Health folders", "—",
     "—", "—", "—", "—", "none", "Ops probes — not in business numerator"),
    ("Mobile 1", "GAP-M1-LOGOUT", "PATCH", "/mobile1api/v1/mobilemembersession/{id}", "missing",
     "—", "Mobile1", "PATCH mobilemembersession/{id} (logout - skipped)", "—",
     "—", "—", "—", "—", "none", "Backlog: logout PATCH not in TestNG"),
    # Mobile 2
    ("Mobile 2", "M2-01", "GET", "/mobile2api/v1/mobileactivity/{ext}", "improved",
     "mobileactivity.feature", "Mobile2", "GET mobileactivity/{ext}", "—",
     "MobileActivityRequestTest", "getMobileActivity_returnsActivitySummary", "activity-* + master", "okdirect,newyork",
     "multi_plan;assertions", "Lean L1–L4 vs Cucumber"),
    ("Mobile 2", "M2-02", "GET", "/mobile2api/v1/mobiletransactionhistory/{ext}", "improved",
     "mobileTransactionHistory.feature", "Mobile2", "GET mobiletransactionhistory/{ext}?duration&page", "—",
     "MobileTransactionHistoryRequestTest", "getMobileTransactionHistory_returnsTransactions", "transactionhistory-* + master",
     "okdirect,newyork", "multi_plan;assertions", ""),
    ("Mobile 2", "M2-03", "GET", "/mobile2api/v1/investments/{ext}", "improved",
     "investment.feature", "Mobile2", "GET investments/{ext}", "—",
     "MobileInvestmentRequestTest", "getMobileInvestments_returnsInvestments", "investment-* + master", "okdirect,newyork",
     "multi_plan;assertions", ""),
    ("Mobile 2", "M2-04", "GET", "/mobile2api/v1/mobilebanks", "improved",
     "mobilebank.feature", "Mobile2", "GET mobilebanks / filterDomesticBanks=true", "—",
     "MobileBanksRequestTest", "getMobileBanks_filterDomesticBanks_returnsBanks", "banks-* + master", "okdirect",
     "assertions", "OKD only in suites"),
    ("Mobile 2", "M2-05", "GET", "/mobile2api/v1/mobilebanks/{id}", "newly_added",
     "mobilebank.feature (partial)", "Mobile2", "GET mobilebanks/{id}", "—",
     "MobileBanksRequestTest", "getMobileBankById_returnsBank", "banks-* + master", "okdirect",
     "data_creation", "QA-1386 — not always in early Dinesh lists"),
    ("Mobile 2", "M2-06", "POST", "/mobile2api/v1/mobilebanks", "improved",
     "mobilebank.feature", "Mobile2", "POST mobilebanks", "—",
     "MobileBanksRequestTest", "postMobileBanks_addsDomesticBank_returnsBanks", "banks-* + master", "okdirect",
     "data_creation;assertions", ""),
    ("Mobile 2", "M2-07", "PUT", "/mobile2api/v1/mobilebanks", "unchanged",
     "mobilebank.feature", "Mobile2", "PUT mobilebanks", "—",
     "MobileBanksRequestTest", "putMobileBanks_updatesDomesticBank_returnsBanks", "mobile2-smoke", "okdirect",
     "none", "Destructive — excluded from master by design"),
    ("Mobile 2", "M2-08", "DELETE", "/mobile2api/v1/mobilebanks", "unchanged",
     "mobilebank.feature", "Mobile2", "DELETE mobilebanks", "—",
     "MobileBanksRequestTest", "deleteMobileBanks_deletesDomesticBank_returnsBanks", "mobile2-smoke", "okdirect",
     "none", "Destructive — excluded from master"),
    ("Mobile 2", "M2-09", "GET", "/mobile2api/v1/content", "improved",
     "contentservice.feature", "Mobile2", "GET content", "—",
     "MobileContentRequestTest", "getContent_commonSavingTips_returnsContent", "content-* + master", "okdirect,newyork",
     "multi_plan;assertions", ""),
    ("Mobile 2", "M2-10", "GET", "/mobile2api/v1/plans", "improved",
     "planselection.feature", "Mobile2", "GET plans (anonymous)", "—",
     "MobilePlansRequestTest", "getMobilePlans_returnsPlans", "plans-* + master", "okdirect,newyork",
     "multi_plan", ""),
    ("Mobile 2", "M2-11", "GET", "/mobile2api/v1/plans/{id}", "improved",
     "planselection.feature", "Mobile2", "GET plans/{id} (anonymous)", "—",
     "MobilePlansRequestTest", "getMobilePlanById_returnsPlan", "plans-* + master", "okdirect,newyork",
     "multi_plan", ""),
    ("Mobile 2", "M2-12", "GET", "/mobile2api/v1/mobilecontribution", "improved",
     "mobilecontribution.feature", "Mobile2", "GET mobilecontribution", "—",
     "MobileContributionRequestTest", "getMobileContribution_returnsContributionOptions", "contribution-* + master",
     "okdirect,newyork", "multi_plan", ""),
    ("Mobile 2", "M2-13", "GET", "/mobile2api/v1/mobilecontributioncheck", "improved",
     "mobilecontribution.feature", "Mobile2", "GET mobilecontributioncheck", "—",
     "MobileContributionCheckRequestTest", "getMobileContributionCheck_returnsShowContributionFlag", "contribution-* + master",
     "okdirect,newyork", "multi_plan", ""),
    ("Mobile 2", "M2-14", "GET", "/mobile2api/v1/mobilecontribution/{ext}/{id}", "improved",
     "mobilecontribution.feature", "Mobile2", "GET mobilecontribution/{ext}/{id}", "—",
     "MobileContributionDetailRequestTest", "getMobileContributionById_returnsRecurringContribution", "contribution-* + master",
     "okdirect,newyork", "data_creation", "Dynamic SQL fixture (Stage1 401 known)"),
    ("Mobile 2", "M2-15", "POST", "/mobile2api/v1/mobilecontribution", "improved",
     "mobilecontribution.feature", "Mobile2", "POST mobilecontribution", "—",
     "MobileContributionPostRequestTest", "postMobileContribution_createsRecurringContribution", "contribution-* + master",
     "okdirect,newyork", "data_creation;assertions", ""),
    ("Mobile 2", "M2-16", "PUT", "/mobile2api/v1/mobilecontribution/{ext}/{id}", "improved",
     "mobilecontribution.feature", "Mobile2", "PUT mobilecontribution/{ext}/{id}", "—",
     "MobileContributionPutRequestTest", "putMobileContributionById_updatesRecurringContribution", "contribution-* + master",
     "okdirect,newyork", "data_creation", "Stage1 fixture caveat"),
    ("Mobile 2", "M2-17", "DELETE", "/mobile2api/v1/mobilecontribution/{ext}/{id}", "unchanged",
     "mobilecontribution.feature", "Mobile2", "DELETE mobilecontribution/{ext}/{id}", "—",
     "MobileContributionDeleteRequestTest", "deleteMobileContributionById_removesAutomationOwnedContribution",
     "contribution-regression", "okdirect", "data_creation", "OKD module only; not master"),
    ("Mobile 2", "M2-18", "GET", "/mobile2api/v1/mobiledashboard", "improved",
     "mobiledashboard.feature", "Mobile2", "GET mobiledashboard", "—",
     "MobileDashboardRequestTest", "getMobileDashboard", "dashboard-* + master", "okdirect,newyork",
     "multi_plan;assertions", "8 Cucumber tests → 1 lean TestNG"),
    ("Mobile 2", "M2-19", "GET", "/mobile2api/v1/mobileytdsummary/{ext}", "newly_added",
     "— (not a separate early Cucumber feature)", "Mobile2", "GET mobileytdsummary/{ext}", "—",
     "MobileYtdSummaryRequestTest", "getMobileYtdSummary_returnsYtdContributionSummary", "dashboard-* + smoke + master",
     "okdirect,newyork", "multi_plan", "Added after first Dinesh cut"),
    ("Mobile 2", "M2-20", "GET", "/mobile2api/v1/mobilemembers/{planId}/{username}", "excluded",
     "e2e.feature / harness", "Mobile2", "GET mobilemembers/{planId}/{username} (acceptance role)", "—",
     "MobileMembersRequestTest", "getMobileMembers_returnsMemberForHarness", "mobile2-smoke", "okdirect",
     "none", "401 with member JWT by design — not in business 24/25"),
    ("Mobile 2", "M2-21", "GET", "/mobile2api/v1/mobilebalancetrend/{ext}", "improved",
     "mobileBalanceTrend.feature", "Mobile2", "GET mobilebalancetrend/{ext}", "—",
     "MobileBalanceTrendRequestTest", "getMobileBalanceTrend_returnsBalanceTrend", "balancetrend-* + master",
     "okdirect,newyork", "multi_plan;assertions", ""),
    ("Mobile 2", "M2-22", "GET", "/mobile2api/v1/mobileperformance/{ext}", "improved",
     "mobilePerformance.feature", "Mobile2", "GET mobileperformance/{ext}", "—",
     "MobilePerformanceRequestTest", "getMobilePerformance_returnsPerformance", "balancetrend-* + master",
     "okdirect,newyork", "multi_plan;assertions", ""),
    ("Mobile 2", "M2-23", "GET", "/mobile2api/v1/mobilestackup/{planId}", "improved",
     "mobileStackup.feature", "Mobile2", "GET mobilestackup/{planId}", "—",
     "MobileStackupRequestTest", "getMobileStackup_returnsStackup", "balancetrend-* + smoke + master",
     "okdirect,newyork,nmdirect", "multi_plan", "Duplicate class in stackup + balancetrend packages"),
    ("Mobile 2", "M2-24", "GET", "/mobile2api/v1/mobileugift", "improved",
     "mobileugift.feature", "Mobile2", "GET mobileugift", "—",
     "MobileUgiftRequestTest", "getMobileUgift_returnsUgiftPage", "ugift-* + master", "okdirect,newyork",
     "multi_plan", ""),
    ("Mobile 2", "M2-25", "PATCH", "/mobile2api/v1/mobileugift/{ext}", "improved",
     "mobileugift.feature", "Mobile2", "PATCH mobileugift/{ext}", "—",
     "MobileUgiftRequestTest", "patchMobileUgift_assignsUgiftId", "ugift-* + master", "okdirect,newyork",
     "assertions", "Idempotent assign"),
    ("Mobile 2", "OPS-M2-HEALTH", "GET/DELETE", "/mobile2api/health/* and /openapi.json", "excluded",
     "—", "Mobile2", "Docs & Health folder", "—",
     "—", "—", "—", "—", "none", "Ops probes — not in business numerator"),
    ("Mobile 2", "GAP-M2-UPROMISE-BANK", "POST", "/mobile2api/v1/mobilebanks?planId=upromise", "missing",
     "—", "Mobile2", "POST mobilebanks?planId=upromise", "—",
     "—", "—", "—", "—", "none", "Postman-only variant; Java covers domestic add"),
    # Enrollment
    ("Enrollment", "ENR-01", "GET", "/enrollmentapi/health/liveness", "newly_added",
     "— (Cucumber enrollment was limited)", "Enrollment -E2E (historical)", "liveness", "—",
     "EnrollmentPingRequestTest", "liveness", "enrollment-smoke", "okdirect", "assertions", "New in MSC TestNG"),
    ("Enrollment", "ENR-02", "GET", "/enrollmentapi/v1/ping", "improved",
     "unite-enrollment features (ping)", "Enrollment -E2E", "ping", "—",
     "EnrollmentPingRequestTest", "ping", "enrollment-smoke", "okdirect", "assertions", ""),
    ("Enrollment", "ENR-03", "GET", "/enrollmentapi/v1/certificate", "newly_added",
     "—", "Enrollment -E2E", "certificate", "—",
     "EnrollmentCertificateRequestTest", "certificate", "enrollment-smoke", "okdirect", "encryption", "Cert for AES encrypt"),
    ("Enrollment", "ENR-04", "GET", "/enrollmentapi/v1/usstates", "improved",
     "unite-metadata usstates.feature", "Enrollment -E2E", "usstates", "—",
     "EnrollmentUsStatesRequestTest", "usstates", "enrollment-smoke", "okdirect", "assertions", ""),
    ("Enrollment", "ENR-05", "GET", "/enrollmentapi/v1/country", "newly_added",
     "—", "Enrollment -E2E / Excel", "country", "—",
     "EnrollmentCountryRequestTest", "country", "enrollment-smoke", "okdirect", "assertions", ""),
    ("Enrollment", "ENR-06", "GET", "/enrollmentapi/v1/plans", "improved",
     "unite-metadata plans.feature", "Enrollment -E2E", "plans", "—",
     "EnrollmentPlansRequestTest", "plans", "enrollment-smoke", "okdirect", "assertions", ""),
    ("Enrollment", "ENR-07", "GET", "/enrollmentapi/v1/plans/{planId}", "improved",
     "unite-metadata plans.feature", "Enrollment -E2E", "plans/{id}", "—",
     "EnrollmentPlansRequestTest", "plansById", "enrollment-smoke", "okdirect", "assertions", ""),
    ("Enrollment", "ENR-08", "GET", "/enrollmentapi/v1/content", "newly_added",
     "—", "Enrollment -E2E", "content", "—",
     "EnrollmentContentRequestTest", "content", "regression+integration", "okdirect,newyork",
     "multi_plan;encryption", ""),
    ("Enrollment", "ENR-09", "POST", "/mobile1api/v1/mobilemembersession", "unchanged",
     "mobilemembersession.feature", "Enrollment -E2E / Mobile1", "optional member session", "—",
     "MobileMemberSessionRequestTest", "session", "smoke (functional)", "okdirect", "none", "Optional; not wizard"),
    ("Enrollment", "ENR-10", "POST", "/enrollmentapi/v1/enrollments/enrollmentstarted", "newly_added",
     "—", "Enrollment -E2E", "enrollmentstarted", "—",
     "EnrollmentStartedRequestTest", "enrollmentstarted", "regression+integration", "okdirect,newyork",
     "encryption;multi_plan;data_creation", ""),
    ("Enrollment", "ENR-11", "POST", "/enrollmentapi/v1/enrollments/prospects", "improved",
     "unite-account / enrollment", "Enrollment -E2E", "prospects", "—",
     "ProspectRequestTest", "prospects", "regression+integration", "okdirect,newyork",
     "encryption;multi_plan;data_creation", "QAAUTOTEST username pattern"),
    ("Enrollment", "ENR-12", "POST", "/enrollmentapi/v1/enrollments/enrollment/owner-entered", "improved",
     "unite-profile owners", "Enrollment -E2E", "owner-entered", "—",
     "OwnerEnteredTests", "owner-entered", "regression+integration", "okdirect,newyork",
     "encryption;multi_plan", ""),
    ("Enrollment", "ENR-13", "POST", "/enrollmentapi/v1/enrollments/enrollment/owner-address-entered", "newly_added",
     "unite-profile ownerAddress", "Enrollment -E2E", "owner-address-entered", "—",
     "OwnerAddressEnteredRequestTest", "owner-address-entered", "regression+integration", "okdirect,newyork",
     "encryption;multi_plan", ""),
    ("Enrollment", "ENR-14", "POST", "/enrollmentapi/v1/enrollments/enrollment/beneficiary-entered", "improved",
     "unite-profile beneficiaries", "Enrollment -E2E", "beneficiary-entered", "—",
     "BeneficiaryEnteredTests", "beneficiary-entered", "regression+integration", "okdirect,newyork",
     "encryption;multi_plan", ""),
    ("Enrollment", "ENR-15", "POST", "/enrollmentapi/v1/verify/routingnumber", "improved",
     "unite-bank bankinfo", "Enrollment -E2E", "verify/routingnumber", "—",
     "VerifyBankRoutingNumberRequestTest", "verify routing", "regression+integration", "okdirect,newyork",
     "encryption;multi_plan", ""),
    ("Enrollment", "ENR-16", "POST", "/enrollmentapi/v1/enrollments/enrollment/bank-entered", "improved",
     "unite-bank", "Enrollment -E2E", "bank-entered", "—",
     "BankEnteredRequestTests", "bank-entered", "regression+integration", "okdirect,newyork",
     "encryption;multi_plan", ""),
    ("Enrollment", "ENR-17", "POST", "/enrollmentapi/v1/enrollments/enrollment/recurring-contribution-entered", "newly_added",
     "—", "Enrollment -E2E", "recurring-contribution-entered", "—",
     "RecurringContributionEnteredRequestTest", "recurring", "regression+integration", "okdirect,newyork",
     "encryption;multi_plan", ""),
    ("Enrollment", "ENR-18", "POST", "/enrollmentapi/v1/enrollmentallocationfunds/get", "newly_added",
     "unite-metadata allocationfunds", "Enrollment -E2E / Excel", "allocation funds", "—",
     "AllocationFundRequestTest", "allocation funds", "regression+integration", "okdirect,newyork",
     "encryption;multi_plan", ""),
    ("Enrollment", "ENR-19", "POST", "/enrollmentapi/v1/enrollments/enrollment/allocations-entered", "improved",
     "unite-account", "Enrollment -E2E", "allocations-entered", "—",
     "AllocationsEnteredRequestTests", "allocations-entered", "regression+integration", "okdirect,newyork",
     "encryption;multi_plan", ""),
    ("Enrollment", "ENR-20", "POST", "/enrollmentapi/v1/enrollments/enrollment/review-confirm-entered", "newly_added",
     "—", "Enrollment -E2E", "review-confirm-entered", "—",
     "ReviewConfirmEnteredRequestTest", "review-confirm", "regression+integration", "okdirect,newyork",
     "encryption;multi_plan;data_creation", "QA-1604 — account create path"),
    ("Enrollment", "ENR-21", "GET", "/enrollmentapi/v1/subsequentenrollment/banks", "newly_added",
     "—", "Enrollment -E2E", "subsequent banks", "—",
     "SubsequentEnrollmentBanksRequestTest", "subsequent banks", "regression+integration", "okdirect,newyork",
     "encryption;multi_plan", "QA-1792"),
    ("Enrollment", "ENR-22", "POST", "/enrollmentapi/v1/enrollments/subsequentenrollment/beneficiary-entered", "newly_added",
     "—", "— (missing from original Excel catalog)", "—", "—",
     "SubsequentBeneficiaryEnteredRequestTest", "subsequent beneficiary", "regression+integration", "okdirect,newyork",
     "encryption;multi_plan", "QA-1853 — Java ahead of Excel"),
    ("Enrollment", "ENR-23", "POST", "/enrollmentapi/v1/enrollments/subsequentenrollment/bank-entered", "newly_added",
     "—", "— (missing from original Excel catalog)", "—", "—",
     "SubsequentEnrollmentBankEnteredRequestTest", "subsequent bank", "regression+integration", "okdirect,newyork",
     "encryption;multi_plan", "QA-1854"),
    ("Enrollment", "ENR-24", "POST", "/enrollmentapi/v1/enrollments/subsequentenrollment/recurring-contribution-entered", "newly_added",
     "—", "— (missing from original Excel catalog)", "—", "—",
     "SubsequentEnrollmentRecurringContributionRequestTest", "subsequent recurring", "regression+integration",
     "okdirect,newyork", "encryption;multi_plan", "QA-1855"),
    ("Enrollment", "ENR-25", "POST", "/enrollmentapi/v1/enrollments/subsequentenrollment/review-confirm-entered", "newly_added",
     "—", "Enrollment -E2E", "subsequent review-confirm", "—",
     "SubsequentEnrollmentReviewConfirmEnteredRequestTest", "subsequent review-confirm", "regression+integration",
     "okdirect,newyork", "encryption;multi_plan", "QA-1791"),
    ("Enrollment", "ENR-26", "POST", "/enrollmentapi/v1/enrollments/submit", "excluded",
     "partner", "Enrollment End Points.xlsx", "submit", "—",
     "—", "—", "—", "—", "none", "Deferred partner QA-1808"),
    ("Enrollment", "ENR-27", "GET", "/enrollmentapi/v1/upromiseaccount", "excluded",
     "partner", "Enrollment End Points.xlsx", "upromiseaccount", "—",
     "—", "—", "—", "—", "none", "Deferred partner QA-1807"),
    ("Enrollment", "ENR-28", "POST", "/enrollmentapi/v1/oauth/token", "excluded",
     "—", "Enrollment End Points.xlsx", "oauth/token", "—",
     "—", "—", "—", "—", "none", "Not MSC E2E"),
]


def shade_cell(cell, hex_color: str) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), hex_color)
    shd.set(qn("w:val"), "clear")
    tc_pr.append(shd)


def set_run_font(run, size=11, bold=False, color=None, name="Calibri"):
    run.font.size = Pt(size)
    run.bold = bold
    run.font.name = name
    if color:
        run.font.color.rgb = color


def set_cell_text(cell, text: str, bold: bool = False, color: RGBColor | None = None, size: int = 9) -> None:
    cell.text = ""
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.space_before = Pt(2)
    run = p.add_run(str(text))
    set_run_font(run, size=size, bold=bold, color=color or GRAY)


def style_header_row(row) -> None:
    for cell in row.cells:
        shade_cell(cell, "003057")
        for p in cell.paragraphs:
            for run in p.runs:
                set_run_font(run, size=9, bold=True, color=WHITE)


def setup_doc(doc: Document) -> None:
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(11)
    style.font.color.rgb = GRAY
    section = doc.sections[0]
    section.top_margin = Cm(2.2)
    section.bottom_margin = Cm(2.2)
    section.left_margin = Cm(2.4)
    section.right_margin = Cm(2.4)
    hp = section.header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r = hp.add_run("Unite MSC traceability  |  Internal  |  QA-1942")
    set_run_font(r, size=8, color=GRAY)
    fp = section.footer.paragraphs[0]
    r2 = fp.add_run(f"QA Automation AMSQUAD  ·  {SIGNOFF_DATE}  ·  No credentials")
    set_run_font(r2, size=8, color=GRAY)


def heading(doc, text, level=1):
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        run.font.color.rgb = NAVY
        run.font.name = "Calibri"


def para(doc, text, size=11, bold=False, color=None, center=False):
    p = doc.add_paragraph()
    if center:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(text)
    set_run_font(r, size=size, bold=bold, color=color or GRAY)
    return p


def callout(doc, text, bg=GREEN_BG):
    table = doc.add_table(rows=1, cols=1)
    cell = table.rows[0].cells[0]
    shade_cell(cell, bg)
    set_cell_text(cell, text, bold=True, color=NAVY, size=11)
    doc.add_paragraph()


def kv_table(doc, rows):
    t = doc.add_table(rows=len(rows), cols=2)
    t.style = "Table Grid"
    for i, (k, v) in enumerate(rows):
        shade_cell(t.rows[i].cells[0], LIGHT_BG)
        set_cell_text(t.rows[i].cells[0], k, bold=True, color=NAVY, size=10)
        set_cell_text(t.rows[i].cells[1], v, size=10)
    doc.add_paragraph()


def grid_table(doc, headers, data, delta_col=None):
    t = doc.add_table(rows=1 + len(data), cols=len(headers))
    t.style = "Table Grid"
    for i, h in enumerate(headers):
        set_cell_text(t.rows[0].cells[i], h, bold=True, color=WHITE, size=8)
    style_header_row(t.rows[0])
    for ri, row in enumerate(data, start=1):
        for ci, val in enumerate(row):
            bg = "FFFFFF"
            if delta_col is not None and ci == delta_col:
                s = str(val).lower()
                bg = {
                    "improved": GREEN_BG,
                    "newly_added": LIGHT_BG,
                    "unchanged": "FFFFFF",
                    "excluded": AMBER_BG,
                    "missing": RED_BG,
                }.get(s, "FFFFFF")
            elif ci == 0:
                bg = LIGHT_BG
            shade_cell(t.rows[ri].cells[ci], bg)
            set_cell_text(t.rows[ri].cells[ci], val, size=8, color=NAVY if ci == 0 else GRAY)
    doc.add_paragraph()


def write_csv():
    path = ROOT / "legacy-to-canonical-traceability.csv"
    lines = [",".join(CSV_HEADERS)]
    for row in ROWS:
        escaped = []
        for cell in row:
            s = str(cell).replace('"', '""')
            if "," in s or '"' in s:
                s = f'"{s}"'
            escaped.append(s)
        lines.append(",".join(escaped))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Created {path}")


def counts():
    from collections import Counter
    c = Counter(r[4] for r in ROWS)
    return c


def write_md():
    c = counts()
    path = ROOT / "legacy-to-canonical-traceability.md"
    body = f"""# Unite MSC — legacy to canonical traceability (QA-1942)

**As of:** {SIGNOFF_DATE}  
**Jira:** [QA-1942](https://ascensuscollegesavings.atlassian.net/browse/QA-1942) · Epic QA-796  
**Companion CSV:** [legacy-to-canonical-traceability.csv](./legacy-to-canonical-traceability.csv)  
**Word:** [deliverables/Unite-MSC-Legacy-to-Canonical-Traceability.docx](./deliverables/Unite-MSC-Legacy-to-Canonical-Traceability.docx)  
**Enhancement backlog:** [enhancement-backlog.md](./enhancement-backlog.md)

SharePoint: attach CSV + Word + this MD when the Enrollment/API hub story runs. Do not upload Postman environments.

## Purpose

One reviewer path from **legacy Cucumber / Dinesh Excel / Postman** to **canonical TestNG** in GitLab `api-test-automation` (`mobile/mobile1`, `mobile/mobile2`, `mobile/enrollment`).

## How this was built (code evidence)

| Source | Path |
|--------|------|
| Canonical Java | `C:\\Workspace\\GitLab\\api-test-automation\\mobile\\` |
| Legacy Cucumber | `C:\\Workspace\\GitLab\\MobileAutomation\\UniteMSC\\unite-mobile1` and `unite-mobile2` |
| Postman (KB copies) | `programs/unite-msc/mobile-1/postman/`, `mobile-2/postman/` |
| Dinesh / GS early register | `programs/government-savings-assessment/01-inventory/mobile1-endpoint-current-state.csv` (6 M1 rows) and `mobile2-endpoint-current-state.csv` (25 M2 rows) |
| Sign-off registers | `mobile-1/mappings/`, `mobile-2/mappings/`, `enrollment/coverage/` |
| Bruno | **None** in `api-test-automation` (2026-09-15) |

Improvements are tagged only where Java or suite XML shows them: `idp`, `encryption`, `data_creation`, `assertions`, `multi_plan`.

## Scorecard (this matrix)

| Delta | Rows |
|-------|------|
| improved | {c.get("improved", 0)} |
| newly_added | {c.get("newly_added", 0)} |
| unchanged | {c.get("unchanged", 0)} |
| excluded | {c.get("excluded", 0)} |
| missing (backlog) | {c.get("missing", 0)} |

**Business automation that is coded:** Mobile 1 = 26 endpoints; Mobile 2 = 24 in-scope (M2-20 harness excluded); Enrollment = 25 of 28 catalog (3 partner deferred).

## What got better vs legacy (not in old IDP/Postman “not run”)

- **IDP:** `idptokenexchange` and `mobilememberidptoken` TestNG on nmdirect. Legacy Cucumber had no IDP feature. Postman kept IDP under Not Run / idp-login-only.
- **Encryption:** Enrollment POSTs use certificate + framework encrypt (not plaintext Postman).
- **Data creation:** QAAUTOTEST enrollment usernames; contribution SQL fixtures; device/biometric helpers.
- **Assertions:** Lean L1–L4 JSON/POJO instead of heavy Cucumber (dashboard 8 scenarios → 1 TestNG).
- **Multi-plan:** M2 okdirect+newyork on master; Enrollment okdirect+newyork; M1 nmdirect on auth/IDP; stackup also nmdirect in smoke.
- **Catalog holes filled:** subsequent beneficiary/bank/recurring were **in Java** but missing from original Enrollment Excel.

## Gaps after comparison (short)

See [enhancement-backlog.md](./enhancement-backlog.md). Headline:

1. **Bruno** — zero `.bru` files. Separate conversion story.
2. **PATCH logout** (`mobilemembersession/{{id}}`) — Postman skipped; no TestNG.
3. **POST mobilebanks?planId=upromise** — Postman-only; Java covers domestic add.
4. **Enrollment nmdirect in CI** — localhost example only.
5. **Enrollment GitLab nightly** — not wired (Mobile 2 nightly exists).
6. **L5 SQL field compare** — analysis only ([QA-1054](https://ascensuscollegesavings.atlassian.net/browse/QA-1054)); leadership L1–L4 bar.
7. **Partner APIs** — submit, Upromise, OAuth (QA-1808 / QA-1807).
8. **qTest / Jira links** — not this matrix (next-sprint story).

Health, OpenAPI, and M2 harness GET `mobilemembers/{{planId}}/{{username}}` are **excluded**, not missing product coverage.

## How to trace (reviewer)

1. Pick `endpoint_id` in the CSV.
2. Open `java_class` under `api-test-automation/mobile/...`.
3. Confirm `suite` XML in `testsuites/`.
4. Confirm Postman request name in the KB collection (or note Java-only subsequent enrollment).
5. Bruno column is `—` until that project lands.
"""
    path.write_text(body, encoding="utf-8")
    print(f"Created {path}")


def write_backlog_md():
    path = ROOT / "enhancement-backlog.md"
    path.write_text(
        f"""# Unite MSC — enhancement / gap backlog (from QA-1942)

**Audience:** receiving automation team  
**As of:** {SIGNOFF_DATE}  
**Parent:** [QA-1942](https://ascensuscollegesavings.atlassian.net/browse/QA-1942)

These are **not** coding defects in the migrated happy path. They are the next-layer items after L1–L4 sign-off.

| ID | Item | Why it showed up | Suggested next story |
|----|------|------------------|----------------------|
| E-01 | Bruno collections | AC asked for Bruno map; repo has no `.bru` | Convert Postman (secrets stripped) |
| E-02 | PATCH logout session | Postman “Not Run”; no TestNG | Optional smoke if product wants logout coverage |
| E-03 | POST banks `planId=upromise` | Extra Postman query variant | Only if Upromise bank add is in-scope |
| E-04 | Enrollment nmdirect on CI XML | Localhost example only | After IDP/QC4 nmdirect is stable |
| E-05 | Enrollment GitLab nightly | Mobile 2 has nightly; Enrollment does not | Copy QA-1405 pattern |
| E-06 | L5 SQL API–DB asserts | QA-1054; Rajib/Henry L1–L4 only | Use `mobile-2/sql-field-validation/` if leadership reopens |
| E-07 | Partner submit / Upromise / OAuth | Excel catalog deferred | QA-1808 / QA-1807 |
| E-08 | Negatives / contract dump | Lean assertions by design | Receiving-team enhancement |
| E-09 | Deduplicate `MobileStackupRequestTest` packages | Two Java packages | Cleanup MR |
| E-10 | qTest manual cases + Jira links | Traceability to test management | Next sprint story already drafted |
| E-11 | SharePoint publish of this pack | Docs live in Git today | Ride Enrollment SharePoint story |
| E-12 | IDP QC4 401 on automation JWT | Java exists; env still flakes | Env/DevOps, not missing class |

Do **not** treat ops health/OpenAPI or M2 harness `GET mobilemembers/{{planId}}/{{username}}` as enhancement of business APIs.
""",
        encoding="utf-8",
    )
    print(f"Created {path}")


def write_docx():
    c = counts()
    doc = Document()
    setup_doc(doc)
    for _ in range(2):
        doc.add_paragraph()
    para(doc, "UNITE MSC", size=14, bold=True, color=TEAL, center=True)
    para(doc, "Legacy-to-canonical traceability", size=26, bold=True, color=NAVY, center=True)
    para(doc, "Postman · Cucumber · Dinesh Excel · TestNG", size=14, color=TEAL, center=True)
    para(doc, "QA-1942  ·  PACKAGE COMPLETE", size=16, bold=True, color=GREEN, center=True)
    para(doc, f"{SIGNOFF_DATE}  ·  QA Automation (AMSQUAD)", size=11, color=GRAY, center=True)
    doc.add_page_break()

    heading(doc, "1. Purpose")
    para(
        doc,
        "Single traceability pack so a reviewer can go from a legacy Cucumber feature, Dinesh endpoint row, or Postman request to the canonical TestNG class, method, and suite. Bruno is listed as not present. SharePoint publish is a later story — keep these files in Git until then.",
    )
    heading(doc, "2. What we compared")
    kv_table(
        doc,
        [
            ("Canonical code", "api-test-automation/mobile/{mobile1,mobile2,enrollment}"),
            ("Legacy Cucumber", "UniteMSC unite-mobile1 / unite-mobile2 features"),
            ("Postman", "KB copies Mobile1 + Mobile2 collections (33 + 34 requests)"),
            ("Dinesh / GS cut", "GS inventory: 6 Mobile 1 rows, 25 Mobile 2 rows"),
            ("Current registers", "26 M1 + 25 M2 rows + 28 Enrollment catalog"),
            ("Bruno", "None in the automation repo"),
        ],
    )
    heading(doc, "3. Scorecard")
    grid_table(
        doc,
        ["Delta", "Meaning", "Rows"],
        [
            ["improved", "Same API; better plants, encrypt, data, or assertions", str(c.get("improved", 0))],
            ["newly_added", "Not in early Dinesh/Cucumber/Excel cut", str(c.get("newly_added", 0))],
            ["unchanged", "Parity with legacy/Postman, no extra capability claimed", str(c.get("unchanged", 0))],
            ["excluded", "Ops, harness, or deferred partner — not a miss", str(c.get("excluded", 0))],
            ["missing", "Unmapped → enhancement backlog", str(c.get("missing", 0))],
        ],
        delta_col=0,
    )
    callout(
        doc,
        "Coded business APIs: Mobile 1 = 26. Mobile 2 = 24 in-scope (harness excluded). Enrollment = 25/28 (3 partner deferred).",
        GREEN_BG,
    )
    heading(doc, "4. Improvements vs legacy (code-backed)")
    grid_table(
        doc,
        ["Theme", "Evidence"],
        [
            ["IDP", "M1-22 idptokenexchange and M1-23 mobilememberidptoken on nmdirect. No Cucumber IDP feature. Postman IDP was Not Run."],
            ["Encryption", "Enrollment certificate + encrypted POSTs in TestNG."],
            ["Data creation", "QAAUTOTEST enrollment users; contribution SQL fixture; device/biometric helpers."],
            ["Assertions", "Lean L1–L4. Dashboard: many Cucumber scenarios → one TestNG."],
            ["Multi-plan", "M2 + Enrollment okdirect and newyork. M1 IDP/auth nmdirect. Stackup smoke includes nmdirect."],
            ["Excel holes", "Subsequent beneficiary / bank / recurring coded in Java; original Enrollment Excel omitted them."],
        ],
    )
    heading(doc, "5. Gaps after comparison")
    para(doc, "Full list: enhancement-backlog.md. Headline for leadership:")
    grid_table(
        doc,
        ["Gap", "Disposition"],
        [
            ["Bruno", "Missing — convert later"],
            ["PATCH logout session", "Missing TestNG — optional"],
            ["POST banks planId=upromise", "Postman-only variant"],
            ["Enrollment nmdirect CI + nightly", "Follow-up stories (already drafted)"],
            ["L5 SQL field compare", "Not implemented — QA-1054 / Jul 23 L1–L4 bar"],
            ["Partner submit / Upromise / OAuth", "Excluded — QA-1808 / QA-1807"],
            ["Health / OpenAPI / M2 harness", "Excluded from business count"],
        ],
        delta_col=None,
    )
    heading(doc, "6. How to use the CSV")
    para(
        doc,
        "Open legacy-to-canonical-traceability.csv. Filter module. Columns: delta, legacy_cucumber, postman_request, bruno_request (always em dash), java_class, java_method, suite, plants, improvements. A reviewer traces endpoint → class → suite XML → optional Postman name.",
    )
    heading(doc, "7. Document control")
    kv_table(
        doc,
        [
            ("Jira", "QA-1942 (subtasks QA-2048–QA-2053)"),
            ("Epic", "QA-796"),
            ("KB folder", "programs/unite-msc/traceability/"),
            ("Regenerate", "python programs/unite-msc/traceability/tools/generate_traceability_pack.py"),
        ],
    )
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "Unite-MSC-Legacy-to-Canonical-Traceability.docx"
    doc.save(path)
    print(f"Created {path}")


def write_readme():
    path = ROOT / "README.md"
    path.write_text(
        """# QA-1942 — Legacy to canonical traceability

| File | Use |
|------|-----|
| [legacy-to-canonical-traceability.md](./legacy-to-canonical-traceability.md) | Narrative (SharePoint-friendly) |
| [legacy-to-canonical-traceability.csv](./legacy-to-canonical-traceability.csv) | Full matrix |
| [enhancement-backlog.md](./enhancement-backlog.md) | Gaps for the receiving team |
| [deliverables/Unite-MSC-Legacy-to-Canonical-Traceability.docx](./deliverables/Unite-MSC-Legacy-to-Canonical-Traceability.docx) | Word for review / later SharePoint |

```powershell
python programs/unite-msc/traceability/tools/generate_traceability_pack.py
```
""",
        encoding="utf-8",
    )


if __name__ == "__main__":
    write_csv()
    write_md()
    write_backlog_md()
    write_readme()
    write_docx()
