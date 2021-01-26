'''Submission Detail
53 / 53 test cases passed.                      Status: Accepted
Runtime: 100 ms                                 Memory Usage: 16.9 MB'''

class Solution:
    def getId(self, n, w):
        if n >= 0:
            return n // w
        else:
            return n // w - 1

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k <= 0 or t < 0:
            return False

        w = t + 1
        buckets = dict()
        for i in range(len(nums)):
            n = nums[i]
            id = self.getId(n, w)
            if id in buckets:
                return True
            if id - 1 in buckets and -t <= n - buckets[id - 1] <= t:
                return True
            if id + 1 in buckets and -t <= n - buckets[id + 1] <= t:
                return True
            buckets[id] = n
            if i >= k:
                del buckets[self.getId(nums[i - k], w)]

        return False
