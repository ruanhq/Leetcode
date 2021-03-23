#extract direct ancestry from a binary tree:
#4. Median of two sorted array -> generalize to getting the kth largest/smallest element in the two sorted arrays.

def printAncestors(root, target):
    if root == None:
        return False
    if root.val == target:
        return True
    if (printAncestors(root.left, target)
    or printAncestors(root.right, target)):
        print root.val
        return True
    return False

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(7)
printAncestors(root, 7)

schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]

#Get the director ancestor!
def printAncestors(root, target):
    if root == None:
        return False
    if root.val == target:
        return True
    if(printAncestors(root.left, target) or printAncestors(root.right, target)):
        print(root.val)
        return True
    return False


#Construct a binary tree class:
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(7)
printAncestors(root, 7)
#to display the lowest ancestory, just pop the stack.










