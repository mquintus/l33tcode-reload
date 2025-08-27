# 3459 - Length of Longest V-Shaped Diagonal Segment
class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        dirs = [[1, 1],[1, -1],[-1, -1],[-1, 1]]
        rows, cols = len(grid), len(grid[0])

        @cache
        def dfs(r,c, currentDirection, hasMadeTurnYet, nextNumber):
            nr = r + dirs[currentDirection][0] 
            nc = c + dirs[currentDirection][1] 

            if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] != nextNumber:
                return 0

            nextnextNumber = 2 - nextNumber
            maxStep = dfs(nr, nc, currentDirection, hasMadeTurnYet, nextnextNumber)
            if not hasMadeTurnYet:
                maxStepTurned = dfs(nr, nc, (currentDirection+1)%4, True, nextnextNumber)
                maxStep = max(maxStep, maxStepTurned)
            maxStep += 1
            return maxStep
            
        answer = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    for direction in range(4):
                        answer = max(answer, dfs(r,c, direction, False, 2) + 1)
        return answer
