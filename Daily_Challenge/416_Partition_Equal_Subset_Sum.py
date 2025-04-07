# 416 - Partition Equal Subset Sum
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total %2 == 1: return False

        goal = total // 2
        dp = [False for i in range(goal+1)]
        dp[0] = True

        for val in nums:
            if val > goal:
                continue
            for i in range(goal, val, -1):
                dp[i] |= dp[i - val]
            dp[val] = True


        return dp[goal]
