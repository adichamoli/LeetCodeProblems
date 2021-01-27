'''116 / 116 test cases passed.                         Status: Accepted
Runtime: 68 ms                                          Memory Usage: 14.3 MB'''

class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals)
        
        output = []
        
        cur_interval = None
        
        for interval in intervals:
            if cur_interval is None:
                cur_interval = interval
            else:
                if interval[0] <= cur_interval[1]:
                    cur_interval = [cur_interval[0], max(interval[1], cur_interval[1])]
                else:
                    output.append(cur_interval)
                    cur_interval = interval
        output.append(cur_interval)
        return output

    def partitionLabels(self, S: str) -> List[int]:
        
        first = {}
        last = {}
        
        l_ = len(S)
        
        for ii, char in enumerate(S):
            if char not in first:
                first[char] = ii
        
        for ii, char in enumerate(S[::-1]):
            if char not in last:
                last[char] = l_ - ii -1
        
        intervals = []
        
        for key in first:
            intervals.append([first[key], last[key]])
        
        merged_intervals = self.merge(intervals)
                
        return [elt[1] - elt[0] + 1 for elt in merged_intervals]