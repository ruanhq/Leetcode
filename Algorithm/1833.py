#1833. Maximum Ice Cream Bars:
import heapq
class Solution(object):
    def maxIceCream(self, costs, coins):
        n = len(costs)
        heaps1 = []
        result = 0
        for i in range(len(costs)):
            heapq.heappush(heaps1, costs[i])
        while heaps1 and coins > 0:
            curAmnt = heaps1.popleft()
            if curAmnt < coins:
                coins -= curAmnt
                result += 1
        return result


#Utilizing a heap to store the element from small to large.
