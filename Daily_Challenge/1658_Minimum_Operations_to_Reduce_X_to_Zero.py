# 1658 - Minimum Operations to Reduce X to Zero
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        s = sum(nums)

        if x > s:
            return -1

        if x == s:
            return n

        if x < s:
            target = s - x
            # find a subarray that sums up to `target`
        
        l = 0
        r = 0
        s = nums[0]
        maxlength = -1
        while l < n:
            if s < target:
                if r < n - 1:
                    r += 1
                    s += nums[r]
                else:
                    break
            elif s > target:
                s -= nums[l]
                l += 1
            elif s == target:
                maxlength = max(maxlength, (r - l + 1))
                s -= nums[l]
                l += 1

        if maxlength > 0:
            return n - maxlength

        return -1
