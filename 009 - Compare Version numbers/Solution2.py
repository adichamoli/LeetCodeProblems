'''81 / 81 test cases passed.                    Status: Accepted
Runtime: 28 ms                                   Memory Usage: 14.2 MB'''

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        s1 = version1.split('.')
        s2 = version2.split('.')
        
        if len(s1) >= len(s2):
            s2.extend('0'*(len(s1)-len(s2)))
        else:
            s1.extend('0'*(len(s2)-len(s1)))
            
        c = [int(s1[i])-int(s2[i]) for i in range(len(s1))]
        print(c)
        for item in c:
            if item < 0:
                return -1
            elif item > 0:
                return 1
        return 0