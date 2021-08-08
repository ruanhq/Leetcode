#424. Longest Repeating Character Replacement:

from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqDict = defaultdict(int)
        maxFreq = 0
        result = 0
        left = 0
        n = len(s)
        i = 0
        while i < n:
            freqDict[s[i]] += 1
            maxFreq = max(maxFreq, freqDict[s[i]])
            if i - left + 1 - maxFreq > k:
                freqDict[s[left]] -= 1
                left += 1
            else:
                result = max(result, i - left + 1)
            i += 1
        return result


#Similar two-pointers problems:
#159, 380, 424

