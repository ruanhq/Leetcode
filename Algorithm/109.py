#109. Convert Sorted List to Binary Search Tree:

class Solution:
	def findMiddleNode(self, head):
        slowPointer = head
        fastPointer = head
        previousPointer = None
        while fastPointer and fastPointer.next:
            previousPointer = slowPointer
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
        if previousPointer:
            previousPointer.next = None
        return slowPointer
    #Then perform recursion to construct the tree from the root node.
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        #First you may need to find the root of the tree
        #where the tree has the index in the middle of the linked list:
        if not head:
            return None
        middle = self.findMiddleNode(head)
        node = TreeNode(middle.val)
        if head == mid:
            return node
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(middle.next)
        return node


#Another method would help you convert the linked list to array:
def mapListToValues(self, head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def mapListToValues(self, head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

#Convert the linked list to the balance binary tree -> 
#expanding the binary tree from the middle node and then
#expanding the binary tree from the middle node and then
#construct the left and right sub-tree from scratch here.

#to construct via binary search here.
def convertListToBalancedBST(arr, l, r):
    if l > r:
        return None
    mid = l + (r - l)// 2
    node = TreeNode(arr[mid])
    if l == r:
        return node
    node.left = convertListToBalancedBST(arr, l, mid - 1)
    node.right = convertListToBalancedBST(arr, mid + 1, r)
    return node

def mapListToValues(self, head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def mapListToValues(self, head):
    result = []
    while head:
        result.append(head.val)
        head = head.next 
    return result


#sort the linked list which is already sorted on absolute values:
class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class SortList:
    def __init__(self):
        self.head = None

    def sortedList(self, head):
        prev = self.head
        curr = self.head.next


#still similar to that of constructing a left or right subtree here.
def flattenBinaryTreeToLinkedList(node):
    if not node:
        return None
    if not node.left and not node.right:
        return node
    leftTree = flattenBinaryTreeToLinkedList(node.left)
    rightTree = flattenBinaryTreeToLinkedList(node.right)
    if leftTree:
    	leftTree.right = node.right
        node.right = leftTree
    	node.left = None
    if rightTree:
        return rightTree
    else:
        return leftTree

def flatten(self, root: TreeNode) -> None:
    flattenBinaryTreeToLinkedList(root)








