-- ============================================================================
-- Query: get-balance-history
-- Feature: mobileBalanceTrend, mobilePerformance
-- BFF Endpoint: GET /mobile2api/v1/mobilebalancetrend/{ext}
-- Downstream API: GET transactionapi/v1/balancehistory/{ext}
-- Source repo: C:\Workspace\GitLab\MobileAutomation\UniteMSC\unite-transaction\
-- Source file: transaction repository XML (balance history DAOs)
-- Source method: BalanceHistoryService
-- DB tables: tu_stmt_bal (statement balance), backend-specific txn tables
-- Parameters: :seqAcctId
-- Returns: units, contrib, balance history by rm (report month)
-- Notes: Placeholder — see StatementBalanceTableDao findByAccountId
-- ============================================================================

SELECT
    sb.seq_acct_id,
    sb.rm,
    sb.fund_id,
    sb.units,
    sb.contrib,
    sb.cyrcontrib
FROM tu_stmt_bal sb
WHERE sb.seq_acct_id = :seqAcctId
  AND sb.ctl_rec_stat = 'A'
ORDER BY sb.rm DESC, sb.fund_id;
