#239. Sliding window maximum:
def maxSlidingWindow(self, nums, k):
    d = collections.deque()
    outs = []
    for i, n in enumerate(nums):
        while d and nums[d[-1]] < n:
            d.pop()
        d += i
        