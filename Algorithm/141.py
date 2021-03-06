#141. Linked list cycle:
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        current_set = set()
        while head is not None:
            if head in current_set:
                return True
            current_set.add(head)
            head = head.next
        return False

        