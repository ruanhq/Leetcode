#580. Count Student number in departments

SELECT dept_name, COUNT(DISTINCT student_id) AS student_number
FROM department LEFT JOIN student 
ON department.dept_id = student.dept_id
GROUP BY department.dept_id
ORDER BY student_name DESC;