'''18 / 18 test cases passed.                        Status: Accepted
Runtime: 32 ms                                       Memory Usage: 14 MB'''

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        a = [1,2,3,4,5,6,7,8,9]
        r = []
        c = combinations(a,k)
        for a in c:
            if sum(a) == n:
                r.append(a)
                
        return r