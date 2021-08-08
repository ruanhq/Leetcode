#542. 01-matrix:
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def bfs(node):
            q = deque()
            i, j = node
            q.append((i, j), 0)
            visited = set()
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while q:
                for nodes in q:
                    coord, d = q.popleft()
                    x, y = coord
                    if matrix[x][y] == 0:
                        return d
                    visited.add(coord)
                    for dire in dirs:
                        newX, newY = x + dire[0], y + dire[1]
                        if newX >= 0 and newX <= len(matrix) - 1 and newY >= 0 and newY <= len(matrix[0]) - 1 and (newX, newY) not in visited:
                            q.append(((newX, newY), d + 1))
            return -1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                d = bfs((i, j))
                matrix[i][j] = d
    return matrix


#bfs searching through 4 different directions here.
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def bfs(node):
            q = deque()
            i, j = node
            q.append((i, j), 0)
            visited = set()
            while q:
                for i in range(len(q)):
                    coord, d = q.popleft()
                    x, y = coord
                    if mat[x][y] == 0:




while q:
    for nodes in q:
        coord, d = q.popleft()
        x, y = coord
        if mat[x][y] == 0:
            return d
        visited.add(coord)
        for dire in dirs:
            newX, newY = x + dire[0], y + dire[1]
            if newX >= 0 and newX <= len(mat) and newY >= 0 and newY <= len(mat[0]) and (newX, newY) not in visited:
                q.append(((newX, newY), d + 1))
return 0

for i in range(len(mat)):
    for j in range(len(mat[0])):
        d = bfs((i, j))
        matrix[i][j] = d 
return matrix


#bfs((i, j))
for i in range(len(mat)):
    for j in range(len(mat[0])):
        d = bfs((i, j))
        matrix[i][j] = d










