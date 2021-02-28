#888. Fair Candy Swap
class Solution(object):
    def fairCandySwap(self, A, B):
        Sa, Sb = sum(A), sum(B)
        setB = set(B)
        for x in A:
            if x + (Sb - Sa) / 2 in setB:
                return [x, x + (Sb - Sa) / 2]
def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
	nA = sum(A)
	nB = sum(B)


