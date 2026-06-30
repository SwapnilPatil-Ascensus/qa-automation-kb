-- ============================================================================
-- Query: get-owner-by-id
-- Feature: mobiledashboard
-- BFF Endpoint: GET /mobile2api/v1/mobiledashboard
-- Downstream API: GET profileapi/v1/owners/{seqPersonId}
-- Source repo: C:\Workspace\GitLab\MobileAutomation\UniteMSC\unite-profile\
-- Source file: src/main/java/com/cs529/profile/service/OwnerService.java
-- Source method: getById
-- DB tables: tu_person
-- Parameters: :seqPersonId
-- Returns: first_name, last_name, dob → ownerFirstName, ownerLastName, ownerDob
-- Notes: ORM findByCriteria; API formats dob as yyyy-MM-dd HH:mm:ss
-- ============================================================================

SELECT
    p.seq_person_id     AS seq_person_id,
    p.first_name        AS first_name,
    p.middle_initial    AS middle_initial,
    p.last_name         AS last_name,
    p.suffix            AS suffix,
    p.dob               AS dob
FROM tu_person p
WHERE p.seq_person_id = :seqPersonId
  AND p.ctl_rec_stat = 'A';
