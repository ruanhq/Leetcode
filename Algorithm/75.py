#75 Sort Colors:
class Solution(object):
    def sortColors(self, nums):
        n = len(nums)
        pointerZero = 0
        pointerTwo = n - 1
        currentPoint = 0
        while current <= pointerTwo:
            if nums[current] == 2:
                nums[current], nums[pointerTwo] = nums[pointerTwo], nums[current]
                pointerTwo -= 1
            elif nums[current] == 0:
                nums[current], nums[pointerZero] = nums[pointerZero], nums[current]
                pointerZero += 1
                currentPoint += 1
            else:
            	currentPoint += 1
        return nums



