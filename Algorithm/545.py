#545. Boundary Binary Tree:
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        def is_leaf(node: TreeNode):
            if not node:
                return False
            if node and not node.left and not node.right:
                return True

        def leftBoundary(node: TreeNode, result: List[int]):
        	curResult = []
            while node:
                if not is_leaf(node):
                    curResult.append(node.val)
                if node.left:
                    node = node.left
                else:
                	node = node.right
            result += curResult[::-1]

        def rightBoundary(node: TreeNode, result: List[int]):
            while node:
                if not is_leaf(node):
                    result.append(node.val)
                if node.right:
                    node = node.right
                else:
                    node = node.left
        boundaryResult = []

        def LeavesAppend(node: TreeNode, result: List[int]):
        	if not is_leaf(node):
        	    boundaryResult.append(root.val)
            if node.left:
        	    LeavesAppend(node.left):
            if node.right:
                LeavesAppend(node.right)
        if is_leaf(node):
            

        leftBoundary(root.left, boundaryResult)
        leavesAppend(root, boundaryResult)
        rightBoundary(root.right, boundaryResult)
        return boundaryResult



