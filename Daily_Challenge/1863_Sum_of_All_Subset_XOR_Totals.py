# 1863 - Sum of All Subset XOR Totals
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        globalSum = 0
        def rec(i, val):
            nonlocal globalSum 
            if i == len(nums):
                globalSum += val
                return
            rec(i+1, val^nums[i])
            rec(i+1, val)
        rec(0,0)
        return globalSum
