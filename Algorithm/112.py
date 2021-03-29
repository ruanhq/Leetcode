#112. Path Sum:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def search(node: TreeNode, remaining):
            if node is None:
                return False
            #getting to the root.
            if node and not node.left and not node.right:
                return node.val == remaining
            else:
                return search(node.left, remaining - node.val) or search(node.right, remaining - node.val)
        if root is None:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        return search(root.left, targetSum - root.val) or search(root.right, targetSum - root.val)
    
    