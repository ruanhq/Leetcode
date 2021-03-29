#23. Merge K Sorted List:
lists = [[1,4,5],[1,3,4],[2,6]]
q2 = queue.PriorityQueue()
for l in lists:
    if l:
        q2.put((l, 1))

for l in lists:
    if l:
        q2.put((l, 1))


import heapq
customers = []
heapq.heappush(customers, (2, "Harry"))
heapq.heappush(customers, (3, "Charles"))
heapq.heappush(customers, (1, "Riya"))
heapq.heappush(customers, (4, "Stacy"))
while customers:
    print(heapq.heappop(q))

from queue import PriorityQueue
customers = PriorityQueue() #we initialise the PQ class instead of using a function to operate upon a list. 
customers.put((2, "Harry"))
customers.put((3, "Charles"))
customers.put((1, "Riya"))
customers.put((4, "Stacy"))

while customers:
    print(customers.get())

#maintain a priority queue here:
from Queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, 1))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next 
            node = node.next 
            if node:
                q.put((node.val, node))
        return head.next













