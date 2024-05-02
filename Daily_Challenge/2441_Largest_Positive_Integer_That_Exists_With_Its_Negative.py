# 2441 - Largest Positive Integer That Exists With Its Negative
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        exists = set()
        largest = -1
        for el in nums:
            if abs(el) <= largest:
                continue

            if el in exists:
                continue

            if -1*el in exists:
                largest = max(largest, abs(el))
                exists.remove(-1*el)
                continue
            
            exists.add(el)
        return largest
