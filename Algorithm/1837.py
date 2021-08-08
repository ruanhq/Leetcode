#1837. Sum of Digits in base K:
class Solution:
    def sumBase(self, n: int, k: int):
        result = 0
        #the residual after the base k would be the element at this digit:
        while n:
            n, remedi = divmod(n, k)
            result += remedi
        return result