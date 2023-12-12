# 1464 - Maximum Product of Two Elements in an Array
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        Intuition: Select the two largest items
        '''

        max1 = -1
        max2 = -1

        for el in nums:
            if el >= max1:
                max2 = max1
                max1 = el
            elif el >= max2:
                max2 = el

        return (max1 - 1) * (max2 - 1)
