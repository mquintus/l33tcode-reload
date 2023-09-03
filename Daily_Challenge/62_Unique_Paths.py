class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * max(m,n) for _ in range(max(m,n))]

        def solve(x,y):
            if x == 0:
                return 1
            if y == 0:
                return 1
            if x == 1:
                return y+1
            if y == 1:
                return x+1

            if dp[x][y] != -1:
                return dp[x][y]

            dp[x][y] = solve(x-1,y) + solve(x,y-1)
            return dp[x][y]
        

        return solve(m-1,n-1)
