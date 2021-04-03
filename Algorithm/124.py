#124. Binary Tree Maximum PathSum:
class Solution(object):
    def maxSum(self, node):
        if not node:
            return -sys.maxint
        leftSum = max(self.maxSum(node.left), 0)
        rightSum = max(self.maxSum(node.right), 0)
        newPathSum = node.val + leftSum + rightSum
        self.currentResult = max(
        self.currentResult, node.val + leftSum + rightSum)
        return node.val + max(leftSum, rightSum)

    def maxPathSum(self, root):
        self.currentResult = -sys.maxint
        self.maxSum(root)
        return self.currentResult

#OrderedDict().move_to_end(key)
class Solution(object):
    def maxSum(self, node):
        if not node:
            return -sys.maxint




