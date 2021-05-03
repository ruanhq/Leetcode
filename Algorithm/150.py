#150. Evaluate Reverse Polish Notation:
operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a/ b)
        }


class Solution(object):
    def evalList(self, tokens):
        operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: int(a/ b)
        }
        curStack = []
        for strs in tokens:
            if strs in operations:
                number2 = curStack.pop()
                number1 = curStack.pop()
                thisOperation = operations[strs]
                curStack.append(thisOperation(number1, number2))
            else:
                curStack.append(strs)
        result = curStack.pop()
        return result