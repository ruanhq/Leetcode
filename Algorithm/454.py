#454. FourSumII
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        result = 0
        m1 = {}
        for a in nums1:
            for b in nums2:
            	#Get the value from the key a + b with default value 0
            	m1[a + b] = m1.get(a + b, 0) + 1
        for c in nums3:
            for d in nums4:
                result + = m1.get(-(c + d), 0)
        return result

