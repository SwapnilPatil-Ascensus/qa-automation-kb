-- ============================================================================
-- Query: get-beneficiary-by-id
-- Feature: mobiledashboard
-- BFF Endpoint: GET /mobile2api/v1/mobiledashboard
-- Downstream API: GET profileapi/v1/beneficiaries/{seqBeneId}
-- Source repo: C:\Workspace\GitLab\MobileAutomation\UniteMSC\unite-profile\
-- Source file: src/main/java/com/cs529/profile/service/BeneficiaryService.java
-- Source method: getById
-- DB tables: tu_bene
-- Parameters: :seqBeneId
-- Returns: bene name, address, dob fields on MobileAccount
-- Notes: ORM findByCriteria on BeneficiaryTable
-- ============================================================================

SELECT
    b.seq_bene_id       AS seq_bene_id,
    b.first_name        AS first_name,
    b.middle_initial    AS middle_initial,
    b.last_name         AS last_name,
    b.suffix            AS suffix,
    b.dob               AS dob,
    b.ml_addline1       AS ml_addline1,
    b.ml_addline2       AS ml_addline2,
    b.ml_addline3       AS ml_addline3,
    b.ml_city           AS ml_city,
    b.ml_statelabel     AS ml_statelabel,
    b.ml_zipcode        AS ml_zipcode
FROM tu_bene b
WHERE b.seq_bene_id = :seqBeneId
  AND b.ctl_rec_stat = 'A';
