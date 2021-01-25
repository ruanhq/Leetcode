#1468. Calculate Salaries:
WITH A1 AS (
SELECT S.company_id, S.employee_id, S.employee_name, S.salary, B.max_salary 
FROM Salaries S JOIN (SELECT company_id, MAX(salary) AS max_salary FROM Salaries
    GROUP BY company_id)  B
    ON S.company_id = B.company_id
)
SELECT company_id, employee_id, employee_name, 
(CASE 
    WHEN max_salary < 1000 THEN ROUND(salary, 0)
    WHEN max_salary BETWEEN 1000 and 10000 THEN ROUND(salary * (1 - (24/100)), 0)
    ELSE ROUND(salary * (1- (49/100)), 0)
END) AS salary
FROM A1;

#Using between!