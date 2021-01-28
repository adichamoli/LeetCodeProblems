'''187 / 187 test cases passed.                  Status: Accepted
Runtime: 52 ms                                   Memory Usage: 14.4 MB'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cumprod, ans = 1, nums[0]
        max_neg_cumprod = None
        
        for num in nums:
            if cumprod == 0: cumprod, max_neg_cumprod = num, None
            else: cumprod *= num
            
            if cumprod == 0: max_curr_cumprod = 0
            if cumprod > 0: max_curr_cumprod = cumprod
            else: max_curr_cumprod = cumprod/max_neg_cumprod if max_neg_cumprod else cumprod
            
            ans = max(ans, max_curr_cumprod)
            
            if cumprod < 0:
                max_neg_cumprod = cumprod if not max_neg_cumprod else max(max_neg_cumprod, cumprod)
        
        return int(ans)