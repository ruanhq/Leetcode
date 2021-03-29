#74. Search a 2D matrix:
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        m = len(matrix)
        n = len(matrix[0])
        high = m * n - 1
        pivot = 0
        while low <= high:
            pivotIndex = (low + high)// 2
            currentValue = matrix[pivotIndex// n][pivotIndex % n]
            if currentValue == target:
                return True
            elif currentValue > target:
                high = pivotIndex - 1
            else:
                low = pivotIndex + 1
        return False


