#241. Different ways to add parentheses:
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        result = []
        #The combination of left list and right list:
        for i in range(len(expression)):
            if expression[i] in "-+*":
                leftList = self.diffWaysToCompute(expression[:i])
                rightList = self.diffWaysToCompute(expression[(i + 1):])
                for left in leftList:
                    for right in rightList:
                        if expression[i] == "*":
                            result.append(left * right)
                        elif expression[i] == "+":
                            result.append(left + right)
                        elif expression[i] == "-":
                        	result.append(left - right)
        return result

#the property of the divide-and-conquer type problem is that
#the solution is formed by the left and right part and then integrated together.
def diffWaysToCompute(self, expression: str) -> List[int]:
    if expression.isdigit():
        return [int(expression)]
    result = []


#2 * len(arr) times reversing flip, would have a structured procedure
3, 2, 4, 1 -> two times making the maximum non-ordered element in the required position?
-> 4, 2, 3, 1 -> 1, 3, 2, 4
-> 3, 1, 2, 4 -> 2, 1, 3, 4
-> 1, 2, 3, 4

