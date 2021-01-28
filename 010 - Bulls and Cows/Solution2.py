'''152 / 152 test cases passed.                       Status: Accepted
Runtime: 44 ms                                        Memory Usage: 14.5 MB'''

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cow_digit_set = collections.defaultdict(int)
        bull_id_set = set([])
        bulls = 0
        cows = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                bull_id_set.add(i)
            else:
                cow_digit_set[secret[i]] += 1
                
        for i in range(len(secret)):
            if i in bull_id_set:
                continue
            if guess[i] in cow_digit_set:
                cow_digit_set[guess[i]] -= 1
                if cow_digit_set[guess[i]] == 0:
                    del cow_digit_set[guess[i]]
                cows += 1
                
        return "{}A{}B".format(bulls, cows)