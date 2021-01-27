'''59 / 59 test cases passed.                              Status: Accepted
Runtime: 416 ms                                            Memory Usage: 14.4 MB'''

class Solution(object):
    def largestOverlap(self, A, B):
        def count_ones(n):
            res = 0
            while n > 0:
                res += 1
                n -= n&(-n)
            return res
        m,n = len(A), len(A[0])
        bin_a = []
        bin_b = []
        for i in range(m):
            temp_a = temp_b = 0
            for j in range(n):
                temp_a = (temp_a<<1) + A[i][j]
                temp_b = (temp_b<<1) + B[i][j]
            bin_a += [temp_a]
            bin_b += [temp_b<<n]
        bin_b = [0]*m+bin_b+[0]*m
        res = 0
        for i in range(2*m):
            for j in range(2*n):
                temp = 0
                for a,b in zip(bin_a, bin_b[i:i+m]):
                    temp += count_ones(a&(b>>j))
                res = max(res,temp)
        return res