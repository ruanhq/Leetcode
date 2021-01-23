#1435. Create a Session Bar Chart:
WITH A1 AS (
    SELECT duration/60 AS mins
    FROM sessions
)

SELECT '[0-5>' AS bin,
       SUM(CASE WHEN mins<5 THEN 1 ELSE 0 END) AS total
FROM A1
UNION ALL
SELECT '[5-10>' AS bin,
       SUM(CASE WHEN mins>=5 AND mins<10 THEN 1 ELSE 0 END) AS total
FROM A1
UNION ALL
SELECT '[10-15>' AS bin,
       SUM(CASE WHEN mins>=10 AND mins<15 THEN 1 ELSE 0 END) AS total
FROM A1
UNION ALL
SELECT '15 or more' AS bin,
       SUM(CASE WHEN mins>=15 THEN 1 ELSE 0 END) AS total
FROM A1



