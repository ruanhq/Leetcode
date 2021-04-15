#138. CopyList with Random Pointer:
class Node:
    def __init__(self, x, next = None, random = None):
        self.val = int(x)
        self.next = next 
        self.random = random

class Node:
    def __init__(self, x, next = None, random = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Node:
    def __init__(self, x, next = None, random = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        mapping = {}
        cur = head
        while cur:
            mapping[cur] = Node(cur.val, None, None)
            cur = cur.next
        cur = head
        while cur:
            if cur.next:
            	mapping[cur].next = mapping[cur.next]
            if cur.random:
                mapping[cur].random = mapping[cur.random]
            cur = cur.next
        return mapping[head]

#deep copy: any changes in the copied object won't reflect
#in the previous object.
#copy: changes in the new(copied) object would reflect in the
#previous object.

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        mapping = {}
        cur = head
        while cur:
            mapping[cur] = Node(cur.val, None, None)
            cur = cur.next
        cur = head
        while cur:
            if cur.next:
                mapping[cur].next = mapping[cur.next]
            if cur.random:
                mapping[cur].random = mapping[cur.random]
            cur = cur.next
        return mapping[head]

#Construct an object with various properties here.

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        mapping = {}
        cur = head
        while cur:
            mapping[cur] = Node(cur.val, None, None)
            cur = cur.next
        cur = head
        while cur:
            if cur.next:
                mapping[cur].next = mapping[cur.next]
            if cur.random:
                mapping[cur].random = mapping[cur.random]
            cur = cur.next
        return mapping[head]















