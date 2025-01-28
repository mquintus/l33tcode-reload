# 2658 - Maximum Number of Fish in a Grid
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return 0
            if grid[r][c] == 0:
                return 0
            points = grid[r][c]
            grid[r][c] = 0
            for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                nr = dr + r
                nc = dc + c
                points += bfs(nr,nc)
            return points

        maxpoints = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0: continue
                points = bfs(r,c)
                maxpoints = max(points,maxpoints)
        
        return maxpoints
