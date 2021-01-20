#1699. Number of callse between two persons
WITH A1 AS(
SELECT from_id AS person1, to_id AS person2, duration FROM Calls WHERE from_id < to_id
UNION ALL
SELECT to_id AS person1, from_id AS person2, duration FROM Calls WHERE from_id > to_id
)

SELECT person1, person2, count(*) AS call_count, sum(duration) AS total_duration
FROM A1
GROUP BY person1, person2
ORDER BY person1, person2;