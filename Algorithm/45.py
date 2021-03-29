#45. Jump Game:
class Solution:
    def jumpGame(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 1
        