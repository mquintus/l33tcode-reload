class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1], [1,1], [1,2,1]]
        for i in range(3, numRows):
            dp.append([1])
            for a in range(1, i):
                dp[i].append(dp[i-1][a - 1] + dp[i-1][a])
            dp[i].append(1)
        return dp[:numRows]
