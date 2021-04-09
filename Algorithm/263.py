#263- UglyNumber
import math
class Solution(object):
    def isUgly(self, n):
        if n <= 0:
            return False
        elif n == 1:
            return True

        while n > 1:
            if n % 2 == 0:
                n = n // 2
            elif n % 3 == 0:
                n = n // 3
            elif n % 5 == 0:
                n = n //5
            elif isPrime(n) or n >= 6:
                return False
        return True