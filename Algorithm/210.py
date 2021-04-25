#210 Course Schedule II:
from collections import deque
def findOrder(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """
    if prerequisites == []:
        return list(range(numCourses))
    result = []
    courseList = set([v for vlist in prerequisites for v in vlist])
    graphList = {v: [e[0] for e in prerequisites if e[1] == v] for v in courseList}
    #WLOG, start from the first element:
    visited = [False] * (numCourses + 2)
    NodeQueue = deque([0])
    while NodeQueue:
        currentcourse = NodeQueue.pop()
        if not visited[currentcourse]:
            result.append(currentcourse)
            visited[currentcourse] = True
        for v in graphList[currentcourse]:
            if not visited[v]:
                NodeQueue.append(v)
    return result if len(set(result)) == numCourses else []


numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

numCourses = 2
prerequisites = []
findOrder(numCourses, prerequisites)

findOrder(numCourses, prerequisites)



def findOrder(numCourses, prerequisites):
    inDegree = {v: 0 for v in range(numCourses)}
    graph = {v: [] for v in range(numCourses)}
    for pair in prereuisites:
        parent, child = pair[1], pair[0]
        inDegree[child] += 1
        graph[parent].append(child)
    sourceVertex = deque([])
    for v in inDegree:
        if inDegree[v] == 0:
            sourceVertex.append(v)
    result = []
    while sourceVertex:
        currentNode = sourceVertex.popleft()
        result.append(currentNode)
        for child in graph[currentNode]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sourceVertex.append(child)
    if len(result) == numCourses:
        return result 
    else:
        return []

def findOrder(numCourses, prerequisites):
    inDegree = {v: 0 for v in range(numCourses)}
    graph = {v: [] for v in range(numCourses)}
    for pair in prerequisites:
        parent, child = pair[1], pair[0]
        inDegree[child] += 1
        graph[parent].append(child)
    sourceVertex = deque([])
    for v in inDegree:
        if inDegree[v] == 0:
            sourceVertex.append(v)
    result = []
    while sourceVertex:
        currentNode = sourceVertex.popleft()
        result.append(currentNode)
        for child in graph[currentNode]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sourceVertex.append(child)
    if len(result) == numCourses:
        return result
    else:
        return []





















