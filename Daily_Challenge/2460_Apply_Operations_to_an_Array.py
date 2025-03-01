# 2460 - Apply Operations to an Array
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        newNums = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        c = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                c += 1
                continue
            newNums.append(nums[i])
        newNums.extend([0]*c)
        return newNums
