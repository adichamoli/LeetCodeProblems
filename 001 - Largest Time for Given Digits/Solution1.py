'''172 / 172 test cases passed.                     Status: Accepted
Runtime: 52 ms                                      Memory Usage: 14.5 MB'''

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        return max(['{0}{1}:{2}{3}'.format(*t) \
                   for t in itertools.permutations(arr) if t[:2] < (2,4) and t[2] < 6] or [""])


