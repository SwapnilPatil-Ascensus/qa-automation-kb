-- ============================================================================
-- Query: get-bene-ssn-by-acct
-- Feature: mobiledashboard (bene SSN fields on account when exposed)
-- BFF Endpoint: GET /mobile2api/v1/mobiledashboard
-- Downstream API: GET accountapi/v1/accounts
-- Source repo: C:\Workspace\GitLab\MobileAutomation\UniteMSC\unite-account\
-- Source file: src/main/resources/com/cs529/account/repository/AccountTableDao.xml
-- Source method: getBeneSsnByAcctIdAndExt
-- DB tables: tu_acct, tu_bene
-- Parameters: :uiiAcctId (prefix only in query — ext in result)
-- Returns: beneSsnE, beneSsnCi
-- Notes: explicit XML query; encrypted SSN fields — compare only if scenario asserts
-- ============================================================================

SELECT
    b.ssn_e             AS bene_ssn_e,
    b.ssn_ci            AS bene_ssn_ci,
    a.uii_acct_ext      AS uii_acct_ext,
    a.ctl_ins_dttm      AS bene_acct_ctl_ins_dttm
FROM tu_bene b
JOIN tu_acct a ON b.seq_bene_id = a.seq_bene_id
WHERE a.uii_acct_id = :uiiAcctId
  AND a.ctl_rec_stat = 'A'
  AND b.ctl_rec_stat = 'A';
