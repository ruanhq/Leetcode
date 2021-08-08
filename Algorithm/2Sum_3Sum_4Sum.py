#2sum -> 3sum -> 4sum:

#Let's start from the brute force solution here:

class Solution:
    def threeSum(self, nums: List[int]):
    	#Starts from the maps you have seen:
        seenMap = {}
        duplicatesValue = set()
        result = set()
        for i, value in enumerate(nums):
            if value not in dups:
                duplicatesValue.append(value)
                for j, values in enumerate(nums[i + 1: ]):
                    complement = -value - values
                    if complement in seenMap and seenMap[complement] == i:
                        result.append(tuple(value, values, complement))
                    seenMap[values] = i

        for i, value in enumerate(nums):
            if value not in dups:
                duplicatesValue.append(value)
                for j, values in enumerate(nums[i + 1: ]):
                    complement = -value - values
                    if complement in seenMap and seenMap[complement] == i:
                        result.append(tuple(value, values, complement))
                    seenMap[values] = i
        return result


#4sum:
#adding a tuple on top of the sets here.
#add a tuple on top of the sets.

class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        if len(nums) < 4:
            return []
        if nums[0] * 4 > target or nums[-1] * 4 < target:
            return []
        setA = set()
        result = set()
        for i in range(len(nums)):
            if nums[i] not in setA:
                for j in range(i + 1, len(nums)):
                    dict = {}
                    for k in range(j + 1, len(nums)):
                        a = nums[i]
                        b = nums[j]
                        c = nums[k]
                        d = target - a - b - c
                        if d not in dict: #dict[c] -> k ----> O(n^3)
                            dict[c] = k
                        else:
                            result.add(tuple(sorted([a, b, c, d])))
        return result


class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        if len(nums) < 4:
            return []
        if nums[0] * 4 > target or nums[-1] * 4 < target:
            return []
        setA = set()
        result = set()
        for i in range(len(nums)):
            if nums[i] not in setA:
                for j in range(i + 1, len(nums)):
                    dict1 = {}
                    for k in range(j + 1, len(nums)):
                        a = nums[i]
                        b = nums[j]
                        c = nums[k]
                        d = target - a - b - c
                        if d not in dict1:
                            dict1[c] = k
                        else:
                            result.add(tuple(sorted([a, b, c, d])))
        return result
#8 to the power of 2.

#return the tuples such that: 

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]):
        n = len(nums1)
        








m1.get(-(c + d), 0) ---> number of occurrences in m1 here.
m1.get(-(c + d), 0) ---> number of occurrences in m1 here,
number of occurrences in m1 here




get(key[, default])
get(key[, default])
diction = {"Name": "Harry"}
diction.get("Yar", "SFDSD")
dictionary.get(value, default_value)
diction.get("Year", "SFDSD")
dictiona.get(value, default_value)




#H-index





#H-index in log time:

#What would be the index?
#data quality issue, data difference issue -> add variables

#while left <= right:
#by default, it should be left <= right:

















