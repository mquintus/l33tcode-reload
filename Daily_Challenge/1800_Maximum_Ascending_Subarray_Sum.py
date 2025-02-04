# 1800 - Maximum Ascending Subarray Sum
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        s = nums[0]
        prev = nums[0]
        cs = s
        for el in nums[1:]:
            if prev >= el:
                cs = el
            else:
                cs += el
            s = max(s, cs)
            prev = el
            
        return s
