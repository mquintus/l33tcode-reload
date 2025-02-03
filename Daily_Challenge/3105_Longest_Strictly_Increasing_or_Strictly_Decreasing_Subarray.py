# 3105 - Longest Strictly Increasing or Strictly Decreasing Subarray
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        incl = 0
        incr = 0
        decl = 0
        decr = 0

        ret = 1

        while decr < len(nums) - 1:
            decr += 1
            if nums[decr] >= nums[decr-1]:
                decl = decr
            ret = max(ret, decr-decl+1)
            #print(decl, decr, nums[decl:decr+1])

        while incr < len(nums) - 1:
            incr += 1
            if nums[incr] <= nums[incr-1]:
                incl = incr
            ret = max(ret, incr-incl+1)

        return ret

