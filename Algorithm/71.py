#71. Simplify path, just stack.
#Canonical Path here.
class Solution:
    def simplifyPath(self, path: str) -> str:
        resultList = path.split("/")
        currentListStack = []
        for c in resultList:
            if c == "..":
                if currentListStack:
                    currentListStack.pop()
            elif c == "." or not c:
                continue
            else:
                currentListStack.append(c)
        result = "/" + str("/".join(currentListStack))
        return result

