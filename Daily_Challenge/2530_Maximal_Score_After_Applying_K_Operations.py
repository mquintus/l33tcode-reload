# 2530 - Maximal Score After Applying K Operations
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-el for el in nums]
        heapq.heapify(nums)
        score = 0
        for _ in range(k):
            score -= heapq.heapreplace(nums, nums[0]//3)
        return score
