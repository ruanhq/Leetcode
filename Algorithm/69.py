#69. Sqrt(x):

class Solution(object):
    def mySqrt(self, x):
        if x < 2:
            return x
        if x == 2:
            return 1
        low = 1
        high = x
        while low <= high:
            med = (low + high) // 2
            num = med * med 
            if num > x:
                high = med - 1
            elif num < x:
                low = med + 1
            else:
                return med 
        return high