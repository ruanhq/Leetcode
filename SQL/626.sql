#626. Exchange Seats

SELECT 
(
CASE WHEN mod(id, 2) = 0 THEN id - 1
WHEN mod(id, 2) = 1 AND id != (SELECT MAX(id) FROM seat) THEN id + 1
ELSE id
END 
) AS id, Student
FROM seat 
ORDER BY id ASC;