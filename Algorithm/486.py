#486. Predict the winner:
#two pointer doesn't work here.
#It may not be the optimal strategy to find the maximum element here.
#will it be able to iterative through the end then we judge whether the 
#sum is larger or equal than zero?
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def getScore(nums, l, r):
            if l == r:
                return nums[l]
            return max(nums[l] - getScore(nums, l + 1, r),
            	nums[r] - getScore(nums, l, r - 1))
        return getScore(nums, 0, len(nums) - 1) >= 0


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def getScore(nums, l, r):
            if l == r:
                return nums[l]
            return max(nums[l] - getScore(nums, l + 1, r),
            nums[r] - getScore(nums, l, r - 1))
        return getScore(nums, 0, len(nums) - 1) >= 0


