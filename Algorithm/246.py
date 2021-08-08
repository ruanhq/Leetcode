#246. Strobogrammatic Number:
#Here first, the digits should only include 0, 1, 6, 8, 9
#where in the reversed order 6 would become 9 and 9 would become 6.
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        reversedNumber = ""
        for i in reversed(range(num)):
            if num[i] == "1" or num[i] == "0" or num[i] == "8":
                reversedNumber += num[i]
            elif num[i] == "6":
                reversedNumber += "9"
            elif num[i] == "9":
                reversedNumber += "6"
            else:
                 return False
        return reversedNumber == num

#reconstruct the sequence from scratch here.

