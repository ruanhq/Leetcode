#754. Reaching a number:
1 + ... + (k - 1) < target
(1 + ... + (k)) = N ->  >= target
#check the difference between N - target:
#if N - target even, only want to modify the
#step with index of (N - target) / 2, move left,
#
#if N - target is odd -> add one step one by one until the (N - target) is even
We want to find the k 
class Solution:
    def reachNumber(self, target: int) -> int:
        sumOfNumber = 0
        result = 0
        target = abs(target)
        k = 0
        while sumOfNumber < target:
            sumOfNumber += k
            k += 1
        while (sumOfNumber - target) % 2 == 1:
            sumOfNumber += k
            k += 1
        return k - 1


