# 1913 - Maximum Product Difference Between Two Pairs
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        '''
        Intuition:
        Find the smallest two and the largest two.
        '''
        min1 = 100000
        min2 = 100000
        max1 = -1
        max2 = -1

        for num in nums:
            if num <= min1:
                min2 = min1
                min1 = num
            elif num <= min2:
                min2 = num
            
            if num >= max1:
                max2 = max1
                max1 = num
            elif num >= max2:
                max2 = num
        
        return max1*max2 - min1*min2
