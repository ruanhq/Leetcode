#Topological Sort:
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        inDegree = {v: 0 for v in range(numCourses)}
        graphs = {v: [] for v in range(numCourses)}
        result = []
        SourceVertexList = []
        for i in prerequisites:
            parent, child = i[1], i[0]
            graphs[parent].append(child)
            inDegree[child] += 1
        for i in range(numCourses):
            if inDegree[i] == 0:
                SourceVertexList.append(i)
        while SourceVertexList:
            currentNode = SourceVertexList.pop()
            result.append(currentNode)
            for v in graphs[currentNode]:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    SourceVertexList.append(v)
        return len(result) == numCourses

class Graph():
    def __init__(self, nNode):
        self.graph = defaultdict(list)
        self.nNode = nNode
    def constructLink(self, u, v):
        self.graph[u].append(v)
    def topologicalSort(self):
        inDegree = {v: 0 for v in range(self.nNode)}
        SourceVertexList = []
        result = []
        for i in range(self.nNode):
            for v in self.graph[i]:
                parent, child = i, v
                inDegree[child] += 1
        for i in 
#assume max(u, v) = n,
#each of the u, v represent a number between 0 and n.
class Graph():
    def __init__(self, nNode):
        self.graph = defaultdict(list)
        self.nNode = nNode
    def constructLink(self, u, v):
        self.graph[u].append(v)
    def topologicalSort(self):
        inDegree = {v: 0 for v in range(self.nNode)}
        SourceVertexList = []
        result = []
        #construct a graph structure here:
        for i in range(self.nNode):
            for v in self.graph[i]:
                parent, child = i, v
                inDegree[child] += 1
        for i in range(self.nNode):
            if inDegree[i] == 0:
                SourceVertexList.append(i)
        while SourceVertexList:
            currentNode = SourceVertexList.pop()
            result.append(currentNode)
            for v in self.graph[currentNode]:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    SourceVertexList.append(v)
        if len(result) == self.nNode:
            return result
        else:
            print("Can't exhaust all of the nodes in the graph")
G1 = Graph(10)
G1.constructLink(9, 3)
G1.constructLink(7, 4)
G1.constructLink(5, 2)
G1.constructLink(6, 0)
G1.constructLink(8, 6)
G1.constructLink(2, 1)
G1.constructLink(4, 8)
G1.constructLink(3, 2)
G1.constructLink(4, 0)
G1.constructLink(5, 3)
G1.constructLink(6, 2)
G1.constructLink(7, 2)
G1.constructLink(5, 1)
G1.constructLink(4, 5)
G1.constructLink(5, 2)
G1.topologicalSort()

#may need to try different imbalanced ratio here.


from collections import defaultdict, OrderedDict, deque
D1 = defaultdict(int)
D2 = defaultdict(list)
D3 = OrderedDict()
D4 = deque()
D5 = deque()






#lasso: laplacian prior, ridge: gaussian prior
#why regularization l1/ l2 -> l3, l4: 
#add up the elements(L1)
#measure the length of arrow(L2)
#how many elements it has(L0)
#the largest element(L-infty)









