#168. Excel Sheet Column Title:
class Solution(object):
    def convertToTitle(self, columnNumber):
        capitalList = [chr(x) for x in range(ord("A"), ord("Z") + 1) ]
        result = ""
        while columnNumber > 0:
            result += capitalList[(columnNumber - 1) % 26]
            columnNumber = ((columnNumber - 1) // 26)
        return result[::-1]