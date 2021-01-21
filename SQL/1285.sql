#1285. Find the start and end number of continuous ranges
WITH A1 AS(
SELECT log_id, row_number() OVER (ORDER BY log_id) AS rk FROM Logs
)

SELECT min(log_id) AS start_id, max(log_id) AS end_id
FROM 
(
    SELECT log_id, rk, (log_id - rk) AS similar_rk FROM A1
) AS A2

GROUP BY similar_rk;