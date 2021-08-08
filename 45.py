#jumpGame II:
class Solution:
    def jump(self, nums: List[int]):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 0
        result = 1
        maxReach = nums[0]
        maxCurrentPosition = nums[0]
        for i in range(1, n):
        	if maxCurrentPosition < i:
        		result += 1
        		maxCurrentPosition = maxReach
            maxReach = max(maxReach, nums[i] + i)
        return result


#jumpGame II:

class Solution:
    