'''120 / 120 test cases passed.                          Status: Accepted
Runtime: 40 ms                                           Memory Usage: 14.1 MB'''

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]