# 446 - Arithmetic Slices II - Subsequence
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        hashmap = {}
        dp = {}
        total_count = 0
        # dp[step][tail][prev] = length
        for i, el in enumerate(nums):
            for j, el2 in enumerate(nums[:i]):
                step = el - el2
                if step not in dp:
                    dp[step] = {}
                
                if i not in dp[step]:
                    dp[step][i] = 0
                dp[step][i] += 1
                
                if j in dp[step]:
                    dp[step][i] += dp[step][j]
                    total_count += dp[step][j]

        return total_count

