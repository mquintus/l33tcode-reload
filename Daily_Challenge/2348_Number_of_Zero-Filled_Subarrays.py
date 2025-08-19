# 2348 - Number of Zero-Filled Subarrays
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        p1 = 0
        count = 0
        while p1 < len(nums):
            p2 = p1
            if nums[p1] == 0:
                while p2 < len(nums) and nums[p2] == 0:
                    p2 += 1
                    count += p2 - p1
                p1 = p2
            p1 += 1
        return count
