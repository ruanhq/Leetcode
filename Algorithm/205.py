#205. Isomorphic Strings:

class Solution(object):
    def isIsomorphic(self, s, t):
        hash1 = {}
        hash2 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in hash2 and hash2[s[i]] != t[i]:
                return False
            if t[i] in hash1 and hash2[t[i]] != s[i]:
                return False
            hash1[s[i]] = t[i]
            hash2[t[i]] = s[i]
        return True

#To test whether two strings are isomorphic:
def isIsomorphic(self, s, t):
    d1 = [[] for _ in range(1000)]
    d2 = [[] for _ in range(1000)]
    for i, val in enumerate(s):
        d1[ord(val)].append(i)
    for i, val in enumerate(t):
        d2[ord(val)].append(i)
    return sorted(d1) == sorted(d2)


def isIsomorphic(self, s, t):
    ss1 = [s.find(i) for i in s]
    ss2 = [t.find(j) for j in t]
    return ss1 = ss2

#
map(s.find, s) == map(t.find, t)
[s.find(i) for i in s] == [t.find(j) for j in t]
len(set(zip(s, t))) == len(set(s)) == len(set(t))

def isIsomorphicMore(self, s, t):
    d1, d2 = [0 for _ in range(1000)], [0 for _ in range(1000)]
    for i in range(len(s)):
        if d1[ord(s[i])] != d2[ord(t[i])]:
            return False
        d1[ord(s[i])] = i + 1
        d2[ord(t[i])] = i + 1
    return True

def isIsomorphicMore(self, s, t):
    d1, d2 = [0 for _ in range(10000)], [0 for _ in range(10000)]
    for i in range(len(s)):
        if d1[ord(s[i])] != d2[ord(t[i])]:
            return False
        d1[ord(s[i])] = i + 1
        d2[ord(t[i])] = i + 1
    return True

class Solution(object):
    def depthSum(self, nestedList):
        def DFS(nestedList, depth):
            currentSum = 0
            for member in nestedList:
                if member.isInteger():
                    currentSum += member.getInteger() * depth 
                else:
                    currentSum += DFS(member.getList(), depth + 1)
            return currentSum
        return DFS(nestedList, 1)

s1 = [-1, 2, -4, 12, -25, 100]
result = [None] * len(s1)
low = 0
high = len(s1) - 1
for k in reversed(range(len(s1))):
    if s1[low] <= s1[high]:
        result[k] = s1[high]
        high -= 1
    else:
        result[k] = s1[low]
        low += 1
result



from functools import lru_cache
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(None)
        def relation(i, j):
            if i == j:
                return 1
            elif i > j:
                return 0
            if s[i] == s[j]:
                return 2 + relation(i + 1, j - 1)
            else:
                return max(relation(i + 1, j), relation(i, j - 1))
        s1 = list(s)
        return relation(0, len(s1) - 1)



#Palindrome Substrings:
class Solution:
    def countSubstrings(self, s: str) -> int:
        low = 0
        right = len(s)
        for i in range(len(s)):
            for a, b in [(i, i), (i, i + 1)]:
                while a >= 0 and b < L and s[a] == s[b]:
                    a -= 1
                    b += 1
                r += (b - a) // 2
        return r
























