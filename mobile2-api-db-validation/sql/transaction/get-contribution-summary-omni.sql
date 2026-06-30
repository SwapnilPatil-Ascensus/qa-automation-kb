-- ============================================================================
-- Query: get-contribution-summary-omni
-- Feature: mobiledashboard, mobilecontribution
-- BFF Endpoint: GET /mobile2api/v1/mobileytdsummary/{ext}
-- Downstream API: GET transactionapi/v1/contributionsummary/{ext}
-- Source repo: C:\Workspace\GitLab\MobileAutomation\UniteMSC\unite-transaction\
-- Source file: StatementBalanceTableDao.xml
-- Source method: getOMNIContributionSummary
-- DB tables: tu_acct_txn, tu_txn_type
-- Parameters: :uiiAcctId, :ext, :taxYear
-- Returns: cyrcontrib
-- Notes: OMNI backend; txn_state = 'V'
-- ============================================================================

SELECT
    SUM(o.ahbr_cash * t.change_factor) AS cyrcontrib,
    o.tax_year                         AS tax_year
FROM tu_acct_txn o
JOIN tu_txn_type t ON o.seq_txn_type_id = t.seq_txn_type_id
WHERE o.uii_acct_id = :uiiAcctId
  AND o.uii_acct_ext = :ext
  AND o.tax_year >= :taxYear
  AND o.txn_state = 'V'
  AND t.display_hist = 'Y'
  AND ((t.txn_code = '114' AND t.activity_code = '001')
    OR (t.txn_code = '301' AND t.activity_code = '002' AND t.usage_code = '4')
    OR (t.txn_code = '301' AND t.activity_code = '007' AND t.usage_code = 'F'))
GROUP BY o.uii_acct_id, o.uii_acct_ext, o.tax_year;
