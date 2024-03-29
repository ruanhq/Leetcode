#11. Container with most water:
class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        result = 0
        while left < right:
            result = max(result, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result


