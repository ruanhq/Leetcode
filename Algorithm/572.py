#572. Substree of another tree:
def comparingSame(s: treeNode, t: treeNode):
    if s is not None and t is None:
        return False
    if s is None and t is not None:
        return False
    if s is None and t is None:
        return True
    if s.val == t.val and comparingSame(s.left, t.left) and comparingSame(s.right, t.right):
        return True
    else:
        return False

def isSubTree(s: treeNode, t: treeNode):
    if comparingSame(s, t):
        return True
    if s is None or t is None:
        return False
    return isSubTree(s, t.left) or isSubTree(s, t.right)
