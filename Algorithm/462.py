#462.Minimum moves to equal array elements II
#you may want to find the 
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        n = len(nums)
        median = nums[n//2]
        for i in range(n):
            result += abs(median - nums[i])
        return result