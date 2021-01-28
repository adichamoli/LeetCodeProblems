'''36 / 36 test cases passed.                    Status: Accepted
Runtime: 28 ms                                   Memory Usage: 14.3 MB'''

class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        s = s.split()
        if len(p) != len(s): return False
        return len(set(zip(p, s))) == len(set(p)) == len(set(s))