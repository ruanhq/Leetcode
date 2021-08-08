#950. Reveal cards in increasing order:
import collections 
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]):
    	#First we construct a queue:
    	N = len(deck)
        index = collections.deque(range(N))
        result = [None] * N
        for cards in sorted(deck):
            result[index.popleft()] = cards
            if index:
                index.append(index.popleft())
        return result


#transform the binary sequences to an integer.
#How to handle out-of-scope requirements?

#Python cross-validation:
