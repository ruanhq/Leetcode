#64. MinimumPathSum:
class Solution(object):
    def minimumPathSum(self, grid):
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])
        resultDict = [["DOWN"] * m for _ in range(n)]
        for i in range(1, n):
            grid[i][0] = grid[i - 1][0] + grid[i][0]
            resultDict[i][0] = "DOWN"
        for j in range(1, m):
            grid[0][j] = grid[0][j - 1] + grid[0][j]
            resultDict[0][j] = "RIGHT"
        for i in range(1, n):
            for j in range(1, m):
            	if grid[i][j - 1] <= grid[i - 1][j]:
            	    resultDict[i][j] = "RIGHT"
            	    grid[i][j] = grid[i][j] + grid[i][j - 1]
            	else:
            	    resultDict[i][j] = "DOWN"
            	    grid[i][j] = grid[i][j] + grid[i - 1][j]
        resultSum = grid[n - 1][m - 1]
        rowPointer = n - 1
        colPointer = m - 1
        resultPath = []
        while rowPointer > 0 and colPointer > 0:
        	resultPath.append([rowPointer, colPointer])
            if grid[rowPointer][colPointer] == "DOWN":
                rowPointer -= 1
            else:
                colPointer -= 1
        return resultPath[::-1]






#Followup: Storing the minimum path sum here:
#If you want to finish the two tasks simultaneously, you may
#need another O(n * m) space.
def minimumPathSum(grid):
    if not grid:
        return 0
    n = len(grid)
    m = len(grid[0])
    resultDict = [["DOWN"] * m for _ in range(n)]
    for i in range(1, n):
        grid[i][0] = grid[i - 1][0] + grid[i][0]
        resultDict[i][0] = "DOWN"
    for j in range(1, m):
        grid[0][j] = grid[0][j - 1] + grid[0][j]
        resultDict[0][j] = "RIGHT"
    for i in range(1, n):
        for j in range(1, m):
            if grid[i][j - 1] <= grid[i - 1][j]:
                resultDict[i][j] = "RIGHT"
                grid[i][j] = grid[i][j] + grid[i][j - 1]
            else:
                resultDict[i][j] = "DOWN"
                grid[i][j] = grid[i][j] + grid[i - 1][j]
    resultSum = grid[n - 1][m - 1]
    rowPointer = n - 1
    colPointer = m - 1
    resultPath = []
    while rowPointer > 0 and colPointer > 0:
        resultPath.append([rowPointer, colPointer])
        if grid[rowPointer][colPointer] == "DOWN":
            rowPointer -= 1
        else:
            colPointer -= 1
    if rowPointer == 0:
        for j in range(colPointer, -1, -1):
            resultPath.append([0, j])
    elif colPointer == 0:
        for j in range(rowPointer, -1, -1):
            resultPath.append([j, 0])
    return resultPath[::-1]


minimumPathSum([[1,3,1],[1,5,1],[4,2,1]])









