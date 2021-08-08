SELECT
B.Name AS Department,
A.Name AS Employee,
A.Salary
FROM
(SELECT E.*, DENSE_RANK() OVER (PARTITION BY DepartmentId ORDER BY Salary DESC) AS deptPayRank FROM Employee AS E) AS A
JOIN 
Department as B
ON A.DepartmentId = B.Id
WHERE deptPayRank = 1;

SELECT  D.Name AS Department,
E.Name AS Employee,
E.Salary
FROM 
(
	, DENSE_RANK() OVER (PARTITION BY DepartmentId ORDER BY Salary DESC) AS deptPayRank FROM Employee AS E
)