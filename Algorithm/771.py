#771. Jewels and Stones:
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        result = 0
        for chars in stones:
            if chars in jewels:
                result += 1
        return result




        