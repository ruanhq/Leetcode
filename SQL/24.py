#24. Swap nodes in pairs

class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        start = head
        while head and head.next:
            head.val, head.next.val = head.next.val, head.val
            head = head.next.next
        return start




