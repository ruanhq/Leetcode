#valid parenthesis: a typical first in first out structure.

class Solution:
  def isValid(strings: str) -> bool:
    stacks = []
    leftParenthesis = ["(", "[", "{"]
    mapList = {"(": ")", "[": "]", "{": "}"}
    for num in strings:
      if num in leftParenthesis:
        stacks.append(num)
      elif stacks and mapList[stacks[-1]] == num:
        stacks.pop()
      else:
        return False
    return stacks == []



