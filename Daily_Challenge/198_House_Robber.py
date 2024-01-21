# 198 - House Robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def tos(i):
            if i >= n:
                return 0
            take = nums[i] + tos(i+2)
            skip = tos(i+1)
            return max(take, skip)

        return tos(0)
