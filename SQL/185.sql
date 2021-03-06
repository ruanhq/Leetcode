#185. Department Top 3 salaries:
select d.Name as Department, A.name as Employee, 
A.salary
from 
(
select E.*, dense_rank() over(partition by DepartmentId
order by Salary desc) as deptPayRank 
FROM Employee as E 
) AS A
JOIN Department AS D 
ON A.DepartmentId = D.Id 
where A.deptPayRank <= 3;
