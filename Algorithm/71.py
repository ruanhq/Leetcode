#71. Simplify path, just stack.
class Solution:
    def simplifyPath(self, path: str) -> str:
        pathStack = []
        directoryList = path.split("/")
        for slices in directoryList:
            if slices == ".." and pathStack:
                pathStack.pop()
            elif slices == "." or not slices:
                continue
            else:
                pathStack.append(slices)
        result = "/" + "/".join(pathStack)
        return result
