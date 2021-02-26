#579:
#Get the cumulative sum of an employee's salary over a period of
#3 months but exclude the most recent month:
SELECT A.Id, MAX(B.Month) AS Month,
SUM(B.Salary) AS Salary
FROM Employee A, Employee B
WHERE A.Id = B.Id AND B.Month 
BETWEEN (A.Month - 3) AND (A.Month - 1)
GROUP BY A.Id, A.Month
ORDER BY Id, Month DESC;
#breakwaters

