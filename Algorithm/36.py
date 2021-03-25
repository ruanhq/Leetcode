#36. Valid Sudoku:
class Solution:
    def isOneRowValid(self, Row: List[str]) -> bool:
        Row = [element for element in Row if element != "."]
        return (len(Row) == len(set(Row)))
    def checkRowWiseValid(self, board) -> bool:
        for row in board:
            if !self.isOneRowValid(row):
                return False
        return True
    def checkColumnWiseValid(self, board) -> bool:
        for col in zip(*board):
            if !self.isOneRowValid(col):
                return False
        return True    
    def blockWiseValid(self, board) -> bool:
        i = 0
        j = 0
        for i in range(0, 3, 6):
            for j in range(0, 3, 6):
                squares = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if !self.isOneRowValid(squares):
                    return False
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    	a1 = self.blockWiseValid(board)
    	a2 = self.checkColumnWiseValid(board)
    	a3 = self.checkRowWiseValid(board)
    	return (a1 and a2 and a3)

#To get the row-wise element: for col in zip(*board)
#To get the col-wise element: for row in board
#square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
#[t for t in unit if t != "."] len(set(units)) == len(units)
#len(set(units)) == len(units)
#zip(*board), for row in board, for col in zip(*board)
#square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
#zip(*board), for row in board, for col in zip(*board)




