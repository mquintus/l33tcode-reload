# 2419 - Longest Subarray With Maximum Bitwise AND
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        target = max(nums)
        l = 0
        res = 0
        for el in nums:
            if el == target:
                l += 1
                res = max(res,l)
            else:
                l = 0
        return res
