#287. Find the duplicate number:

class Solution:
    def findDuplicate(self, nums: List[int]):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

#Why not using the set?

#is there ensured duplicated numbers here?
class Solution:
    def findDuplicate(self, nums: List[int]) -> float:
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return nums[i]
        #Else we will return False here(there's no duplicated numbers here)
        return None

#detect cycle in the linked list:
class Solution:
    def isHappy(self, n: int):
        currentSeen = set()
        while n != 1:
            n = int([int(t) ** 2 for t in str(n)])
            #detect a cycle(you have seen this element here)
            if n in currentSeen:
                return False
            currentSeen.add(n)
        return True


class Solution:
    def isHappy(self, n: int):
        #maintain a set including the numbers you have already seen here.
        currentSeen = set()
        while n != 1:
            n = int([int(t) ** 2 for t in str(n)])
            if n in currentSeen:
                return False
            currentSeen.add(n)
        return True

#To detect whether there is a circle in the linked list.
def isHappy(n):
    currentSeen = set()
    while n != 1:
        n = int(sum(int(t) ** 2 for t in str(n)))
        #detect a cycle(you have seen this element here)
        if n in currentSeen:
            return False
        currentSeen.add(n)
    return True


#Initiate the binary tree structure:
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left
        self.right = right

#Binary Tree level order traversal:
class Solution:
    def levelOrder(self, root: TreeNode):
        result = []
        if not root:
            return []
        currentLevel = [root]
        while currentLevel:
            nextLevel = []
            result.append([node.val for node in currentLevel])
            for node in currentLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            currentLevel = nextLevel
        return result

#level order traversal:
class Solution:
    def levelOrder(self, root: TreeNode):
        result = []
        if not root:
            return []
        currentLevel = [root]
        while len(currentLevel) > 0:
            nextLevel = []
            result.append([node.val for node in currentLevel])
            #For each node in this layer, append the left subtree 
            #and right subtree to the current node(next-level)-> adding all of the nodes to the output(result list)
            for node in currentLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            currentLevel = nextLevel
        return result

class Solution:
    def levelOrder(self, root):
        result = []
        if not root:
            return []
        currentLevel = [root]
        while currentLevel:
            nextLevel = []
            result.append([node.val for node in currentLevel])
            for node in currentLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            currentLevel = nextLevel
        return result


class Solution:
    def levelOrder(self, root):
        result = []
        if not root:
            return []
        currentLevel = [root]
        while currentLevel:
            nextLevel = []
            result.append([node.val for node in currentLevel])
            for node in currentLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            currentLevel = nextLevel
        return result


class Solution:
    def levelOrder(self, root: TreeNode):
        result = []
        if not root:
            return []
        currentLevel = [root]
        while currentLevel:
            nextLevel = []
            result.append([node.val for node in currentLevel])
            for node in currentLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            currentLevel = nextLevel
        return result





class Solution:
    def merge(self, intervals: List[List[int]]):
        intervals.sort(key = lambda X: X[0])
        result = []
        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                if interval[1] > result[-1][1]:
                    result[-1][1] = interval[1]
        return result

        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
            	#if the end of the current interval is within range
            	#there are intersections.
                if interval[1] > result[-1][1]:
                    result[-1][1] = interval[1]
        return result

class Solution:
    def merge(self, intervals: List[List[int]]):
        intervals.sort(key = lambda X: X[0])
        result = []
        for interval in intervals:
            if not result or interval[0] > result[-1][1]:
                result.append(interval)
            else:
                if interval[1] > result[-1][1]:
                    result[-1][1] = interval[1]
        return result

#BFS: Topological sort

#initiate the data structure here first:
class Solution:
    def merge(self, intervals: List[List[int]]):



class Solution(object):
    def levelOrder(self, root):
        result = []
        if root is None:
            return []
        currentLevel = [root]
        while currentLevel:
            result.append([node.val for node in currentLevel])
            nextLevel = []
            for node in currentLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            currentLevel = nextLevel
        return result

class Solution(object):
    def levelOrder(self, root):
        result = []
        if root is None:
            return []
        currentLevel = [root]
        while currentLevel:
            result.append([node.val for node in currentLevel])
            nextLevel = []
            for node in currentLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            currentLevel = nextLevel
        return result

class Solution:
    def dailyTemperatures(self, T: List[int]):
        n = len(T)
        stack = []
        result = [0] * n
        for i in range(n - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                result[i] = stack[-1] - i
            stack.append(i)
        return result

        n = len(T)
        stacks = []
        result = [0] * n 
        for i in range(n-1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
               stack.pop()
            if stack:
               result[i] = stack[-1] - i
            stack.append(i)
        return result

    def dailyTemperatures(self, T: List[int]):
        n = len(T)
        stack = []
        result = [0] * n
        for i in range(n - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                result[i] = stack[-1] - i 
            stack.append(i)
        return result








class Solution(object):
    def addTwoNumbers(self, l1, l2):
        root = n = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            v1 = 0
            v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        root = n = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            v1 = 0 
            v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next



#def addTwo

root.next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        root = n = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            v1 = 0
            v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next


#k-th missing positive number:

class Solution:
    def findKPositive(self, arr, k):
    	#how many numbers left here:
        currentIndicator = (arr[0] - 1)
        i = 0
        if currentIndicator >= k:
            return k
        while currentIndicator <= k and i < len(arr) - 1:
        	if arr[i + 1] - arr[i] > 1:
        		if arr[i + 1] - arr[i] - 1 < k - currentIndicator:
        			currentIndicator += arr[i + 1] - arr[i]
        			i += 1
        	    else:
        	        return arr[i] + (k - currentIndicator)
        	else:
        	    i += 1
        #Then return the last element plus the remaining points to add.
        return (k - currentIndicator) + arr[len(arr)-1]






















