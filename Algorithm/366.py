#366. Find Leaves of binary tree:
from collections import defaultdict
class Solution:
    def findLeaves(self, root: TreeNode):
        result = []
        def searching(node, layer):
            if not node:
                return layer
            leftDepth = searching(node.left, layer)
            rightDepth = searching(node.right, layer)
            maxDepth = max(leftDepth, rightDepth)
            result[layer].append(node.val)
            return (layer + 1)
        searching(root, 0)
        return result

class Solution:
    def findLeaves(self, root: TreeNode):
        result = []
        def searching(node, layer):
            if not node:
                return layer
            leftDepth = searching(node.left, layer)
            rightDepth = searching(node.right, layer)
            maxDepth = max(leftDepth, rightDepth)
            result[layer].append(node.val)
            return (layer + 1)
        searching(root, 0)
        return result


from collections import defaultdict
class WordDistance:
    def __init__(self, words: List[str]):
        self.wordDict = defaultdict(list)
        for (index, word) in enumerate(words):
            self.wordDict[word].append(index)

    def shortest(self, word1: str, word2: str) -> int:
        dicWord1 = self.wordDict[word1]
        dicWord2 = self.wordDict[word2]
        minDistance = 10000000
        p1 = p2 = 0
        while p1 < len(dicWord1) and p2 < len(dicWord2):
            minDistance = min(minDistance, abs(dicWord1[p1] - dicWord2[p2]))
            if dicWord1[p1] < dicWord2[p2]:
                p1 += 1
            else:
                p2 += 1
        return minDistance

def evalRPN(self, tokens: List[str]) -> int:
    stack = []
    for i in tokens:
        if i[-1].isdigit():
            stack.append(int(i))
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            print(num2, i, num1)
            if i == "+":
                stack.append(num1 + num2)
            if i == "-":
                stack.append(num1 - num2)
            if i == "*":
                stack.append(num1 * num2)
            if i == "/":
                stack.append(int(num1/ num2))
            stack.append(i)
    return stack.pop()



def permute(nums):
    result = []
    def searching(m):
        if m == len(nums):
            result.append(nums[:])
        for i in range(m, len(nums)):
            nums[i], nums[m] = nums[m], nums[i]
            searching(m + 1)
            nums[i], nums[m] = nums[m], nums[i]
    searching(0)
    return result


def permute(nums):
    result = []
    def searching(m):
        if m == len(nums):
            result.append(nums[:])
        for i in range(m, len(nums)):
            nums[i], nums[m] = nums[m], nums[i]
            searching(m + 1)
            nums[i], nums[m] = nums[m], nums[i]
    searching(0)
    return result

























