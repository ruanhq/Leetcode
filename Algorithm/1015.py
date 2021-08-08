#1015. Smallest Integer Divisible by K:
#n only contains 
#First if k is an even number, return -1
#Then k = 17: 
#divide by 17, 
#111 = 11 * 10 + 1
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        c = 1
        m = 1
        while True:
            if m % k == 0:
                return c
            c += 1
            m = (10 * m + 1)
        return -1
#11 = 1 * 10 + 1 ()
#111 = 11 * 10 + 1 ()
#1111 = 111 * 10 + 1 ()
#11111 = 1111 * 10 + 1 ()
#111111 = 11111 * 10 + 1 ()
#1111111 = 111111 * 10 + 1 ()
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        c = 1
        m = 1
        while True:
            if m % k == 0:
                return c
            c += 1
            m = (10 * m + 1)
        return -1





#So the remainder of m divided by k is 