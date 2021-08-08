#235. Lowest Common Ancestor of a Binary Search Tree:

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        parentVal = root.val
        pVal = p.val 
        qVal = q.val
        if pVal > parentVal and qVal > parentVal:
            return self.lowestCommonAncestor(root.right, p, q)
        elif pVal < parentVal and qVal < parentVal:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

#if the pVal and qVal is larger than the root, then the answer is in the 
#right subtree of root

#else: then the answer is in the left subtree

#In bst, the left subtree has elements less than the nodes element and 
#the right subtree has elements greater than the nodes element here.

#binary tree doesn't have this property that the left subtree must smaller than
#the root here.


#adding the data in November into the current datasets here

#adding the data in November into the current dataset here.

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        parentVal = root.val
        pVal = p.val
        qVal = q.val
        if pVal > parentVal and qVal > parentVal:
            return self.lowestCommonAncestor(root.right, p, q)
        elif pVal < parentVal and qVal < parentVal:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root