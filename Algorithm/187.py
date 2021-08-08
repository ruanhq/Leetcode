#187. Repeated DNA sequences:
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        n = len(s)
        hash1 = set()
        hash2 = []
        for i in range(n - 9):
            curStr = s[i : (i + 10)]
            if curStr not in hash1:
                hash1.add(curStr)
            else:
                if curStr not in hash2:
                    hash2.append(curStr)
        return hash2

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        n = len(s)
        hash1 = set()
        hash2 = []
        for i in range(n - 9):
            curStr = s[i : (i + 10)]
            if curStr not in hash1:
                hash1.add(curStr)
            else:
                if curStr not in hash2:
                    hash2.append(curStr)
        return hash2




