'''156 / 156 test cases passed.                         Status: Accepted
Runtime: 68 ms                                          Memory Usage: 17.5 MB'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        intervals.append(newInterval)
        intervals.sort()
        res = []
        res.append(intervals[0])
        
        for start, end in intervals[1:]:
            if start > res[-1][1]:
                res.append([start, end])
            elif end > res[-1][1]:
                res[-1][1] = end
        return res