class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)        
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for r in range(0, n):
            for l in range(r-1, -1, -1):
                if s[l] == s[r]:
                    dp[l][r] = dp[l+1][r]
                elif s[l] != s[r]:
                    dp[l][r] = float('inf')
                    for k in range(l,r):
                        dp[l][r] = min(dp[l][r], dp[l][k] + dp[k+1][r])

        return dp[0][n-1]
