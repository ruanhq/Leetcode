#202.Happy Number:
class Solution:
    def isHappy(self, n: int) -> bool:
      current_set = set()
      while n != 1:
      	n = sum([int(t) ** 2 for t in str(n)])
      	#Will repeat:
      	if n in current_set:
      		return False
      	else:
      		current_set.add(n)
      return True




