#103. Zigzag traversal:
class Solution:
    def zigzagLevelOrder(self, root):
        queue = collections.deque([root])
        result = []
        i = 0
        while queue:
            r = []
            for _ in range(len(queue)):
                q = queue.popleft()
                if q:
                    r.append(q.val)
                    queue.append(q.left)
                    queue.append(q.right)
            r = r[::-1] if i % 2 == 1 else r
            if r:
                result.append(r)
            i += 1
        return result


#each of the level would be a queue and popleft the left
#end element and then append its left/ right child.


