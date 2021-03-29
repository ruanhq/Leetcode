#478. Generate random point in a circle
import random
import math
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x_center = x_center
        self.radius = radius
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        theta = math.pi * 2 * random.uniform(0, 1)
        r = random.uniform(0, 1) * self.radius
        return [self.x_center + r * math.cos(theta), self.y_center + r * math.sin(theta)]
