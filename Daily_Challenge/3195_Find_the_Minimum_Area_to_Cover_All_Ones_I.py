# 3195 - Find the Minimum Area to Cover All Ones I
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        left = len(grid[0])
        right = -1
        up = len(grid)
        down = -1
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    left = min(left, j)
                    right = max(right, j)

                    up = min(up, i)
                    down = max(down, i)

                    #print(i, j)
        if up == -1: return 0
        #print(right, left, down, up)
        return (right-left+1)*(down-up+1)
