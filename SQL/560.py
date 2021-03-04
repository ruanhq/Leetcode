#560. Subarray sum equals to K:
#sliding windows:
class Solution:
  def subarraySum(self, nums: List[int], k: int) -> int:
    count = 0
  	hashmaps = {0: 1}
  	for num in nums:
  	  s += num
  	  dif = s - k
  	  #if the sum - k already in the dictionary, if so, increase the count.
  	  if s-k in hashmaps:
  	  	count += hashmaps[s-k]
  	  if s in hashmaps:
  	  	hashmaps[s] += 1
  	  else:
  	  	hashmaps[s] = 1
  	return count
#hashmaps[s-k] -> where they start from -> continuous numbers of the sum.
#s-k in hashmaps:
#count += hashmaps[s-k]
#if s in hashmaps:
#then 




