'''36 / 36 test cases passed.                    Status: Accepted
Runtime: 44 ms                                   Memory Usage: 14 MB'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict1,dict2={},{}
        s_split = s.split()
        if len(pattern) != len(s_split): return False
        for i in range(len(pattern)):
            if pattern[i] in dict1 and dict1[pattern[i]] != s_split[i]:
                return(False)
                
            if s_split[i] in dict2 and dict2[s_split[i]] != pattern[i]:
                return(False)
                
            dict1[pattern[i]] = s_split[i]
            dict2[s_split[i]] = pattern[i]
        return True