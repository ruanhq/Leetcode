#366. Find Leaves of binary tree:
from collections import defaultdict
class Solution:
    def findLeaves(self, root: TreeNode):
        result = []
        def searching(node, layer):
            if not node:
                return layer
            leftDepth = searching(node.left, layer)
            rightDepth = searching(node.right, layer)
            maxDepth = max(leftDepth, rightDepth)
            result[layer].append(node.val)
            return (layer + 1)
        searching(root, 0)
        return result
