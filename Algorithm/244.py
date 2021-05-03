#244. Shortest Word Distance II:
from collections import defaultdict
class WordDistance:
    def __init__(self, words: List[str]):
    	self.words = words
    	self.wordDict = defaultdict(list)
    	for index, word in wordsDict:
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