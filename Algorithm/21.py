#21. Merge Two sorted Lists:
#l1 and l2 are at the start of the list.
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    	dummy = cur = ListNode(0)
    	while l1 and l2:
    		if l1.val < l2.val:
    			cur.next = l1
    			l1 = l1.next 
    		else:
    			cur.next = l2
    			l2 = l2.next
    		cur =cur.next
    	cur.next = l1 or l2
    	return dummy.next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = current = ListNode(0)
        while l1 < l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next 
        if l1:
            current.next = l1
        if l2:
            current.next = l2
        return dummy.next


    