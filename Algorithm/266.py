#266. Palindrome permutation:

dic = {}
    for item in s:
        dic[item] = dic.get(item, 0) + 1
    # return sum(v % 2 for v in dic.values()) < 2
    count1 = 0
    for val in dic.values():
        if val % 2 == 1:
            count1 += 1
        if count1 > 1:
            return False
    return True


from collections import defaultdict
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        dic = {}
        for item in s:
            dic[item] = dic.get(item, 0) + 1
        count1 = 0
        for val in dic.values():
            if val % 2:
                count1 += 1
            if count1 > 1:
                return False
        return True

#Whether the string can form a palindrome?
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        dics = {}
        for item in s:
            dics[item] = dics.get(item, 0) + 1
        count1 = 0
        for val in dics.values():
            if val % 2:
                count1 += 1
            if count1 > 1:
                return False #only at most one number allowed for 1-time occurrence.
        return True