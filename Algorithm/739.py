#739. Daily Temperature:

class Solution:
    def dailyTemperature(self, T: List[int]) -> List[int]:
        n = len(T)
        stack = []
        ans = [0] * n
        for i in range(n - 1, - 1, - 1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans

#scan from the right to left:
class Solution:
    def dailyTemperature(self, T: List[int]) -> List[int]:
        n = len(T)
        #Construct a stack here first:
        stack = []
        ans = [0] * n
        for i in range(n - 1, - 1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i 
            stack.append(i)
        return ans



class Solution:
    def dailyTemperature(self, T: List[int]) -> List[int]:
        n = len(T)
        stack = []
        ans = [0] * n
        for i in range(n-1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans

#Permutation of length m:
class Solution:
    def dailyTemperature(self, T: List[int]) -> List[int]:
        n = len(T)
        stack = []
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans
