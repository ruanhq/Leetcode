#extract direct ancestry from a binary tree:


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


def printAncestors(root, target):
    if root == None:
    	return False
    if root.val == target:
    	return True