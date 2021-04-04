#146. LRU Cache
class Solution:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dicts = OrderedDict()

    def get(self, key):
        if key not in self.dic:
            return -1
        v = self.dic.pop(key)
        self.dic[key] = v #make the dic remain the same
        return v

    def put(self, key, value): 
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.capacity > 0:
                capacity -= 1
            else:
                self.dic.popitem(last = False)
        self.dic[key] = value

#
#OrderedDict().popitem(last = True or False)
#OrderedDict().pop(key)
#OrderedDict().popitem(last = True or False)
#LRU Cache -> OrderedDict move_to_end:






