# 3423 - Maximum Difference Between Adjacent Elements in a Circular Array
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        nums = nums
        md = abs(nums[0]-nums[-1])
        for i in range(1, len(nums)):
            md = max(md, abs(nums[i]-nums[i-1]))
        return md

