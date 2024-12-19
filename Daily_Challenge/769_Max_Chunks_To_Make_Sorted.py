# 769 - Max Chunks To Make Sorted
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        low = arr[0]
        up = arr[0]
        chunks = 0
        for i, el in enumerate(arr):
            low = min(low, el)
            up = max(up, el)
            if low == 0 and up <= i:
                chunks += 1
            
        return chunks
