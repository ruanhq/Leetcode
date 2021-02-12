#578. Get Highest Answer Rate question
WITH A1 AS (SELECT question_id,
SUM(CASE WHEN action = 'answer' THEN 1
ELSE 0 END) AS answer_number
SUM(CASE WHEN action = 'show' THEN 1
ELSE 0 END) AS show_number
FROM survey_log
GROUP BY question_id)
SELECT question_id AS survey_log
FROM A1
ORDER BY (answer_number/show_number) DESC 
LIMIT 1;



