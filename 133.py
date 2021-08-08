#133. Clone Graph:
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        adjacentList = 





#S = "25525511135"
# 255.255.11.135
# 255.255.111.35
#101023: 


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x, n = 1/ x, -n
        if n%2 == 0:
            result = self.myPow(x * x, n // 2)
        else:
            result = x * self.myPow(x, n - 1)


#
nums = [1, 2, 3, 1, 1, 3]

#
class Solution:
	def solve(self, index, s, ds):
	    if index == len(s):
	        self.result.append(ds[:])
	        return
	    for i in range(idx, len(s)):
	        if s[index: (i + 1)] == s[index :(i + 1)][::-1]:
	            ds.append(s[idx:(i + 1)])
	            self.solve(i + 1, s, ds)
	            ds.pop()
    def partition(self, s):
        self.result = []
        ds = []
        self.solve(0, s, ds)
        return self.result
    def solve(self, index, s, ds):
        if index == len(s):
            self.result.append(ds[:])
            return
