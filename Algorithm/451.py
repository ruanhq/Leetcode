#451 Sort Characters By Frequency:
from collections import Counter
import heapq
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        countStr = Counter(s).most_common()
        for i, j in countStr:
            result += j * i
        return result


#方法一： counter -> Sort by frequency
#方法二： counter -> heapify ordering

class Solution:
    def frequencySort(self, s):
        freq = Counter(s)
        result = []
        heap1 = []
        for character, count in freq.items():
            heapq.heappush(heap1, (-count, character))
        while heap1:
            count, character = heapq.heappop(heap)
            result.append((character) * (-count))
        return "".join(result)

#Using the heap then pop them one by one(O(nlogn) time complexity).

