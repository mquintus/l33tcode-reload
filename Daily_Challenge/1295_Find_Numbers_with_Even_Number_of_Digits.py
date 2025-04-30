# 1295 - Find Numbers with Even Number of Digits
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([1 for el in nums if len(str(el))%2 == 0])
