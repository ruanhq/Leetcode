class Solution:
    def sortTransformedArray(self, nums: List[int], a: int,
        b: int, c: int):
        nums = [t * x * x + t * b + c for t in nums]
        result = [None] * len(nums)
        