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

