-- ============================================================================
-- Query: get-banks-by-member
-- Feature: mobilebank, mobiledashboard (on-prem overlap)
-- BFF Endpoint: GET /mobile2api/v1/mobilebanks
-- Downstream API: GET bankapi/v1/banks
-- Source repo: C:\Workspace\GitLab\MobileAutomation\UniteMSC\unite-bank\
-- Source file: src/main/resources/com/cs529/bank/repository/BankTableDao.xml
-- Source method: findByMemberId
-- DB tables: tu_bank, tu_bnk_instruction, tu_acct
-- Parameters: :memberId
-- Returns: bank list for member accounts
-- Notes: explicit XML; dashboard mobileBanks often from on-prem — use for mobilebank feature
-- ============================================================================

SELECT
    b.seq_bnk_id        AS seq_bnk_id,
    b.bank_name         AS bank_name,
    b.routing_num       AS routing_num,
    b.acct_num          AS acct_num,
    b.status            AS status,
    a.uii_acct_id       AS prefix,
    a.uii_acct_ext      AS ext
FROM tu_bank b
JOIN tu_bnk_instruction bi ON bi.seq_bnk_id = b.seq_bnk_id
JOIN tu_acct a ON a.seq_acct_id = bi.seq_acct_id
WHERE a.uii_member_id = :memberId
  AND b.ctl_rec_stat = 'A'
  AND a.ctl_rec_stat = 'A';
