# 2221 - Find Triangular Sum of an Array
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        for l in range(len(nums)-1, 0, -1):
            for i in range(l):
                nums[i] = (nums[i] + nums[i+1]) % 10
        return nums[0] % 10
