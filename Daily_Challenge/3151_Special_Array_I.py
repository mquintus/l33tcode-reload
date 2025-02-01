# 3151 - Special Array I
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if (nums[i]+nums[i-1]) %2 == 0:
                return False
        return True
