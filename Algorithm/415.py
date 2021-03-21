#415. Add Strings:
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        n_1 = len(num1) - 1
        n_2 = len(num2) - 1
        while n_1 >= 0 or n_2 >= 0:
            x_1 = ord(num1[n_1]) - ord('0') if n_1 >= 0 else 0
            x_2 = ord(num2[n_2]) - ord('0') if n_2 >= 0 else 0
            value = (x_1 + x_2 + cy) % 10
            cy = (x_1 + x_2 + cy) // 10
            res.append(value)
            n_1 = n_1 - 1
            n_2 = n_2 - 1

        if cy:
        	res.append(cy)
        return ''join(str(x) for x in res[::-1])

