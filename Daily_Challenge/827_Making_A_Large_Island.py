# 827 - Making A Large Island
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        if sum([sum(row) for row in grid]) == rows*cols:
            return rows*cols

        def find_island(r,c):
            border_tiles = set()
            size = 0
            states = [(r,c)]
            grid[r][c] = 0
            while states:
                r,c = states.pop()
                size += 1
                for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                    nr = r+dr
                    nc = c+dc
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                        continue
                    if grid[nr][nc] == 1:
                        states.append((nr,nc))
                        grid[nr][nc] = 0
                    else:
                        border_tiles.add((nr,nc))

            return border_tiles, size

        biggest = 1
        newgrid = [[1 for c in range(cols)] for r in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    border_tiles, size = find_island(r,c)
                    for br,bc in border_tiles:
                        newgrid[br][bc] += size
                        biggest = max(biggest,newgrid[br][bc])
        
        return biggest
