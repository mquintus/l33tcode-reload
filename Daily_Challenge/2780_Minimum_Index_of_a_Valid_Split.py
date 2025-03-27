# 2780 - Minimum Index of a Valid Split
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        d = sorted(nums)[n//2]

        dc = sum([1 for el in nums if el == d])

        c = 0
        for i, el in enumerate(nums):
            if el == d:
                c += 1
            if c > (i+1) // 2 and dc - c > (n - i - 1)//2:
                return i 
        return -1
