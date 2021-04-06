#59. Spiral Matrix II

class Solution(object):
    def generateMatrix(self, n):
        if n == 1:
            return [[1]]
        if n == 0:
            return []
        matrix = [[0] * n for _ in range(n)]
        currentNumber = 1
        curDirec = 1
        left = top = 0
        right = bottom = n - 1
        while left <= right and top <= bottom:
            if curDirec == 1:
                for i in range(left, right + 1):
                    matrix[top][i] = currentNumber
                    currentNumber += 1
                top += 1
                curDirec = 2
            elif curDirec == 2:
                for i in range(top, bottom + 1):
                    matrix[i][right] = currentNumber
                    currentNumber += 1
                right -= 1
                curDirec = 3
            elif curDirec == 3:
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = currentNumber
                    currentNumber += 1
                bottom -= 1
                curDirec = 4
            elif curDirec == 4:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = currentNumber
                    currentNumber += 1
                left += 1
                curDirec = 1
        return matrix

