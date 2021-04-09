#107. Binary Tree Level Order Traversal II:
class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return root
        next_level = [root]
        result = []
        while next_level:
            currentLevel = next_level
            result.append([])
            next_level = []

            for node in currentLevel:
                result[-1].append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
        return result[::-1]


