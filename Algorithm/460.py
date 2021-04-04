#LFU:
from collections import defaultdict, OrderedDict

class Node:
    def __init__(self, key, val, freq):
        self.key = key
        self.val = val
        self.freq = freq



class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
