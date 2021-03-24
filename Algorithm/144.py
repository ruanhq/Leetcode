#144. Binary Tree Preorder Traversal:
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        currentLayer = [root]
        result = []
        while currentLayer:
            current_node = currentLayer
            if current_node:
                result.append(current_node.val)
                currentLayer.append(current_node.right)
                currentLayer.append(current_node.left)
        return result


