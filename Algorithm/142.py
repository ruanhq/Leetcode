#142. Cycled Linked List II
class Solution(object):
    def detectCycle(self, head):
        AlreadyNodeSet = set()
        node = head
        while node is not None:
            if node in AlreadyNodeSet:
            	return node
            else:
            	AlreadyNodeSet.add(node)
            	node = node.next 
        return None

