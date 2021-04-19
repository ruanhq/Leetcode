#994. Rotting Oranges:
#O(V + E)
from collections import deque
class Solution(object):
    def orangeRotting(self, grid):
        

#To control the direction:
directionList = [(1,0), (0, 1), (-1, 0), (0, -1)]
for xx, yy in directionList:
    xx1 = x1 + xx
    yy1 = y1 + yy


for xx, yy in directionList:
    xx1 = x1 + xx
    yy1 = y1 + yy

#BFS重点突破.

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2) + fib(n - 3)
#Construct a sentinel node and the link it next to the head,
#Then you may want to return this node.


@lru_cache(maxsize = 10)
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return fib(n - 1) + fib(n - 2) + fib(n - 3)


#Making it rotton:
#for nodes adjacent to the leftMost one: make all of them rotton
#then push the new rotton ones in the current queue.
@lru_cache(maxsize = 10)
def fib(n):
    if n == 0:
        return 0
    if n == 1:
    	return 1
    if n == 2:
        return 2
    return fib(n - 1) + fib(n - 2) + fib(n - 3)










