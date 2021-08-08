#137. Single-Number II:

#store the -> if the model -> once-> put out to twice appearance.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = (3 * sum(set(nums)) - sum(nums)) // 2
        return result




from collections import Counter
class Solution:
    def singleNumber(self, nums) -> int:
        numList = Counter(nums)
        


