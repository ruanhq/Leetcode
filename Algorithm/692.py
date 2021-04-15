#692. Top-K Frequent Words
import collections, heapq
class Solution(object):
    def topKFrequent(self, words, k):
        ct1 = collections.Counter(words)
        heap1 = [(-freq, word) for word, freq in ct1]
        heapq.heapify(heap1)
        return [heapq.heappop(heap1)[1] for _ in range(k)]

