'''120 / 120 test cases passed.                          Status: Accepted
Runtime: 56 ms                                           Memory Usage: 14.5 MB'''

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s2 = s + s
        s2 = s2[1:-1]
        
        return s2.find(s) != -1