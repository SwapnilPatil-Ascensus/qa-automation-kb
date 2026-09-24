-- Header: x-app-version (required for GET /plans/{id} and all requests)
-- Downstream: unite-metadata → TU_CODES (type = MIN_MOBILE_VERSION)
-- Source: mobile/mobile1/sql/mobile.sql → get.mobile.min.version

SELECT tc.code_id   AS code,
       tc.description AS x_app_version
FROM tu_codes tc
WHERE tc.type = 'MIN_MOBILE_VERSION'
  AND tc.ctl_rec_stat = 'A';

-- Postman default: x-app-version = '1.8.0'
-- If GET /plans/{id} returns HTTP 426, increase to value from query above (e.g. 3.1.0)
