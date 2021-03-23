#11. Container with most water:
#As this would be the area, not only the distance between lines,
#you may want to work closely with the pointers.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right  = len(height) - 1
        result = 0
        while left < right:
            result = max(result, min(height[left], height[right]) *(right - left))
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return result

