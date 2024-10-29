# 2684 - Maximum Number of Moves in a Grid
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        maxGrid = [[-1]*n for _ in range(m)]
    
        def moveForward(row, col):
            #print(row, col)
            if col >= n-1: return 0
            if maxGrid[row][col] != -1: return maxGrid[row][col]
            nextcol = col + 1
            longestPath = 0
            for nextrow in range(max(0,row-1), min(m, row+2)):
                if grid[nextrow][nextcol] > grid[row][col]:
                    longestPath = max(longestPath, 1+moveForward(nextrow, nextcol))
            maxGrid[row][col] = longestPath
            #print(row, col,longestPath)
            return maxGrid[row][col]

        maxSteps = 0
        for row in range(m):
            maxSteps = max(maxSteps, moveForward(row,0))
            if maxSteps == n-1: break
        
        return maxSteps
