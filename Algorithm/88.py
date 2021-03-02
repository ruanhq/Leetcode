#88. Merge sorted array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        result = []
        nums1_cpy = nums1[:m]
        nums1[:] = []
        p1 = 0
        p2 = 0 
        while p1 < m and p2 < n:
            if nums1_cpy[p1] < nums2[p2]:
                nums1.append(nums1_cpy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1
        if p1 < m:
            nums1[(p1+p2):(p1+m)] = nums1_cpy[p1:m]
        if p2 < n: 
            nums1[(p1+p2):(p1+n)] = nums2[p2:n]
        return result













