#1197. Minimum Knight Moves:
import functools
import numpy as np 
class Solution(object):
    def minKnightMoves(self, x, y):
        def dfItera(x, y):
            if x + y == 0:
                return 0
            if x + y == 2:
                return 2
            if x + y == 1:
                return 3
            s1 = min(dfItera(np.abs(x - 1), np.abs(y - 2)),
            dfItera(np.abs(x - 2), np.abs(y - 1)))
            return s1
        return dfItera(np.abs(x), np.abs(y))

