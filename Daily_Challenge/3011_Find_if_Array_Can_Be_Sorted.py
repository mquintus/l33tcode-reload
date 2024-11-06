# 3011 - Find if Array Can Be Sorted
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        p0 = 0
        p1 = 1

        numberofbits = nums[p0].bit_count()
        maxval = nums[p0]
        minval = nums[p0]
        prevmaxval = float("-inf")
        # Sliding Window
        while p1 < len(nums):
            newbitcount = nums[p1].bit_count()
            if newbitcount == numberofbits:
               maxval = max(maxval, nums[p1])
               minval = min(maxval, nums[p1])  
            else:
               if nums[p1] < maxval: return False
               p0 = p1
               numberofbits = nums[p0].bit_count()
               prevmaxval = maxval
               maxval = nums[p0]
               minval = nums[p0]
            if minval < prevmaxval: return False
               
            p1 += 1
        return True



