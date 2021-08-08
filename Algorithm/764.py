class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            low = i + 1
            high = len(nums)
            while low < high:
                sums = nums[i] + nums[low] + nums[high]
                if abs(target - sums) < abs(diff):
                    diff = target - sums
                if sums < target:
                    low += 1
                else:
                    high -= 1
            if diff == 0:
                break
        return target - diff




class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        ns = ''.join(S.split("-")).upper()
        