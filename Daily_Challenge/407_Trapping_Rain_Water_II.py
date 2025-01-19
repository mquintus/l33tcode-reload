# 407 - Trapping Rain Water II
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        rows = len(heightMap)
        cols = len(heightMap[0])
        if cols <= 2:
            return 0
        if rows <= 2:
            return 0
        wall = []
        visited = set()
        wallheight = float('inf')
        for r in range(rows):
            for c in [0, cols-1]:
                wall.append((heightMap[r][c], r, c))
                wallheight = min(wallheight, heightMap[r][c])
                visited.add((r,c))
        for r in [0, rows-1]:
            for c in range(cols):
                wall.append((heightMap[r][c], r, c))
                wallheight = min(wallheight, heightMap[r][c])
                visited.add((r,c))
        
        water = 0
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        heapq.heapify(wall)
        while wall:
            h,r,c = heapq.heappop(wall)
            for dr,dc in directions:
                nr = r+dr
                nc = c+dc
                if nr <= 0 or nc <= 0 or nc >= cols-1 or nr >= rows-1:
                    continue
                if (nr,nc) in visited:
                    continue
                visited.add((nr,nc))

                if heightMap[nr][nc] < h:
                    water += h - heightMap[nr][nc]

                heapq.heappush(wall, (max(h, heightMap[nr][nc]), nr, nc))
        return water

