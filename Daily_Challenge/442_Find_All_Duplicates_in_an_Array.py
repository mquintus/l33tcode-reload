# 442 - Find All Duplicates in an Array
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        results = []
        for el in nums:
            pos = abs(el) - 1
            if nums[pos] < 0:
                results.append(abs(el))
            else:
                nums[pos] *= -1
        return results
