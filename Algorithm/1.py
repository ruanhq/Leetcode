#1.py

class Solutin:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		n = len(nums)
		dict_default = {}
		for i in range(n):
			if nums[i] in dict_default:
				return dict_default[nums[i]], i
			else:
				dict_default[target - nums[i]] = i
		return -1, -1 

