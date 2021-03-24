#255. Verify Preorder Sequence in binary Search Tree
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stacks = []
        smallest = -1 << 31
        for node in preorder:
            if node < smallest:
            	return False
            while stacks and node > stacks[-1]:
                smallest = stacks.pop()
            stacks.append(node)
        return True