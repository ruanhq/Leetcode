#1270. All people report to the given manager

SELECT e1.employee_id
FROM employees AS e1
JOIN employees AS e2
ON e1.manager_id = e2.employee_id
JOIN employees AS e3 
ON e2.manager_id = e3.employee_id
WHERE e3.manager_id = 1 AND e1.employee_id != 1;