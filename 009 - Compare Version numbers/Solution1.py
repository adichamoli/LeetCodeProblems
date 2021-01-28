'''81 / 81 test cases passed.                    Status: Accepted
Runtime: 28 ms                                   Memory Usage: 14.2 MB'''

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        len1 = len(v1)
        len2 = len(v2)
        
        for i in range(max(len1,len2)):
            x = int(v1[i]) if i<len1 else 0
            y = int(v2[i]) if i<len2 else 0
            
            if x is not y:
                return 1 if x>y else -1
        return 0