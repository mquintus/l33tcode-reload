# 1752 - Check if Array Is Sorted and Rotated
class Solution:
    def check(self, nums: List[int]) -> bool:
        prev = nums[0]
        smallest = nums[0]
        rot = False
        for i in range(1,len(nums)):
            el = nums[i]
            if el < prev:
                if rot: return False
                rot = True
            if rot and el > smallest: return False
            prev = el
        return True
