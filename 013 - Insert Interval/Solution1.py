'''156 / 156 test cases passed.                         Status: Accepted
Runtime: 76 ms                                          Memory Usage: 17.5 MB'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        
        i, start, end = 0, 0, 1
        
        # Add all intervals that comes before the new Interval
        while i < len(intervals) and intervals[i][end] < newInterval[start]:
            merged.append(intervals[i])
            i += 1
            
        # Merge all intervals that overlap with new interval
        while i < len(intervals) and intervals[i][start] <= newInterval[end]:
            newInterval[start] = min(intervals[i][start], newInterval[start])
            newInterval[end] = max(intervals[i][end], newInterval[end])
            i += 1
         
        # Insert new interval
        merged.append(newInterval)
        
        # All all remaining intervals to the result
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1
            
        return merged