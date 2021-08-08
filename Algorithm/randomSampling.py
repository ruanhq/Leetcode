#python random sampling:
import random
random.random()
random.randrange(10, 20)
random.random()
[random.random() for _ in range(40)]
print(random.randrange(3))
print(random.randrange(3, 6))
upToFive = list(range(5))
random.shuffle(upToFive)
display1 = random.choice(["A1", "A2", "A3", "A4"])
display1
source = list(range(10))
[random.choice(source) for _ in range(17)]
#the sample size is larger than the number of list.
random.sample(source, 8)
class Stream(object):
    def __init__(self, n):
        self.n = n
    def hasNext(self):
        return 1 if self.n <= 100 else 0
    def getNext(self):
        return random.randrange(100) if self.hasNext() else None
    def update(self):
        self.n += 1
    def leng(self):
        return self.n

#adoption: begin to use sth new.
#internal adoption: 


from collections import OrderedDict
ord1 = OrderedDict()
ord1['a1'] = 1
ord1['a2'] = 2
ord1['a3'] = 3
ord1['a4'] = 4
ord1['a5'] = 5
for key, value in ord1.items():
    print(key, value)

ord1.move_to_end(3)
ord1.popitem()

class Solution(object):
    def cloneGraph1(self, node): #DFS iteratively
        if not node:
            return node
        m = {node: Node(node.val)}
        stack = [node]
        while stack:
            n = stack.pop()
            for neigh in n.neighbors:
                if neigh not in m:
                    stack.append(neigh)
                    m[neigh] = Node(neigh.val)
                m[n].neighbors.append(m[neigh])
        return m[node]
        
class Solution(object):
    def cloneGraph1(self, node):
        if not node:
            return node
        m = {node: Node(node.val)}
        stack = [node]
        while stack:
            n = stack.pop()
            for neigh in n.neighbors:
                if neigh not in m:
                    stack.append(neigh)
                    m[neigh] = Node(neigh.val)
                m[n].neighbors.append(m[neigh])
        return m[node]

















