#658. Find K closest elements:
import bisect
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        #the index that we insert their where if we insert the value in the left, the order preserves.
        left = bisect_left(arr, x) - 1
        right = left + 1
        while right - left - 1 < k:
            if left == -1:
                right += 1
                continue
            if right == n or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
        return arr[(left + 1): right]

#left = bisect_left(arr, x) - 1
#right = left + 1
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        left = bisect_left(arr, x) - 1
        right = left + 1
        #then we are using two pointers to control the direction to move.
        while right - left - 1 < k:
            if left == -1:
                right += 1
                continue
            if right == n or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
        return arr[(left + 1): right]

#lead and contribute significantly to spark mllib
#work on spark pipeline
#ensure standards and procedures are being adhered to.
#distributed data processing and modeling algorithms.
#hands-on experience in building scalable services for data analytics,
#model implementation
#spark and spark ml; scala is a strong plus.
#Mapping the tuple to the values -> key here are the tuples(list)
#To get the group anagrams:
def groupAnagrams(str: List[str]):
    from collections import defaultdict
    result = defaultdict(list)
    for s in strs:
        result[tuple(sorted(s))].append(s)