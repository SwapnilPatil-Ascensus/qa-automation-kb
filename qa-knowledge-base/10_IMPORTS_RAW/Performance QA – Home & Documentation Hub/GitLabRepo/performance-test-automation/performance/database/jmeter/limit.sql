select resource_name, current_utilization, max_utilization, limit_value 
    from v$resource_limit 
    where resource_name in ('sessions', 'processes');

SELECT
  'Currently, ' 
  || (SELECT COUNT(*) FROM V$SESSION)
  || ' out of ' 
  || VP.VALUE 
  || ' connections are used.' AS USAGE_MESSAGE
FROM 
  V$PARAMETER VP
WHERE VP.NAME = 'sessions';
