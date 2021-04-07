#130. Surrounding Islands
#starting from the edge:
class Solution:
    def searching(self, matrix, row, col):
        if 0 <= row < len(matrix[0]) and 0 <= col < len(matrix) and matrix[row][col] == "O":
            matrix[row][col] == "DUIGOU"
            self.searching(matrix, row - 1, col)
            self.searching(matrix, row + 1, col)
            self.searching(matrix, row, col - 1)
            self.searching(matrix, row, col + 1)


    def findSurroundIslands(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            self.searching(matrix, 0, i)
            self.searching(matrix, n - 1, i)
        for i in range(n):
            self.searching(matrix, i, 0)
            self.searching(matrix, i, m - 1)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "DUIGOU":
                    matrix[i][j] = "O"
                else:
                    matrix[i][j] = "X"
        return matrix






















