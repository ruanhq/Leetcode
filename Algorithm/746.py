#746. Min Cost Climbing stairs
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        for i in range(2, n):
            cost[i] += min(cost[i - 2], cost[i - 1])
        return min(cost[n - 2], cost[n - 1])

