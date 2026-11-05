-- ============================================================================
-- Query: get-traunch-stackup
-- Feature: mobileStackup, mobiledashboard (displayInStackup)
-- BFF Endpoint: GET /mobile2api/v1/mobilestackup/{planId}
-- Downstream API: GET metadataapi/v1/stackup
-- Source repo: C:\Workspace\GitLab\MobileAutomation\UniteMSC\unite-metadata\
-- Source file: src/main/resources/com/cs529/metadata/repository/TraunchStackupDataTableDao.xml
-- Source method: StackupService
-- DB tables: tu_traunch_stackup
-- Parameters: :traunchId
-- Returns: stackup configuration rows
-- Notes: explicit XML; used for stackup feature — placeholder for mobiledashboard cross-ref
-- ============================================================================

SELECT
    s.traunch_id        AS traunch_id,
    s.stackup_data      AS stackup_data
FROM tu_traunch_stackup s
WHERE s.traunch_id = :traunchId
  AND s.ctl_rec_stat = 'A';
