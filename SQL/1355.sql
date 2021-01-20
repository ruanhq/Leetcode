#1355: Activity Participants
WITH A1 AS(
SELECT F.activity AS activity, COUNT(DISTINCT F.id) AS COUNTS
FROM
Friends AS F
 JOIN
Activities as A
ON F.activity = A.name
GROUP BY A.name
)
SELECT activity FROM A1
WHERE COUNTS <> (SELECT max(COUNTS) FROM A1) AND COUNTS <> (SELECT min(COUNTS) FROM A1);