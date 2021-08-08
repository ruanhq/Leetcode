#99. recover Binary tree:
class Solution:
    def recoverTree(self, root: TreeNode):
    	#return the inorder traversal of the current binary searching tree.
        def inorder(r: TreeNode):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        def findSwapping(nums: List[int]):
            n = len(nums)
            x = y = -1
            for i in range(n - 1):
                if nums[i + 1] < nums[i]:
                    y = nums[i + 1]
                    if x == -1:
                        x = nums[i]
                    else:
                        break
            return x, y

        def recover(r: TreeNode, count: int):
            if r:
                if r.val == x or r.val == y:
                    r.val = y if r.val == x else x
                    count -= 1
                    if count == 0:
                        return
                 recover(r.left, count)
                 recover(r.right, count)
        #first using the inorder traversal of the binary tree, and it should be monotonically increasing or their will be a swap.
        nums = inorder(root)
        x, y = findSwapping(nums)
        recover(root, 2)
################
[1, 3, 2, 4]
[1, 2, 3]

[4, 2, 3, 1]
[1, 3, 2, 4]
[2, 1, 3]

class Solution:
    def recoverTree(self, root: TreeNode):
        def inorder(r: TreeNode):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        def findSwapping(nums: List[int]):
            n = len(nums)
            x = y = -1 
            for i in range(n - 1):
                if nums[i + 1] < nums[i]:
                    y = nums[i + 1]
                    if x == -1:
                        x = nums[i]
                    else:
                        break
            return x, y
        #count records the number of elements yet to remove.
        def recover(r: TreeNode, count: int):
            if r:
                if r.val == x or r.val == y:
                    r.val = y if r.val == x else x
                    count -= 1
                    if count == 0:
                        return
                recover(r.left, count)
                recover(r.right, count)
        #Then grab from scratch
        nums = inorder(root)
        x, y =findSwapping(nums)
        recover(root, 2)











