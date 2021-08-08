#1131. Maximum of absolute value expression:
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        points = []
        for i, (x, y) in enumerate(zip(arr1, arr2)):
            points.append([
                x + y + i,
                x - y + i,
                x - y - i,
                x + y - i
                ])
        result = max(max(currentList) for currentList in zip(*points))
        return result



