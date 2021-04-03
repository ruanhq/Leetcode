#8. StringToInteger(atoi)
class Solution(object):
    def myAtoi(self, s):
        nStr = len(s)
        if nStr == 0:
            return 0
        result = 0
        sign = 0
        i = 0
        maxInt = 2 ** 31 - 1
        minInt = - 2 ** 31 
        indices = 0
        while i < nStr and s[i] == " ":
            i += 1
        while i < nStr and (s[i] == "+" or s[i] == "-"):
            if indices > 0:
                return 0
            if s[i] == "+":
                sign = 1
            else:
                sign = -1
            indices += 1
        while i < nStr and ord(s[i]) <= "9" and ord(s[i]) >= "0":
            if result > maxInt / 10 or 
            (result == maxInt/ 10 and ord(s[i]) - ord("0") > maxInt % 10):
                if sign == 1:
                    return maxInt
                else:
                    return minInt
            result = result * 10 + ord(s[i]) - ord("0")
            i += 1
        return result * sign




