#Team scores in Football Tournament

WITH A1 AS(
SELECT * FROM
Teams
LEFT JOIN 
Matches
ON 
Teams.team_id = Matches.host_team OR 
Teams.team_id = Matches.guest_team
)
SELECT 
team_id, team_name,
SUM(CASE WHEN team_id = host_team AND host_goals > guest_goals THEN 3 ELSE 0 END) +
SUM(CASE WHEN team_id = guest_team AND guest_goals > host_goals THEN 3 ELSE 0 END) + 
SUM(CASE WHEN team_id = host_team AND host_goals = guest_goals THEN 1 ELSE 0 END) +
SUM(CASE WHEN team_id = guest_team AND host_goals = guest_goals THEN 1 ELSE 0 END) AS num_points
FROM A1
GROUP BY team_id
ORDER BY num_points DESC, team_id ASC;
