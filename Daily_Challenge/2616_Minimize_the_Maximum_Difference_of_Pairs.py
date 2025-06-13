# 2616 - Minimize the Maximum Difference of Pairs
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        def amount_pairs_difference(diff):
            i = 1
            amount = 0
            while i < len(nums):
                if nums[i] - nums[i-1] <= diff:
                    i += 1
                    amount += 1
                i += 1
            return amount
        
        left = 0
        right = nums[-1] - nums[0] + 1
        #print(left,right)
        while left < right:
            mid = (left+right)//2
            amount = amount_pairs_difference(mid)
            if amount >= p:
                amount = amount_pairs_difference(mid-1)
                if amount < p:
                    return mid
                else:
                    right = mid
                    
            else:
                left = mid + 1
        return mid
