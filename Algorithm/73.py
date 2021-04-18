#73. Set Matrix Zeroes:
class Solution(object):
    def setZeroes(self, matrix):
        rowSet = ()
        colSet = ()
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rowSet.add(i)
                    colSet.add(j)
        for i in range(n):
            for j in range(m):
                if i in rowSet or j in colSet:
                    matrix[i][j] = 0
        return matrix


        for i in range(n):
            for j in range(m):
                