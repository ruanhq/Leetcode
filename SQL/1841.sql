#1841. League Statistics:

WTIH A1 AS (
SELECT Teams.team_id, Teams.team_name, A.scoreFor, A.scoreAga
FROM 
(
SELECT home_team_id AS team_id, home_team_goals AS scoreFor,
away_team_goals AS scoreAga FROM Matches
UNION ALL 
SELECT away_team_id AS team_id, away_team_goals AS scoreFor,
home_team_goals AS scoreAga FROM Matches
) AS A
JOIN Teams
ON A.team_id = Teams.team_id
)
SELECT team_name, 
COUNT(team_id) AS matches_played,
SUM(CASE 
        WHEN scoreFor > scoreAga THEN 3
        WHEN scoreFor = scoreAga THEN 1
        ELSE 0
    END) AS points,
SUM(scoreFor) AS goal_for,
SUM(scoreAga) AS goal_against,
SUM(scoreFor - scoreAga) AS goal_diff
FROM A1
GROUP BY team_id
ORDER BY points DESC, goal_diff DESC, team_name ASC;




本身的宽表 -> 第一版, 迭代(高低收益分开) -> 客户状态
only 易购/轨迹类变量 
模型监控部: 计算文件,

B卡: 易购/轨迹类变量:
上研维护宽表: 只有超短期B卡 客群
一致客群(用信) -> 客群一致



#You may want to use Counter instead of defaultdict

#career interest/ career interest or the different ones.




#Table A: user_id | timestamp | action_id
#output: numberOfMinutes | numberOfUsers
# numberOfMinutes represents the # minutes
# numberOfUsers represents the users spending the numberOfMinutes in the twitter.


SELECT user_id, action_id
#Here we utilize the 

#First we can groupBy user_id
WITH A1 AS (SELECT user_id, action_id, MAX(timestamp) AS logOutTimeStamp,
MIN(timestamp) AS logInTimeStamp
FROM A 
GROUP BY user_id, action_id),
A2 AS (
SELECT user_id, SUM(ROUND(cast(logOutTimeStamp AS date) - cast(logInTimeStamp AS date)) * 24 * 60) AS sumMinutes
FROM A1 GROUP BY user_id
)
#Group by the numberOfMinutes
SELECT sumMinutes AS numberOfMinutes, COUNT(DISTINCT user_id) AS numberOfUsers
FROM A2 GROUP BY 1;



#Input: "A": 0.4, "B": 0.3, "C": 0.2, "D": 0.1, construct a pairs:

#Now we may want to use the random number generator.
#output is a random value with the probability of the values
#corresponding to this character.

#random number:

#We may want to construct a nested structure 
combinations = [(black, green) 
for black in range(1, 7)
for green in range(1, 7)]
success = [black > green for black, green in combinations]
sum(success)
#set up automated alert for detecting bias in experiment data:
#set up automated alert for detection of the bias in experiment data here.

#product + python: 
nums.sort(reverse = True)
nums[k - 1]
#product and python to do the running here:
#How to handle out-of-scope requirements?



#1. Deep learning: train a image classifier
#2. NLP: Train a text classifier




























