# 2929 - Distribute Candies Among Children II
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        comb = 0
        for i in range(0, min(n, limit)+1):
            comb += max(min(limit, n - i) - max(0, n - i - limit) + 1, 0)
        return comb
