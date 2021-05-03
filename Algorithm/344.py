#344. Reverse String
class Solution(object):
    def reverseString(self, strs):
        i1, i2 = 0, len(strs) - 1
        while i1 < i2:
            strs[i2], strs[i1] = strs[i1], strs[i2]
            i2 -= 1
            i1 += 1
        return strs