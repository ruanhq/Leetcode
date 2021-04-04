#1756. Design Most Recently Used Queue:
class MRUQueue(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.n = n
        self.list = [t + 1 for t in list(range(n))]

    def fetch(self, k):
        """
        :type k: int
        :rtype: int
        """
        i = 0
        for i in range(k - 1, self.n - 1):
            self.list[i], self.list[i + 1] = self.list[i + 1], self.list[i]
        result = self.list[(self.n - 1)]
        return result
    

#Usage of SortedList:
class MRUQueue(object):
    def __init__(self, n: int):
        self.sl = SortedList((i - 1, i) for i in range(1, n + 1))

    def fetch(self, k: int) -> int:
        _, item = self.sl[k - 1]
        lastItemHelper, _ = self.sl[-1]
        del self.sl[k - 1]
        self.sl.add((lastItemHelper + 1, item))
        return item


self.sl.add((lastItemHelper + 1, item))
return item

#Usage of SortedList
