#414. Third Maximum Number:
#First if the number of element in the array is smaller than 3, it will return the maximum.
#Then we are going to remove the second maximum element, then pop out the third maximum element.
#            
#            
#            
#            
#            
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        maximum = max(nums)
        if len(nums) < 3:
            return maximum
        nums.remove(maximum)
        secondMaximum = max(nums)
        nums.remove(secondMaximum)
        if not nums:
            return maximum
        else:
            return max(nums)
