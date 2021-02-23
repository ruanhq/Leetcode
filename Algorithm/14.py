#14. Longest Common Prefix:
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        zips = list(zip(*strs))
        pre_fix = ""
        for i in zips:
            if len(set(i)) == 1:
                pre_fix += i[0]
            else:
                break
        return pre_fix