#Daily Temperature 739
class Solution(object):
  def dailyTemperatures(self, T):
  	n = len(T)
  	result = [0] * n
  	stack = []
  	for i in range(n-1, -1, -1):
  		while stack and T[i] >= T[stack[-1]]:
  			stack.pop()
  		if stack:
  			result[i] = stack[-1] - i
  		stack.append(i)
  	return result


for i in range(n - 1, -1, -1):
	while stack and T[i] >= T[stack[-1]]:
		stack.pop()
	if stack:
		result[i] = stack[-1] - i 
	stack.append(i)
	return result

