-- ============================================================================
-- Query: get-plan-by-traunch
-- Feature: mobiledashboard, planselection, mobileStackup
-- BFF Endpoint: GET /mobile2api/v1/mobiledashboard
-- Downstream API: GET metadataapi/v1/plans/traunch/{deprecatedId}
-- Source repo: C:\Workspace\GitLab\MobileAutomation\UniteMSC\unite-metadata\
-- Source file: src/main/java/com/cs529/metadata/repository/TraunchTable.java
-- Source method: PlanService.getByTraunchId / getByDeprecatedId
-- DB tables: tu_traunch
-- Parameters: :traunchId (deprecated id e.g. 100001)
-- Returns: branding (plan id), asof_date, name
-- Notes: ORM findByCriteria; API planId = branding column, asOfDate formatted MM/dd/yyyy
-- ============================================================================

SELECT
    t.traunch_id        AS traunch_id,
    t.branding          AS plan_id,
    t.name              AS plan_name,
    t.asof_date         AS asof_date,
    t.backend_type      AS backend_type
FROM tu_traunch t
WHERE t.traunch_id = :traunchId
  AND t.ctl_rec_stat = 'A';
