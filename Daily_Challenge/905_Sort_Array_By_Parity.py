# 905 - Sort Array By Parity
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        p1 = 0
        p2 = 1

        while p2 < len(nums):
            if nums[p1] % 2 == 0:
                p1 += 1

            if nums[p2] % 2 == 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
            p2 += 1

        return nums
