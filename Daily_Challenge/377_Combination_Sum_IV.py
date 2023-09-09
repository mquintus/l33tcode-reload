class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [-1 for _ in range(1001)]
        def solve(curr_sum):
            if curr_sum == target:
                return 1
            if curr_sum > target:
                return 0
            if dp[curr_sum] != -1:
                return dp[curr_sum]

            combinations = 0
            for j in nums:            
                combinations += solve(curr_sum + j)
            dp[curr_sum] = combinations
            return combinations
        return solve(0)
