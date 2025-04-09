# 3375 - Minimum Operations to Make Array Values Equal to K
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k: return -1
        nums = set(nums)
        diff = 1 if k in nums else 0
        return len(nums) - diff
