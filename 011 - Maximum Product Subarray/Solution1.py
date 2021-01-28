'''187 / 187 test cases passed.                  Status: Accepted
Runtime: 76 ms                                   Memory Usage: 14.5 MB'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
            totalmax = nums[0]
            currentmin = nums[0]
            currentmax = nums[0]
            current = nums[0]
            
            for i in range(1,len(nums)):
                current = nums[i]
                
                currentmaxtemp = max(currentmin*current, currentmax*current, current)
                currentmintemp = min(currentmin*current, currentmax*current, current)
                
                currentmin = currentmintemp
                currentmax = currentmaxtemp
                
                if currentmax > totalmax:
                    totalmax = currentmax
                    
            return totalmax