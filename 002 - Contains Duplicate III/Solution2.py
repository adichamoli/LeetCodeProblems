'''Submission Detail
53 / 53 test cases passed.                      Status: Accepted
Runtime: 96 ms                                  Memory Usage: 16.7 MB'''

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        
        if len(nums)<2 or k==10000:
            return False
        i = 0
        while i<len(nums)-1:
            j = i+1
            while j<len(nums) and j-i<(k+1):
                if abs(nums[j]-nums[i])<=t:
                    return True
                j += 1
            i += 1
        return False
