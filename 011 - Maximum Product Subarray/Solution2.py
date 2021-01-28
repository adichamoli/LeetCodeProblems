'''187 / 187 test cases passed.                  Status: Accepted
Runtime: 60 ms                                   Memory Usage: 14.4 MB'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = float('-inf')
        max_ending_here = min_ending_here = 1
        for num in nums:
            nxt_max = max(num, max_ending_here * num, min_ending_here * num)
            min_ending_here = min(num, max_ending_here * num, min_ending_here * num)
            max_ending_here = nxt_max
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far