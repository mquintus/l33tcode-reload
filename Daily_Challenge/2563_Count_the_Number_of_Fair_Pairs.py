# 2563 - Count the Number of Fair Pairs
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0
        for i, el in enumerate(nums):
            p0 = bisect_left(nums, lower-el, i+1)
            p1 = bisect_right(nums, upper-el, i+1)
            count += p1 - p0
        return count

