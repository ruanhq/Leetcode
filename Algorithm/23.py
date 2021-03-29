#23. Merge K Sorted List:
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next 
            if node:
                q.put((node.val, node))
        return head.next

