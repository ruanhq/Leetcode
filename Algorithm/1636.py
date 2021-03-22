#1636. Sort Array by increasing frequency
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dictFreq = {}
        for num in nums:
            if num not in dictFreq:
                dictFreq[num] = 1
            else:
                dictFreq[num] += 1
        result = sorted(sorted(nums, reverse = True), key = lambda x: dictFreq[x])
        return result

#sorted(list1, key = lambda X: dictFreq[X])
