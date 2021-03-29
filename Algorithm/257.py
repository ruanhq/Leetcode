#257. Binary Tree Paths:
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def searching(node, currentPath, result):
            if node:
            	currentPath += str(node.val)
            	if not node.left and not node.right:
            	    result.append(currentPath)
            	    return
            	else:
            	    currentPath += "->"
            	    searching(node.left, currentPath, result)
            	    searching(node.right, currentPath, result)
            else:
            	return

        result = []
        searching(root, "", result)
        return result
        
