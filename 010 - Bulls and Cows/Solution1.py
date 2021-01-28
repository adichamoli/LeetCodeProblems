'''152 / 152 test cases passed.                       Status: Accepted
Runtime: 76 ms                                        Memory Usage: 14.5 MB'''

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        new_guess = []
        new_secret = []
            
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                new_secret.append(secret[i])
                new_guess.append(guess[i])
        for key in new_guess:
            if key in new_secret:
                cows += 1
                new_secret.remove(key)
            
        return("{}A{}B".format(bulls, cows))