'''152 / 152 test cases passed.                       Status: Accepted
Runtime: 32 ms                                        Memory Usage: 14.4 MB'''

class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        cows = {k: [0, 0] for k in "0123456789"}
        bullsCount = 0
        for si, gi in zip(secret, guess):
            if si == gi:
                bullsCount += 1
            else:
                cows[si][0] += 1
                cows[gi][1] += 1
    
        return "{}A{}B".format(bullsCount, sum(map(min, cows.values())))