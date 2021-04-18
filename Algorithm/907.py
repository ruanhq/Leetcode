#907. SumOfSubarrayMinimums:
class Solution(object):
    def sumSubarrayMins(self, arr):
        result = 0
        arr = [float("-inf")] + arr + [float("-inf")]
        leftIndex = 0
        rightIndex = 0
        for i in range(1, len(arr) - 1):
            leftIndex = rightIndex = i
            leftIndex -= 1
            rightIndex += 1
            while arr[leftIndex] > arr[i]:
                leftIndex -= 1
            while arr[rightIndex] >= arr[i]:
                rightIndex += 1
            result += (i - leftIndex) * arr[i] * (rightIndex - i)
        return result



np.apply_along_axes(np.sum, data, [0, 1])
X1 = np.argmax(X, axis = 1)


