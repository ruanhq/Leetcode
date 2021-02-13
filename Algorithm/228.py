#228. Summary Ranges
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
    	result = []
    	pointer = 0
    	for i, j in enumerate(nums):
    		if i == len(nums) - 1 or nums[i + 1] - nums[i] > 1:
    			result.append(str(nums[pointer])) +
    			'->' + str(j) if nums[pointer] != j
    			else str(j)
    			pointer = i + 1
    	return result

    	for i, j in enumerate(nums):
    		if i == len(nums) - 1 or 
    		nums[i + 1] - nums[i] > 1
    		result.append(str(nums[pointer])) +
    		'->' + str(j)