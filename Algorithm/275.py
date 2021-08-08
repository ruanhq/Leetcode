#275. H-index II:
[6, 5, 3]
[6, 5, 2, 1, 0]
-> h-index: will return 2(no matter whether they are smaller)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        i = 0
        n = len(citations)
        while i < n and citations[i] > i:
            i += 1
        return i




