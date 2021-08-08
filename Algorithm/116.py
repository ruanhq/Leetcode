#116. populating next right pointers in each node:

from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
    	if not root:
    	    return None
        currentList = deque([root])
        while currentList:
            numberNodeThisLevel = len(currentList)
            for i in range(numberNodeThisLevel):
                currentNode = currentList.popleft()
                if i < numberNodeThisLevel - 1:
                    currentNode.next = currentList[0]
                if currentNode.left:
                    currentList.append(currentNode.left)
                if currentNode.right:
                    currentList.append(currentNode.right)
        return root
#Making the right pointers -> similar to that levelwise traversal here.

#The storage space required would be O(log-n)

#This GBDT model classifies accoutns based only on the direct behavior features
#of each account.


#a deep feature is a feature that is a function of the 
#direct features of entities linked to the entity in question.

#aggregation function of 

#flatten binary tree to linked lists -> here

class Solution:
    def connect(self, root: 'None') -> 'Node':
        if not root:
            return None
        currentList = deque([root])
        while currentList:
            numberNodeThisLevel = len(currentList)
            for i in range(numberNodeThisLevel):
                currentNode = currentList.popleft()
                if i < numberNodeThisLevel - 1:
                    currentNode.next = currentList[0]
                if currentNode.left:
                    currentList.append(currentNode.left)
                if currentNode.right:
                    currentList.append(currentNode.right)
        return root



#Minimum path sum would be the minimal of local minimum
simulating some pseudo-labels, pseudolabels.. 
We leverage a technique from transfer learning and extract the 
last hidden layer s output from the first stage model as the input of 
the second stage..

Then the hidden layers will be related to the ones.

       2
     5   6
   11 10 13
  15 11 18 16
#result would be 11.
      -1 
     2   1
    -1 2  -1

      -1
     2  1
   -1  1  0

      -1 
     2   1
   -1  3  -1
tr = [[-1],[3,2],[-3,1,-1]]
def minimumTotal(self, triangle: List[List[int]]) -> int:
    if len(triangle) == 1:
        return triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j > 0:
                leftAppend = triangle[i - 1][j - 1]
            else:
                leftAppend = float("inf")
            if j < len(triangle[i]) - 1:
                rightAppend = triangle[i - 1][j]
            else:
                rightAppend = float("inf")
            triangle[i][j] = min(leftAppend, rightAppend) + triangle[i][j]
    result = min(triangle[len(triangle) - 1])
    return result






















        





        


        