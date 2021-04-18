#209. Minimum size subarray sum:
#159. Longest Substring with at most two distinct characters:


#Using two pointers to search for the element.
class Solution(object):
    def minimumSubarraySum(self, target, nums):
        pointer = 0
        result = 100000000
        curSum = 0
        for i in range(len(nums)):
            curSum += nums[i]
            while curSum >= target:
                result = min(result, i - pointer + 1)
                curSum -= nums[pointer]
                pointer += 1
        if result >= 100000000:
            return 0
        else:
            return result


#Longest substring with at most 5 distinct characters:
from collections import defaultdict
def longestSubstringWithFiveCharacters(nums):
    currentHashMap = defaultdict(int)
    result = 0 
    pointer = 0
    n = len(nums)
    for i in range(nums):
        currentHashMap[nums[i]] = i
        if len(currentHashMap) > 2:
            indexToDelete = min(currentHashMap.values())
            del currentHashMap[nums[indexToDelete]]
            pointer = indexToDelete + 1
    result = max(result, i - pointer + 1)
    return result

#delete an index from the array:
#Two pointers: scanning the pointer from left to right 
#and then modify the index/ array here.