#continuous integration(CI) is the practice of merging all developers
#working copies to a shared mainline several times per day.

#continuous delivery(condinuous deployment CD) is a software engineering
#approach in which teams produce software in short cycles, ensuring that
#software can be reliably released at any time and when releasing the 
#software, without doing so manually.

#help automate the pipeline, we would suggest an isolated pipeline here.





#calculate the dot product here:
import numpy as np
X1 = np.array([1, 2, 3, 4, 5, 6])
X2 = np.array([9, 8, 7, 6, 5, 4])
X1.dot(X2)


def dotFunction(X1, X2):
    result = 0
    assert len(X1) == len(X2)
    for x1, x2 in X1, X2:
        result += x1 * x2
    return result
results = map(dotFunction, (X1, X2))


#amazon, microsoft and google for the modeling here.
import numpy as np 
X1 = np.array([1, 2, 3])
X2 = np.array([5, 7, 9])
X1.dot(X2)


def bucketSort(X):
    arr = []
    nSlot = 10
    for i in range(nSlot):
        arr.append([])
    for j in x:
        indexB = int(nSlot * j)
        arr[indexB].append(j)
    for i in range(nSlot):
    	insertionSort(arr[i])
    #concatenate all the bucket together.


#Split the array into multiple buckets and then calculate the minimum difference between any two 
#of the values in the array here.
def containsNearbyAlmostDuplicates(self, nums: List[int], k: int, t: int) -> bool:
    if t == 0 and len(set(nums)) == len(nums):
        return False
    n = len(nums)
    width = t + 1
    for idx, number in enumerate(nums):
        bucketIdx = number // width
        if bucketIdx in bucket:
            return True
        elif bucketIdx + 1 in bucket and abs(number - bucket[bucketIdx + 1]) < width:
            return True
        elif bucketIdx - 1 in bucket and abs(number - bucket[bucketIdx - 1]) < width:
            return True
        bucket[bucketIdx] = number
        if idx >= k:
            del bucket[nums[idx - k] // width]
    return False

    if t == 0 and len(set(nums)) == len(nums):
        return False
    n = len(nums)
    width = t + 1
    for idx, number in enumerate(nums):
        bucketIdx = number // width
        if bucketIdx in bucket:
            return True
        elif bucketIdx + 1 in bucket and abs(number - bucket[bucketIdx + 1]) < width:
            return True
        elif bucketIdx - 1 in bucket and abs(number - bucket[bucketIdx - 1]) < width:
            return True
        bucket[bucketIdx] = number
        if idx >= k:
            del bucket[nums[idx - k] // width]
    return False
    return False
    return False
#Why not construct a recursive tree here?
#Try to construct a recursive tree.


#maximum binary tree:

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        #construct the maximum binary tree with a recursive manner here:
        if not nums:
            return None
        root = TreeNode(max(nums))
        #a binary tree with this order, would I need reordering? no
        index = nums.index(max(nums))
        #construct the left and right subtree from the current root node:
        root.left = self.constructMaximumBinaryTree(nums[:index])
        root.right = self.constructMaximumBinaryTree(nums[(index + 1):])

people with subprime scores tend to have even higher interest rates, 
at 16.40% for a used car.constructMaximumBinaryTree
help borrowers with credit scores in these categories beating the 
average, since interest rates starts as low as 2.99% APR for new 
vehicle purchases and excellent credit

easy online application for pre-qualification
For the autoloan team,

#statisticians who uses python and lives in SF.

why data science? any project and any challenging problem? how did you solve it 
what would be the biggest problem you have been facing in data science?
#why data science:
I have felt the tremendous potential for the data-driven solution can help the business 
as well as the 














