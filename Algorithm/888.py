#888. Fair Candy Swap
def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
	nA = sum(A)
	nB = sum(B)
	setB = set(B)
	for a in A:
		if a + (nB - nA)/2 in setB:
			return [a, a + (nB -nA)/2]


