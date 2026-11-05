-- ============================================================================
-- Query: get-contribution-summary-jett
-- Feature: mobiledashboard (@md13 YTD), mobilecontribution
-- BFF Endpoint: GET /mobile2api/v1/mobileytdsummary/{ext}
-- Downstream API: GET transactionapi/v1/contributionsummary/{ext}
-- Source repo: C:\Workspace\GitLab\MobileAutomation\UniteMSC\unite-transaction\
-- Source file: src/main/resources/com/cs529/transaction/repository/StatementBalanceTableDao.xml
-- Source method: StatementBalanceDao.getJETTContributionSummaryByAcctId
-- DB tables: tjet_acct_txn, tjet_traunch_txn_type
-- Parameters: :seqAcctId, :taxYear (inclusive lower bound)
-- Returns: cyrcontrib (YTD contribution sum)
-- Notes: explicit XML getJETTContributionSummary; backend JETT plans
-- ============================================================================

SELECT
    SUM(t.amount * t.change_factor) AS cyrcontrib,
    t.tax_year                      AS tax_year
FROM tjet_acct_txn t
JOIN tjet_traunch_txn_type tt
  ON t.seq_tjet_txn_type_id = tt.seq_tjet_txn_type_id
 AND t.traunch_id = tt.traunch_id
WHERE t.seq_acct_id = :seqAcctId
  AND t.tax_year >= :taxYear
  AND (tt.transaction_type = 'CONTRIBUTION'
       OR (tt.transaction_type = 'ROLLOVER_IN' AND tt.transaction_sub_type IS NULL))
GROUP BY t.seq_acct_id, t.tax_year;
