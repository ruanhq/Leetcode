#695. Max area of island::
#Island category questions: requiring an indicator of
#whether we have seen it.
class Solution:
	def maxAreaofIsland(self, grid: List[List[int]]) -> int:
		n_r = len(grid)
		n_c = len(grid)
		seen_indicator = set()
		def area(i, j):
			if(i < 0 or i >= n_r or j < 0 or j >= n_c 
				or
               (i, j) in seen_indicator or grid[i][j] == 0):
			return 0
			seen_indicator.add((i, j))
			this_area = 1 + area(i, j+1) + area(i, j-1) +
			area(i-1,j) + area(i+1,j)
			return this_area
		return max(area(r, c)
			for r in range(n_r) for c in range(n_c))