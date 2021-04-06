#109. Convert Sorted List to binary search tree:

class Solution(object):
    def getSubTree(self, NodeList):
        
    def sortedListToBST(self, head):
        result = []
        startNode = head
        while startNode:
            result.append(startNode.val)
            startNode = startNode.next
