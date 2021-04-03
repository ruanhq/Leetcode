#146. LRU Cache
class Solution:
    def __init__(self, capacity):
        self.dic = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.dic:
            return -1
        v = self.dic.pop(key)
        self.dic[key] = v
        return v

    def put(self, key, value):
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.capacity > 0:
                self.capacity -= 1
            else:
                self.dic.popitem(last = False)
        self.dic[key] = value

#OrderedDict().popitem(last = True or False)
#OrderedDict().pop(key)
#OrderedDict().popitem(last = True or False)
#LRU Cache -> OrderedDict move_to_end:
class Solution(object):
    def rightSideView(self, root):
        deque = collections.deque()
        if root:
            deque.append(root)
        res = []
        while deque:
            size, val = len(deque), 0
            for _ in range(size):
                node = deque.popleft()
                val = node.val # store last value in each level
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            res.append(val)
        return res
