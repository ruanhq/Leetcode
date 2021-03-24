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

#The array has been sorted in increasing order.
def binarySearch(arr, low, high, x):
    mid = (low + high) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return binarySearch(arr, low, mid - 1, x)
    else:
        return binarySearch(arr, mid + 1, high, x)

#Binary tree traversal:
def preorder(root):
  return [root.val] + preorder(root.left) + preorder(root.right) if root else []
def inorder(root):
  return  inorder(root.left) + [root.val] + inorder(root.right) if root else []
def postorder(root):
  return  postorder(root.left) + postorder(root.right) + [root.val] if root else []

def inorder(root):
    if root:
    	return inorder(root.left) + [root.val] + inorder(root.right)
    else:
        return []

def postorder(root):
    if root:
        return postorder(root.right) + postorder(root.left) + [root.val]
    else:
        return []



def preorder(root):
    if root:
        return [root.val] + preorder(root.left) + preorder(root.right)
    else:
        return []







