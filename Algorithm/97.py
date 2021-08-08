#97. Interleaving string:
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1Count = len(s1)
        s2Count = len(s2)
        s3Count = len(s3)
        historyDict = [[False] * (s1Count + 1) for _ in range(s2Count + 1)]
        if s1Count + s2Count != s3Count:
        	return False
        for i in range(s1Count):
        	for j in range(s2Count):
        	    if i == 0 and j == 0:
        	        historyDict[i][j] = True
        	    elif i == 0:
        	        historyDict[i][j] = (historyDict[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        	    elif j == 0:
        	        historyDict[i][j] = (historyDict[i - 1][j] and s1[i - 1] == s3[i + j - 1])
        	    else:
        	        historyDict[i][j] = (historyDict[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or
        	        (historyDict[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        result = historyDict[s1Count][s2Count]
        return result



