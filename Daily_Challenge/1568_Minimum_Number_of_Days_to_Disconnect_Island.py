# 1568 - Minimum Number of Days to Disconnect Island
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        if sum([sum(row) for row in grid]) == 1:
            return 1
        
        n = len(grid)
        m = len(grid[0])

        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        def exploreIsland(row, col):
            cells = [(row, col)]
            visited = set([(row, col)])
            while cells:
                row, col = cells.pop()
                for dr,dc in dirs:
                    nrow = row+dr
                    ncol = col+dc 
                
                    if nrow >= 0 and nrow < n:
                        if ncol >= 0 and ncol < m:
                            if (nrow, ncol) not in visited:
                                if grid[nrow][ncol] == 1:
                                    cells.append((nrow, ncol))
                                    visited.add((nrow, ncol))
            return visited


        visitedLand = set()
        allIslands = []
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1 and (row, col) not in visitedLand:
                    nextIsland = exploreIsland(row, col)
                    allIslands.append(nextIsland)
                    visitedLand |= nextIsland
        if len(allIslands) != 1:
            return 0
        #return 1
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 0:
                    continue

                grid[row][col] = 0
                for startrow, startcol in visitedLand:
                    if (startrow, startcol) == (row, col):
                        continue
                    newIsland = exploreIsland(startrow, startcol)
                    if len(newIsland) != len(visitedLand) - 1:
                        print(len(newIsland), len(visitedLand))
                        return 1
                    break
                grid[row][col] = 1
        
        return 2
