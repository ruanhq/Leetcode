#245. Shortest Distance III:
class Solution:
    def shortestWordDistance(self, wordsDict: List[str],
    word1: str, word2: str):
        seen = {}
        result = float('inf')
        for index, word in enumerate(wordsDict):
            if word1 == word and word2 in seen:
                result = min(result, i - seen[word2])
            if word2 == word and word1 in seen:
                result = min(result, i - seen[word1])
            if word1 == w or word2 == w:
                seen[w] = 1
        return result


        seen = {}
        result = float('inf')
        for index, word in enumerate(wordsDict):
            if word1 == word and word2 in seen:
                result = min(result, i - seen[word2])
            if word2 == w and word1 in seen:
                result = min(result, i - seen[word1])
            if word1 == w or word2 == w:
                seen[w] = i
        return result


        if word1 == word2:
            result = 100000000
            dicts = []
            for i in range(len(wordsDict)):
                if wordsDict[i] == word1:
                    dicts.append(i)
            for j in range(1, len(dicts)):
                result = min(result, dicts[j] - dicts[j - 1])
            return result



import heapq
heapq.heapify(heaps1)
heapq.heappop(heaps1)
heapq.heappush(heaps1, 100)





