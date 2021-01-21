#1459.Rectangles Areas
SELECT T1.id AS p1, T2.id AS p2,
ABS(T2.x_value - T1.x_value) * ABS(T2.y_value - T1.y_value) AS area
FROM Points as T1
JOIN
Points as T2
ON T1.id < T2.id
WHERE T1.x_value <> T2.x_value AND T1.y_value <> T2.y_value
ORDER BY area DESC, p1 ASC, p2 ASC;