#122. Best Time to Buy and sell stock II:
#One-pass greedy solution:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        index = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                result += prices[i] - prices[i - 1]
        return result

