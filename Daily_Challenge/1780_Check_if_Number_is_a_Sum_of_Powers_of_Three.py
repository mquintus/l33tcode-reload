# 1780 - Check if Number is a Sum of Powers of Three
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        po = 1
        pot = []
        for y in range(100):
            pot.append(po)
            po = po * 3
            if po > 10**7:
                break
        
        def skiptake(curr, i):
            if curr == n:
                return True
            if i >= len(pot) or curr > n or pot[i] > n:
                return False
            if pot[i] == n:
                return True
            skip = skiptake(curr, i+1)
            take = skiptake(curr + pot[i], i+1)
            return take or skip
        
        return skiptake(0,0)
