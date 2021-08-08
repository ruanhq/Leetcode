#226.Invert Binary Tree:
class Solution:
    def invertTree(self, root: TreeNode):
        if root is None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


class Solution:
    def invertTree(self, root: TreeNode):
        if root is None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root



class Solution:
    def permute(self, nums):
        result = []
        def searching(m):
            if m == len(nums):
                result.append(nums[:])
            for i in range(m, len(nums)):
                nums[i], nums[m] = nums[m], nums[i]
                searching(m + 1)
                nums[i], nums[m] = nums[m], nums[i]
        searching(0)
        return result
