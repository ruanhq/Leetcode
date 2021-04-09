#204. CountPrimes:
class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        result = [True] * n
        result[0] = result[1] = False
        for i in range(2, n):
            for j in range(i * i, n, i):
                result[j] = False
        return sum(result)




