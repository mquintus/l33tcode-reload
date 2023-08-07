from math import factorial
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        combinations = 1
        modulo = 10**9 + 7

        if n == goal:
            return factorial(n) % modulo
        if n > goal:
            return 0

        dp = [[0 for _ in range(n + 1)] for _ in range(goal + 1)]

        for g in range(1, goal + 1):
            # If there are more unique songs than the length of the playlist
            # the contraint is not fulfilled to have
            # all songs in the playlist
            for uniquesongs in range(g + 1, n):
                dp[g][uniquesongs] = 0

            # The number of ways to have the same number 
            # of unique songs as the goal is the factorial
            if g <= n:
                dp[g][g] = dp[g - 1][g - 1] * g

        # Empty playlist
        dp[0][0] = 1

        for g in range(1, goal + 1):
            for u in range(1, g + 1):
                if u > n:
                    continue
                dp[g][u] = dp[g - 1][u - 1] * (n - u + 1)
                if u > k:
                    dp[g][u] = dp[g][u] + dp[g - 1][u] * (u - k)

        return dp[g][n] % modulo
