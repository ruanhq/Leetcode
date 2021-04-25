#Course Schedule:
from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        verticeSet = set([v for sublist in prerequisites for v in sublist])
        graph = {v: [e[1] for e in prerequisites if e[0] == v] for v in verticeSet}
        for v in verticeSet:
            bfs = deque(graph[v])
            visited = set()
            while bfs:
                current = bfs.pop()
                visited.add(current)
                if current == v:
                    return False
                for n in graph[current]:
                    if n not in visited:
                        bfs.appendleft(n)
        return True
    

    #BFS typical application.

#Breadth-first searching:
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
    #utilize a visit object to store the visiting status.
    def bfs(self, s):
        visited = [False] * (max(self.graph) + 2)
        queueCurrent = deque()
        queueCurrent.append(s)
        visited[s] = True
        result = []
        while queueCurrent:
            s = queueCurrent.pop(0)
            print(s, end = " ")
            result.append(s)
            for i in self.graph[s]:
                if visited[i] == False:
                    queueCurrent.appendleft(i)
                    visited[i] = True
########################
g = Graph()
g.addEdge(0, 1)
g.addEdge(1, 4)
g.addEdge(2, 3)
g.addEdge(1, 5)
g.addEdge(4, 2)
g.addEdge(3, 0)
g.bfs(3)
########################





