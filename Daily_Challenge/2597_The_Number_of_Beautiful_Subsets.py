# 2597 - The Number of Beautiful Subsets
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        cnt = [0 for _ in range(1002)]
        n = len(nums)

        def dfs(i):
            if i == n:
                return 1
            take = 0
            skip = dfs(i + 1)
            if cnt[nums[i] - k] == 0:
                 cnt[nums[i]] += 1
                 take = dfs(i + 1)
                 cnt[nums[i]] -= 1
            return take + skip

        return dfs(0) - 1
