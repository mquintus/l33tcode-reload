# 611 - Valid Triangle Number
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        valids = 0
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            first = nums[i]
            for j in range(i+1, n-1):
                second = nums[j]
                third = first+second
                k = bisect.bisect_left(nums, third)
                if k <= j: break
                valids += k-j-1
        return valids


                    
