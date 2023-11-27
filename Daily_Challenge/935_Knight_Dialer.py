# 935 - Knight Dialer
class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9+7

        valid_moves = [
            [4,6],
            [6,8],
            [7,9],
            [4,8],
            [0,3,9],
            [],
            [0,1,7],
            [2,6],
            [1,3],
            [2,4]
        ]

        dp = [1 for _ in range(10)]

        if n == 1:
            return sum(dp) % MOD
        
        dp[5] = 0
        for i in range(1, n):
            dp_next = [0 for _ in range(10)]
            for d in range(10):
                for vm in valid_moves[d]:
                    dp_next[vm] += dp[d]
            
            for d in range(10):
                dp[d] = dp_next[d] % MOD
            
        
        return sum(dp) % MOD


