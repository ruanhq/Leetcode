#1824. Minimum Sideway Jumps:
#state transition equation:
#S[n]: S[n] = S[n - 1] if obs[n] = 0
#S[n] 
#using t[n] to store the position at that time?

S[n] = S[n - 1] + (obs[t[n - 1]] == 0)
S[n] = S[n - 1] + (obs[t[n - 1]] == 0)

#detect the problem -> propose the solution -> have the hypothesis(what's your underlying 
#hypothesis here)?

#How to calculate the profit & -> bidding with 20% percent 
#of the risk of the failure -> 

CASE, ROLE PLAY -> walk through comprensively here.


for i in obstacles[1:]:
    for j in range(4):
        if i == j:
            old_dp = dp
            if i == 0:
                dp[0] = min





#写sql，写

#The probability of a selected random positive sample ranks higher
#than a randomly selected negative sample.

#TPR vs FPR
#orders -> computational biology

#S[n]: S[n] = S[n - 1] if obs[n] == 0.


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return nums
        i = len(nums) - 1
        while i > 0:
            if nums[i - 1] < nums[i]:
                break
            i = i - 1
        i = i - 1
        j = len(nums) - 1
        while j > i:
            if nums[j] > nums[i]:
                break
            j = j - 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1: ] = sorted(nums[i + 1:])
        return nums

#Find the left-most index i making nums[i - 1] < nums[i]
#Then find the first element from right-end larger than the value in 
#index i -> rank the values right of i by increasing order here.
#swap i-th and j-th index and make the first & second 
#Probability of making a 
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return nums
        i = len(nums) - 1
        j = i
        while i > 0:
            if nums[i - 1] < nums[i]:
                break
            i = i - 1
        i -= 1
        while j > i:
            if nums[j] > nums[i]:
                break
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1: ] = sorted(nums[i + 1:])
        return nums
#
#dictionary.get(value, default_values)
#Construct a map for value1, value2 -> then construct another 
#map for value3, value4.

dictionary.get("Name", "Harrys")
dict2.get("Name2", "Harrys2")
#

class Solution:
    def fourSum(self, nums, target):
        nums.sort() 
        if len(nums) < 4:
            return []
        if nums[0] * 4 > target or nums[-1] * 4 < target:
            return []
        


















































