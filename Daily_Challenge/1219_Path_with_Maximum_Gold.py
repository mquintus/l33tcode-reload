# 1219 - Path with Maximum Gold
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def dfs(row, col):
            if row < 0 or row >= n or col < 0 or col >= m:
                return 0
            curr_val = grid[row][col]
            if curr_val == 0:
                return 0
            grid[row][col] = 0
            
            bestsolution = 0
            for nextrow, nextcol in [(row+1,col),(row-1,col),(row,col+1),(row,col-1)]:
                bestsolution = max(bestsolution, dfs(nextrow, nextcol))

            grid[row][col] = curr_val
            return curr_val + bestsolution
            

        n = len(grid)
        m = len(grid[0])
        bestsolution = 0
        for startrow in range(n):
            for startcol in range(m):
                bestsolution = max(bestsolution, dfs(startrow, startcol))
        return bestsolution
