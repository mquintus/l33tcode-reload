# 3066 - Minimum Operations to Exceed Threshold Value II
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        op = 0
        heapq.heapify(nums)
        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, x * 2 + y)
            op += 1
        return op
