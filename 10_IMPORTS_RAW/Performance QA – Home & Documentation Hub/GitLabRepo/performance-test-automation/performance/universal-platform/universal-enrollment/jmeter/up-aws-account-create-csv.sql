WITH funds AS (
    SELECT tf.traunch_id, f.fund_id,
           ROW_NUMBER() OVER (PARTITION BY tf.traunch_id ORDER BY f.fund_id) as rn
    FROM tu_traunch_fund tf, tu_funds f
    WHERE tf.traunch_id IN ('100066', '100009', '100080', '100081', '100049')
      AND tf.ctl_rec_stat = 'A'
      AND f.web_status = 'A'
      AND f.back_status = 'A'
      AND f.fund_id = tf.fund_id
)
SELECT 
    branding, 
    LOWER(REGEXP_REPLACE(uuid_traunch_id, '(.{8})(.{4})(.{4})(.{4})(.{12})', '\1-\2-\3-\4-\5')) AS planId,
    fund_1,
    fund_2,
    fund_3
FROM (
    SELECT 
        t.traunch_id,
        t.branding,
        t.uuid_traunch_id,
        f.fund_id,
        f.rn
    FROM tu_traunch t, funds f
    WHERE t.traunch_id = f.traunch_id
      AND f.rn <= 3
) pivoted
PIVOT (
    MAX(fund_id) FOR rn IN (1 AS fund_1, 2 AS fund_2, 3 AS fund_3)
)
ORDER BY branding;
