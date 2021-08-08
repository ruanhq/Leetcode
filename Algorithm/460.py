#460 LFU: least frequently used cache:
from collections import default
class LFUCache(object):
    def __init__(self, capacity):
        self.cache = defaultdict(int)
        self.fK = defaultdict(list)
        self.kF = defaultdict(int)
        self.capacity = capacity
        self.min_key = 1

    def move_key(self, key, freq):
        self.fK[freq].remove(key)
        self.fK[freq + 1].append(key)

    def get(self, key):
        if key in self.cache:
            freq = self.kF[key]
            self.kF[key] += 1
            self.move_key(key, freq)
            if len(self.fK[self.min_key]) == 0:
                self.min_key += 1
            return self.cache[key]
        return -1

    def put(self, key, value):
        if self.capacity == 0:
            return
        if key in self.cache:
            freq = self.kF[key]
            self.kF[key] += 1
            self.move_key(key, freq)
            self.cache[key] = value
        #case the cache is full, we need to remove the least frequently used.
        elif len(self.cache.keys()) == self.capacity:
            if not self.fK[self.min_key]:
                self.min_key += 1
            k = self.fK[self.min_key].pop(0)
            del self.cache[k]
            del self.kF[k]
            #set the new key-value in the cache:
            self.cache[key] = value
            self.kF[key] = 1
            self.min_key = 1
            self.fK[1].append(key)
        #Adding the new key-value pairs:
        else:
        	self.cache[key] = value
        	self.kF[key] = 1
        	self.min_key = 1
        	self.fK[1].append(key)
        	