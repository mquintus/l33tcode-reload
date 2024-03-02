# 977 - Squares of a Sorted Array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        p0 = 0
        p1 = len(nums) - 1
        newArray = []
        sq0 = nums[p0] ** 2
        sq1 = nums[p1] ** 2
        while p0 <= p1:
            if sq0 > sq1:
                newArray.insert(0, sq0)
                p0 += 1
                sq0 = nums[p0] ** 2
            else:
                newArray.insert(0, sq1)
                p1 -= 1
                sq1 = nums[p1] ** 2
        return newArray
