#215. K-th Largest Element in an Array:

import heapq
from heapq import heapify
class Solution(object):
    def findKthLargest(self, nums, k):
        heap0 = []
        for num in nums:
            heapq.heappush(heap0, num)
            if len(heap0) > k:
            	heapq.heappop()
        heapify(heap0)
        return heap0[-k]




