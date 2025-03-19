# 3191 - Minimum Operations to Make Binary Array Elements Equal to One I
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        n = len(nums)
        for i,  el in enumerate(nums):
            if el == 0:
                ops += 1
                if i+1 >= n or i+2 >= n:
                    return -1
                nums[i+1] = 1-nums[i+1]
                nums[i+2] = 1-nums[i+2]
        return ops
