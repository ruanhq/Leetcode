#163. Missing Ranges:
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums = [lower - 1] + nums + [upper + 1]
        result = []
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 2:
                result.append(str(nums[i] + 1))
            elif nums[i + 1] - nums[i] > 2:
                result.append(str(nums[i] + 1) + "->" + str(nums[i + 1] - 1))
        return result

#Time complexity: O(n)
#Space complexity: O(n)