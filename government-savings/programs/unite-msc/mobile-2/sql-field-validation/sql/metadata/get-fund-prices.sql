-- ============================================================================
-- Query: get-fund-prices
-- Feature: mobiledashboard (balance calculation)
-- BFF Endpoint: GET /mobile2api/v1/mobiledashboard (via account includeFundPositions)
-- Downstream API: GET metadataapi/v1/prices (plan + asofDate)
-- Source repo: C:\Workspace\GitLab\MobileAutomation\UniteMSC\unite-metadata\
-- Source file: src/main/resources/com/cs529/metadata/repository/PriceTableDao.xml
-- Source method: PriceService / MetadataGateway.getFundPrices
-- DB tables: tu_fund_price, tu_funds, tu_traunch_fund, tu_traunch
-- Parameters: :planId (branding e.g. upromise), :asofDate
-- Returns: fund omni_fund_id (deprecated id), price, fund_id
-- Notes: Service matches fund position fundId to price deprecatedId; price on asof_date
-- ============================================================================

SELECT
    f.fund_id           AS fund_id,
    f.omni_fund_id      AS omni_fund_id,
    fp.price_date       AS price_date,
    fp.price            AS price,
    f.fund_name         AS fund_name
FROM tu_fund_price fp
JOIN tu_funds f ON f.fund_id = fp.fund_id
JOIN tu_traunch_fund tf ON tf.fund_id = f.fund_id
JOIN tu_traunch tr ON tr.traunch_id = tf.traunch_id
WHERE tr.branding = :planId
  AND fp.price_date = :asofDate
  AND fp.ctl_rec_stat = 'A'
  AND f.ctl_rec_stat = 'A'
  AND tf.ctl_rec_stat = 'A'
  AND tr.ctl_rec_stat = 'A'
ORDER BY f.fund_id;
