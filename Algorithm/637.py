#637. Average of Levels in binary tree:
import numpy as np
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        result = []
        levels = []
        nextLevel = [root]
        while nextLevel:
            currentLevel = nextLevel
            nextLevel = []
            for node in currentLevel:
                levels.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            result.append(round(np.mean(levels), 5))
            levels = []
        return result