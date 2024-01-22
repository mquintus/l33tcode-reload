# 645 - Set Mismatch
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        allNumbers = set(nums)
        missing = -1
        for el in range(1, len(nums) + 1):
            if el not in allNumbers:
                missing = el
                break

        sortedNumbers = sorted(nums)
        prev = 0
        for i in sortedNumbers:
            if i == prev:
                return [i, missing]
            prev = i
