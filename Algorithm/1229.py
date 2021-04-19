#1229. MinAvailableDuration:
class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        pointSlot1 = 0
        pointSlot2 = 0
        slots1.sort(key = lambda X: (X[0], X[1]))
        slots2.sort(key = lambda X: (X[0], X[1]))
        while pointSlot1 < len(slots1) and pointSlot2 < len(slots2):
            currentLeft = max(slots1[pointSlot1][0],
            slots2[pointSlot2][0])
            currentRight = min(slots1[pointSlot1][1],
            slots1[pointSlot2][1])
            if currentRight - currentLeft >= duration:
                return [currentLeft, currentLeft + duration]
            if slots1[pointSlot1][1] >= slots2[pointSlot2][1]:
                pointSlot2 += 1
            else:
                pointSlot1 += 1
        return []

#######################
#Two-pointers
#One-pointers
#One-pass
#Binary Tree
#Binary Search Tree
#Stack
#Queue/ PriorityQueue
#Heap
#Dynamic Programming
#Array
#Sort
#LinkedList
#######################

#Python Collections:
from collections import deque, Counter, OrderedDict, defaultdict
S = "aaaaaabbbbbccccdddeefffgggghhhhhiiiiii"
d1 = deque([])
d2 = Counter(S)
d3 = OrderedDict()


d1.append(3)
d1.append(4)
d1.append(5)
d1.append(6)
d1.extend([4,8, 9])
d1.append(11)

from heapq import heapify, heappush, heappop, nlargest, nsmallest
li2 = [5, 7, 9, 3, 4]
heapq.heapify(li2)
heapq.heappush(li2, 17)
heapq.heapify(li2)
heapq._heapify_max(li2)
heapq.heapreplace(li2, 10)
heapq.nlargest(2, li2)
heapq.nsmallest(3, li2)
heapq._heapify_max(li2)
ctSorted = sorted(Counter(S).items(), key = lambda X: X[1], reverse = True)


