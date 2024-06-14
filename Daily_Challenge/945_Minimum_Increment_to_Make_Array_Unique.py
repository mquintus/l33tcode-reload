# 945 - Minimum Increment to Make Array Unique
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        steps = 0
        nums.sort()
        prev = nums[0]
        for i in range(1, len(nums)):
            req = prev + 1
            missing = (req - nums[i])
            if missing > 0:
                steps += missing
                prev = req
            else:
                prev = nums[i]
        return steps
