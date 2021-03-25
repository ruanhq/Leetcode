#78. Subsets -> classic problem here, iterative, recursive, backtracking.

#Iterative
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for num in nums:
            subsets += [s + [num] for s in subsets]
        return subsets

#Recursive:
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        