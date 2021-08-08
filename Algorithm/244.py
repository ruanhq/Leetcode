#244. Shortest Word Distance II:
from collections import defaultdict
class WordDistance:
    def __init__(self, words: List[str]):
        self.words = words
        self.dicts = {}
        for i in range(len(words)):
            if words[i] in self.dicts:
                self.dicts[words[i]].append(i)
            else:
                self.dicts[words[i]] = [i]
        self.wordDict = defaultdict(list)
        for (index, word) in enumerate(self.words):
            self.wordDict[word].append(index)

    def shortest(self, word1: str, word2: str):
    	dicWord1 = self.wordsDict[word1]
    	dicWord2 = self.wordsDict[word2]
    	minDistance = 100000000000
    	p1 = p2 = 0
    	while p1 < len(dicWord1) and p2 < len(dicWord2):
    	    minDistance = min(minDistance, abs(dicWord1[p1] - dicWord2[p2]))
    	    if dicWord1[p1] < dicWord2[p2]:
    	    	p1 += 1
    	    else:
    	    	p2 += 1
    	return minDistance

wdic1 = defaultdict(list)
wdic2 = defaultdict(list)
wdic3 = defaultdict(list)
for index, word in enumerate(w1):
    wdic1[word].append(index)
for index, word in enumerate(w2):
    wdic2[word].append(index)
for index, word in enumerate(w3):
    wdic3[word].append(index)    
    
list1 = 
result.append(currentResult[:] + [n/ d])
result.append(currentResult[:] + [n/ d])

class WordDistance:
    def __init__(self, words: List[str]):
        self.words = words
        self.wordDict = defaultdict(list)
        for index, word in enumerate(words):
            self.wordDict[word].append(index)

    def shortest(self, word1L: str, word2L: str):
        dicWord1 = self.wordDict(word1L)
        dicWord2 = self.wordDict(word2L)
        minDistance = 1000000000
        p1 = p2 = 0
        while p1 < len(dicWord1) and p2 < len(dicWord2):
            minDistance = min(minDistance, abs(dicWord1[p1] - dicWord2[p2]))
            if dicWord1[p1] < dicWord2[p2]:
                p1 += 1
            else:
                p2 += 1
        return minDistance
    def manhattanDistance(self, X, Y):
    	manhattanDist = 0
        for (x, y) in zip(X, Y):
            manhattanDist += abs(x - y)
        return manhattanDist
    def shortest(self, word1L: str, word2L: str, word3L: str):
        dicWord1 = self.wordDict(word1L)
        dicWord2 = self.wordDict(word2L)
        dicWord3 = self.wordDict(word3L)
        minDistance = 1000000000
        p1 = p2 = p3 = 0
        while p1 < len(dicWord1) and p2 < len(dicWord2):
            minDistance = min(minDistance, abs())




class Solution:
    def maxAbsValExpr(self, xS, yS):
        result = max( abs(x1 - x2) + abs(y1 - y2) + abs(i - j) 
        	for i, (x1, y1) in enumerate(zip(xS, yS))
        	for j, (x2, y2) in enumerate(zip(xS, yS)))

result = 0
xS = [1, 0, -1, -2, 2, 1, 0, -1, 3, 2, 1, 0, 4, 3, 2, 1]
yS = [10, 9, 8, 7,  6, 5, 2, 3,  4, -5, -8, -1, -2, 17, 19, 22]
for i, (x1, y1) in enumerate(zip(xS, yS)):
    result += i * (y1 - x1)

class Solution:
    def maxAbsValExpr(self, xS, yS):
        result = max(abs(x1 - x2) + abs(y1 - y2) + abs(i - j)
        	for i, (x1, y1) in enumerate(zip(xS, yS))
        	for j, (x2, y2) in enumerate(zip(xS, yS)))



    def maxAbsValExpr(self, xS, yS):
        result = max(abs(x1 - x2) + abs(y1 - y2) + abs(i - j)
        	for i, (x1, y1) in enumerate(zip(xS, yS))
        	for j, (x2, y2) in enumerate(zip(xS, yS)))








