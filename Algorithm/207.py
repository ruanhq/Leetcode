#207. Course Schedule:
#####

#First doing the depth-first search for the directed graph:

def depthFirstSearch(listNodes: List[List[int]]):
    


#Topological Sort:拓扑排序:

prer_graph = {course: {} for course in range(8)}
counts = 0
finished_course_list = []
for course, prer in prerequisites:
    prer_graph[course][prer] = True

for course in range(numCourses):
    if not prer_graph[course]:
        finished_course_list.append(course)

while finished_course_list:
    counts += 1
    finished_course = finished_course_list.pop()
    for course, prers in prer_graph.iteritems():
        if finished_course in prers:
            del prers[finished_courses]
            if len(prers) == 0:
                finished_course_list.append(course)

return counts == numCourses


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        graph = [[] for _ in range(n)]
        g = [0] * n
        for v, u in prerequisites:
            graph[u].append(v)
            g[v] += 1
        S = [ v for v in range(n) if g[v] == 0]
        while S:
            u = S.pop()
            for v in graph[u]:
                g[v] -= 1
                if g[v] == 0:
                    S.append(v)
        return not any(g)


(SELECT E.*, DENSE_RANK() OVER(PARTITION BY DepartmentId ORDER BY Salary DESC) AS deptRank 
FROM Employee AS E) AS A


















