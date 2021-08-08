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

#maintain a heap: O(n)
#construct a heap: O(nlogn)
#q.put((node.val, node))
#node = node.next
#point = point.next
#point.next = ListNode(val)
#val, node = q.get()
#point.next = ListNode(val)
#node = node.next
#if node: q.put((node.val, node))
while not q.empty():
    val, node = q.get()
    point.next = ListNode(val)
    point = point.next 
    node = node.next
    if node:
        q.put((node.val, node))
return head.next

while not q.empty():
    val, node = q.get()
    point.next = ListNode(val)
    point = point.next 
    node = node.next 
    if node:
        q.put((node.val, node))
return head.next




