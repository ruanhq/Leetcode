#valid parenthesis: a typical first in first out structure.
class Solution:
  def isValid(self, s: str) -> bool:
  	stack = []
  	start_par = ["(", "[", "{"]
  	maps = {'(': ')', '[': ']', '{': '}'}
  	for i in range(len(s)):
  		if s[i] in start_par:
  			stack.append(s[i])
  		if stack and maps[stack[-1]] == s[i]:
  			stack.pop()
  		else:
  			False
  	return not stack






