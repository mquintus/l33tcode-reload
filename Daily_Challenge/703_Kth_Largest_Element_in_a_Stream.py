# 703 - Kth Largest Element in a Stream
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.vals = []
        self.k = k
        for num in nums:
            self.add(num)
        #print(self.vals)

    def add(self, val: int) -> int:
        heapq.heappush(self.vals, val)
        
        if len(self.vals) > self.k:
            heapq.heappop(self.vals)
        
        return self.vals[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
