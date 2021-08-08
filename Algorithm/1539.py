#1539. K-th Missing Positive Number:

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr[0] - 1 >= k:
            return k
        i = 0
        currentIndicator = arr[0] - 1
        while currentIndicator <= k and i < len(arr):
            if arr[i + 1] - arr[i] > 1:
            	if arr[i + 1] - arr[i] - 1 < k - currentIndicator:
            	    currentIndicator += arr[i + 1] - arr[i] - 1
                    i += 1
                else:
                    return arr[i] + (k - currentIndicator)
            else:
                i += 1
        #didn't get the one:
        return (arr[len(arr) - 1] + k - currentIndicator)



class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr[0] - 1 >= k:
            return k 
        i = 0
        currentIndicator = arr[0] - 1
        while currentIndicator <= k and i < len(arr):
            if arr[i + 1] - arr[i] > 1:
                if arr[i + 1] - arr[i] - 1 < k - currentIndicator:
                    currentIndicator += arr[i + 1] - arr[i] - 1
                    i += 1
                else:
                    return arr[i] + (k - currentIndicator)
            else:
                i += 1
        return (arr[len(arr) - 1] + k - currentIndicator)



        





