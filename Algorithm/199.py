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
    #pop the elements by orders:
    while matrix:



matrix = [[1],[2],[3]]
spiralOrder(matri)

if matrix and matrix[0] != "[]"




