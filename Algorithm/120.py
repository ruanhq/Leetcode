#120. Triangle:

#own feature engineering with data scientists, to 
#build scalable, reliable ML pipelines for low latency,
#high throughput, high accuracy models and rules.

#Own end-to-end model development and deployment or 
#support the tech lead for the development 
#and deployment

#ensuring data integrity of product analytics and ML models
#and rules from automated traffic.



class Solution(object):
    def minimumTotal(self, triangle):
        for i in range(len(triangle)):
        	for j in range(len(triangle[i])):
        	    lpare = triangle[i - 1][j - 1] if i > 0 else float("inf")
        	    rpare = triangle[i - 1][j] if j < len(triangle[i]) - 1 else float("inf")
        	    triangle[i][j] = min(lpare, rpare) + triangle[i][j]
        result = min(triangle[len(triangle) - 1])
        return result

#account takeover:

1. machine finger records, browsing history(trajectory history)/ IP history
2. purchasing behavior
3. Trajectory, buyer/payer -> time difference
4. spam messaging, interaction effects.

#1m trip, 350 risky trips
#1m trip, 650 risky trips

#Visualize the relationship between variables and the different values here
#trajectory and buyer/payer -> time difference 

#Estimate the people who watching the fireworks:
#Number of cities
#s
####

 #Own model development process through model development and 
 #deployment as well as the model testing.

class Solution(object):
    def minimumTotal(self, triangle):
        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                lpare = triangle[i - 1][j - 1] if i > 0 else float("inf")
                rpare = triangle[i - 1][j] if j < len(triangle[i]) - 1 else float("inf")
                triangle[i][j] = min(lpare, rpare) + triangle
        result = min(triangle[len(triangle) - 1])
        return result

dictionary = ["cat","batj","ratss"]
#minimum total is the sum of the past left guy and the past right guy
#minimum path sum would be the minimum of path sum ending in each of element in the last layer.
#optimal subproblems -> formed by optimal subproblems -> we can have state transition function/equation
class Solution(object):
    def minimumTotal(self, triangle):
        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                lpare = 



























