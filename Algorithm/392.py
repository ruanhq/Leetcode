#392. Is_Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t)
        indice_n2 = 0
        indice_n1 = 0
        if not s:
            return True
        while indice_n2 < n2:
            if s[indice_n1] == t[indice_n2]:
                indice_n1 += 1
                indice_n2 += 1
            else:
                indice_n2 += 1
            if indice_n1 == n1:
                return True
        return False
        