'''Submission Detail
53 / 53 test cases passed.                      Status: Accepted
Runtime: 124 ms                                 Memory Usage: 17 MB'''

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k < 0 or t < 0:
            return False
        window = collections.OrderedDict()
        for n in nums:
            # Make sure window size
            if len(window) > k:
                window.popitem(False)
                
            bucket = n if not t else n // t
            # At most 2t items.
            for m in (window.get(bucket - 1), window.get(bucket), window.get(bucket + 1)):
                if m is not None and abs(n - m) <= t:
                    return True
            window[bucket] = n
        return False