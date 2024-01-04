# 2870 - Minimum Number of Operations to Make Array Empty
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)
        operations = 0
        for v in counts.values():
            if v == 1:
                return -1
            if v % 3 == 0:
                operations += v // 3
                continue
            if v % 3 == 1:
                operations += (v - 4) // 3 + 2
                continue
            if v % 3 == 2:
                operations += (v - 1) // 3 + 1
                continue
        return operations
