#453 Minimum moves to equal array elements:
class Solution:
    def minMoves(self, nums: List[int]) -> int:
    	nums.sort()
    	count = 0
    	for i in range(n - 1, 1, -1):
    		count += nums[i] - nums[0]
    	return count





