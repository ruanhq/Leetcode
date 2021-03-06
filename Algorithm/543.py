#543. Diameter of binary tree:
class Solution:
	def diameterOfBinaryTree(self, root: TreeNode) -> int:
		self.diameter = 0
		def getDepth(node):
			if not node:
				return 0
			L1 = getDepth(node.left)
			R1 = getDepth(node.right)
			self.diameter = max(self.diameter, L1 + R1)
			return max(L1, R1) + 1
		result = getDepth(root)
		return self.diameter