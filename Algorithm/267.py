#267. Palindrome Permutation II:

from collections import defaultdict
class Solution:
    def generatePalindromes(self, s: str):
        hashMaps = {}
        for item in s:
            hashMaps[item] = hashMaps.get(item, 0) + 1

    def backtracking(self, s, index, mid, ans):
        if index == len(s) - 1:
            return ans
        for i in range(index, len(s)):
            if i >= 1 and s[i] == s[i - 1] and s[i - 1] == s[index]:
                continue
            if i != index:
                perMu = s[:index] + s[i] + s[index+1: i] + s[index] + s[i + 1:]
                result.append(perMu + mid + permu[::-1])
            else:
            	perMu = s
            self.backtracking(perMu, index + 1, mid ,ans)
        return ans


######


"""
1. post duplicate messages over multiple accounts or multiple duplicate messages on one account
2. following/unfollowing large number of accounts in a short time
3. having large number of spam complaints filed against the account
4. aggressively liking/ following and retweeting
5. posting malicious links.
6. posting tweets which mainly consists of links instead of 
posting personal updates.
7. posting unrelated tweets to a trending topic to determine what conduct is considered to be spamming.

Spam detection is based on both user-centric and url-centric.
"""



