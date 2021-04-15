#498. Diagonal Traverse
class Solution(object):
    def findDiagonalOrder(self, mat):
        result = []
        if not mat or not mat[0]:
            return []
        n, m = len(mat), len(mat[0])
        for d in range(n + m - 1):
            currentList = []
            rowInd = d if d < n else n - 1
            colInd = 0 if d < n else d - n + 1
            while rowInd >= 0 and colInd < m:
                currentList.append(mat[rowInd][colInd])
                rowInd -= 1
                colInd += 1
            if d % 2 != 0:
                result.extend(currentList[::-1])
            else:
                result.extend(currentList)
        return result

#方法1: defaultdict(list): in the same diagonal, rowInd + colInd is constant,
#Then reverse the element in each of the subarray -> utilize a defaultdict here.
#方法2: iteratively append on the current list.

class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        resultDict = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                resultDict[i + j].append(mat[i][j])
        result = []
        for k in range(len(mat) + len(mat[0]) - 1):
            if k % 2 == 0:
                result.extend(resultDict[k][::-1])
            else:
                result.extend(resultDict[k])
        return result


