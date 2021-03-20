#1047. Remove all adjacent duplicates in string:
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stacks = []
        for chars in S:
            if stacks and chars == stacks[-1]:
                stacks.pop()
            else:
                stacks.append(chars)
        result = "".join(stacks)
        return result