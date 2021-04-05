#58. LengthOfLastWord
class Solution(object):
    def lengthOfLastWord(self, s):
        ind = len(s) - 1
        result = 0
        while ind >= 0 and s[ind] == " ":
            ind -= 1
        while ind >= 0 and s[ind] != " ":
            result += 1
            ind -= 1
        return result