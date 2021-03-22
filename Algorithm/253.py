#253. Meeting Room II:

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        result = 0
        heap = []
        intervals.sort()
        for interval in intervals:
            while heap and heap[0] <= interval[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, interval[1])
            result = max(result, len(heap))
        return result

#heapq.heappop
#heap = []
#heapq.heappush(heap, i[1]): add the element in the heap and maintain the heap structure(orders).
#heapq.heappop(heap)
#heapq.heappop(heap)
#
