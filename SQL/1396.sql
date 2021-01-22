#1396. Get the second most recent activity:
WITH A1 AS(
SELECT username, count(DISTINCT endDate) AS act_count FROM UserActivity
    GROUP BY username
    HAVING act_count = 1
)
SELECT username, activity, startDate, endDate
FROM UserActivity WHERE 
username IN(
SELECT username FROM A1
)
UNION
(SELECT username, activity, startDate, endDate
FROM (SELECT username, activity, startDate, endDate, row_number() OVER (partition By username order BY endDate DESC) AS RK FROM UserActivity) AS A2 WHERE 
username NOT IN (SELECT username FROM A1) AND 
RK = 2)
