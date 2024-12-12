# 2558 - Take Gifts From the Richest Pile
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts[:] = [-a for a in gifts]
        heapq.heapify(gifts)
        for _ in range(k):
            best = -1 * gifts[0]
            heapq.heapreplace(gifts, -1 * (int)(best**.5))
        return -1 * sum(gifts)
