# 1289 - Minimum Falling Path Sum II
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return grid[0][0]
        m = len(grid[0])
        prev_row = [0] * m
        curr_row = [0] * m
        
        for row in grid:
            for i, cell in enumerate(row):
                if i == 0:
                    min_val = min(prev_row[i+1:])
                elif i == m-1:
                    min_val = min(prev_row[:i])
                else:
                    min_val = min([min(prev_row[:i]),min(prev_row[i+1:])])
                curr_row[i] = cell + min_val
            prev_row = [*curr_row]
        return min(curr_row)
