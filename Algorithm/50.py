#50. Pow(x, n):
class Solution:
    def myPow(self, x: floot, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
        	n = -n
        	x = 1/ x
        if n % 2 == 0:
            return self.myPow(x * x, n / 2)
        if n % 2 == 1:
            return x * self.myPow(x * x, n // 2)

#It requires the myPow(x*x, n//2), myPow(x*x, n/2)
