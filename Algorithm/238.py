#238.py
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #storing two arrays.
        maps1 = [0] * len(nums)
        maps1[0] = nums[0]
        maps2 = [0] * len(nums)
        maps2[len(nums) - 1] = nums[len(nums) - 1]
        result = [0] * len(nums)
        for i in range(1, len(nums)):
            maps1[i] = maps1[i - 1] * nums[i]
        for j in range(len(nums) - 2, -1, -1):
            maps2[j] = maps2[j + 1] * nums[j]
        result[0] = maps2[1]
        result[len(nums) - 1] = maps1[len(nums) - 2]
        for i in range(1, len(nums) - 1):
            result[i] = maps1[i - 1] * maps2[i + 1]
        return result
