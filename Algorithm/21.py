#21. Merge Two Sorted Lists:
class Solution:
    def mergeTwoLists(self, l1, l2):
        DummyNode = ListNode(-1)
        previous = DummyNode
        while l1 and l2:
            if l1.val <= l2.val:
                previous.next = l1
                l1 = l1.next 
            else:
                previous.next = l2
                l2 = l2.next 
        previous.next = l1 if l1 is not None else l2 
        return DummyNode.next