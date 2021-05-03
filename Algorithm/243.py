#shortest word distance:
def shortestDistance(wordsDict: List[str], word1: str, word2: str):
    result = 100000000
    index1 = index2 = 0
    for index, word in enumerate(wordsDict):
        if word == word1:
            index1 = index
            result = min(index1 - index2, result)
        elif word == word2:
            index2 = index 
            result = min(inred2 - index1, result)
    return result


#index, element -> here
index1 = index2 = -1
for index, element in enumerate(lists):
    if word == word1:
        index1 = index
        result = min(result, index1 - index2)
    elif word == word2:
        index2 = index
        result = min(result, index2 - index1)
return result



def getFactors(self, n):
    ans, stack, x = [], [], 2
    while True:
        if x > n / x:
            if not stack:
                return ans
            ans.append(stack + [n])
            x = stack.pop()
            n *= x
            x += 1
        elif n % x == 0:
            stack.append(x)
            n /= x
        else:
            x += 1

#All permutations:
def permutations(self, list1):
    def backtracking(result, temper, list1):
        if len(temper) == len(list1):
            result.append(temper[:])
        for i in range(len(list1)):
            if list1[i] in temper:
            	continue
            temper.append(list1[i])
            backtracking(result, temper, list1)
            temper.pop()
    result = []
    backtracking(result, [], list1)
    return result







def levelTraversal(self, root):
    if not root:
        return None
    ques = [root]
    print("current value is" %root.val)
    while ques:
        thisLevel = [node.val for node in ques]
        nextLevel = []
        for node in ques:
            print("current Value is" %node.val)
        for node in ques:
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
        ques = nextLevel
    return

def levelTraversal(self, root):
    if not root:
        return None
    ques = [root]
    print("current Value is " %root.val)
    while ques:
        thisLevel = [node.val for node in ques]
        nextLevel = []
        for node in ques:
            print("current Value is" %node.val)
        for node in ques:
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
        ques = nextLevel
    return

def levelTraversal(self, root):
    if not root:
        return None
    ques = [root]
    print("The current value is" %root.val)
    while ques:
        thisLevel = [node.val for node in ques]
        nextLevel = []
        for node in ques:
            print("The current value is " %root.val)
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
        ques = nextLevel
    return

























