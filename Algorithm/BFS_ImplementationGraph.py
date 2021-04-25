#BFS searching:
import collections 
from collections import defaultdict
class GraphBFSDFS(object):
    def __init__(self):
        self.graph = defaultdict(list)
        self.result = []
    def constructGraph(self, u, v):
        self.graph[u].append(v)
    def bfsSearch(self, s):
        currentQueue = []
        currentQueue.append(s)
        visited = [False] * max(self.graph + 2)
        result = []
        while currentQueue:
            currentNode = currentQueue.pop(0)
            visited[currentNode] = True
            result.append(currentNode)
            for node in self.graph[currentNode]:
                if not visited[node]:
                    currentQueue.append(node)
        return result
    def dfsSearch(self, s, visited):
        currentQueue = []
        visited.add(s)
        self.result.append(s)
        for neighbor in self.graph[s]:
            if neighbor not in visited:
                self.dfsSearch(neighbor, visited)
    def dfsSearch(self, s, visited):
        currentQueue = []
        visited.add(s)
        self.result.append(s)
        if len(visited) >= max(max(self.graph.keys()), max(self.graph.values())):
            return
        for neighbor in self.graph[s]:
        	if neighbor not in visited:
        		self.dfsSearch(neighbor, visited)
    def dfs(self, v):
        visited = set()
        self.dfsSearch(v, visited)
        return self.result


g = GraphBFSDFS()
g.constructGraph(2, 3)
g.constructGraph(3, 4)
g.constructGraph(5, 2)
g.constructGraph(3, 8)
g.constructGraph(6, 7)
g.constructGraph(8, 1)
g.constructGraph(5, 0)
g.constructGraph(4, 6)
g.constructGraph(8, 5)
g.dfs(8)
g.bfs(8)
g.bfs(8)



