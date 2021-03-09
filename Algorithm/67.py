#67.add binary:
class Solution:
	def addBinary(self, a: str, b: str) -> str:
		result = ""
		#utilize a carryover point:
		carryover = 0
		listA = list(a)
		listB = list(b)
		while listA or listB or carryover:
			if listA:
				carryover += int(listA.pop())
			if listB:
				carryover += int(listB.pop())
			result += str(carryover % 2)
			carryover //= 2
		return result[::-1]

