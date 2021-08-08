#大厂算法题列表

#linkedin: https://1o24bbs.com/t/topic/12345
#apple: https://1o24bbs.com/t/topic/12344
#

class Solution(object):
    def topologicalSort(self, numCourses, verT):
    	VertexList = set([v for lists in verT for v in lists])
        inDegree = {v: 0 for v in range(numCourses)}
        graphs = {v: [] for v in range(numCourses)}
        SourceVertex = []
        result = []
        for i in verT:
            parent, child = i[1], i[0]
            graphs[parent].append(child)
            inDegree[child] += 1
        for i in range(numCourses):
            if inDegree[i] == 0:
                SourceVertex.append(i)
        while SourceVertex:
            currentNode = SourceVertex.pop()
            result.append(currentNode)
            for v in graphs[currentNode]:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    SourceVertex.append(v)
        return len(result) == numCourses


from collections import defaultdict, Orderedict

D1 = defaultdict(int)
D2 = defaultdict(list)
D3 = Orderedict()

def findEndingIndex(self, nums, target):
    index = -1
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            low = mid + 1
            index = mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return index
