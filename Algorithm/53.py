#53. Maximum Subarray:
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        current_max = nums[0]
        result = nums[0]
        for i in range(1, n):
            current_max = max(current_max + nums[i], nums[i])
            result = max(current_max, result)
        return result


