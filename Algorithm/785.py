#785. Graph Bipartite:
#Graph coloring
from collections import deque
#BFS:
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colorList = {}
        for fromNode in range(len(graph)):
            if fromNode in colorList:
                continue
            currentQueue = deque([fromNode])
            colorList[fromNode] = 1
            while currentQueue:
                currentNode = currentQueue.popleft()
                for toNode in graph[currentNode]:
                    if toNode in colorList:
                        if colorList[toNode] == colorList[currentNode]:
                            return False
                    else:
                        currentQueue.append(toNode)
                        colorList[toNode] = colorList[currentNode] * (-1)
        return True
#DFS -> graph coloring list.
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colorList = {}
        currentStack = []
        for node in range(len(graph)):
            if node in colorList:
                continue
            currentStack = [node]
            colorList[node] = 1
            while stack:
                currentNode = stack.pop()
                for toNode in graph[currentNode]:
                    if toNode in colorList:
                        if colorList[toNode] == colorList[currentNode]:
                            return False
                    else:
                        stack.append(toNode)
                        colorList[toNode] = colorList[currentNode] * (-1)
        return True













