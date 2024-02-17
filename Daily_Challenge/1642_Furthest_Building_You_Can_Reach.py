# 1642 - Furthest Building You Can Reach
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladder_heap = []
        i = 0
        while i < len(heights) - 1:
            height = heights[i + 1] - heights[i]
            #print(i, bricks, ladders, ladder_heap)

            if height <= 0:
                i += 1
                continue
            
            if ladders > 0:
                ladders -= 1
                i += 1
                heapq.heappush(ladder_heap, height)
                continue
            
            if bricks >= 0:
                new_height = height
                if ladder_heap:
                    new_height = ladder_heap[0]
                if height > new_height and bricks >= new_height:
                    bricks -= heapq.heappop(ladder_heap)
                    ladders += 1
                    continue
                if bricks >= height:
                    bricks -= height
                    i += 1
                    continue
            break
        return i
