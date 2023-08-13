class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = [True for _ in range(len(nums))]

        def solve(i):
            if i > len(nums):
                return False

            if i == len(nums):
                return True
            
            if dp[i] == False:
                return False

            if i + 2 < len(nums) and nums[i] == nums[i + 1] == nums[i + 2]:
                if solve(i + 3):
                    return True
            if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                if solve(i + 2):
                    return True
            if i + 2 < len(nums) and nums[i] == nums[i + 1] - 1 == nums[i + 2] - 2:
                if solve(i + 3):
                    return True

            dp[i] = False
            return False

        return solve(0)
