# 2270 - Number of Ways to Split Array
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        avg = (totalSum+1) // 2
        
        currSum = 0
        counter = 0
        for el in nums[:-1]:
            currSum += el
            if currSum >= avg:
                counter += 1

        return counter
