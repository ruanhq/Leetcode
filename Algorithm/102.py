#102. BinaryTree Level Order Traversal:
class Solution:
    def levelOrder(self, root: TreeNode):
        result = []
        if not root:
            return []
        currentLevel = [root]
        while currentLevel:
            nextLevel = []
            result.append([node.val for node in currentLevel])
            for node in currentLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            currentLevel = nextLevel
        return result

