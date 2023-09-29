# 896 - Monotonic Array
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        alwaysIncreasing = True
        alwaysDecreasing = True
        old = nums[0]
        for num in nums[1:]:
            alwaysIncreasing &= (num >= old)
            alwaysDecreasing &= (num <= old)
            old = num
        return alwaysIncreasing or alwaysDecreasing
