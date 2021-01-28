#1194. Tournament Winner:
WITH A1 AS (
SELECT first_player player_id, first_score score
FROM matches
UNION ALL
SELECT second_player player_id, second_score score
FROM matches
),
A2 AS (
SELECT player_id, SUM(score) AS score
    FROM A1
    GROUP BY player_id
)

SELECT DISTINCT group_id, FIRST_VALUE(C.player_id) OVER(PARTITION BY group_id ORDER BY score DESC, C.player_id) player_id 
FROM A2 C LEFT JOIN players P ON C.player_id = P.player_id

#WITH A1 AS(
#),
#A2 AS (
#)