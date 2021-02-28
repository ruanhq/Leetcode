#200. Number of islands:
def numIslands(self, grid: List[List[str]]) -> int:
	if len(grid) == 0:
		return 0
	m = len(grid)
	n = len(grid[0])
	count = 0
	def graph_searching(grid, x, y):
		if grid[x][y] == '0':
			return
		grid[x][y] = '0'
		if x != 0:
			graph_searching(grid, x - 1, y)
		if x != m - 1:
			graph_searching(grid, x + 1, y)
		if y != 0:
			graph_searching(grid, x, y - 1)
		if y != n - 1:
			graph_searching(grid, x, y + 1)

	for i in range(m):
		for j in range(n):
			if grid[i][j] == '1':
				graph_searching(grid, i, j)
				count += 1
	return count



