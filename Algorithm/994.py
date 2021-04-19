#994. Rotting Oranges:
#O(V + E)
from collections import deque
class Solution(object):
    def orangeRotting(self, grid):
        if not grid:
            return 0
        freshCount = 0
        steps = 0
        rottenOrange = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rottenOrange.append((i, j))
                elif grid[i][j] == 1:
                    freshCount += 1
        while rottenOrange and freshCount > 0:
            steps += 1
            for _ in range(len(rottenOrange)):
                x1, y1 = rottenOrange.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    xx1 = x1 + dx 
                    yy1 = y1 + dy
                    if xx1 < 0 or xx1 == len(grid) or yy1 < 0 or yy1 == len(grid[0]):
                        continue
                    if grid[xx1][yy1] == 0 or grid[xx1][yy1] == 2:
                    	continue
                    freshCount -= 1
                    grid[xx1][yy1] = 2
                    rottenOrange.append((xx1, yy1))
        if freshCount == 0:
            return -1
        else:
            return steps


#To control the direction:
directionList = [(1,0), (0, 1), (-1, 0), (0, -1)]
for xx, yy in directionList:
    xx1 = x1 + xx
    yy1 = y1 + yy

#BFS重点突破.

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2) + fib(n - 3)
#Construct a sentinel node and the link it next to the head,
#Then you may want to return this node.


@lru_cache(maxsize = 10)
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return fib(n - 1) + fib(n - 2) + fib(n - 3)


#Making it rotton:
#for nodes adjacent to the leftMost one: make all of them rotton
#then push the new rotton ones in the current queue.
@lru_cache(maxsize = 10)
def fib(n):
    if n == 0:
        return 0
    if n == 1:
    	return 1
    if n == 2:
        return 2
    return fib(n - 1) + fib(n - 2) + fib(n - 3)










