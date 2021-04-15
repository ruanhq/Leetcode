#1811 Finding Interview Candidates:

WITH A1 AS (
SELECT gold_medal AS user_id, COUNT(DISTINCT contest_id) AS ContestCount
FROM Contests GROUP BY contest_id
	),
A2 AS (
SELECT gold_medal AS user_id, contest_id FROM Contests
UNION ALL
SELECT silver_medal AS user_id, contest_id FROM Contests
UNION ALL
SELECT bronze_medal AS user_id, contest_id FROM Contests
	),
A3 AS(
SELECT user_id, LEAD(contest_id, 1) OVER(PARTITION BY user_id
	ORDER BY contest_id ASC) AS leadID,
LAG(contest_id, 1) OVER(PARTITION BY user_id ORDER BY contest_id ASC) AS lagID
FROM A2
	),
A4 AS(
SELECT DISTINCT user_id FROM A3 WHERE A3.user_id = A3.leadID AND
A3.lagID = A3.user_id
	)

SELECT name, mail FROM Users
WHERE Users.user_id IN
(SELECT DISTINCT user_id FROM A1 WHERE A1.ContestCount >= 3)
OR 
(SELECT DISTINCT user_id FROM A4)


A2 AS (
SELECT gold_medal AS user_id
	)
