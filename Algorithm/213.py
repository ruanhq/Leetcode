#213 House Robber II:
class Solution:
    def rob(self, nums: List[int]):
        if len(nums) < 1:
            return 0
        if len(nums) == 1:
            return nums[0]

        #calculate the maximum of amount except either end's values:
        def calATE(arr):
            n = len(arr)
            states = [None for _ in range(n + 1)]
            states[n] = 0
            states[n - 1] = arr[n - 1]
            for i in range(n - 2, - 1, -1):
                states[i] = max(states[i + 1], nums[i] + states[i + 2])
            return states[0]
        resultWithoutStart = calATE(nums[1:])
        resultWithoutEnd = calATE(nums[:(len(nums) - 1)])
        return max(resultWithoutStart, resultWithoutEnd)
#House robber II:



def rob(nums):
    if len(nums) < 1:
        return 0
    if len(nums) == 1:
        return nums[0]
    def calate(arr):
        n = len(arr)
        states = [None for _ in range(n + 1)]
        states[n] = 0
        states[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            states[i] = max(states[i + 1], nums[i] + states[i + 2])
        return states[0]
    result = max(calate(nums[:(len(nums) - 1)]), calate(nums[1:]))
    return result

def calate(arr):
    n = len(arr)
    states = [0 for _ in range(n + 1)]
    states[n] = 0
    states[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        states[i] = max(states[i + 1], nums[i] + states[i + 2])
    return states[0]



calate([2, 1, 1])

[2, 1, 1] -> [1+2 = 3  ,1, 1, 0]


def rob(nums):
    if len(nums) < 1:
        return 0
    if len(nums) == 1:
        return nums[0]
    def calate(arr):
        #护城河:
        n = len(arr)
        states = [0 for _ in range(n + 1)]
        states[n] = 0
        states[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            states[i] = max(states[i + 1], states[i + 2] + nums[i])
        return states[0]
    























