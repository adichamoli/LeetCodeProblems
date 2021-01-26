#Solution 1

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        return max(['{0}{1}:{2}{3}'.format(*t) \
                   for t in itertools.permutations(arr) if t[:2] < (2,4) and t[2] < 6] or [""])


#Solution 2

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        
        max_time = -1
        # enumerate all possibilities, with the permutation() func
        for h, i, j, k in itertools.permutations(A):
            hour = h*10 + i
            minute = j*10 + k
            if hour < 24 and minute < 60:
                max_time = max(max_time, hour * 60 + minute)
        
        if max_time == -1:
            return ""
        else:
            return "{:02d}:{:02d}".format(max_time // 60, max_time % 60)