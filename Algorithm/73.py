#73. Set Matrix Zeroes:
class Solution(object):
    def setZeroes(self, matrix):
        #using the sets to store the indexes of column and rows to mapping to 0:
        rowSet = ()
        colSet = ()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rowSet.add(i)
                    colSet.add(j)
        for i in range(n):
            for j in range(m):
                if i in rowSet or j in colSet:
                    matrix[i][j] = 0
        return matrix

#to reduce overfitting, there are multiple ways: l1/l2 regularization, simplify the model,
#do some data augmentations here.

class Solution(object):
    def setZeroes(self, matrix):
        rowSet = ()
        colSet = ()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rowSet.add(i)
                    colSet.add(j)
        for i in range(n):
            for j in range(m):
                if i in rowSet or j in colSet:
                    matrix[i][j] = 0
        return matrix


s = ['a', 'b', 'c', 'd', 'e', ' ', 'f',
'g',  'h', ' ', 'm', 'n', 'o']

def reverseII(s: str):
    n = len(s)
    spaceIndex = [0]
    for i in range(n):
        if s[i] == ' ':
            spaceIndex.append(i)
    spaceIndex.append(n)
    result = []
    for i in range(len(spaceIndex) - 1):
        curWord = ''.join(s[spaceIndex[i]: (spaceIndex[i + 1] - 1)])
        reverseWord = curWord[::-1]
        result.append(list(reverseWord))
    return result



class Solution(object):
    def setZeroes(self, matrix):
        rowSet = ()
        colSet = ()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rowSet.add(i)
                    colSet.add(j)
        for i in range(n):
            for j in range(m):
                if i in rowSet or j in colSet:
                    matrix[i][j] = 0
        return matrix





class Solution(object):
    def permute(self, nums):
        #Use this to store the results
        result = []
        #searching the m-th element(it's the m-th layer here)
        def searching(m):
            if m == len(nums):
                result.append(nums[:])
            for i in range(m, len(nums)):
                nums[i], nums[m] = nums[m], nums[i]
                searching(m + 1)
                nums[i], nums[m] = nums[m], nums[i]
        searching(0)
        return result


class Solution(object):
    def permute(self, nums):
        result = []
        def searching(m):
            if m == len(nums):
                result.append(nums[:])
            for i in range(m, len(nums)):
                nums[i], nums[m] = nums[m], nums[i]
                searching(m + 1)
                nums[i], nums[m] = nums[m], nums[i]
        searching(0)
        return result










