'''59 / 59 test cases passed.                              Status: Accepted
Runtime: 204 ms                                            Memory Usage: 14.4 MB'''

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        l = len(img1)
        one = [100*(i//l) + i%l for i in range(l**2) if img1[i//l][i%l]]
        two = [100*(i//l) + i%l for i in range(l**2) if img2[i//l][i%l]]
        c = Counter(i-j for i in one for j in two)
        return max(c.values() or [0])