#1789. Primary Department for each employee

select employee_id, department_id from Employee 
WHERE primary_flag = "Y"
UNION

SELECT employee_id, department_id
FROM Employee 
GROUP BY employee_id
HAVING COUNT(employee_id) = 1;



