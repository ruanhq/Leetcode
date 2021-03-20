#1331. Rank Transform of an array:
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
    	hashSet = {}
    	rank = 1
    	for num in sorted(arr):
    		if num not in hashSet:
    			hashSet[num] = rank 
    			rank += 1
    	for idx, val in enumerate(arr):
    		arr[idx] = hashSet[val]
    	return arr

#Get the rank of the list.

