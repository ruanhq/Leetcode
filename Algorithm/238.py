#238. Product of array except self:
#Get two documentary array where 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lengt = len(nums)
        L, R, result = [0] * lengt, [0] * lengt, [0] * lengt
        L[0] = 1
        R[lengt - 1] = 1
        for i in range(1, lengt):
            L[i] = L[i - 1] * nums[i - 1]
        for i in reversed(range(lengt - 1)):
            R[i] = R[i + 1] * nums[i + 1]
        for i in range(lengt):
            result[i] = L[i] * R[i]
        return result
#total ads revenue -> # active users * CTR * price 



