#95 UniqueBinarySearchTreesII:

class Solution:
    def generateTrees(self, n: int):
        def helper(start, end):
            if start > end:
                return [None, ]
            allTrees = []
            #how to construct a tree(includes a left subtree
            #and a right subtree with the current node i as the root to assemble a valid tree)
            for i in range(start, end + 1):
                leftTree = helper(start, i - 1)
                rightTree = helper(i + 1, end)
                for l in leftTree:
                    for r in rightTree:
                        currentTree = TreeNode(i)
                        currentTree.left = l 
                        currentTree.right = r 
                        allTrees.append(currentTree)
            return allTrees
        if n == 0:
            return [] 
        else:
            return helper(1, n)
#it may just simulate the whole process of assembling a tree here.

def helper(start, end):
    if start > end:
        return [None, ]
    allTrees = [] 
    for i in range(start, end + 1):
        leftTree = helper(start, i - 1)
        rightTree = helper(i + 1, end)
        for l in leftTree:
            for r in rightTree:
                currentTree = TreeNode(i)
                currentTree.left = l 
                currentTree.right = r
                allTrees.append(currentTree)
    return allTrees







