#463.py
#Island perimeter:
#only count positive direction counting.
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n_r = len(grid)
        n_c = len(grid[0])
        result = 0
        for i in range(n_r):
            for j in range(n_c):
                if(grid[i][j] == 1):
                    result += 4
                    if (i > 0 and grid[i - 1][j] == 1):
                        result -= 2
                    if (j > 0 and grid[i][j - 1] == 1):
                        result -= 2
        return result