#230. K-th smallest element in a BST:

#kthSmallest(node.left)
#1 <= k <= n <= 10^4
#0 <= Node.val <= 10^4
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(node):
            if node:
                return inorder(node.left) + [node.val] + inorder(node.right)
            else:
                return []
        inOrderSeq = inorder(root)
        return inOrderSeq[k - 1]

knn overfitting: smaller k may lead to severe overfitting here.
#batch prediction, online prediction and model monitoring ->

#support vector more overfit, 

#CI/CD pipeline here: automatic, scalable modeling pipeline here
#CICD pipeline here for automatic, scalable modeling pipeline here
class Solution:
    def kthSmallest(self, root: TreeNode):
        stacks = []
        while True:
            





