#113. Path Sum II:
class Solution:
    def searchingTree(self, node, remaining, currentPath, result):
        if not node:
            return
        currentPath.append(node.val)
        if remaining == node.val and not node.left and not node.right:
            result.append(list(currentPath))
        else:
            self.searchingTree(node.left, remaining - node.val, currentPath, result)
            self.searchingTree(node.right, remaining - node.val, currentPath, result)
        currentPath.pop()

    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        result = []
        self.searchingTree(root, targetSum, [], result)
        return result

