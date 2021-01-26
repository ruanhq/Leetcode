#1440. Evaluate Boolean Expression
SELECT E.left_operand, E.operator, E.right_operand,
(CASE WHEN operator = ">" THEN IF(V1.value > V2.value, 'true', 'false')
     WHEN operator = "<" THEN IF(V1.value < V2.value, 'true', 'false')
     ELSE IF (V1.value = V2.value, 'true', 'false')
     END) AS value FROM 
Expressions E
JOIN Variables V1 ON V1.name = E.left_operand
JOIN Variables V2 ON V2.name = E.right_operand
