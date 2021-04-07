#48. RotateImage:
class Solution:
    def rotateImage(matrix: List[List[int]]) -> List[List[int]]:
        nDim = len(matrix)
        low = 0
        high = len(matrix) - 1
        while low < high:
            matrix[low], matrix[high] = matrix[high], matrix[low]
            low += 1
            high -= 1

        for i in range(nDim):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        return matrix


class Solution:
    