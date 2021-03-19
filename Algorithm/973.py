#K-closest points to origin:
class Solution:
  def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    points.sort(key = lambda X: X[0] ** 2 + X[1] ** 2)
    return points[:k]



