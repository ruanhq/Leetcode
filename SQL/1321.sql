#1321. Restaurant Growth
#Using Self-Join
WITH A1 AS(
SELECT visited_on, SUM(amount) AS day_amount FROM Customer GROUP BY visited_on
)

SELECT AA1.visited_on AS visited_on, SUM(AA2.day_amount) AS amount,
ROUND(AVG(AA2.day_amount), 2) AS average_amount

FROM A1 AA1, A1 AA2
WHERE DATEDIFF(AA1.visited_on, AA2.visited_on) BETWEEN 0 AND 6
GROUP BY AA1.visited_on
HAVING COUNT(AA2.visited_on) = 7