class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]
        newDigit = 2
        for i in range(1, n + 1):
            if i == newDigit:
                newDigit = i * 2
            dp.append(1 + dp[i - newDigit])
        return dp
