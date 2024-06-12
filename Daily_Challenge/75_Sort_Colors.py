# 75 - Sort Colors
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        p0 = 0
        p1 = n - 1
        while i <= p1 and p1 > p0:
            if nums[i] == 0:
                nums[p0], nums[i] = nums[i], nums[p0]
                p0 += 1
            elif nums[i] == 2:
                nums[p1], nums[i] = nums[i], nums[p1]
                p1 -= 1
                i -= 1
            i += 1

        
