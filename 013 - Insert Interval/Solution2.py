'''156 / 156 test cases passed.                         Status: Accepted
Runtime: 76 ms                                          Memory Usage: 17.6 MB'''

class Solution:
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    smaller, larger = [], []
    for interval in intervals:
      if interval[1] < newInterval[0]:
        smaller.append(interval)
      elif interval[0] > newInterval[1]:
        larger.append(interval)
      else:
        newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
    return smaller + [newInterval] + larger