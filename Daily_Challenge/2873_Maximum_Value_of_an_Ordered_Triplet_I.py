# 2873 - Maximum Value of an Ordered Triplet I
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxval = 0
        n = len(nums)
        for i in range(n-2):
            vi = nums[i]
            for j in range(i+1, n-1):
                vj = nums[j]
                for k in range(j+1, n):
                    vk = nums[k]
                    val = ((vi - vj) * vk)
                    maxval = max(maxval, val)
        return maxval
                    
