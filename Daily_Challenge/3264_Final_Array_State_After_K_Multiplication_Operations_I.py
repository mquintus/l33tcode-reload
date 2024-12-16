# 3264 - Final Array State After K Multiplication Operations I
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        for i, el in enumerate(nums):
            heapq.heappush(heap, (el, i))
        
        for _ in range(k):
            el, i = heap[0]
            nums[i] *= multiplier
            heapq.heapreplace(heap, (nums[i], i))
    
        return nums
