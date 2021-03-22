#1663. Smallest string with a given numeric value:
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result = ['a'] * n
        for i in range(n):
            if (n - i - 1) * 26 >= k:
                result[i] = 'a'
                k -= 1
            else:
                addon = k - (n - i - 1) * 26
                result[i] = chr(96 + addon)
                k -= addon
        return "".join(chars for chars in result)
    
                
#Input the chars would be written as: chr(96 + 10)/ chr(96 + 15)
