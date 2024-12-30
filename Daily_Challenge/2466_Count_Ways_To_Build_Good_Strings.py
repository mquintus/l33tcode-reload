# 2466 - Count Ways To Build Good Strings
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9+7
        dp = [0 for _ in range(high+1)]
        dp[0] = 1
        answer = 0
        for i in range(1,high+1):
            dp[i] = 0
            if i - zero >= 0:
                dp[i] += dp[i-zero]
            if i - one >= 0:
                dp[i] += dp[i-one]

            if i >= low and i <= high:
                answer += dp[i]

            dp[i] = dp[i] % MOD
            
        return answer % MOD
