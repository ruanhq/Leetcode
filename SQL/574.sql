#574. Winning Candidate:
SELECT Name FROM Candidate 
WHERE id IN 
(
SELECT id FROM 
(SELECT 
	Candidate AS id, 
	count(id) AS voteCount
	GROUP BY 1 
	ORDER BY voteCount DESC 
	LIMIT 1
	) AS A1
)