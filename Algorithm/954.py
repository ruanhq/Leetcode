#954. Array of Doubled Pairs:
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        countsDict = collections.Counter(arr)
        for x in sorted(arr, key = abs):
            if countsDict[x] == 0:
                continue
            if 2 * x not in countsDict:
                return False
            countsDict[x] -= 1
            countsDict[2 * x] -= 1
        return True

#Which do not have most views from one of the video?
#
#
#
#marginal impacts / overall revenue(which part of the overall revenue in this scenario here?)

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        countsDict = collections.Counter(arr)
        for x in sorted(arr, key = abs):
            if countsDict[x] == 0:
                continue
            if 2 * x not in countsDict:
                return False
            countsDict[x] -= 1
            countsDict[2 * x] -= 1
        return True