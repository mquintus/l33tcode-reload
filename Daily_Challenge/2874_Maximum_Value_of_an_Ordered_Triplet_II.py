# 2874 - Maximum Value of an Ordered Triplet II
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxDiff = nums[0] - nums[1]
        maxElement = max(nums[0], nums[1])
        maxTriplet = 0
        for i in range(2, len(nums)):
            #print(maxTriplet, maxDiff, nums[i], maxDiff * nums[i])
            maxTriplet = max([maxTriplet, maxDiff * nums[i]])
            maxElement = max([maxElement, nums[i]])
            maxDiff = max(maxDiff, maxElement - nums[i])
        return maxTriplet
            
