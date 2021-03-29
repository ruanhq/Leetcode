#470. Rand10() using Rand7()
class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        value = 55
        while value >= 40:
            x1 = rand7()
            x2 = rand7()
            value = x1 - 1 + (x2 - 1) * 7
        
        residual = value % 10 + 1
        return residual
    