# 576 - Out of Boundary Paths
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if maxMove == 0:
            return 0

        grid = [[0 for p in range(n)] for q in range(m)]

        for p in range(n):
            grid[0][p] += 1
            grid[m-1][p] += 1
        for q in range(m):
            grid[q][0] += 1
            grid[q][n-1] += 1

        directions = [(-1,0),(0,-1),(1,0),(0,1)]
        MOD = 10**9 + 7

        ways = grid[startRow][startColumn]
        for _ in range(maxMove - 1):
            secondGrid = [[0] * n for row in grid]

            for p in range(m):
                for q in range(n):
                    
                    for i, j in directions:
                        i += p
                        j += q
                        if i not in range(m):
                            continue
                        if j not in range(n):
                            continue
                        secondGrid[p][q] += grid[i][j]
            grid = secondGrid
            ways += grid[startRow][startColumn] % MOD
        return ways % MOD



