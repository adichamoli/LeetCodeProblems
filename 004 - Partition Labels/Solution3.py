'''116 / 116 test cases passed.                         Status: Accepted
Runtime: 32 ms                                          Memory Usage: 14.4 MB'''

class Solution:
    def partitionLabels(self, S: str) -> List[int]:     
        charLastIndexMap = {}
        n = len(S)
        for i in range(n):
            charLastIndexMap[S[i]] = i
        
        res = []
        start,end = 0,0 
        for i in range(n):
            end = max(end, charLastIndexMap[S[i]])
            if i == end:
                subStrLen = end-start+1
                res.append(subStrLen)
                start = end+1
        return res