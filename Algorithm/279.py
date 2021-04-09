#279. PerfectSquares:
import numpy as np 
import math
class Solution(object):
    def numSquares(self, n):
        squareNumbers = [i ** 2 for i in range(0, int(math.sqrt(n) + 1))]
        resultList = [float("inf") for _ in range(n + 2)]
        resultList[0] = 0
        for i in range(1, n + 1):
            for square in squareNumbers:
                if i < square:
                    break
                resultList[i] = min(resultList[i], resultList[i - square] + 1)
        return resultList[-1]


def isPrime(n):
    i = int(math.sqrt(n))
    while i > 1:
        if n % i == 0:
            return False
        i -= 1
    return True