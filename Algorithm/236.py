#236. Lowest Common Ancestor of a binary tree:
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        stack = [root]
        parent = {root: None}
        