#130. Surrounding Islands

class Solution(object):
    def searching(self, board, row, col):
        if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == "O":
            board[row][col] = "DUIGOU"
            self.searching(board, row + 1, col)
            self.searching(board, row - 1, col)
            self.searching(board, row, col - 1)
            self.searching(board, row, col + 1)

    def solve1(self, board):
        if not board or not board[0]:
            return
        for i in range(len(board[0])):
            self.searching(board, 0,i)
            self.searching(board, len(board) - 1, i)
        for j in range(len(board)):
            self.searching(board, j, 0)
            self.searching(board, j, len(board[0]) - 1)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "DUIGOU":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
        return board
























