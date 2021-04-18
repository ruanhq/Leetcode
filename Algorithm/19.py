#19. Remove N-th node from end of the list:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyNode = ListNode(0)
        dummyNode.next = head
        start = dummyNode 
        index = 0
        while start != None:
        	index += 1
        	start = start.next 
        index -= n 
        start = dummyNode
        while index > 1:
        	index -= 1
        	start = start.next
        start.next = start.next.next
        return dummyNode.next
#If return head, for the one-element linked list, it may not work anymore.
#So you may need to create a dummyNode to connect to the head.
#Construct a dummynode at the start of the linked list!








