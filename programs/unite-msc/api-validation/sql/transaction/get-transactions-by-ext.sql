-- ============================================================================
-- Query: get-transactions-by-ext
-- Feature: mobileTransactionHistory, mobileactivity
-- BFF Endpoint: GET /mobile2api/v1/mobiletransactionhistory/{ext}
-- Downstream API: GET transactionapi/v1/transactions/{ext}
-- Source repo: C:\Workspace\GitLab\MobileAutomation\UniteMSC\unite-transaction\
-- Source file: src/main/resources/com/cs529/transaction/repository/
-- Source method: TransactionService (backend-specific DAOs)
-- DB tables: tjet_acct_txn / tu_acct_txn / tenv_acct_txn (varies by plan backend)
-- Parameters: :seqAcctId or :uiiAcctId, :ext
-- Returns: transaction history columns
-- Notes: Placeholder — expand per backend when documenting transaction history feature
-- ============================================================================

-- Backend-specific: resolve seq_acct_id from tu_acct first
-- SELECT ... FROM tjet_acct_txn WHERE seq_acct_id = :seqAcctId ORDER BY trade_date DESC;

SELECT
    a.seq_acct_id,
    a.uii_acct_id,
    a.uii_acct_ext,
    a.traunch_id
FROM tu_acct a
WHERE a.uii_acct_ext = :ext
  AND a.uii_member_id = :memberId
  AND a.ctl_rec_stat = 'A';
