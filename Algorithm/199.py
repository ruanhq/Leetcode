#199. Binary Tree Right Side View

from collections import deque
class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
        currentLayerQueue = deque()
        currentLayerQueue.append(root)
        result = []
        while currentLayerQueue:
            for _ in range(len(currentLayerQueue)):
                currentNode = currentLayerQueue.popleft()
                if currentNode.left:
                    currentLayerQueue.append(currentNode.left)
                if currentNode.right:
                    currentLayerQueue.append(currentNode.right)
            result.append(currentNode.val)
        return result

from collections import deque

matrix = [[4,5,6], [7,8,9]]
for row in matrix:
    row.pop()


def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    n = len(matrix)
    result = []
    while matrix:
        result += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        if matrix and matrix[0] != "[]":
            result += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    return result


matrix = [[1],[2],[3]]
spiralOrder(matri)






