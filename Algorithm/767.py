#767. Reorganize String:
from collections import Counter
class Solution(object):
    def reorganizeString(self, S):
        n = len(S)
        ctSorted = sorted(Counter(S).items(), key = lambda X: X[1],
        reverse = True)
        reOrderStr = []
        for key, value in ctSorted:
            if value > (n + 1)/ 2:
                return ""
            reOrderStr.extend(value * key)
        result = [None] * n
        if n % 2 == 0:
            middle = n / 2
            for j in range(middle):
                result[2 * j] = reOrderStr[j]
                result[2 * j + 1] = reOrderStr[j + middle]
        else:
            middle = (n// 2 + 1)
            for j in range(middle):
                result[2 * j] = reOrderStr[j]
            for j in range(1, middle):
                result[2 * j - 1] = reOrderStr[middle + j - 1]
        return "".join(result)



