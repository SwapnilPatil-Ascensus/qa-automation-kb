-- ============================================================================
-- Query: get-bank-instructions-by-ext
-- Feature: mobilebank, mobilecontribution
-- BFF Endpoint: GET /mobile2api/v1/mobilebanks/{id}
-- Downstream API: GET bankapi/v1/bankinstructions/{ext}
-- Source repo: C:\Workspace\GitLab\MobileAutomation\UniteMSC\unite-bank\
-- Source file: src/main/resources/com/cs529/bank/repository/BankInstructionTableDao.xml
-- Source method: findByAccountExt / recurring instruction queries
-- DB tables: tu_bnk_instruction, tu_acct, tu_bank
-- Parameters: :ext, :memberId
-- Returns: bank instruction rows for account extension
-- Notes: explicit XML
-- ============================================================================

SELECT
    bi.seq_pay_id       AS seq_pay_id,
    bi.seq_acct_id      AS seq_acct_id,
    bi.seq_bnk_id       AS seq_bnk_id,
    bi.status           AS status,
    a.uii_acct_ext      AS ext
FROM tu_bnk_instruction bi
JOIN tu_acct a ON a.seq_acct_id = bi.seq_acct_id
WHERE a.uii_acct_ext = :ext
  AND a.uii_member_id = :memberId
  AND a.ctl_rec_stat = 'A';
