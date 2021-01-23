WITH A1 AS(
    SELECT exam_id, exam.student_id, student_name, score, RANK() OVER(PARTITION BY exam_id ORDER BY score) rkSmall, RANK() OVER(PARTITION BY exam_id ORDER BY score DESC) rkLarge 
    FROM exam 
    LEFT JOIN 
    student
    ON exam.student_id = student.student_id
)

SELECT DISTINCT student_id, student_name
FROM A1
WHERE student_id NOT IN (SELECT student_id FROM A1 WHERE rkSmall = 1 or rkLarge = 1)
ORDER BY student_id