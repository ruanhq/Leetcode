#260.Single Number III:
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        bitMask = 0
        for num in nums:
            bitMask ^= num
        #calculate the difference between different bitMasks here:
        diff = bitMask & (-bitMask)
        x = 0
        for num in nums:
            if num & diff:
                x ^= num
        return [x, bitMask ^ x]