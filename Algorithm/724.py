#724. FindingPivotIndex:
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        prefixSum = 0
        for i, x in enumerate(nums):
            if prefixSum == (totalSum - x - prefixSum):
                return i
            prefixSum += x
        return -1



#How to decide whether video creator bonus a good program financially?
#video creator bonus?

#marginal improvement of this solution?
#generate 100 points(X, Y) to ensure the 100 poitns follow the slope as 2 and 
#the r-square as 0.8.

#arrays of doubled pairs:

#arrange the counter with their absolute values here.











