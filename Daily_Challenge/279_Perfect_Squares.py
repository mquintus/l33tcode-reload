# 279 - Perfect Squares
class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i ** 2 for i in range(1, int(n ** 0.5) + 1)][::-1]
        m = len(squares)
        # take or skip
        dp = [[-1] * (n+1) for _ in range(m+1)]

        def solve(i, x):
            if x == 0:
                return 0
            if i == m:
                return float('inf')
            if dp[i][x] != -1:
                return dp[i][x]
            if squares[i] == x:
                return 1
            
            skip = solve(i+1, x)
            take = float('inf')
            if squares[i] <= x:
                take = 1 + solve(i, x - squares[i])

            dp[i][x] = min(take, skip)
            return dp[i][x]

        return solve(0, n)
