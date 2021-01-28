#571. Find median given frequency table

#
#+----------+-------------+
#|  Number  |  Frequency  |
#+----------+-------------|
#|  0       |  7          |
#|  1       |  1          |
#|  2       |  3          |
#|  3       |  1          |
#+----------+-------------+

WITH cte AS (SELECT floor((sum(frequency) + 1) / 2) AS m1
    , FLOOR((SUM(frequency) + 2) / 2) AS m2
FROM numbers )
    , cte2 AS (select number
    , SUM(frequency) OVER (ORDER BY number ROWS UNBOUNDED PRECEDING) AS presum
FROM numbers ),
    N1 AS (
    	SELECT number FROM cte2 WHERE presum >= (SELECT m1 FROM cte) LIMIT 1
    	),
    N2 AS (
    	SELECT number FROM cte2 WHERE presum >= (SELECT m2 FROM cte) LIMIT 1
    	)
SELECT AVG(number) AS median 
FROM (
	SELECT * FROM N1 UNION
	SELECT * FROM N2 
) AS T;

SUM(frequency) OVER (ORDER BY number ROWS UNBOUNDED PRECEDING) AS presum FROM numbers

#CURRENT Row: the current row
#UNBOUNDED PRECEDING: all rows before the current row -> fixed(like the running sum)
#UNBOUNDED FOLLOWING: all rows after the current row -> fixed
#x preceding: x rows before the current row -> relative
#y following: y rows after the current row -> relative
