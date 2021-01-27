#1204. Last Person to Fit in the elevator
SELECT person_name
FROM 
(SELECT person_name, SUM(weight) OVER (ORDER BY turn ASC) AS running_total
FROM Queue) A1
WHERe A1.running_total <= 1000
ORDER BY running_total DESC
LIMIT 1

#create a column called running_total where it fits in the dataset.
