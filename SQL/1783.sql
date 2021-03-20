#1783. Grand Slam Titles

WITH A1 AS 
(SELECT Wimbledon AS player_id FROM Championships
UNION 
SELECT Fr_open AS player_id FROM Championships
UNION 
SELECT US_open AS player_id FROM Championships
UNION 
SELECT Au_open AS player_id FROM ChampionShips)

SELECT player_id, player_name, COUNT(*)

FROM 
Players INNER JOIN A1 ON Players.player_id = A1.player_id
GROUP BY player_id, player_name;

#union all: not remove duplicates, union: removing duplicates automatically.
