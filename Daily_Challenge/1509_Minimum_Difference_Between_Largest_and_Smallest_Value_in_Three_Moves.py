# 1509 - Minimum Difference Between Largest and Smallest Value in Three Moves
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 5:
            return 0

        bestDistance = float('inf')
        nums.sort()
        for k in range(0,4):
            smallest = nums[k]
            biggest =  nums[n-4+k]
            #print(k, smallest)
            #print(n-4+k, biggest)
            distance = biggest - smallest
            bestDistance = min([distance, bestDistance])

        return bestDistance
        
        
