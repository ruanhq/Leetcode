#283.Move zeros:
class Solution(object):
	def moveZeroes(self, nums):
		i=0
		n = len(nums)
		while i < n:
			if nums[i] == 0:
				nums.pop(i)
				nums.append(0)
				n-=1
			else:
				i+=1

#nums.pop(i) means move out the element in index i
#where append means add another element at the end of the array.
