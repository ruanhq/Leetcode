#255. Verify preorder sequence in binary search tree
def verifyPreorder(self, preorder):
    stack = []
    lower = -1 << 31
    for x in preorder:
        if x < lower:
            return False
        while stack and x > stack[-1]:
            lower = stack.pop()
        stack.append(x)
    return True



chk, stack = None, []
for n in preorder:
	while stack and n > stack[-1]:
		chk = stack.pop()
	if chk != None and n < chk:
		return False
	stack.append(n)
return True


