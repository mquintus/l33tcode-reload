# 2529 - Maximum Count of Positive Integer and Negative Integer
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = bisect.bisect_left(nums, 0)
        p = bisect.bisect_right(nums, 0)
        return max(n,len(nums)-p)
