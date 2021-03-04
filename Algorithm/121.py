#121. Best time to buy and sell stock
class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		curmax = 0
		curmin = 10000
		curresult = 0
		for i in range(len(prices)):
			if curmin > prices[i]:
				curmin = prices[i]
			elif prices[i] - curmin > curresult:
				curresult = prices[i] - curmin

#you need to buy first before you sell a stock.


