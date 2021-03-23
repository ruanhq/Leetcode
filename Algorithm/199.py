#199. Binary Tree Right Side View:
#using a queue for each of the layer and popleft eachtime to get the child which
#in the next layer; 
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        result = []
        this_level_nodes = deque([root])
        while this_level_nodes:
            current_level = this_level_nodes
            this_level_nodes = deque()
            while current_level:
                node = current_level.popleft()
                if node.left:
                    this_level_nodes.append(node.left)
                else:
                    this_level_nodes.append(node.right)
            result.append(node.val)
        return result


