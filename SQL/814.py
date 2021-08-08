#814. Binary Tree Pruning:
class Solution:
    def pruneTree(self, root: TreeNode):
        def checkOneElement(node):
            if not node:
                return False
            leftCheck = checkOneElement(node.left)
            rightCheck = checkOneElement(node.right)
            if not leftCheck:
                node.left = None
            if not rightCheck:
                node.right = None
            if node.val == 1 or leftCheck or rightCheck:
                return True
            else:
                return False

        result = checkOneElement(root)
        if result:
            return root
        else:
            return None

online one important feature missing, you cannot train the model again:
create a mask(update the model?) -> impute the missing values.

class Solution:
    def pruneTree(self, root: TreeNode):
        if not root:
            return None
        if root.val == 0 and not root.left and not root.right:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.val == 0 and not root.left and not root.right:
            return None
        return root




#面经列表:
feature importance types: weights, information gain, covers.
weights: total occurrences in the trees
information gain, covers,




class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
    	#if the root is zero, root have no left/ right children:
    	#return None
        if not root:
            return None
        if root.val == 0 and not root.left and not root.right:
            return None
        #Making root.left/ root.right None or result.
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.val == 0 and not root.left and not root.right:
            return None
        return root

























