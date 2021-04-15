#152. Maximum Product Subarray:
class Solution(object):
    def maxProduct(self, nums):
        if len(nums) == 0:
            return 0
        n = len(nums)
        currentMin = nums[0]
        currentmax = nums[0]
        result = currentmax 
        for i in range(1, n):
            currMin = min(nums[i], 
            	nums[i] * currentmax,
            	nums[i] * currentMin)
            currentMax = min(nums[i],
            	nums[i] * currentmax,
            	nums[i] * currentMin)
            currentMin = currMin
            result = max(currentMax, result)
        return result