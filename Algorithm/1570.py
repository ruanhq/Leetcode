#1570. Dot Product of two sparse vectors:

class SparseVector:
	def __init__(self, nums: List[int]):
		self.nonzeroElement = {}
		for i, n in enumerate(nums):
			if n != 0:
				self.nonzeroElement[i] = n 
    
    def dotProduct(self, vec: 'SparseVector') -> int:
    	result = 0
    	for i, n in self.nonzeroElement.items():
    		if i in vec.nonzeroElement:
    			result += n * vec.nonzeroElement[i]
    	return result


#Dot product of two sparse vector -> using the hashset:

def dotProduct(sparseVec1, sparseVec2):
	nonzeroVector1 = {}
	for i, n in enumerate(sparseVec1):
		if n != 0:
			nonzeroVector1[i] = n
	nonzeroVector2 = {}
	for i, n in enumerate(sparseVec2):
		if n != 0:
			nonzeroVector2[i] = n
	result = 0 
	for i, n in nonzeroVector1.items():
		if i in nonzeroVector2:
			result += nonzeroVector2[i] * n
	return result
