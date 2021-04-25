#1197. Minimum Knight Moves:

class Solution(object):
    def minKnightMoves(self, x, y):
        def dfItera(x, y):
            if x + y == 0:
                return 0
            if x + y == 2:
                return 2
            if x + y == 1:
                return 3
            return min(dfItera(x - 1, y - 2), dfItera(x - 2, y - 1)) + 1
        return dfItera(np.abs(x), np.abs(y))
        