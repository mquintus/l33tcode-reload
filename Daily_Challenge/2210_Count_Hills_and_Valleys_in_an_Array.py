# 2210 - Count Hills and Valleys in an Array
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        prev = nums[0]
        mid = nums[1]
        for curr in nums[2:]:
            if curr == mid:
                continue
            if mid > prev and mid > curr or (mid < prev and mid < curr):
                count += 1
            prev = mid
            mid = curr
        return count

