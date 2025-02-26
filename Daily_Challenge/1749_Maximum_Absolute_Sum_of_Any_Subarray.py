# 1749 - Maximum Absolute Sum of Any Subarray
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        def slide(fac = 1):
            p0 = 0
            p1 = 0
            val = nums[p0]*fac
            score = abs(val)
            while p1 < n:
                while p0 < n and (val < 0 or nums[p0]*fac < 0):
                    val -= nums[p0]*fac
                    p0 += 1
                p1 += 1
                if p1 < n:
                    val += nums[p1]*fac
                score = max(score, val)
            return score
        score = max(slide(1), slide(-1))
        return score

                
