#topological sort:
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        stack.insert(0, v)
    def topologicalSort(self):
        visited = [False] * self.V 
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        print(stack)


g1 = Graph(6)
g1.addEdge(5, 2);
g1.addEdge(5, 0);
g1.addEdge(4, 0);
g1.addEdge(4, 1);
g1.addEdge(2, 3); 
g1.addEdge(4, 2); 
g1.topologicalSort()

g1 = Graph(6)
g1.addEdge(5, 2);
g1.addEdge(5, 0);
g1.addEdge(4, 0);
g1.addEdge(4, 1);
g1.addEdge(2, 3);
g1.addEdge(4, 2);
g1.topologicalSort()

class Solution:
    def canFinish(self, numCourses, prerequisites):
        prerGraph = {course:{} for course in range(numCourses)}
        counts = 0
        finishedCourseList = []
        for course, prereq in prerequisites:
            prerGraph[course][prereq] = True
        for course in range(numCourses):
            if not prerGraph[course]:
                finishedCourseList.append(course)

        while finishedCourseList:
            counts += 1
            finishedCourseList

























