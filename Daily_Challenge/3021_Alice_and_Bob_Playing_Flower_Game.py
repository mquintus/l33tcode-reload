# 3021 - Alice and Bob Playing Flower Game
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # Alice wins if (x + y) is odd
        evens_n = n // 2
        odds_n = (n+1) // 2

        evens_m = m // 2
        odds_m = (m+1) // 2
        
        return evens_n*odds_m + odds_n*evens_m
