# 70 - Climbing Stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 2]
        i = 2
        if n < 3:
            return dp[n-1]

        for _ in range(2, n):
            dp.append(dp[i-2] + dp[i-1])
            dp.pop(0)
        return dp[-1]
