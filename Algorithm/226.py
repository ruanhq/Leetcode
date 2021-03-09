#226. Invert Binary Tree:
class Solution:
	def invertTree(self, root: TreeNode) -> TreeNode:
		if root:
			root.left, root.right = self.invertTree(root.right),
			self.invertTree(root.left)
		return root

#BFS:
class Solution:
	def invertTreeMethod2(self, root: TreeNode) -> TreeNode:
		queue = collections.deque([(root)])
		while queue:
			node = queue.popleft()
			if node:
				node.left, node.right = node.right, node.left
				queue.append(node.left)
				queue.append(node.right)
		return root

#DFS
class Solution:
	def invertTreeMethod3(self, root: TreeNode) -> TreeNode:
		stack = [root]
		while stack:
			node = stack.pop()
			if node:
				node.left, node.right = node.right, node.left
				stack.extend([node.right, node.left])
		return root



queu = collections.deque(["A1", "A2", "A3", "A4", "A5"])
queu.popleft()

stack = ["A1", "A2", "A3", "A4", "A5"]
stack.pop()
stack.extend(["A6", "A7"])
stack


class Solution:
	def invertTreeMethod3(self, root: TreeNode) -> TreeNode:
		stack = [root]
		while stack:
			node = stack.pop()
			if node:
				node.left, node.right = node.right, node.left
				stack.append(node.left)
				stack.append(node.right)
		return root






