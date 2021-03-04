#3. Longest Substring without repeating characters:
#A pretty typical usage of the hashMap:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        hashMap = {}
        i = 0
        j = 0
        result = 0
        for j in range(n):
        	if s[j] in hashMap:
        		#refresh the starter!
        		i = max(hashMap(s[j]), i)
        	result = max(result, j - i + 1)
        	hashMap[s[j]] = j + 1
        return result




