# 2016 - Maximum Difference Between Increasing Elements
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        best_difference = -1
        smallest = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > smallest:
                best_difference = max(best_difference, nums[i] - smallest)
            smallest = min(nums[i], smallest)
        return best_difference
