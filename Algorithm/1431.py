#1431. Kids with the greatest number of candies:
class Solution:
    def kidsWithCandies(self, candies: List[int],
    	extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        result = []
        for i in range(len(candies)):
        	if candies[i] + extraCandies >= maxCandy:
        		result.append(True)
        	else:
        		result.append(False)
        return False